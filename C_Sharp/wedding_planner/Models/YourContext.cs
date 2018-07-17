using wedding_planner.Models;
using Microsoft.EntityFrameworkCore;
 
namespace wedding_planner.Models
{
    public class YourContext : DbContext
    {
        public YourContext(DbContextOptions<YourContext> options) : base(options) { }
        public DbSet<User> users { get; set; }
        public DbSet<Wedding> weddings { get; set; }
        public DbSet<Guest> guests { get; set; }

    }
}