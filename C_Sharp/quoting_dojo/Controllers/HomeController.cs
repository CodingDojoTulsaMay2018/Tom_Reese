using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using quoting_dojo.Models;
using System.Web;
using DbConnection;

namespace quoting_dojo.Controllers
{
    public class HomeController : Controller
    {
  
        public IActionResult Index()
        {
            return View();
        }

        [HttpGet]
        public IActionResult Quotes()
        {

            DateTime CurrentTime  = DateTime.Now;
             List<Dictionary<string, object>> AllUsers = DbConnector.Query("SELECT * FROM quotes");
            ViewBag.AllUsers = AllUsers;
                        return View();

            }
        [HttpPost]
        public IActionResult Quotes(string djquotes, string quotext)
        {
            DateTime CurrentTime  = DateTime.Now;
            System.Console.WriteLine(djquotes);
            System.Console.WriteLine(quotext);
            string date = CurrentTime.ToString("yyyy-MM-dd HH:mm:ss");
            string query = $"INSERT INTO quotes (quote, quoter, created_at) VALUES ('{quotext}','{djquotes}', '{date}')";
            DbConnector.Execute(query);
            return RedirectToAction("Index");
        }
    }
}
