var search = {};

// log n
search.binarySearch = function(needle, haystack) {
    if (typeof(haystack) === 'undefined' || !haystack.length) return -1;

    var mid, element;

    var high = haystack.length - 1;
    var low = 0;

    while (low <= high) {
        console.log('try');
        mid = parseInt((low + high) / 2);
        element = haystack[mid];
        if (element > needle) {
            high = mid - 1;
        } else if (element < needle) {
            low = mid + 1;
        } else {
            return mid;
        }
    }
    return -1;
};



