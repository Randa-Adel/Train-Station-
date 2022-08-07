# Train Station

def book(Train,carriages):
   crNum = int(input("Enter The Carriage Number : "))
   crseat = int(input("Enter The Seat Number : "))
   if Train[crNum-1][2][crseat-1] == 1:
       print("This Seat Already Reserved !")
   else :
       Train[crNum-1][2][crseat-1] = 1
       print(f"You Succesfully Reserve Seat {crseat} in Carriage {crNum}")


def cancel(Train,carriages):
    crNum = int(input("Enter The Carriage Number : "))
    crseat = int(input("Enter The Seat Number : "))
    if Train[crNum-1][2][crseat-1] == 0:
        print("This Seat Already Not Reserved !")
    else:
        Train[crNum-1][2][crseat-1] = 0
        print(f"You Succesfully Cancel The Reservation Of Seat {crseat} in Carriage {crNum}")
def show_Available_Seat(Train,carriages):
    for i in range(carriages):
        print(f"Avalible Seats In Carriage {i+1}")
        for j in Train[i][2]:
            if Train[i][2][j] == 0:
                print(f"The Seat Number {j+1}")

def Print_Profits(Train,carriages):
    Total_Profits = 0
    for i in range(carriages):
        prof = Train[i][1]
        for j in Train[i][2]:
            if Train[i][2][j] == 1:
                Total_Profits += prof
    print(f"THE TOTAL PROFITS IN TRAIN  = {Total_Profits}")
    print("-"*50)



def menu():
    print("Enter 1 To Book A Ticket .")
    print("Enter 2 To Cancel A Ticket .")
    print("Enter 3 To Show Available Seat .")
    print("Enter 4 To Print Profits in Details .")
    print("Enter 0 To Exit .")
    choice = int(input("Your Choice : "))
    print("*"*30)
    return choice
def Main():
    carriages = int(input("Enter The Number Of Carriages : "))
    Train = {}
    for i in range(carriages):
        print(f"Carrige#{i+1}")
        carriage_class = int(input("Enter Class : "))
        carriage_Price = int(input("Enter Price : "))
        carriage_Reserved_seat = {i: 0 for i in range(30)}
        x = {i: (carriage_class, carriage_Price, carriage_Reserved_seat)}
        Train.update(x)
    print("*" * 30)
    flag = True
    while flag:
        choice = menu()
        if choice == 0:
            flag = False
        elif choice == 1:
            book(Train,carriages)
        elif choice == 2:
            cancel(Train,carriages)
        elif choice == 3:
            show_Available_Seat(Train,carriages)
        elif choice == 4:
            Print_Profits(Train,carriages)




Main()

