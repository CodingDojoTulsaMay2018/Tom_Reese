using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;


namespace dojosecrets.Models{
    public class Like
    {
        [Key]
        public int Id {get;set;}
        
        public int Userid {get; set;}
        public User Liked {get; set;}

        public int Secretid {get; set;}
        public Secret Haslikes { get; set; }



    
    }
}