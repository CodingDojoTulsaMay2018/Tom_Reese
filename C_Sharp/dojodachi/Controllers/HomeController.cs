using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using dojodachi.Models;

namespace dojodachi.Controllers
{
    public class HomeController : Controller

    {

    Dachi pet = new Dachi();

    Random rand = new Random();
   
     public IActionResult Index()
    {
                
        if(HttpContext.Session.GetInt32("fullness") == null)
        {
            HttpContext.Session.SetInt32("fullness", 20);
            HttpContext.Session.SetInt32("happiness", 20);
            HttpContext.Session.SetInt32("meals", 3);
            HttpContext.Session.SetInt32("energy", 50);
        } 
        pet.Happiness = (int)HttpContext.Session.GetInt32("happiness");
        pet.Energy = (int)HttpContext.Session.GetInt32("energy");
        pet.Fullness = (int)HttpContext.Session.GetInt32("fullness");
        pet.Meals = (int)HttpContext.Session.GetInt32("meals");          
        TempData["img"]  = "~/images/smile.png";
        return View(pet);
    }

        public IActionResult Feed()
        {

        int mealsleft = (int)HttpContext.Session.GetInt32("meals");

        if(mealsleft > 0)
        {
        var addFullness = rand.Next(5,11);
        int currentFullness = (int)HttpContext.Session.GetInt32("fullness");
        currentFullness += addFullness;
        HttpContext.Session.SetInt32("fullness", currentFullness);
        mealsleft--;
        HttpContext.Session.SetInt32("meals", mealsleft);
        }   
        TempData["msg"] = "You fed Smiley!";
        TempData["full"] = HttpContext.Session.GetInt32("fullness");
        TempData["happ"] = HttpContext.Session.GetInt32("happiness");
        TempData["meal"] = HttpContext.Session.GetInt32("meals");
        TempData["ener"] = HttpContext.Session.GetInt32("energy");                 
        // TempData["img"]  = (<img src='~/images/smile.png'>);
        return RedirectToAction("Index");
        }

        public IActionResult Play()
        {
            TempData["msg"] = "You played with Smiley!";

            return RedirectToAction("Index");
        }

        public IActionResult Work()
        {
            TempData["msg"] = "You went to work!";

            return RedirectToAction("Index");
        }

        public IActionResult Sleep()
        {
            TempData["msg"] = "You went to sleep!";
            return RedirectToAction("Index");
        }

        public IActionResult Reset()
        {
            HttpContext.Session.Clear();
            TempData["msg"] = "You started a new game!";
            return RedirectToAction("Index");
        }


        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
