from Bill import customers
import re

class bills():
    i = customers.i
    itemp = customers.itemp
    item = customers.item
    oritem = customers.oritem

    print('\t\t D_MART BILLING SYSTEM')
    print('***************************************')
    print('Name\tPrice\tQuantity\tTotal')
    print('***************************************')
    ct = 0
    ind = 0
    for x in range(i):
        print("%s\t%0.2f\t\t%d\t\t%0.2f" % (oritem[ind], oritem[ind + 1], oritem[ind + 2], oritem[ind + 3]))
        ct = ct + oritem[ind + 3]
        ind = ind + 4
    print('_______________________________________')
    print('Total Amount = Rs %0.2f' % ct)


    id = input("Enter Customer ID = ")
    idcheck = "[A-Z]{2}[0-9]{3}"
    if re.search(idcheck, id):
        pass
    else:
        b = 1
        print("Incorrect Customer ID Please Check it!")
    if id.startswith("PI"):
        final = ct - (ct / 5)
        disc = "PI"
        b = 0
        print(f"Platinum Card Holder Discount (20%) = Rs {ct / 5}\nFinal Amount = Rs {final}")
        print("\nThank You and Visit Again")
    if id.startswith("GD"):
        final = ct - (ct / 10)
        disc="GD"
        b = 0
        print(f"Gold Card Holder Discount (10%) = Rs {ct / 10}\nFinal Amount = Rs {final}")
        print("\nThank You and Visit Again")
    if id.startswith("SI"):
        final = ct - (ct / 20)
        disc="SI"
        b = 0
        print(f"Silver Card Holder Discount (5%) = Rs {ct / 20}\nFinal Amount = Rs {final}")
        print("\nThank You and Visit Again")