import time

def vend():
    print("Welcome to Vending Machine\nThis Machine accepts only 1$ and 5$\nSo please enter correct denominations \n")
    time.sleep(1)
    print("How many 1$ are you going to insert (enter 0 if none)")
    ones = int(input())
    print("How many 5$ are you going to insert (enter 0 if none)")
    fives = int(input())
    total = ones + (5 * fives)

    A_name = "Cotton Candy"
    B_name = "Sweet Candy"
    C_name = "Soda"
    D_name = "Potato Chips"
    # A_price = 6
    # B_price = 5
    # C_price = 3 
    # D_price = 4
    items1 = 0 
    items2 = 0
    items3 = 0
    items4 = 0
    
    A1 = 4
    A2 = 5
    A3 = 6
    A4 = 7
    B1 = 1
    B2 = 3
    B3 = 5
    B4 = 7
    C1 = 1
    C2 = 2
    C3 = 5
    C4 = 6
    D1 = 1
    D2 = 2
    D3 = 8
    D4 = 9
    bill = 0
    bpoint = 0
    while( total > 0 ):
         
        print("Total money you have is "+ str(total) + "$\n")
        print("what do you like to buy?\n") 
        time.sleep(1)
        print ("1.{}, | enter 1".format(A_name))
        print ("2.{}, | enter 2".format(B_name))
        print ("3.{}, | enter 3".format(C_name))
        print ("4.{}, | enter 4".format(D_name))
        print("5.Exit")
        inp = int(input())
        while(inp < 1 or inp >5):
            print("Please enter Valid input")
            inp = int(input())

        if(inp == 1 ):
            print("\nPlease select flavour You like\n")
            print("1.Normal       Price = "+str(A1)+"$")
            print("2.Chocolate  Price = "+str(A2)+"$")
            print("3.Vannila   Price = "+str(A3)+"$")
            print("4.Mixed     Price = "+str(A4)+"$")
            print("5.Main menu")

            inp2 = int(input())
            while(inp2 < 1 or inp2 >5):
                print("Please enter Valid input")
                inp2 = int(input())
            while(inp2 > 0):
                if(inp2 == 1):
                    if(total >= A1):
                        total = total - A1
                        bill = bill + A1
                        items1 = items1+ 1
                        inp2 = 0
                        #print("Success !, Please collect items\n")
                    else:
                        print("You dont have enough money, Please select another item \n")
                        break


                elif(inp2 == 2):
                    if(total >= A2):
                        total = total - A2
                        bill = bill + A2
                        items1 = items1+ 1
                        inp2 = 0
                        #print("Success !, Please collect items\n")
                    else:
                        print("You dont have enough money, Please select another item \n")
                        break

                elif(inp2 == 3):
                    if(total >= A3):
                        total = total - A3
                        bill = bill + A3
                        items1 = items1+ 1
                        inp2 = 0
                        #print("Success !, Please collect items\n")
                    else:
                        print("You dont have enough money, Please select another item \n")
                        break

                elif(inp2 == 4):
                    if(total >= A4):
                        total = total - A4
                        bill = bill + A4
                        items1 = items1+ 1
                        inp2 = 0
                        #print("Success !, Please collect items\n")
                    else:
                        print("You dont have enough money, Please select another item \n")
                        break
                elif(inp2 == 5):
                    break 
                else:
                    print("Please enter Valid input\n")

        elif(inp == 2):
            print("\nPlease select flavour You like\n")
            print("1.Normal     Price = "+str(B1)+"$")
            print("2.Strawberry Price = "+str(B2)+"$")
            print("3.Vannila    Price = "+str(B3)+"$")
            print("4.Mixed      Price = "+str(B4)+"$")
            print("5.Main menu")

            inp2 = int(input())
            while(inp2 < 1 and inp2 >4):
                print("Please enter Valid input")
                inp2 = int(input())
            while(inp2 > 0):
                if(inp2 == 1):
                    if(total >= B1):
                        total = total - B1
                        bill = bill + B1
                        items2 = items2+ 1
                        inp2 = 0
                        #print("Success !, Please collect items\n")
                    else:
                        print("You dont have enough money, Please select another item \n")
                        break


                elif(inp2 == 2):
                    if(total >= B2):
                        total = total - B2
                        bill = bill + B2
                        items2 = items2+ 1
                        inp2 = 0
                        #print("Success !, Please collect items\n")
                    else:
                        print("You dont have enough money, Please select another item \n")
                        break

                elif(inp2 == 3):
                    if(total >= B3):
                        total = total - B3
                        bill = bill + B3
                        items2 = items2+ 1
                        inp2 = 0
                        #print("Success !, Please collect items\n")
                    else:
                        print("You dont have enough money, Please select another item \n")
                        break

                elif(inp2 == 4):
                    if(total >= B4):
                        total = total - B4
                        bill = bill + B4
                        items2 = items2+ 1
                        inp2 = 0
                        #print("Success !, Please collect items\n")
                    else:
                        print("You dont have enough money, Please select another item \n")
                        break
                elif(inp2 == 5):
                    break 
                else:
                    print("Please enter Valid input\n")

        elif(inp == 3):
            print("\nPlease select flavour You like\n")
            print("1.Normal     Price = "+str(C1)+"$")
            print("2.Salt       Price = "+str(C2)+"$")
            print("3.Sweet      Price = "+str(C3)+"$")
            print("4.Mixed      Price = "+str(C4)+"$")
            print("5.Main menu")

            inp2 = int(input())
            while(inp2 < 1 and inp2 >4):
                print("Please enter Valid input")
                inp2 = int(input())
            while(inp2 > 0):
                if(inp2 == 1):
                    if(total >= C1):
                        total = total - C1
                        bill = bill + C1
                        items3 = items3+ 1
                        inp2 = 0
                        #print("Success !, Please collect items\n")
                    else:
                        print("You dont have enough money, Please select another item \n")
                        break


                elif(inp2 == 2):
                    if(total >= C2):
                        total = total - C2
                        bill = bill + C2
                        items3 = items3+ 1
                        inp2 = 0
                        #print("Success !, Please collect items\n")
                    else:
                        print("You dont have enough money, Please select another item \n")
                        break

                elif(inp2 == 3):
                    if(total >= C3):
                        total = total - C3
                        bill = bill + C3
                        items3 = items3+ 1
                        inp2 = 0
                        #print("Success !, Please collect items\n")
                    else:
                        print("You dont have enough money, Please select another item \n")
                        break

                elif(inp2 == 4):
                    if(total >= C4):
                        total = total - C4
                        bill = bill + C4
                        items3 = items3+ 1
                        inp2 = 0
                        #print("Success !, Please collect items\n")
                    else:
                        print("You dont have enough money, Please select another item \n")
                        break
                elif(inp2 == 5):
                    break 
                else:
                    print("Please enter Valid input\n")       

        elif(inp == 4):
            print("\nPlease select flavour You like\n")
            print("1.Normal     Price = "+str(D1)+"$")
            print("2.Spicy      Price = "+str(D2)+"$")
            print("3.Salty      Price = "+str(D3)+"$")
            print("4.Mixed      Price = "+str(D4)+"$")
            print("5.Main menu")

            inp2 = int(input())
            while(inp2 < 1 and inp2 >4):
                print("Please enter Valid input")
                inp2 = int(input())
            while(inp2 > 0):
                if(inp2 == 1):
                    if(total >= D1):
                        total = total - D1
                        bill = bill + D1
                        items4 = items4+ 1
                        inp2 = 0
                        #print("Success !, Please collect items\n")
                    else:
                        print("You dont have enough money, Please select another item \n")
                        break


                elif(inp2 == 2):
                    if(total >= D2):
                        total = total - D2
                        bill = bill + D2
                        items4 = items4+ 1
                        inp2 = 0
                        #print("Success !, Please collect items\n")
                    else:
                        print("You dont have enough money, Please select another item \n")
                        break

                elif(inp2 == 3):
                    if(total >= D3):
                        total = total - D3
                        bill = bill + D3
                        items4 = items4+ 1
                        inp2 = 0
                        #print("Success !, Please collect items\n")
                    else:
                        print("You dont have enough money, Please select another item \n")
                        break

                elif(inp2 == 4):
                    if(total >= D4):
                        total = total - D4
                        bill = bill + D4
                        items4 = items4+ 1
                        inp2 = 0
                        #print("Success !, Please collect items\n")
                    else:
                        print("You dont have enough money, Please select another item \n")
                        break
                elif(inp2 == 5):
                    break 
                else:
                    print("Please enter Valid input\n") 
        elif(inp == 5):
            bpoint = 1
            break
    
    if(bill > 0):
        time.sleep(1)
        print ("Your Total bill = "+str(bill) +"\n")
        time.sleep(1)
        print("Finally!,You brought..\n "+str(items1)+" Cotton candie\n "+str(items2)+" Sweet candie\n "+str(items3)+" Soda\n "+str(items4)+" Potato chip\n ")    
        time.sleep(1)
        print("Successfully Dispensed! Please Collect")
        time.sleep(1)
    if(bpoint == 0 ):
        print("Sorry!, You don't Have enough Money to buy any more .\n")
    if(total>0):
        print("take back if any change comes \nThankyou!!!")
    time.sleep(1)

#main
ru = 1
while(ru>0):
    vend()
    print("1.exit machine\n2.reset machine")
   
    i = int(input())
    if(i == 2):
        print("This Machine resets in....   ")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
    else:
        ru = 0
        print("This Machine exits in....   ")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
    