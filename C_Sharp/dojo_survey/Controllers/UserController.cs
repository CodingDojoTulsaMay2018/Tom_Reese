using Microsoft.AspNetCore.Mvc;
using System.Net;
using System;
using System.Collections.Generic;

    namespace dojo_survey.Controllers     
    {
        public class UserController : Controller   
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

        }
    }