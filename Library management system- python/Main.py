import Return
import ListSplit
import dt
import Borrow

def start():
    while(True):
        print("                     Welcome to the library management system     ")
        print("-------------ITHARI INTERNATIONAL COLLEGE(project by dipinbhandari-20048435(londonmetid)---------------")
        print("Enter 101. To Display")
        print("Enter 202. To Borrow a book")
        print("Enter 303. To return a book")
        print("Enter 404. To exit")
        try:
            a=int(input("Select a choice from above: "))
            print()
            if(a==101):
                with open("dipinlibrarystock.txt","r") as f:
                    lines=f.read()
                    print(lines)
                    print ()
   
            elif(a==202):
                ListSplit.listSplit()
                Borrow.borrowBook()
            elif(a==303):
                ListSplit.listSplit()
                Return.returnBook()
            elif(a==404):
                print("Thank you for using library management system")
                break
            else:
                print("Please enter a valid choice from above")
        except ValueError:
            print("Please input as suggested.")
start()
