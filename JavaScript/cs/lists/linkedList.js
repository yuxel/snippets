var linkedList = {};

//ref : http://www.nczonline.net/blog/2009/04/13/computer-science-in-javascript-linked-list/
linkedList.Singly = function () {
    this._length = 0;
    this._head = null;
};


linkedList.Singly.prototype.print = function (){
    var result = [];
    
    var current = this._head;
   
    while(current.next) {
        result.push(current.data);
        current = current.next;
    }
    
    result.push(current.data);

    console.log(result);
};


linkedList.Singly.prototype.reverse = function (){
    var aux,
        prev = null;

    while (this._head) {
        aux = this._head.next;
        this._head.next = prev;
        prev = this._head;
        this._head = aux;
    }
    this._head = prev;
};


linkedList.Singly.prototype.add = function (data){
        var node = {
                data: data,
                next: null
            },

            current;

        if (this._head === null){
            this._head = node;
        } else {
            current = this._head;

            while(current.next){
                current = current.next;
            }

            current.next = node;
        }

        this._length++;
};



///////
// ref: http://www.nczonline.net/blog/2009/04/21/computer-science-in-javascript-doubly-linked-lists/

linkedList.Doubly = function () {
    this._length = 0;
    this._head = null;
    this._tail = null;
};


linkedList.Doubly.prototype.add = function (data) {

    var node = {
        data: data,
        next: null,
        prev: null
    };

    //special case: no items in the list yet
    if (this._length == 0) {
        this._head = node;
        this._tail = node;
    } else {
        //attach to the tail node
        this._tail.next = node;
        node.prev = this._tail;
        this._tail = node;
    }        

    //don't forget to update the count
    this._length++;
};

linkedList.Doubly.prototype.reverse = function (){
    var aux,
        prev = null;

    while (this._head) {
        aux = this._head.next;
        this._head.next = prev;
        prev = this._head;
        this._head = aux;
    }
    this._head = prev;
};


linkedList.Doubly.prototype.print = function (){
    var result = [];
    
    var current = this._head;
   
    while(current.next) {
        result.push(current.data);
        current = current.next;
    }
    
    result.push(current.data);

    console.log(result);
};



