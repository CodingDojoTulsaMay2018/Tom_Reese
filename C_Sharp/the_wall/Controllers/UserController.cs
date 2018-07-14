using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using the_wall.Models;
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace the_wall.Controllers
{
    public class UserController : Controller
    {

    private YourContext _context;
    public UserController(YourContext context)
    {
        _context = context;
    }

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
            ViewBag.num = person.Id;
            System.Console.WriteLine("***Created a User***");
            HttpContext.Session.SetInt32("id", person.Id);
            return RedirectToAction("Wall", "Home");
            }

            return RedirectToAction("Index", "User");
        }

        [HttpPost]
        [Route("Login")]

        public IActionResult Login(User guy){
            var user = _context.users.SingleOrDefault(u => u.Email == guy.Email);
            if(user != null && guy.Password != null)
            {
                var Hasher = new PasswordHasher<User>();
                if(0 != Hasher.VerifyHashedPassword(user, user.Password, guy.Password))
                {
                    var it = _context.users.SingleOrDefault(u => u.Email == guy.Email);
                    it.Updated_At = DateTime.Now;
                    int num = (int)it.Id;
                    ViewBag.num = num;
                    _context.SaveChanges();
                    System.Console.WriteLine("***Logging in a User***");
                    HttpContext.Session.SetInt32("id", num);
                    return RedirectToAction("Wall", "Home");}
            ModelState.AddModelError("email", "Incorrect password.");
            return View("Login");
            }
            ModelState.AddModelError("email", "Incorrect email.");
            System.Console.WriteLine("***User was denied login!!!***");
            return View("Login");
        }

        [HttpGet]
        [Route("Login")]
        public IActionResult Login()
        {
            System.Console.WriteLine("***User is trying to log in ***");
            return View("Login");
        }
   
            public IActionResult Logout()
        {
            HttpContext.Session.Clear();
            System.Console.WriteLine("***User is logging out ***");
            return RedirectToAction("Index");
        }
    
    
    
    
    
    
    
    
    
    
    
    }
}
