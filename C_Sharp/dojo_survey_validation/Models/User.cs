using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
    
    namespace dojo_survey_validation.Models
    {
    public class User
    {
        [Required]
        [MinLength(2),MaxLength(15)]
        public string Name { get; set; }

        [Required]
        [MinLength(2),MaxLength(15)]
        public string Language { get; set; }
        
        [MinLength(3)]
        public string Location { get; set; }


        [MinLength(8),MaxLength(30)]
        public string Comment { get; set; }
 
    }
}