using System;
using System.Collections.Generic;
using System.Globalization;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;


namespace login_reg.Models
{

// public class CustomDateAttribute : RangeAttribute
// {
//   public CustomDateAttribute()
//     : base(typeof(DateTime), 
//             DateTime.Now.AddYears(-6).ToShortDateString(),
//             DateTime.Now.ToShortDateString()) 
//   { } 
// }


    public class User
    {
        public long Id { get; set; }

        [Required]
        [MinLength(2)]
        [RegularExpression("^[a-zA-Z]+$", ErrorMessage = "Use letters only please")]
        public string First_Name { get; set; }
        
        [Required]
        [MinLength(2)]
        [RegularExpression("^[a-zA-Z]+$", ErrorMessage = "Use letters only please")]
        public string Last_Name { get; set; }

        [Required]
        [EmailAddress]
        public string Email { get; set; }
       
        [Required]
        [DataType(DataType.Password)]
        [MinLength(8)]
        public string Password { get; set; }

        [NotMapped]
        [CompareAttribute("Password")]
        public string ConfirmPassword { get; set; }

    }
}
