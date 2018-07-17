
using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Collections.Generic;

namespace dojosecrets.Models
{
    public class ViewModel
    {
        public User regUser {get; set;}
        public UserLog loginUser {get; set;}
    }
}