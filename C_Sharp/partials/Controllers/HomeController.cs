using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using partials.Models;

namespace partials.Controllers
{
    public class HomeController : Controller
    {

        [HttpGet]     
        [Route("")]    
        public IActionResult Index()
        {
            return View("index");
        }

        [HttpPost]     
        [Route("result")]    
        public IActionResult Result(string name, string dojo_location, string fav_lang, string comment)
        {
            ViewBag.name = name;
            ViewBag.location = dojo_location;
            ViewBag.language = fav_lang;
            ViewBag.comment = comment;

            return View("result");
            }


        // public IActionResult Index()
        // {
        //     return View();
        // }

        // public IActionResult About()
        // {
        //     ViewData["Message"] = "Your application description page.";

        //     return View();
        // }

        // public IActionResult Contact()
        // {
        //     ViewData["Message"] = "Your contact page.";

        //     return View();
        // }

        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }

    }
}
