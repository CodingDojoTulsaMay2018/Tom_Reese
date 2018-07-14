using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using Microsoft.EntityFrameworkCore;
using the_wall.Models;

namespace the_wall.Controllers
{
    public class HomeController : Controller
    {


    private YourContext _context;
    public HomeController(YourContext context)
    {
        _context = context;
    }

        [Route("Wall")]
        public IActionResult Wall()
        {

        if(HttpContext.Session.GetInt32("id") == null) { 
                return RedirectToAction("Logout", "User");};
            AllModels ViewModels = new AllModels()
            {
                Comments = new Comment(),
                Messages = new Message()
            };

        List<Message> AllMessages = _context.messages.Include(u => u.Creator).Include(c => c.Comments).ToList();
        // List<Comment> AllComments = _context.comments.Include(m => m.BelongsTo).ToList();

        ViewBag.messages = AllMessages;

            System.Console.WriteLine(ViewModels);
            return View(ViewModels);
        }
        
        [HttpPost]
        public IActionResult addMessage(Message message)
        {

            
            User user = _context.users.SingleOrDefault(u => u.Id== HttpContext.Session.GetInt32("id"));
            message.Userid = (int)HttpContext.Session.GetInt32("id");
            _context.Add(message);
            _context.SaveChanges();
            Message saveMessage = _context.messages.Last();
            user.Messages.Add(saveMessage);
            _context.SaveChanges();

            return RedirectToAction("Wall");

        }

        [HttpPost]
        public IActionResult addComment(Comment comment)
        {

            User user = _context.users.SingleOrDefault(u => u.Id== HttpContext.Session.GetInt32("id"));
            int MsgID = Int32.Parse(Request.Form["msg_id"]);
            comment.Creator = user;
            comment.Messageid = MsgID;
            _context.Add(comment);
            _context.SaveChanges();
            return RedirectToAction("Wall");

        }

        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
