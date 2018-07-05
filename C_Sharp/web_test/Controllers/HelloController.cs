using Microsoft.AspNetCore.Mvc;
using System.Net;

    namespace web_test.Controllers     //be sure to use your own project's namespace!
    {
        public class HelloController : Controller   //remember inheritance??
        {
            //for each route this controller is to handle:
            [HttpGet]       //type of request
            [Route("")]     //associated route string (exclude the leading /)
            public string Index()
            {
                return "This is my index!";
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


        }
    }
