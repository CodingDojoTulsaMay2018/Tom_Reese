using dojosecrets.Models;
using Microsoft.EntityFrameworkCore;
 
namespace dojosecrets.Models
{
    public class YourContext : DbContext
    {
        public YourContext(DbContextOptions<YourContext> options) : base(options) { }
        public DbSet<User> users { get; set; }
        public DbSet<Secret> secrets { get; set; }
        public DbSet<Like> likes { get; set; }

    }
}