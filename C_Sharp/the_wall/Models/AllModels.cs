
using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Collections.Generic;

namespace the_wall.Models
{
    public class AllModels
    {
        public Comment Comments {get; set;}
        public Message Messages {get; set;}
        public User Users {get; set;}
    }
}