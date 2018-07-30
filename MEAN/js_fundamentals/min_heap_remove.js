function removeFromMinHeap(heap){
        var i = heap.length-1;
        while(i >=0){
            if(heap[i-1] > heap[i]){
                temp = heap[i-1];
                heap[i-1] = heap[i];
                heap[i] = temp;
                i--
                continue;
            }
            i--;
            continue;
        }
        temp = heap[1];
        heap[1] = heap[0];
        heap[0] = temp; 
    var x = heap[0]
    heap.shift()
    console.log(heap);
    
    return x;
} 
    console.log(removeFromMinHeap([undefined, 3, 12, 8, 17, 13, 15, 10]));
    // changes the heap to [undefined, 8, 12, 10, 17, 13, 15] and returns 3
    console.log(removeFromMinHeap([undefined, 8]));
    // changes the heap to [undefined] and returns 8

