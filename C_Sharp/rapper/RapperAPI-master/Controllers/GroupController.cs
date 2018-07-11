using System;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Linq;

namespace RapperAPI.Controllers {
    public class GroupController : Controller {
        List<Group> allGroups {get; set;}
        List<Artist> allArtists {get; set;}
        public GroupController() {
            allGroups = JsonToFile<Group>.ReadJson();
            allArtists = JsonToFile<Artist>.ReadJson();
        }
        // 1.) Create a route /groups that returns all groups as JSON
        [Route("groups")]
        [HttpGet]
        public JsonResult Groups()
        {
            return Json(allGroups);
        }
        // 2.) Create a route /groups/name/{name} that returns all groups that match the provided name
        [Route("groups/name/{band}")]
        [HttpGet]
        public JsonResult ThatBand(string band)
        {
            var grouper = allGroups.Where(a => a.GroupName == $"{band}");   

            return Json(grouper);
        }

        // 3.) Create a route /groups/id/{id} that returns all groups with the provided Id value
        [Route("groups/id/{num}")]
        [HttpGet]
        public JsonResult ThatGroup(int num)
        {
            var grouper = allGroups.Where(a => a.Id.Equals(num));   
            if(grouper != null){
                var displayArtists = 
                from g in grouper
                join a in allArtists
                on g.Id equals a.GroupId
                group a by g.GroupName into g
                select new {g};
                // string[] member = new string[displayArtists.Count()];
                // displayArtists.ToArray();

                
            
            return Json(displayArtists);
            }
            return Json(grouper);
        }
        // 4.) (Optional) Add an extra boolean parameter to the group routes called displayArtists that will include members for all Group JSON responses
    }
}