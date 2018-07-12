using login_reg.Models;
using Microsoft.EntityFrameworkCore;
 
namespace login_reg.Models
{
    public class YourContext : DbContext
    {
        public YourContext(DbContextOptions<YourContext> options) : base(options) { }
        public DbSet<User> users { get; set; }
    }
}