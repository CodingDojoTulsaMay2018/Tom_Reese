using System;
using System.Collections.Generic;

namespace singly_linked
{
    class Program
    {
        static void Main(string[] args)
        {
            SinglyLinkedList bourbon = new SinglyLinkedList();
            bourbon.add("Bookers");
            bourbon.add("PVW 20th");
            bourbon.add("Little Book");
            bourbon.add("John F. Fitzgerald");
            bourbon.add("Rare Breed");
            bourbon.add("Evan Williams White");
            // bourbon.remove();
            // bourbon.remove();
            // bourbon.remove();
            // bourbon.remove();
            // bourbon.remove();
            // bourbon.remove();
            bourbon.printValues();
            bourbon.find("Rare Breed");
            bourbon.add("Jim Beam");
            bourbon.removeAt("Jim Beam");
        }
    }
}
