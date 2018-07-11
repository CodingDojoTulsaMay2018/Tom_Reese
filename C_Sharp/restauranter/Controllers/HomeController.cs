using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using restauranter.Models;
using Microsoft.EntityFrameworkCore;


namespace restauranter.Controllers
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
        public IActionResult Create(Reviews person)
        {

            if(ModelState.IsValid){
            _context.Add(person);
            _context.SaveChanges();
            return RedirectToAction("Reviews");
            }
            // Reviews NewReview = new Reviews
            // {
            //     Reviewer = person.reviewer,
            //     Review = person.review,
            //     Stars = person.stars,
            //     Restaurant_Name = person.restaurant_name,
            //     Date = person.date
            //     };
            return View("Index");
        }



        public IActionResult Reviews()
        {
            List<Reviews> AllReviews = _context.reviews.ToList();
            ViewBag.info = AllReviews.OrderByDescending(x => x.Date);
            return View();
        }

        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
