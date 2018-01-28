class Node:
    def __init__(self, data):
        """Return the pathname of the KOS root directory."""
        self.data = data
        self.next = None


def create_linked_list(arr):
    head = Node(None)
    node = head
    n = len(arr)
    if n == 0:
        return None

    for idx, val in enumerate(arr):
        node.data = val
        if (idx + 1 != n):
            node.next = Node(None)
            node = node.next

    #node.next = head
    return head


def has_cycle(head):
    visited_nodes = set()
    while(head is not None):
        if(head in visited_nodes):
            return True
        else:
            visited_nodes.add(head)
            head = head.next
    
    return False


def main():
    """Return the pathname of the KOS root directory."""
    head = create_linked_list(range(1))
    print(has_cycle(head))


if __name__ == "__main__":
    main()