#debangshu
import os
import pickle
print("*****WELCOME TO MARINA's HOTEL******")
#---------------------------------------------------

a_list=[]
b_list=[]
c_list=[]
d_list=[]
s_list=[]
r_list=[]
p_list=[]
t_list=[]
rno=101
adsc=1899
def parttwo():
    a=input("\nEnter your name ")
    a_list.append(a)
    b=input("Enter your address ")
    b_list.append(b)
    c=input("Enter your check in date ")
    c_list.append(c)
    d=input("Enter your checkout date ")
    d_list.append(d)
    #---------------------------------------------------
def roomfunction():
    print ("****We have the following rooms for you****")
    print ("1.  Type A---->Rs 18500 Per Night\-")
    print ("2.  Type B---->Rs 15500 Per Night\-")
    print ("3.  Type C---->Rs 12500 Per Night\-")
    print ("4.  Type D---->Rs 9500 Per Night\-")
    x=int(input("****ENTER THE ROOM YOU WANT TO BOOK**** "))
    n=int(input("****DAYS OF STAY**** "))
    if(x==1):
        print ("You have opted room Type-->A")
        s=18500*n
        s_list.append(s)
    elif (x==2):
        print ("you have opted room Type-->B")
        s=15500*n
        s_list.append(s)
    elif (x==3):
        print ("you have opted room Type-->C")
        s=12500*n
        s_list.append(s)
    elif (x==4):
        print ("you have opted room Type-->D")
        s=9000*n
        s_list.append(s)
    else:
        print ("***PLEASE CHOOSE A ROOM FROM THE ABOVE CATEGORIES***")
    print ("Your Room Rent is = ",s,"\n")
    #---------------------------------------------------
def restaurantbill():
    print("*****RESTAURANT MENU*****")
    print("1.Water----->Rs->60/-","\n2.Tea----->Rs->149/-","\n3.Coffee----->Rs->199/-","\n4.Breakfast Combo--->Rs->499/-",
          "\n5.Lunch(VEG)---->Rs->649/-","\n6.Lunch(NON-VEG)---->Rs->999/-","\n7.Dinner(VEG)--->Rs->649/-","\n8.Dinner(NON-VEG)----->Rs->999/-","\n9.Exit")
    while(1):
        c=int(input("Enter your choice:"))
        
        if (c==1):
            d=int(input("Enter the number of MINERAL WATER BOTTLES: "))
            r=60*d
            r_list.append(r)
        elif (c==2):
            d=int(input("Enter the number of TEA(CUPS) you want: "))
            r=149*d
            r_list.append(r)
        elif (c==3):
            d=int(input("Enter the number of COFFEE(CUPS) you want: "))
            r=199*d
            r_list.append(r)
        elif (c==4):
            d=int(input("Enter the number of BREAKFAST COMBO's Required: "))
            r=499*d
            r_list.append(r)
        elif (c==5):
            d=int(input("Enter the number of LUNCH(VEG) Plates Required: "))
            r=649*d
            r_list.append(r)
        elif (c==6):
            d=int(input("Enter the number of LUNCH(NON-VEG) Plates Required: "))
            r=999*d
            r_list.append(r)
        elif (c==7):
            d=int(input("Enter the number of DINNER(VEG) Plates Required: "))
            r=649*d
            r_list.append(r)
        elif (c==8):
            d=int(input("Enter the number of DINNER(VEG) Plates Required: "))
            r=999*d
            r_list.append(r)
        elif(c==9):
            break
        else:
            print ("INVALID OPTION")
    print ("Total Food Cost=Rs-",sum(r_list),"\n")
    #----------------------------------------------------    
def laundrybill():
    print ("******LAUNDARY MENU*******")
    print ("1.Shorts----->Rs-15/-","\n2.Trousers----->Rs-20/-","\n3.Shirt--->Rs-15","\n4.Jeans---->Rs-25/-","\n5.Suit--->Rs-30","\n6.Exit")
    while(1):
        e=int(input("Enter your choice: "))
        if (e==1):
            f=int(input("Enter the quantity:"))
            t=15*f
            t_list.append(t)
        elif (e==2):
            f=int(input("Enter the quantity:"))
            t=20*f
            t_list.append(t)
        elif (e==3):
            f=int(input("Enter the quantity:"))
            t=15*f
            t_list.append(t)
        elif (e==4):
            f=int(input("Enter the quantity:"))
            t=25*f
            t_list.append(t)
        elif (e==5):
            f=int(input("Enter the quantity:"))
            t=30*f
            t_list.append(t)
        elif(e==6):
            break
        else:
            print ("INVALID OPTION")               
    print ("Total Laundary Cost=Rs",sum(t_list),"\n")
    #-----------------------------------------------------------------
def gamebill():
    print ("******GAMES MENU*******")
    print ("1.Table tennis----->Rs-299/-","\n2.Bowling----->Rs-249/-","\n3.Snooker----->Rs-199/-","\n4.Video games----->Rs-120/-","\n5.Pool--->Rs-149/-","\n6.Exit")
    while(1):
        
        g=int(input("Enter your choice: "))
        if (g==1):
            h=int(input("No. of hours:"))
            p=299*h
            p_list.append(p)
        elif (g==2):
            h=int(input("No. of hours:"))
            p=249*h
            p_list.append(p)
        elif (g==3):
            h=int(input("No. of hours:"))
            p=199*h
            p_list.append(p)
        elif (g==4):
            h=int(input("No. of hours:"))
            p=120*h
            p_list.append(p)
        elif (g==5):
            h=int(input("No. of hours:"))
            p=149*h
            p_list.append(p)
        elif(g==6):
            break
        else:
            print ("INVALID OPTION")
    print ("Total Games Bill=Rs-",sum(p_list),"\n")
#--------------------------------------------------------------------
            
def display():
    rno=101
    for i in a_list:
        A=i
    for j in b_list:
        B=j
    for k in c_list:
        C=k
    for l in d_list:
        D=l
    for m in s_list:
        E=m
    for n in r_list:
        F=n
    for o in t_list:
        G=o
    for p in p_list:
        H=p
        
    print ("\n******HOTEL BILL******")
    print ("\nCUSTOMER DETAILS ")
    print ("\nCUSTOMER NAME:- ",A)
    print ("\nCUSTOMER ADDRESS:- ",B)
    print ("\nCHECK-IN DATE:- ",C)
    print ("\nCHECK-OUT DATE:- ",D)
    print ("\nROOM NUMBER:- ",rno)
    print ("\nTOTAL ROOM RENT:- ",E)
    print ("\nTOTAL FOOD BILL:- ",sum(r_list))
    print ("\nTOTAL LAUNDRY BILL:- ",sum(t_list))
    print ("\nTOTAL GAME BILL:- ",sum(p_list))

    total=E+sum(r_list)+sum(t_list)+sum(p_list)
    print ("----SUBTOTAL BILL AMOUNT---- ",total)
    print ("----ADDITIONAL SERVICE CHARGE---- ",adsc)
    print ("----GRANDTOTAL BILL AMOUNT---- ",total+adsc,"\n")
    rno+=1

    #main prog-----------------------------------------------------
parttwo()
roomfunction()
restaurantbill()
laundrybill()
gamebill()
display()
#________________________________________________
dv01=open("Debangshu01.dat","wb+") 
pickle.dump(a_list,dv01,pickle.HIGHEST_PROTOCOL)
pickle.dump(b_list,dv01,pickle.HIGHEST_PROTOCOL)
pickle.dump(c_list,dv01,pickle.HIGHEST_PROTOCOL)
pickle.dump(d_list,dv01,pickle.HIGHEST_PROTOCOL)
pickle.dump(s_list,dv01,pickle.HIGHEST_PROTOCOL)
pickle.dump(r_list,dv01,pickle.HIGHEST_PROTOCOL)
pickle.dump(p_list,dv01,pickle.HIGHEST_PROTOCOL)
dv01.close()


dv02=open("Debangshu01.dat","rb+")
try:
    while True:
        av01=pickle.load(dv02)
        for i in av01:
            print(i)
except EOFError:
    pass
