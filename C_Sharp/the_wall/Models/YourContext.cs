using the_wall.Models;
using Microsoft.EntityFrameworkCore;
 
namespace the_wall.Models
{
    public class YourContext : DbContext
    {
        public YourContext(DbContextOptions<YourContext> options) : base(options) { }
        public DbSet<User> users { get; set; }
        public DbSet<Comment> comments { get; set; }
        public DbSet<Message> messages { get; set; }

    }
}