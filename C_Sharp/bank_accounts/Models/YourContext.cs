using bank_accounts.Models;
using Microsoft.EntityFrameworkCore;
 
namespace bank_accounts.Models
{
    public class YourContext : DbContext
    {
        public YourContext(DbContextOptions<YourContext> options) : base(options) { }
        public DbSet<User> users { get; set; }
        public DbSet<Trans> transactions { get; set; }

    }
}