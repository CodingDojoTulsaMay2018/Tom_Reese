
using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Collections.Generic;

namespace dojosecrets.Models
{
    public class AllModels
    {
        public Secret Secrets {get; set;}
        public Like Likes {get; set;}
        public User Users {get; set;}
    }
}