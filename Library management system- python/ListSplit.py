def listSplit():
    global bookname
    global authorname
    global quantity
    global cost
    bookname=[]
    authorname=[]
    quantity=[]
    cost=[]
    with open("dipinlibrarystock.txt","r") as f:
        
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]
        for dipin in range(len(lines)):
            dipin1=0
            for a in lines[dipin].split(','):
                if(dipin1==0):
                    bookname.append(a)
                elif(dipin1==1):
                    authorname.append(a)
                elif(dipin1==2):
                    quantity.append(a)
                elif(dipin1==3):
                    cost.append(a.strip("$"))
                dipin1+=1
