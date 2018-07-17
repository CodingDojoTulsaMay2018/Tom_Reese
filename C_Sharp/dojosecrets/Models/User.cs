using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;


namespace dojosecrets.Models{
    public class User
    {
        [Key]
        public int Id {get;set;}

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

        public List<Secret> Secrets {get; set;}

        public DateTime Created_At {get; set;} = DateTime.Now;
        
        [Required]
        [DataType(DataType.Password)]
        [MinLength(8)]
        public string Password { get; set; }

        [NotMapped]
        [CompareAttribute("Password")]
        public string ConfirmPassword { get; set; }

        public User()
        {
            Created_At = DateTime.Now;
            Secrets = new List<Secret>();

        }
    }
        public class UserLog
        {

        [Required(ErrorMessage = "Email for login doesn't exist")]
        [EmailAddress]
        [Column("email")]
        public string LogEmail { get; set; }
                
        [Required(ErrorMessage = "Password is incorrect")]
        [DataType(DataType.Password)]
        [MinLength(8)]
        [Column("password")]
        public string LogPassword { get; set; }
}

    }

    
