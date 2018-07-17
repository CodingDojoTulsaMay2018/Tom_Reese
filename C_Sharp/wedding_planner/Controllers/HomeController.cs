using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using wedding_planner.Models;

namespace wedding_planner.Controllers
{
    public class HomeController : Controller
    {
    private YourContext _context;
    public HomeController(YourContext context)
    {
        _context = context;
    }
    [HttpGet]
    [Route("Index")]
        public IActionResult Index()
        {
            return View("Index");
        }


        public IActionResult Dash()
        {
            if(HttpContext.Session.GetInt32("id") == null) { 
                return RedirectToAction("Logout", "User");};

        List<Wedding> AllWeds = _context.weddings.Include(u => u.Guests).ThenInclude(g => g.Attendee).ToList();

        ViewBag.weddings = AllWeds;
        ViewBag.id = (int)HttpContext.Session.GetInt32("id");

            return View();
        }

        [HttpGet]
        [Route("Plan")]
        public IActionResult Plan()
        {
            if(HttpContext.Session.GetInt32("id") == null) { 
                return RedirectToAction("Logout", "User");};



            ViewBag.id = (int)HttpContext.Session.GetInt32("id");
            return View();
        }

        [HttpPost]
        public IActionResult New(Wedding wed)
        {

            if(HttpContext.Session.GetInt32("id") == null) { 
                return RedirectToAction("Logout", "User");};
            if(HttpContext.Session.GetInt32("id") != (int)wed.Userid) { 
                return RedirectToAction("Logout", "User");};
            System.Console.WriteLine("****past planning validations*****");
            
            if (wed.Date < DateTime.Today){
            ModelState.AddModelError("Date", "Date must be today or later.");
            return View("Plan");
            }
            User user = _context.users.SingleOrDefault(u => u.Id== HttpContext.Session.GetInt32("id"));
            wed.Creator = user;
            _context.Add(wed);
            _context.SaveChanges();
            return RedirectToAction("Dash");
            System.Console.WriteLine("errors in wedding planning");
            return View("Plan");
            
        }

        [HttpGet]
        [Route("Home/Delete/{num}")]
        public IActionResult Delete(int num)
        {
               if(HttpContext.Session.GetInt32("id") == null) { 
                return RedirectToAction("Logout", "User");};

            Wedding wed = _context.weddings.SingleOrDefault(u => u.Id == num);
            _context.Remove(wed);
            _context.SaveChanges();


            return RedirectToAction("Dash");
        }

        [HttpGet]
        [Route("Home/In/{num}")]
        public IActionResult In(int num)
        {
               if(HttpContext.Session.GetInt32("id") == null) { 
                return RedirectToAction("Logout", "User");};

            Wedding wed = _context.weddings.Include(g => g.Guests).ThenInclude(a => a.Attendee).SingleOrDefault(u => u.Id == num);
            User user = _context.users.SingleOrDefault(u => u.Id== HttpContext.Session.GetInt32("id"));

            Guest newg = new Guest{
                Userid = user.Id,
                Attendee = user,
                Weddingid = wed.Id,
                Event = wed
            };

            wed.Guests.Add(newg);
            _context.SaveChanges();


            return RedirectToAction("Dash");
        }

        [HttpGet]
        [Route("Home/Out/{num}")]
        public IActionResult Out(int num)
        {
               if(HttpContext.Session.GetInt32("id") == null) { 
                return RedirectToAction("Logout", "User");};

            Wedding wed = _context.weddings.Include(g => g.Guests).ThenInclude(a => a.Attendee).SingleOrDefault(u => u.Id == num);
            
            User user = _context.users.SingleOrDefault(u => u.Id== HttpContext.Session.GetInt32("id"));

            Guest invite = _context.guests.Where(i => i.Userid == user.Id).Where(i => i.Weddingid == num).SingleOrDefault();
            wed.Guests.Remove(invite);
            _context.SaveChanges();


            return RedirectToAction("Dash");
        }

        [HttpGet]
        [Route("Home/Details/{num}")]
        public IActionResult Details(int num)
        {
               if(HttpContext.Session.GetInt32("id") == null) { 
                return RedirectToAction("Logout", "User");};
            
            Wedding wedding = _context.weddings
                            .Include(w => w.Guests)
                            .ThenInclude(g => g.Attendee)
                            .SingleOrDefault(w => w.Id == num);
            ViewBag.CurrentWedding = wedding;
            ViewBag.WeddingGuests = wedding.Guests;
            return View();
        }

    }
}
