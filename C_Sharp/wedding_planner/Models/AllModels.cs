
using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Collections.Generic;

namespace wedding_planner.Models
{
    public class AllModels
    {
        public Wedding Weddings {get; set;}
        public Guest Guests {get; set;}
        public User Users {get; set;}
    }
}