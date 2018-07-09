using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using random_pass.Models;


namespace random_pass.Controllers
{
    public class HomeController : Controller
    {
        public int counter = 0;

        public IActionResult Index()
        {
        if(HttpContext.Session.GetInt32("Counter") == null)
        {
            HttpContext.Session.SetInt32("Counter", 0);
        }

            return View();
        }

        public IActionResult Generate()
        {
        var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        var stringChars = new char[14];
        Random rand = new Random();
        for(var i = 0; i < stringChars.Length;i++){
            stringChars[i] = chars[rand.Next(chars.Length)];
        }
        var finalString = new String(stringChars);
        TempData["passcode"] = finalString;


        counter = (int)HttpContext.Session.GetInt32("Counter");
        counter++;            
        HttpContext.Session.SetInt32("Counter", counter);                     
        int? IntVariable = HttpContext.Session.GetInt32("Counter");
        TempData["Count"] = IntVariable;                    

            return RedirectToAction("Index");
        }

        public IActionResult About()
        {
            ViewData["Message"] = "Your application description page.";

            return View();
        }

        public IActionResult Contact()
        {
            ViewData["Message"] = "Your contact page.";

            return View();
        }

        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
