using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
    
    namespace form_submit.Models
    {
    public class User
    {
        [Required]
        [MinLength(4)]
        public string First_Name { get; set; }

        [Required]
        [MinLength(4)]
        public string Last_Name { get; set; }

        [Required]
        [Range(1,99)]
        public int Age { get; set; }
 
        [Required]
        [EmailAddress]
        public string Email { get; set; }
 
        [Required]
        [DataType(DataType.Password)]
        public string Password { get; set; }
    }
}