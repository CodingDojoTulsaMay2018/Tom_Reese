function insertIntoHeap(heap, val){
    if(!heap.length){
        heap.push(undefined);
        heap.push(val);
        return heap;}
        heap.push(val);
    var i = heap.length-1;
    while(i >=2){
        if(heap[i-1] > heap[i] && heap[i-1] != undefined){
            temp = heap[i-1];
            heap[i-1] = heap[i];
            heap[i] = temp;
            i--
            continue;
        }
        i--;
        continue;
    }
    console.log(heap);
}
    insertIntoHeap([], 13);
    insertIntoHeap([undefined, 3, 8, 10, 11, 9, 20, 14], 7);