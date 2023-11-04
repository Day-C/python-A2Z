
def printpicnic(itemsDict, left_just, right_just):
    print('PICNIC ITEMS'.center(left_just + right_just, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(left_just, '.') + str(v).rjust(right_just))

picnicitems = {"sandwiches": 4, "apples": 5, "cups": 4, "cookies":200}
printpicnic(picnicitems, 12, 5)
printpicnic(picnicitems, 20, 6)
