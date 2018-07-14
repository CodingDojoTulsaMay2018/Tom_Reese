
using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;


namespace the_wall.Models{
    public class Comment
    {
        [Key]
        public int Id {get;set;}

        [Column("comment")]
        public string Post {get;set;}
        
        public int Userid {get; set;}
        public User Creator {get; set;}

        public int Messageid {get; set;}
        public Message Belongsto { get; set; }

        public DateTime Created_At {get; set;}

        public Comment()
        {
            Created_At = DateTime.Now;
        }
    }
}