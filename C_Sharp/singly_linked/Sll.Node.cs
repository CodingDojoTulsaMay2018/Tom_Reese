using System;
using System.Collections.Generic;

namespace singly_linked{

public class SllNode
{
    public string value;
    public SllNode next;
    public SllNode(string value) 
    {
    this.value = value;
    next = null;
    }
}
}