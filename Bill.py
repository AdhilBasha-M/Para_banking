from data import items
class customers():
    i = items.i
    itemp = items.itemp
    item = items.item
    oritem = items.oritem
    t = int(input())
    while ((t >= 1) and (t <= 5)):
        i = i + 1
        print('Number of quantity required')
        n = int(input())
        t1 = item[t]  # extracts item name
        t2 = itemp[t1]  # extracts price of an item
        tc = n * t2
        oritem = oritem + [item[t], itemp[t1], n, tc]
        print('List of items')
        print('1.Soap-Rs.10\n2.Rice-Rs.20\n3.Dhall-Rs.20')
        print('4.Bread-Rs.10\n5.Paste-Rs.20\n6.Exit')
        print('Enter your choice 1 to 5 for purchase 6 for exit')
        t = int(input())