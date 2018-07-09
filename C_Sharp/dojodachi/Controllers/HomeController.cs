using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using dojodachi.Models;
// using System.Web.SessionState;

namespace dojodachi.Controllers
{
    public class HomeController : Controller

    {

    Dachi pet = new Dachi();

    Random rand = new Random();
   
     public IActionResult Index()
    {
        if(HttpContext.Session.GetString("img") == null) {
        HttpContext.Session.SetString("img", "smile");
        TempData["msg"] = "Let's play a new game!";
        }   

        TempData["img"] = HttpContext.Session.GetString("img");

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

        if(HttpContext.Session.GetInt32("meals") == 0 || HttpContext.Session.GetInt32("energy") == 0 || HttpContext.Session.GetInt32("happiness") == 0 || HttpContext.Session.GetInt32("fullness") == 0)
        {TempData["img"] = "dead";
        TempData["msg"] = "Smiley is dead! You killed it, you monster!";
        return View(pet);
        }
        if(HttpContext.Session.GetInt32("fullness") >= 100 && HttpContext.Session.GetInt32("energy") >= 100 && HttpContext.Session.GetInt32("happiness") >= 100)
        {TempData["img"] = "win";
        TempData["msg"] = "you are victorious!! Smiley is now free from your reign!";
        return View(pet);
        }
        return View(pet);
    }


        public IActionResult Feed()
        {

        int mealsleft = (int)HttpContext.Session.GetInt32("meals");
        var chance = rand.Next(0,4);
        if(chance == 0){
        mealsleft--;
        HttpContext.Session.SetInt32("meals", mealsleft);
        TempData["msg"] = "You fed Smiley, but he threw it up! Meals: -1";
        return RedirectToAction("Index");
        }
        else{
        var addFullness = rand.Next(5,11);
        int currentFullness = (int)HttpContext.Session.GetInt32("fullness");
        currentFullness += addFullness;
        HttpContext.Session.SetInt32("fullness", currentFullness);
        mealsleft--;
        HttpContext.Session.SetInt32("meals", mealsleft);
        HttpContext.Session.SetString("img", "smile");
        TempData["img"]  = HttpContext.Session.GetString("img");
        HttpContext.Session.SetString("img", "smile");
        TempData["img"]  = HttpContext.Session.GetString("img");
        TempData["msg"] = ("You fed Smiley! Meals: -1, Fullness: +"+addFullness);
        TempData["full"] = HttpContext.Session.GetInt32("fullness");
        TempData["happ"] = HttpContext.Session.GetInt32("happiness");
        TempData["meal"] = HttpContext.Session.GetInt32("meals");
        TempData["ener"] = HttpContext.Session.GetInt32("energy");                 
        return RedirectToAction("Index");
        }
        }


        public IActionResult Play()
        {
        var chance = rand.Next(0,4);
        if(chance == 0){
            int energyLeft = (int)HttpContext.Session.GetInt32("energy");
            energyLeft -= 5;
            HttpContext.Session.SetInt32("energy", energyLeft);
            TempData["msg"] = "You played with Smiley, but he didn't enjoy it! Energy: -5";
        }
        else{
        var addHappy = rand.Next(5,11);
        int currentHappy = (int)HttpContext.Session.GetInt32("happiness");
        currentHappy += addHappy;
        HttpContext.Session.SetInt32("happiness", currentHappy);
        int energyLeft = (int)HttpContext.Session.GetInt32("energy");
        energyLeft -= 5;
        HttpContext.Session.SetInt32("energy", energyLeft);
        TempData["msg"] = "You played with Smiley! Energy: -5, Happiness: "+addHappy;
        }

        if(HttpContext.Session.GetInt32("energy") <= 0){
            TempData["msg"] = "Smiley is dead! You killed it, you monster!";
            HttpContext.Session.SetString("img", "dead");

            return RedirectToAction("Index");
        }
      
        
        TempData["happ"] = HttpContext.Session.GetInt32("happiness");
        TempData["ener"] = HttpContext.Session.GetInt32("energy");                 
        HttpContext.Session.SetString("img", "smile");

            return RedirectToAction("Index");
        }

        public IActionResult Work()
        {

        var chance = rand.Next(1,4);
        int energyLeft = (int)HttpContext.Session.GetInt32("energy");
        energyLeft -= 5;
        HttpContext.Session.SetInt32("energy", energyLeft); 
        var mealsleft = (int)HttpContext.Session.GetInt32("meals");
        mealsleft += chance;
        HttpContext.Session.SetInt32("meals", mealsleft);                
        HttpContext.Session.SetString("img", "smile");
        TempData["msg"] = ("You went to work! Evergy: -5, Meals: +"+chance);

            return RedirectToAction("Index");
        }

        public IActionResult Sleep()
        {
            int energyLeft = (int)HttpContext.Session.GetInt32("energy");
            energyLeft += 15;
            HttpContext.Session.SetInt32("energy", energyLeft); 

            int currentFullness = (int)HttpContext.Session.GetInt32("fullness");
            currentFullness -= 5;
            HttpContext.Session.SetInt32("fullness", currentFullness);
            int currentHappy = (int)HttpContext.Session.GetInt32("happiness");
            currentHappy -= 5;
            HttpContext.Session.SetInt32("happiness", currentHappy);

            HttpContext.Session.SetString("img", "smile");
            TempData["msg"] = ("You went to sleep! Evergy: +5, Happiness -5, Fullness: -5");

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
