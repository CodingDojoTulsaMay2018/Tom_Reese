using Microsoft.AspNetCore.Mvc;
using System.Net;
using System;
using System.Collections.Generic;
using model_fun.Models;

    namespace model_fun.Controllers     
    {
        public class UserController : Controller   
        {

            [HttpGet]     
            [Route("")]    
            public IActionResult Index()
            {

                Message info = new Message()
                {
                   text = "foheroijfejrojflierjmgfolkejrsmafd;oilrkjcsamo;dgfilkjecrm;odsilafkjmecordilskajfdm;oercilkjsgmvodhfnvskladhjngmvlkrtjdnmgklvsdrjxgm;velrsngf slikujhsnmov;dsriljfgndlfkiljgblitsdfgjfmvd;soilfxujvd;oisljfvm;lisdfjkvm;ogfijdksmv;odlfjsmv;oilrjtkdfmov;ildjfmav;oliejrdmsfgxio"
                };
                return View("index", info);
            }

            [HttpGet]     
            [Route("numbers")]    
            public IActionResult Numbers()
            {

                Numbers set = new Numbers()
                {
                   nummers = new int[]{73,8,3,18,36} 
                };
                return View("numbers", set);
            }

            [HttpGet]     
            [Route("user")]    
            public IActionResult People()
            {

                Singler that = new Singler()
                {
                   single = "Rub McDub"
                };
                return View("user", that);
            }

            [HttpGet]     
            [Route("users")]    
            public IActionResult Users()
            {
                Person guy = new Person()
                {
                   list = new List<string>{"Tom", "Ryan", "Farnk"} 
                };
                return View("users", guy);
            }

        }
    }
