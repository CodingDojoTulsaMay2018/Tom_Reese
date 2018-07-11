using System;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Linq;

namespace RapperAPI.Controllers {

    
    public class ArtistController : Controller {

        private List<Artist> allArtists;

        public ArtistController() {
            allArtists = JsonToFile<Artist>.ReadJson();
        }

        //This method is shown to the user navigating to the default API domain name
        //It just display some basic information on how this API functions
        [Route("")]
        [HttpGet]
        public string Index() {
            //String describing the API functionality
            string instructions = "Welcome to the Music API~~\n========================\n";
            instructions += "    Use the route /artists/ to get artist info.\n";
            instructions += "    End-points:\n";
            instructions += "       *Name/{string}\n";
            instructions += "       *RealName/{string}\n";
            instructions += "       *Hometown/{string}\n";
            instructions += "       *GroupId/{int}\n\n";
            instructions += "    Use the route /groups/ to get group info.\n";
            instructions += "    End-points:\n";
            instructions += "       *Name/{string}\n";
            instructions += "       *GroupId/{int}\n";
            instructions += "       *ListArtists=?(true/false)\n";
            return instructions;
        }
        // 1.) Create a route for /artists that returns all artists as JSON
        [Route("artists")]
        [HttpGet]
        public JsonResult AllArtist()
        {
            return Json(allArtists);
        }
        // 2.) Create a route /artists/name/{name} that returns all artists that match the provided name(RealName)
        [Route("artists/name/{person}")]
        [HttpGet]
        public JsonResult ThatArtist(string person)
        {
            var artist = allArtists.Where(a => a.RealName == $"{person}");   

            return Json(artist);
        }
        // 3.) Create a route /artists/realname/{name} that returns all artists who real names match the provided name
        [Route("artists/realname/{name}")]
        [HttpGet]
        public JsonResult RealArtist(string name)
        {
            var artist = allArtists.Where(a => a.RealName.Contains($"{name}"));   

            return Json(artist);
        }

        // 4.) Create a route /artists/hometown/{town} that returns all artists who are from the provided town

        [Route("artists/hometown/{town}")]
        [HttpGet]
        public JsonResult Homettown(string town)
        {
            var artist = allArtists.Where(a => a.Hometown == $"{town}");   

            return Json(artist);
        }

        // 5.) Create a route /artists/groupid/{id} that returns all artists who have a GroupId that matches id
        [Route("artists/groupid/{id}")]
        [HttpGet]
        public JsonResult gID(int id)
        {
            var artist = allArtists.Where(a => a.GroupId.Equals(id));   

            return Json(artist);
        }
        
    }
}