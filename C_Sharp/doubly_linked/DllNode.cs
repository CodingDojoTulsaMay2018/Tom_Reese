using System;
using System.Collections.Generic;

namespace doubly_linked
{


public class DllNode
{
    public int value;
    public DllNode next;
    public DllNode prev;
    public DllNode(int val) 
    {
    this.value = val;
    next = null;
    prev = null;
    }
}
}

