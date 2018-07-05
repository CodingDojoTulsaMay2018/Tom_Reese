using Microsoft.AspNetCore.Mvc;
using System.Net;
using System;
using System.Collections.Generic;



    namespace web_test.Controllers     //be sure to use your own project's namespace!
    {
        public class HelloController : Controller   //remember inheritance??
        {
            //for each route this controller is to handle:
            [HttpGet]       //type of request
            [Route("")]     //associated route string (exclude the leading /)
            public IActionResult Index()
            {
                    ViewBag.Example = "Hello World!";
                return View();
            }

            [HttpGet]       //type of request
            [Route("projects")]     //associated route string (exclude the leading /)
            public string Projects()
            {
                return "These are my projects!";
            }

            [HttpGet]       //type of request
            [Route("contact")]     //associated route string (exclude the leading /)
            public string Contact()
            {
                return "This is my contact!";
            }

            [HttpGet]       //type of request
            [Route("food")] 
            public IActionResult Method()
            {
                // The anonymous object consists of keys and values
                // The keys should match the parameter names of the method being redirected to
                return RedirectToAction("OtherMethod", new { Food = "sandwiches", Quantity= 5 });
            }
            
            [HttpGet]
            [Route("other/{Food}/{Quantity}")]
            public IActionResult OtherMethod(string Food, int Quantity)
            {
                Console.WriteLine($"I ate {Quantity} {Food}.");
                return View("Index");
                // Writes "I ate 5 sandwiches."
            }


            [HttpGet]
            [Route("method2")]
            public IActionResult Method2()
            {
                System.Console.WriteLine("redirecting to the second controller");
                return RedirectToAction("OtherMethod", "Second");
            }


        }
    }
