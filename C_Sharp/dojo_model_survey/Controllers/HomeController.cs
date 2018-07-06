using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using dojo_model_survey.Models;

namespace dojo_model_survey.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            System.Console.WriteLine("************5refghtrfd****************");
            return View();
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
        [HttpPost("Result")]

        public IActionResult Result(string name,string location,string language, string comment)
        {
            ViewData["Message"] = "Your result page.";
            
            Ninja tom = new Ninja(){
            Name = name,
            Location = location,
            Language = language,
            Comment = comment,
            };
      
            return View(tom);
        }

        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
