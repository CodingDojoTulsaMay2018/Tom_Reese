using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using dojo_survey_validation.Models;

namespace dojo_survey_validation.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
   
        public IActionResult Create(User user)
            {
                if(ModelState.IsValid)
            {
                return RedirectToAction("Result",user);
            }
            else
            {
                return View("Index",user);
            }
            }

        public IActionResult Result(User user)
        {
            ViewData["Message"] = "Your success page.";

            return View("Result", user);
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
