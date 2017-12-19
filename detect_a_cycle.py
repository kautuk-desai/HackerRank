def has_cycle(head):
    
    if head is None:
        return False
    else:
        list_set = set()
        
        while head is not None:
            if head.data in list_set:
                return True
            else:
                list_set.add(head.data)
                head = head.next
        
        return False``