function ListNode(val) {
    this.val = val;
    this.next = null;
}

var mergeTwoLists = function (l1, l2) {
    var head = null;
    if (l1 && l2) {
        if (l1.val <= l2.val) {
            head = new ListNode(l1.val);
            merge(l1.next, l2, head);
        }
        else {
            head = new ListNode(l2.val);
            merge(l1, l2.next, head);
        }

        return head;
    }
    else if (l1) {
        return l1;
    }
    else if (l2) {
        return l2;
    }
    else {
        return head;
    }
};

var merge = function (l1, l2, head) {
    var node;
    if (l1 && l2) {
        if (l1.val <= l2.val) {
            node = new ListNode(l1.val);
            head.next = node;
            merge(l1.next, l2, node);
        }
        else {
            node = new ListNode(l2.val);
            head.next = node;
            merge(l1, l2.next, node);
        }
    }
    else if (l1) {
        node = new ListNode(l1.val);
        head.next = node;
        merge(l1.next, l2, node);
    }
    else if (l2) {
        node = new ListNode(l2.val);
        head.next = node;
        merge(l1, l2.next, node);
    }
};

l1 = {};
l2 = {};
var result = mergeTwoLists(l1, l2);
console.log(JSON.stringify(result));