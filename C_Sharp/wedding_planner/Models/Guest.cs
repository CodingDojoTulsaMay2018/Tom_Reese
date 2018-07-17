
using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;


namespace wedding_planner.Models{
    public class Guest
    {
        [Key]
        public int Id {get;set;}
        
        public int Userid {get; set;}
        public User Attendee {get; set;}

        public int Weddingid {get; set;}
        public Wedding Event { get; set; }



    
    }
}