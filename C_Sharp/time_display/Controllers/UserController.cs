using Microsoft.AspNetCore.Mvc;
using System.Net;
using System;
using System.Collections.Generic;

    namespace time_display.Controllers     
    {
        public class UserController : Controller   
        {

            [HttpGet]     
            [Route("")]    
            public IActionResult Index()
            {
                DateTime dt = DateTime.Now;
                var tom = String.Format("{0:dddd, MMMM d, yyyy}", dt);
                ViewBag.Example = tom;
                return View("index");
            }

        }
    }
