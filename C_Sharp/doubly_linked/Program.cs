using System;
using System.Collections.Generic;

namespace doubly_linked
{
    class Program
    {
        static void Main(string[] args)
        {
            DoublyLinkedList tom = new DoublyLinkedList();
            tom.add(0);
            tom.add(1);
            tom.add(2);
            tom.add(3);
            tom.add(4);
            // tom.remove(7);
            // tom.remove(4);
            tom.remove(0);
            // tom.remove(2);
            tom.reverse();
        }
    }
}
