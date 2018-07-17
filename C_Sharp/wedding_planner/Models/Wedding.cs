using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;


namespace wedding_planner.Models{

    public class Wedding
    {
        [Key]
        public int Id {get;set;}

        [Required]
        [MinLength(2)]
        [RegularExpression("^[a-zA-Z]+$", ErrorMessage = "Use letters only please")]
        public string Bride { get; set; }

        [Required]
        [MinLength(2)]
        [RegularExpression("^[a-zA-Z]+$", ErrorMessage = "Use letters only please")]
        public string Groom { get; set; }

        [Required]
        public DateTime Date {get; set;}

        [Required]
        [MinLength(2), MaxLength(255)]
        public string Address {get;set;}

        public int Userid { get; set; }
        public User Creator {get; set;} 

        public List<Guest> Guests {get; set;}

        public DateTime Created_At {get; set;} = DateTime.Now;

        public Wedding()
        {
            List<Guest> Guests = new List<Guest>();
        }
    }
}