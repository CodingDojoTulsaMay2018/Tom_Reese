using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using wedding_planner.Models;
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace wedding_planner.Controllers
{
    public class UserController : Controller
    {

    private YourContext _context;
    public UserController(YourContext context)
    {
        _context = context;
    }    
        [HttpPost]
        [Route("")]
        public IActionResult Create(User person)
        {
            if(ModelState.IsValid){
            PasswordHasher<User> Hasher = new PasswordHasher<User>();
            person.Password = Hasher.HashPassword(person, person.Password);
            _context.Add(person);
            _context.SaveChanges();
            System.Console.WriteLine("***Created a User***");
            HttpContext.Session.SetInt32("id", person.Id);
            return RedirectToAction("Dash", "Home");
            }
            System.Console.WriteLine("User creation rejected*******");
            return View("~/Views/Home/Index.cshtml");
        }

        [HttpPost]
        // [Route("")]
        [Route("Login")]

        public IActionResult Login(UserLog guy){
            var user = _context.users.SingleOrDefault(u => u.Email == guy.LogEmail);
            if(user != null && guy.LogPassword != null)
            {
                var Hasher = new PasswordHasher<User>();
                if(0 != Hasher.VerifyHashedPassword(user, user.Password, guy.LogPassword))
                {
                    var it = _context.users.SingleOrDefault(u => u.Email == guy.LogEmail);
                    it.Updated_At = DateTime.Now;
                    int num = (int)it.Id;
                    ViewBag.num = num;
                    _context.SaveChanges();
                    System.Console.WriteLine("***Logging in a User***");
                    HttpContext.Session.SetInt32("id", num);
                    return RedirectToAction("Dash", "Home");}
            ModelState.AddModelError("LogPassword", "Incorrect password.");
            return View("~/Views/Home/Index.cshtml");
            }
            ModelState.AddModelError("LogEmail", "Incorrect email.");
            System.Console.WriteLine("***User was denied login!!!***");
            return View("~/Views/Home/Index.cshtml");
        }

        // [HttpGet]
        // [Route("")]
        // public IActionResult Login()
        // {
        //     System.Console.WriteLine("***User is trying to log in ***");
        //     return View("Login");
        // }
   
            public IActionResult Logout()
        {
            HttpContext.Session.Clear();
            System.Console.WriteLine("***User is logging out ***");
            return RedirectToAction("Index", "Home");
        }
    
    
    
    
    
    
    
    
    
    
    
    }
}
