def bubble_sort(zoznam):
    print("Pôvodný zoznam: ",zoznam)
    for i in zoznam:
        for i in range(0,len(zoznam)-1):
            x = zoznam[i]
            if x > zoznam[i+1]:
                zoznam[i],zoznam[i+1] = zoznam[i+1],zoznam[i]
            else:
                continue
    print("Upravený zoznam použitím bubble sortu: ",zoznam)
bubble_sort([23,10,18,50,3,90,32,48])
