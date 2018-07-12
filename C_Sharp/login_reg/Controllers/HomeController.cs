using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using login_reg.Models;
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;


namespace login_reg.Controllers
{
    public class HomeController : Controller
    {

        private YourContext _context;

        public HomeController(YourContext context)
        {
            _context = context;
        }

        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            return View();
        }


        [HttpPost]
        public IActionResult Create(User person)
        {

            if(ModelState.IsValid){
            PasswordHasher<User> Hasher = new PasswordHasher<User>();
            person.Password = Hasher.HashPassword(person, person.Password);
            _context.Add(person);
            _context.SaveChanges();
            return RedirectToAction("Registration");
            }

            return View("Index");
        }

        [HttpPost]
        public IActionResult Login(User guy){
            var user = _context.users.SingleOrDefault(u => u.Email == guy.Email);
            if(user != null && guy.Password != null)
            {
                var Hasher = new PasswordHasher<User>();
                if(0 != Hasher.VerifyHashedPassword(user, user.Password, guy.Password))
                {
                    System.Console.WriteLine("***********SUCCESS**********");
                    return RedirectToAction("Registration");
                }
        }
        System.Console.WriteLine("***********DOUBLE FAIL**********");
        return View("Logging");

        }

        public IActionResult Logging()
        {
            return View();
        }

        public IActionResult Registration()
        {
            List<User> AllUsers = _context.users.ToList();
            ViewBag.info = AllUsers;
            return View();
        }


        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
