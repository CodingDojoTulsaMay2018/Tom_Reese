using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;


namespace dojosecrets.Models{

    public class Secret
    {
        [Key]
        public int Id {get;set;}

        [Required]
        public string Text {get;set;}

        public int Userid { get; set; }
        public User Creator {get; set;} 

        public List<Like> Likes {get; set;}

        public DateTime Created_At {get; set;} = DateTime.Now;
        [NotMapped]
        public string Ago {get; set;}

        public Secret()
        {
            List<Like> Likes = new List<Like>();
        }
    }
}