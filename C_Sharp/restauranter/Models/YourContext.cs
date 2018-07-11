using restauranter.Models;
using Microsoft.EntityFrameworkCore;
 
namespace restauranter.Models
{
    public class YourContext : DbContext
    {
        public YourContext(DbContextOptions<YourContext> options) : base(options) { }
        public DbSet<Reviews> reviews { get; set; }
    }
}
