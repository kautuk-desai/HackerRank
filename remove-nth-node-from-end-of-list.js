/**
 * Definition for singly-linked list.
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
function ListNode(val) {
    this.val = val;
    this.next = null;
}

var removeNthFromEnd = function (head, n) {
    var count = 0;
    var node = head;
    console.log(JSON.stringify(head));
    while (node) {
        count++;
        node = node.next;
    }

    if (count < n || count == 1) {
        return null;
    }
    else if(n === count){
        head = head.next;
        return head;
    }
    else {
        deleteNode(head, n, count, 0);
        return head;
    }
};

var deleteNode = function (head, n, count, index) {
    if (index + n === count - 1) {
        head.next = head.next.next;
        return;
    }
    else {
        deleteNode(head.next, n, count, index + 1);
    }
}

//var head = { "val": 1, "next": { "val": 2, "next": { "val": 3, "next": null } } };
//var head = { "val": 1, "next": null };
var head = {"val":1,"next":{"val":2,"next":{"val":3,"next":{"val":4,"next":{"val":5,"next":{"val":6,"next":{"val":7,"next":{"val":8,"next":{"val":9,"next":{"val":10,"next":{"val":11,"next":null}}}}}}}}}}};

var result = removeNthFromEnd(head, 11);
console.log(result);