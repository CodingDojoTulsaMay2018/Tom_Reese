using Microsoft.AspNetCore.Mvc;
using System.Net;
using System;
using System.Collections.Generic;

    namespace razor_fun.Controllers     
    {
        public class UserController : Controller   
        {

            [HttpGet]     
            [Route("")]    
            public IActionResult Index()
            {
                // ViewBag.Example = "Hello World!";
                return View("index");
            }

        }
    }
