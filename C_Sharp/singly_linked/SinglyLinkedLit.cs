using System;
using System.Collections.Generic;

namespace singly_linked{


public class SinglyLinkedList
{
    public SllNode head;
    public SinglyLinkedList() 
    {
        head = null;
    }

    public void add(string value) 
    {
        SllNode newNode = new SllNode(value);
        if(head == null) 
        {
            head = newNode;
            Console.WriteLine(newNode.value+" is the new node, and the head of the list!");
        } 
        else
        {
            SllNode runner = head;
            while(runner.next != null) {
                runner = runner.next;
            }
            runner.next = newNode;
            Console.WriteLine(runner.value+" has been added to the list!");
        }
    }    

    public bool remove() 
    {
        if(head == null) 
        {
            return false;
        } 
        else
        {
            var runner = head;
            while(runner.next.next != null) {
                runner = runner.next;
            }
            System.Console.WriteLine("Last node "+runner.next.value+" is being removed from the list");
            if(runner == head){
                System.Console.WriteLine(runner.value+" is the head, and we are going to remove the head from the list");
                head = null;
                return true;
            }
            runner.next = null;
            System.Console.WriteLine(runner.value+" is now the last node in the list.");
            return true;
        }
    } 

    public void printValues() 
    {
        if(head == null) 
        {
            System.Console.WriteLine("no nodes in this list!!!");
        } 
        else
        {
            System.Console.WriteLine("Printing values!");
            var runner = head;
            while(runner != null) {
                System.Console.WriteLine(runner.value);
                runner = runner.next;
            }
        }
    } 

    public object find(string label) 
    {
        System.Console.WriteLine("Finding a bourbon!");
        if(head == null){
        System.Console.WriteLine("This list is empty!");
        return null; 
        } 
        var runner = head;
        while(runner != null) {
            if(runner.value == label){
                Console.WriteLine(runner.value+" was matched with "+label);
                return runner;
            }
            runner = runner.next;
            }
            System.Console.WriteLine(label+" wasn't found in this list!");
            return label;
        }
    public object removeAt(string label) 
    {
        System.Console.WriteLine("Attempting to remove "+label+" from the list!");
        if(head == null){
        System.Console.WriteLine("This list is empty!");
        return null; 
        } 
        var runner = head;
        while(runner != null) {
            if(runner.next.value == label){
                Console.WriteLine(runner.next.value+" was matched with "+label);
                if(runner.next.next == null){
                    runner.next=null;
                    System.Console.WriteLine(label+" was the last node in the list.  Now the last node in the list is "+runner.value);
                    return runner;
                }
                runner.next = runner.next.next;
                System.Console.WriteLine(runner.value+" is where we are, and "+runner.next.value+" is what is next.");
                return runner.next;
            }
            runner = runner.next;
            }
            System.Console.WriteLine(label+" wasn't found in this list!");
            return label;
        }
    } 
}
