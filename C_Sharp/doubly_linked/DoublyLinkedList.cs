using System;
using System.Collections.Generic;

namespace doubly_linked
{

public class DoublyLinkedList
{
    public DllNode head;
    public DllNode tail;
    public DoublyLinkedList() 
    {
        head = null;
        tail = null;
    }

    public void add(int value) 
    {
        DllNode newNode = new DllNode(value);
        if(head == null) 
        {
            head = newNode;
            tail = newNode;
            Console.WriteLine(newNode.value+" is the new node, and the head of the list!");
        } 
        else
        {
            DllNode runner = head;
            while(runner.next != null) {
                runner = runner.next;
            }
            runner.next = newNode;
            newNode.prev = runner;
            tail = newNode;
            Console.WriteLine(runner.next.value+" has been added to the list! And the previous node was "+newNode.prev.value);
        }
    }    

    public bool remove(int num) 
    {
        System.Console.WriteLine("Attemping to remove "+num+" from the list");
        if(head == null) 
        {
            return false;
        } 
        var runner = head;
        if(num == head.value && head.next != null){
            System.Console.WriteLine(num+" is the head, and we are going to remove the head from the list, and make sure "+head.next.value+" is the new head");
            head = head.next;
            head.prev = null;
            System.Console.WriteLine(head.value+" is the new head, and the next node is "+head.next.value);
            return true;
        }
        if(num == head.value && head.next == null){
            System.Console.WriteLine(num+" is the head, and we are going to remove the head from the list");
            head = null;
            return true;
        }
        else
        {
        while(runner.value != num) {
            if (runner.next == null && runner.value != num){
                System.Console.WriteLine(num+" is not in the list!");
                return false;
            }
            runner = runner.next;
        }
            if(runner.next == null){
                System.Console.WriteLine(runner.value+" was the last node in the list.  The new last node in the list is "+runner.prev.value);
                runner.prev = tail;
                runner.prev.next = null;
                return true;
            }
             System.Console.WriteLine(runner.value+" was found in the list.  The new order, after removal will be "+runner.prev.value+" then "+runner.next.value);
            runner.prev.next = runner.next;
            runner.next.prev = runner.prev;
            return true;
        }
    } 

    public void reverse() 
    {
        if(head == null) 
        {
            System.Console.WriteLine("no nodes in this list!!!");
        } 
        if(head == tail) 
        {
            System.Console.WriteLine("only one node in this list!!!");
        } 
        else
        {
            DllNode yup = null;
            tail = head;
            var runner = head;
            System.Console.WriteLine("Reversing the list, starting at "+runner.value);
            while(runner != null) {
                yup = runner.prev;
                runner.prev=runner.next;
                runner.next = yup;
                System.Console.WriteLine(runner.value+" is the runner value");
                runner = runner.prev;
            }
            if(yup != null){
                head = yup.prev;
            }
            System.Console.WriteLine(head.value+" is the new head and "+tail.value+" is the new tail");
        }
    } 

   
    } 
}
