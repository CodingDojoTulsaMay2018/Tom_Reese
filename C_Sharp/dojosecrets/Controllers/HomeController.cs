using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using dojosecrets.Models;
using System.Globalization;
using System.Threading;

namespace dojosecrets.Controllers
{
    public class HomeController : Controller
    {
 
    private YourContext _context;
    public HomeController(YourContext context)
    {
        _context = context;
    }



        public IActionResult Index()
        {
            ViewModel logreg = new ViewModel()
            {
                regUser = new User(),
                loginUser = new UserLog()
            };
            return View(logreg);
        }

        public IActionResult Secrets()
        {
            if(HttpContext.Session.GetInt32("id") == null) { 
                return RedirectToAction("Logout");}

            ViewBag.name = HttpContext.Session.GetString("name");
            ViewBag.id = HttpContext.Session.GetInt32("id");
            List<Secret> AllSecrets = _context.secrets.Include(u => u.Likes).ThenInclude(g => g.Liked).ToList();
            foreach(var i in AllSecrets){
              i.Ago = i.Created_At.TimeAgo();
            }
            ViewBag.secrets = AllSecrets.OrderByDescending(x => x.Created_At);
            TempData["secrets"] = "secrets";
            return View();
        }

        [HttpPost]
        public IActionResult Create(ViewModel FormData)
        {
            User user = FormData.regUser;
            if(ModelState.IsValid){
            PasswordHasher<User> Hasher = new PasswordHasher<User>();
            user.Password = Hasher.HashPassword(user, user.Password);
            _context.Add(user);
            _context.SaveChanges();
            System.Console.WriteLine("***Created a User***");
            HttpContext.Session.SetInt32("id", user.Id);
            HttpContext.Session.SetString("name", user.First_Name);
            return RedirectToAction("Secrets");
            }
            System.Console.WriteLine("User creation rejected*******");        
            return View("Index", FormData);
        }

        [HttpPost]
        [Route("Login")]
        public IActionResult Login(ViewModel FormData){
            UserLog loguser = FormData.loginUser;
            if(ModelState.IsValid){
            var user = _context.users.SingleOrDefault(u => u.Email == loguser.LogEmail);
            if(user != null && user.Password != null)
            {
                var Hasher = new PasswordHasher<User>();
                if(0 != Hasher.VerifyHashedPassword(user, user.Password, loguser.LogPassword))
                {
                    ViewBag.num = (int)user.Id;
                    _context.SaveChanges();
                    HttpContext.Session.SetString("name", user.First_Name);
                    System.Console.WriteLine("***Logging in a User***");
                    HttpContext.Session.SetInt32("id", (int)ViewBag.num);
                    return RedirectToAction("Secrets");}
            }
            ModelState.AddModelError("LogPassword", "Incorrect password.");
            return View("Index");
            }
            ModelState.AddModelError("LogEmail", "Incorrect email.");
            System.Console.WriteLine("***User was denied login!!!***");
            return View("Index");
        }


        public IActionResult Popular()
        {
            if(HttpContext.Session.GetInt32("id") == null) { 
                return RedirectToAction("Logout");};
            ViewBag.name = HttpContext.Session.GetString("name");
            ViewBag.id = HttpContext.Session.GetInt32("id");
            List<Secret> AllSecrets = _context.secrets.Include(u => u.Likes).ThenInclude(g => g.Liked).ToList();
            foreach(var i in AllSecrets){
              i.Ago = i.Created_At.TimeAgo();
            }
            ViewBag.secrets = AllSecrets.OrderByDescending(x => x.Likes.Count);

            return View();
        }


    
        [HttpPost]
        public IActionResult New(Secret FormData)
        {
                           if(HttpContext.Session.GetInt32("id") == null) { 
                return RedirectToAction("Logout");};
            if(ModelState.IsValid){
            User user = _context.users.SingleOrDefault(u => u.Id== HttpContext.Session.GetInt32("id"));
            FormData.Creator = user;
            _context.Add(FormData);
            _context.SaveChanges();
            System.Console.WriteLine("***Created a Secret***");
            return RedirectToAction("Secrets");
            }
            System.Console.WriteLine("Secret creation rejected*******");
            return View("Secrets");
        }

        [HttpGet]
        [Route("Home/Like/{num}/{word}")]
        public IActionResult Like(int num, string word)
        {
            if(HttpContext.Session.GetInt32("id") == null) { 
                return RedirectToAction("Logout");};

            Secret it = _context.secrets.Include(g => g.Likes).ThenInclude(a => a.Liked).SingleOrDefault(u => u.Id == num);
            User user = _context.users.SingleOrDefault(u => u.Id== HttpContext.Session.GetInt32("id"));

            Like newl = new Like{
                Userid = user.Id,
                Liked = user,
                Secretid = it.Id,
                Haslikes = it
            };

            it.Likes.Add(newl);
            _context.SaveChanges();
            if(word == "secrets"){
            return RedirectToAction("Secrets");
            }
            return RedirectToAction("Popular");
        }

        [HttpGet]
        [Route("Home/Delete/{num}/{word}")]
        public IActionResult Delete(int num, string word)
        {
               if(HttpContext.Session.GetInt32("id") == null) { 
                return RedirectToAction("Logout");};

            Secret del = _context.secrets.SingleOrDefault(u => u.Id == num);
            _context.Remove(del);
            _context.SaveChanges();
            if(word == "secrets"){
            return RedirectToAction("Secrets");
            }
            return RedirectToAction("Popular");
        }


            public IActionResult Logout()
        {
            HttpContext.Session.Clear();
            System.Console.WriteLine("***User is logging out ***");
            return RedirectToAction("Index");
        }
    
    }
}
