using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;


namespace wedding_planner.Models{
        public class UserLog
    {

        [Required(ErrorMessage = "Email for login doesn't exist")]
        [EmailAddress]
        [Column("email")]
        public string LogEmail { get; set; }
        
        public DateTime Updated_At {get; set;} = DateTime.Now;
        
        [Required(ErrorMessage = "Password is incorrect")]
        [DataType(DataType.Password)]
        [MinLength(8)]
        [Column("password")]
        public string LogPassword { get; set; }
}
}