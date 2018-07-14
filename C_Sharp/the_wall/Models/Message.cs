using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;


namespace the_wall.Models{
    public class Message
    {
        [Key]
        public int Id {get;set;}

        public string Content {get;set;}


        public int Userid { get; set; }
        public User Creator {get; set;}

        public List<Comment> Comments {get; set;}
        public DateTime Created_At {get; set;}

        public Message()
        {
            List<Comment> Comments = new List<Comment>();
            Created_At = DateTime.Now;
        }
    }
}