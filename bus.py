import time
#[Seat_Name, Serial, Passenger_Name,Price,Passward]
buslist = [["A1",1,None,2000,None],
           ["A2",2,"Fahim",2000,1234],
           ["A3",3,None,2000,None],
           ["A4",4,None,2000,None],
           ["B1",5,"Nirob",2000,1234],
           ["B2",6,"Faraf",2000,2345],
           ["B3",7,None,2000,None],
           ["B4",8,"Avro",2000,3456],
           ["C1",9,"Nibir",2000,4567],
           ["C2",10,"Sakib",2000,5678],
           ["C3",11,"Sultan",2000,6789],
           ["C4",12,"Fahad",2000,1234],
           ["D1",13,"Nayem",2000,2345],
           ["D2",14,None,2000,None],
           ["D3",15,"Rakib",2000,2580],
           ["D4",16,None,2000,None],
           ["E1",17,None,2000,None],
           ["E2",18,None,2000,None],
           ["E3",19,None,2000,None],
           ["E4",20,None,2000,None]]
#Journey info
info=["Dhaka","Jashore","Khulna","08:00 AM", "11:00 AM", "12:00 PM"]

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
                time.sleep(2)
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

    

    elif(choice == 0):
        exit()