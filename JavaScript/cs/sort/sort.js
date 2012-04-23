var sort = {};

//n log(n) : log(n) partitions, n operations
//if list is already sorted, quicksort will work slow
sort.quickSort =  function (a) {
    var that = sort;
    if (a.length == 0) return [];

    var left = [], right = [], pivot = a[0];

    for (var i = 1; i < a.length; i++) {
        a[i] < pivot ? left.push(a[i]) : right.push(a[i]);
    }

    return that.quickSort(left).concat(pivot, that.quickSort(right));
}

//n^2
sort.insertionSort = function (sortMe) {
   for (var i = 0, j, tmp; i < sortMe.length; ++i) {
      tmp = sortMe[i];
      for (j = i - 1; j >= 0 && sortMe[j] > tmp; --j)
         sortMe[j + 1] = sortMe[j];
      sortMe[j + 1] = tmp;
   }
   return sortMe;
};

//n
sort.bucketSort = function (arr) {
    var buckets = [];

    for(var i = 0; i < arr.length; i++) {
        var item = arr[i];
        buckets[i] = buckets[i] ? buckets[i] :  0;
        buckets[item] = buckets[item] ? buckets[item] : 0;
        buckets[item]++;
    }

    var result = [];

    for(var i = 0; i < buckets.length; i++) {
        var amount = buckets[i];
        for(j = 0; j < amount; j++) {
            result.push(i);
        }
    }

    return result;
};



//n log(n)
sort.mergeSort = function (arr) {

    var  mergeSort = function (arr) {
        if (arr.length < 2)
            return arr;
     
        var middle = parseInt(arr.length / 2);
        var left   = arr.slice(0, middle);
        var right  = arr.slice(middle, arr.length);
     
        return merge(mergeSort(left), mergeSort(right));
    }
     
    function merge(left, right) {
        var result = [];
     
        while (left.length && right.length) {
            if (left[0] <= right[0]) {
                result.push(left.shift());
            } else {
                result.push(right.shift());
            }
        }
     
        while (left.length)
            result.push(left.shift());
     
        while (right.length)
            result.push(right.shift());
     
        return result;
    }


    return mergeSort(arr);
};


//n2
sort.bubbleSort = function (a) {
    var swapped;
    do {
        swapped = false;
        for (var i=0; i < a.length-1; i++) {
            if (a[i] > a[i+1]) {
                var temp = a[i];
                a[i] = a[i+1];
                a[i+1] = temp;
                swapped = true;
            }
        }
    } while (swapped);
    
    return a;
}
