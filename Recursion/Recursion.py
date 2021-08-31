def lookForKey(box):
    for item in box:
        if item.isaBox():
            lookForKey(item)    # Recursive case
        elif item.isaKey():
            print("found the key")  # Base case