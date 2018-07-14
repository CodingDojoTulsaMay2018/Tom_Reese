using System;
using System.Collections.Generic;
using System.Globalization;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;


namespace bank_accounts.Models
{

    public class Trans
    {
        [Key]
        public long Id_Trans { get; set; }

        public DateTime Created_At { get; set; } = DateTime.Now;
        public double Amount { get; set; } = 0.0;
        
        [Column("userid_user")]
        public User User { get; set; }

    }
}
