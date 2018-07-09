using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
    
    namespace dojodachi.Models
    {
    public class Dachi
    {
    public int Happiness { get; set; }
    public int Fullness{ get; set; }
    public int Energy { get; set; }
    public int Meals { get; set; }
    }
}