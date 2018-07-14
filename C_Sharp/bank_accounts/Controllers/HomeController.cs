using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using bank_accounts.Models;
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace bank_accounts.Controllers
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
            ViewBag.num = person.Id_User;
            return RedirectToAction("Account", new{num = (int)ViewBag.num});
            }

            return View("Index");
        }

        [HttpPost]
        public IActionResult Logging(User guy){
            var user = _context.users.SingleOrDefault(u => u.Email == guy.Email);
            if(user != null && guy.Password != null)
            {
                var Hasher = new PasswordHasher<User>();
                if(0 != Hasher.VerifyHashedPassword(user, user.Password, guy.Password))
                {
            var it = _context.users.SingleOrDefault(u => u.Email == guy.Email);
            it.Updated_At = DateTime.Now;
            int num = (int)it.Id_User;
            ViewBag.num = num;
            _context.SaveChanges();
            User Transactions = _context.users.Include(u => u.Transactions).Where(u => u.Id_User == user.Id_User).SingleOrDefault();
            double sum = 0;
            foreach(var i in Transactions.Transactions){
                sum+=i.Amount;
            }
            user.Balance = sum;
            TempData["sum"] = user.Balance;
                    return RedirectToAction("Account", new{num = (int)ViewBag.num});
                }
        }
        return View("Logging");
        }

        [HttpGet]
        [Route("/Login")]
        public IActionResult Login()
        {
            return View("Login");
        }

        [HttpGet]
        [Route("/account/{num}")]
        public IActionResult Account(int num)
        {
            ViewBag.user = _context.users.SingleOrDefault(u => u.Id_User == num);

            User Transactions = _context.users.Include(u => u.Transactions).Where(u => u.Id_User == num).SingleOrDefault();

            ViewBag.money = Transactions.Transactions.OrderByDescending(x => x.Created_At).ToList();


            return View("Account");
        }

        [HttpPost]
        public IActionResult Money(){
            double amount = Double.Parse(Request.Form["amount"]);
            User user = _context.users.SingleOrDefault(u => u.Id_User == Int32.Parse(Request.Form["user_id"]));

            Trans money = new Trans{
                Amount = Double.Parse(Request.Form["amount"]),
                Created_At = DateTime.Now,
                User = user,
            };

            User Transactions = _context.users.Include(u => u.Transactions).Where(u => u.Id_User == user.Id_User).SingleOrDefault();
            _context.Add(money);
            _context.SaveChanges();
            double sum = 0;
            foreach(var i in Transactions.Transactions){
                sum+=i.Amount;
            }
            user.Balance = sum;
            TempData["sum"] = user.Balance;
            ViewBag.num = (int)user.Id_User;
            return RedirectToAction("Account", new{num = ViewBag.num });
        }
 

    //     public IActionResult Error()
    //     {
    //         return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    //     }
    }
}
