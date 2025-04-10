from datetime import date
from datetime import datetime
import time
#[seatName, Serial, passengerName,Price,Passward,bookDate, bookTime]
buslist = [["A1",1,None,2000,None,None,None],
           ["A2",2,"Fahim",2000,1234,"2025-04-10","10:10"],
           ["A3",3,None,2000,None,None,None],
           ["A4",4,None,2000,None,None,None],
           ["B1",5,"Nirob",2000,1234,"2025-04-09","10:50"],
           ["B2",6,"Faraf",2000,2345,"2025-04-07","08:07"],
           ["B3",7,None,2000,None,None,None],
           ["B4",8,"Avro",2000,3456,"2025-04-05","10:08"],
           ["C1",9,"Nibir",2000,4567,"2025-04-01","08:10"],
           ["C2",10,"Sakib",2000,5678,"2025-04-11","10:02"],
           ["C3",11,"Sultan",2000,6789,"2025-04-03","07:04"],
           ["C4",12,"Fahad",2000,1234,"2025-04-05","15:02"],
           ["D1",13,"Nayem",2000,2345,"2025-04-02","17:19"],
           ["D2",14,None,2000,None,None,None],
           ["D3",15,"Rakib",2000,2580,"2025-04-10","20:25"],
           ["D4",16,None,2000,None,None,None],
           ["E1",17,None,2000,None,None,None],
           ["E2",18,None,2000,None,None,None],
           ["E3",19,None,2000,None,None,None],
           ["E4",20,None,2000,None,None,None]]
info=["Dhaka","Jashore","Khulna","08:00 AM", "11:00 AM", "12:00 PM"]
today = date.today()
now = datetime.now().strftime("%H:%M")

print("====================================")
print("     🚌 Welcome to Bus Service 🚌    ")
print("====================================")
b=len(buslist)

choice=-1
while choice!=0:
    
    # Display the menu for book and cancel ticket
    print("🎫 What would you like to do?")
    print("1️⃣  Show Available Seats")
    print("2️⃣  Book a Ticket")
    print("3️⃣  Check Specific Ticket Details")
    print("4️⃣  Journey Details")
    print("5️⃣  Download Your Ticket")
    print("6️⃣  Cancel a Ticket")
    print("7️⃣  Check All Ticket Status")
    print("8️⃣  All Information")
    print("0️⃣  Exit")
    print("\n" + "="*40)
    choice = int(input("👉 Select Option:"))

    if choice==1:
        count=0
        for i in range(b):
            if buslist[i][2]==None:
                count+=1
                print(f"✅ Seat Name: {buslist[i][0]} | Serial No: {buslist[i][1]}")

        print(f"\n🟢 Total Available Seats: {count}")
        print("         " + "="*20)

    elif choice == 2:
        tic = int(input(f"Enter Seat No(1-{b}):"))
        f=tic-1
        for i in range(b):
            if buslist[f][2]==None:
                a=input("Enter Passenger Name:")
                otp=int(input("Enter 4 digit passward for Security:"))
                buslist[f][2]=a
                print("\n📝 Booking Ticket is Processing...")
                buslist[f][4]=otp
                buslist[f][5]=today
                buslist[f][6]=now
                time.sleep(0.5)
                print(f"🎉 Seat {buslist[f][0]} successfully booked for {a}!")
                print(f"You have to pay TK BDT.{buslist[f][3]}")
                print("         " + "="*20)
                break
            else:
                print("❌ This seat is already booked.")
                print("ℹ️  Use Option 1 to check available seats.")
                print("         " + "="*20)
                break
    elif choice == 3:
        print("\n🔍 Ticket Details:")
        tic = int(input("Enter seat no:"))
        if tic>b or tic<=0 or buslist[tic-1][2] is None:
            print("⚠️ Enter Seat Number Correctly!")
        elif tic<=b:
            name=input("Enter Your Name:")
            if buslist[tic-1][2]==name:
                for i in range(b):
                    print(f"\n🎟Ticket Information for {name}:")
                    print(f"🪑 Seat Number: {buslist[tic-1][0]}")
                    print(f" ⃣ Serial Number: {buslist[tic-1][1]}")
                    print(f"💵 Ticket Price: {buslist[tic-1][3]} tk")
                    print(f"Booking Date   : {(buslist[tic-1][5])}║{buslist[tic-1][6]} ")
                    print(">> Thank you for booking with us!")
                    print("         " + "="*20)
                    break
            else:
                print("Information doesn't match.Please Try again!")
                print("         " + "="*20)
    
    elif choice == 4:
        print("\n💌 Dear Passenger,\n")
        print(f"🚌 Bus Route: {info[0]}  ➡️  {info[1]} ➡️  {info[2]}")
        print("📅 Daily Schedule:\n")
        print(" ╔════════════╦════════════╦════════════╗")
        print(f" ║ {info[0].center(10)} ║ {info[1].center(10)} ║ {info[2].center(10)} ║")
        print(" ╠════════════╬════════════╬════════════╣")
        print(f" ║ {info[3].center(10)} ║ {info[4].center(10)} ║ {info[5].center(10)} ║")
        print(" ╚════════════╩════════════╩════════════╝\n")

        print("📍 Please arrive at the terminal at least 15 minutes early.")
        print("Thank you for choosing Green Line!")
        print("         " + "="*20)

    elif choice ==5:
        name=input("Enter User Name:")
        pas= int(input("Enter Your Passward:"))
        flag=False
        for i in range(b):
            if buslist[i][2]==name and buslist[i][4]==pas:
                flag=True
                print("Downloading...")
                time.sleep(0.5)
                print(f"----------------------")
                print(f"     Green Line        ")
                print(" " + "="*20)
                print(f"Passenger Name : {buslist[i][2]}")
                print(f"Seat No.       : {buslist[i][0]}")
                print(f"Journey Date   : {today}")
                print(f"Departure      : {info[0]}")
                print(f"Destination    : {info[2]}")
                print(f"Departure Time : {info[3]}")
                print(f"Ticket No.     : {buslist[i][1]}")
                print(f"Booking Date   : {(buslist[i][5])}║{buslist[i][6]} ")
                print(f"Fare           : BDT.{buslist[i][3]}")
                print(f"----------------------")
                print("Have a safe journey!")
                break
        if flag==False:
            print("⚠ invalid username & passward")
    
    elif choice == 6:
        print("\n🗑 Cancel a Ticket")
        tic = int(input("🎫 Enter Seat Number to Cancel: "))
        otp=int(input("Enter Your 4 digit passward:"))
        flag=False
        for i in range(b):
            if buslist[tic-1][4]==otp:
                flag=True
                print("✅ OTP Match. Please wait for confirmation...")
                time.sleep(0.5)
                print(f"🧑‍ Dear {buslist[tic-1][2]}")
                print(f"✅ Ticket for Seat {buslist[tic-1][0]} has been cancelled.")
                print(f"You will get TK BDT.{buslist[tic-1][3]}")
                print("         " + "="*20)
                buslist[tic-1][2] = None
                buslist[tic-1][4] = None
                buslist[tic-1][5] = None
                buslist[tic-1][6] = None
                break
        if flag==False:
            print("⚠ OTP Didn't Match!")
    
    elif choice == 7:
        print("N.B: Only admin can see this info.")
        a=input("Enter passward to see information:")
        flag=False
        if a=="admin":
            flag=True
            count=0
            print("\n🧾 All Ticket Status:")
            status="Availabe"
            for i in range(b):
                if buslist[i][2] is None:
                    count+=1
                    status="Availabe"
                    print(f"🟩 {buslist[i][0]} | Serial: {buslist[i][1]} | Status: {status}")
                else:
                    status=f"Booked by {buslist[i][2]}"
                    print(f"🟥 {buslist[i][0]} | Serial: {buslist[i][1]} | Status: {status}")
        else:
            print("⚠ Wrong Password")
    
        if flag==True:
            print(f"\n 🟩 Total Available Seats: {count} || 🟥 Sold Out seats:{b-count}")
        print("         " + "="*20)

    elif choice == 8:
        print("N.B: Only admin can see this info.")
        a=input("Enter passward to see information:")
        if a=="admin":
            print(buslist)
        else:
            print("⚠ Wrong Password")

    elif(choice == 0):
        print("✉️  Thanks for choosing us!")
        exit()