# for loop with the largest number from list
def known_great():
    print("this will tell you what item on your list is the greatest")
    k = int(input("enter the amount of item on your list: "))
    list_1 = []
    for x in range(k):
        f = int(input("enter the items on your list: "))
        list_1.append(f)
    list_1.sort()
    print("the greatest item on this list is", list_1[-1])


# for loop with the smallest number from list
def known_small():
    print("this will tell you what item on your list is the smallest")
    w = int(input("enter the amount of item on your list: "))
    listed = []
    for z in range(w):
        v = int(input("enter the items on your list: "))
        listed.append(v)
    listed.sort()
    print("the smallest item on this list is", listed[0])


# while loop with the greatness number from list
def unknown_great():
    print("this will tell you what item on your list is the greatest")
    print("to stop the list type stop")
    t = 0
    hold = []
    while t != 1:
        c = input("enter the items on your list: ")
        if c == "stop":
            t = t + 1
        else:
            int_1 = int(c)
            hold.append(int_1)
    hold.sort()
    print("the greatest item on this list is", hold[-1])


# while loop with the smallest number from list
def unknown_small():
    print("this will tell you what item on your list is the smallest")
    print("to stop the list type stop")
    h = 0
    hold_1 = []
    while h != 1:
        st = input("enter the items on your list: ")
        if st == "stop":
            h = h + 1
        else:
            int_2 = int(st)
            hold_1.append(int_2)
    hold_1.sort()
    print("the smallest item on this list is", hold_1[0])

