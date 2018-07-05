using Microsoft.AspNetCore.Mvc;
using System.Net;
using System;
using System.Collections.Generic;



    namespace web_test.Controllers     //be sure to use your own project's namespace!
    {

public class SecondController : Controller
{
    
    [HttpGet]
    [Route("method3")]
    public IActionResult OtherMethod()
    {
        System.Console.WriteLine("redirecting, in theory, back to the index.");
        return View("Index");
    }
}

    }