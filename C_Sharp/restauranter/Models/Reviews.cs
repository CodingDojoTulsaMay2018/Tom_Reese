using System;
using System.Collections.Generic;
using System.Globalization;
using System.ComponentModel.DataAnnotations;


namespace restauranter.Models
{

public class CustomDateAttribute : RangeAttribute
{
  public CustomDateAttribute()
    : base(typeof(DateTime), 
            DateTime.Now.AddYears(-6).ToShortDateString(),
            DateTime.Now.ToShortDateString()) 
  { } 
}


    public class Reviews
    {
        public long Id { get; set; }

        [Required]
        [MinLength(1), MaxLength(32)]


        public string Reviewer { get; set; }
        [Required]
        [MinLength(1), MaxLength(255)]

        public string Review { get; set; }
        [Required]
        public int Stars { get; set; }
        [Required]
        [MinLength(1), MaxLength(64)]

        public string Restaurant_Name { get; set; }

        [Required]
        [CustomDateAttribute]

        public DateTime Date { get; set; }

    }
}
