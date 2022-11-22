def bubble_sort(zoznam):
    print(zoznam)
    for i in zoznam:
        for i in range(0,len(zoznam)-1):
            x = zoznam[i]
            if x > zoznam[i+1]:
                zoznam[i],zoznam[i+1] = zoznam[i+1],zoznam[i]
            else:
                continue
    return zoznam
print(bubble_sort([23,10,18,50,3,90,32,48]))
