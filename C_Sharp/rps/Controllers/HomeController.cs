using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;

namespace rps.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
        if(HttpContext.Session.GetInt32("wins") == null || HttpContext.Session.GetInt32("losses") == null || HttpContext.Session.GetInt32("ties") == null) {
        HttpContext.Session.SetInt32("wins", 0);
        HttpContext.Session.SetInt32("ties", 0);
        HttpContext.Session.SetInt32("losses", 0);
        }
        TempData["wins"] = HttpContext.Session.GetInt32("wins");
        TempData["losses"] = HttpContext.Session.GetInt32("losses");
        TempData["ties"] = HttpContext.Session.GetInt32("ties");
                return View();

        }

        public IActionResult Process_Play()
        {
            Random rand = new Random();
            int com = rand.Next(0,3);

            if(com == 0 && Request.Form["hand"] == "rock"){
                var ties = HttpContext.Session.GetInt32("ties");
                ties++;
                HttpContext.Session.SetInt32("ties", (int)ties);
            }
                       if(com == 1 && Request.Form["hand"] == "rock"){
                var losses = HttpContext.Session.GetInt32("losses");
                losses++;
                HttpContext.Session.SetInt32("losses", (int)losses);
            }
                       if(com == 2 && Request.Form["hand"] == "rock"){
                var wins = HttpContext.Session.GetInt32("wins");
                wins++;
                HttpContext.Session.SetInt32("wins", (int)wins);
            }
                        if(com == 1 && Request.Form["hand"] == "paper"){
                var ties = HttpContext.Session.GetInt32("ties");
                ties++;
                HttpContext.Session.SetInt32("ties", (int)ties);
            }
                       if(com == 2 && Request.Form["hand"] == "paper"){
                var losses = HttpContext.Session.GetInt32("losses");
                losses++;
                HttpContext.Session.SetInt32("losses", (int)losses);
            }
                       if(com == 0 && Request.Form["hand"] == "paper"){
                var wins = HttpContext.Session.GetInt32("wins");
                wins++;
                HttpContext.Session.SetInt32("wins", (int)wins);
            }
                        if(com == 2 && Request.Form["hand"] == "scissors"){
                var ties = HttpContext.Session.GetInt32("ties");
                ties++;
                HttpContext.Session.SetInt32("ties", (int)ties);
            }
                       if(com == 0 && Request.Form["hand"] == "scissors"){
                var losses = HttpContext.Session.GetInt32("losses");
                losses++;
                HttpContext.Session.SetInt32("losses", (int)losses);
            }
                       if(com == 1 && Request.Form["hand"] == "scissors"){
                var wins = HttpContext.Session.GetInt32("wins");
                wins++;
                HttpContext.Session.SetInt32("wins", (int)wins);
            }
            // var result = "";
            // if(com == 0){
            //     var result = "Rock";
            // }
            // if(com == 1){
            //     var result = "Paper";
            // }
            // if(com == 2){
            //     var result = "Scissors";
            // }
            TempData["com"] = com;
            TempData["you"] = (string)Request.Form["hand"];
            return RedirectToAction("Index");
        }


    }
}
