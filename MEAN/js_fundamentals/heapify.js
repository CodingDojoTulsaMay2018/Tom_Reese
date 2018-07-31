function heapify(heap){
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

heapify([20, 3, 8, 14, 9, 6, 2]);

