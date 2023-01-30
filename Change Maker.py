print("Welcome to the vending machine change maker program")
print("Change maker initialized.")
stock = {"nickels": 25, "dimes": 25, "quarters": 25, "ones": 0, "fives": 0}

total = 10
c = True 
while c:
    print("Stock contains: " + 
        "\n   " + str(stock["nickels"]) + " nickels" + 
        "\n   " + str(stock["dimes"]) + " dimes" +
        "\n   " + str(stock["quarters"]) + " quarters" +
        "\n   " + str(stock["ones"]) + " ones" +
        "\n   " + str(stock["fives"]) + " fives")

    price = input("Enter the purchase price (xx.xx) or `q' to quit: ")

    if price == 'q':
        c = False
        break
    else: 
        c = True 
        while True:
            try:
                price = float(price) 
                break
            except ValueError:
                print('Invalid purchase price. Try again')
                price = float(input("\nEnter the purchase price (xx.xx) or `q' to quit: "))
                continue
        while True:
            if (float(price) * 100 % 5) == 0 and float(price) >= 0:
                total += float(price)
                break
            else:
                print("Illegal price: Must be a non-negative multiple of 5 cents.\n")
                price = input("\nEnter the purchase price (xx.xx) or `q' to quit: ")


    print("\nMenu for deposits:" +
      "\n\t" + "'n' - deposit a nickel" +
      "\n\t" + "'d' - deposit a dime" +
      "\n\t" + "'q' - deposit a quarter" +
      "\n\t" + "'o' - deposit a one dollar bill" +
      "\n\t" + "'f' - deposit a five dollar bill" +
      "\n\t" + "'c' - cancel the purchase\n")

    price_h = float(price) * 100
    
    if price_h % 100 <= 0:
        break
    else:
        if int(price_h // 100) > 0:
            payment = "Payment due: " + str(int(price)) + " dollars and " + str(int(price_h % 100)) + " cents"
        else:
            if int(price_h % 100) > 0:
                payment = "Payment due: " + str(int(price_h % 100)) + " cents"
        print(payment)

    deposit = input("Indicate your deposit: ")
    
    count_5 = 0
    count_10 = 0
    count_25 = 0
    count_100 = 0
    count_500 = 0
    
    price1 = price_h
    v = True
    while price_h > 0:
        if deposit == "n":
            count_5 += 1
            price1 = price1 - 5
            if price1 <= 0:
                v = True
                break    
            else:
                x = int(price1 // 100)
                y = int(price1 % 100)
                if x < 1:
                    print("Payment due: " + str(y) + " cents")
                else:
                    print("Payment due: " + str(x) + " dollars and " + str(y) + " cents")
            deposit = input("Indicate your deposit: ")
            continue
        elif deposit == "d":
            count_10 += 1
            price1 = price1 - 10
            if price1 <= 0:
                v = True
                break    
            else:
                x = int(price1 // 100)
                y = int(price1 % 100)
                if x < 1:
                    print("Payment due: " + str(y) + " cents")
                else:
                    print("Payment due: " + str(x) + " dollars and " + str(y) + " cents")
            deposit = input("Indicate your deposit: ")
            continue
        elif deposit == "q":
            count_25 += 1
            price1 = price1 - 25
            if price1 <= 0:
                v = True
                break    
            else:
                x = int(price1 // 100)
                y = int(price1 % 100)
                if x < 1:
                    print("Payment due: " + str(y) + " cents")
                else:
                    print("Payment due: " + str(x) + " dollars and " + str(y) + " cents")
            deposit = input("Indicate your deposit: ")
            continue
        elif deposit == "o":
            count_100 += 1
            price1 = price1 - 100  
            if price1 <= 0:
                v = True
                break    
            else:
                x = int(price1 // 100)
                y = int(price1 % 100)
                if x < 1:
                    print("Payment due: " + str(y) + " cents")
                else:
                    print("Payment due: " + str(x) + " dollars and " + str(y) + " cents")
            deposit = input("Indicate your deposit: ")
            continue
        elif deposit == "f":
            count_500 += 1
            price1 = price1 - 500
            if price1 <= 0:
                v = True
                break    
            else:
                x = int(price1 // 100)
                y = int(price1 % 100)
                if x < 1:
                    print("Payment due: " + str(y) + " cents")
                else:
                    print("Payment due: " + str(x) + " dollars and " + str(y) + " cents")
            deposit = input("Indicate your deposit: ")
            continue
        elif deposit == "c":
            v = False
            break
        else:
            print("Illegal selection: " + deposit)
            if price1 < 0:
                v = True
                break
            else:
                if x < 1:
                    print("Payment due: " + str(price1 % 100) + " cents")
                else:
                    print("Payment due: " + str(price1 // 100) + " dollars and " + str(price1 % 100) + " cents")
                
            deposit = input("Indicate your deposit: ")
            continue
    print()
    
    if v == True:
        z = abs(price1)
    if v == False:
        z = price_h - price1 


    if z >= 25:
        q = z // 25
        remain_q = z % 25
        if q <= stock["quarters"]:
            print(f"Please take the change below.")
            print(f"   {int(q)} quarters") 
            stock["quarters"] -= q
            move_q = remain_q
        else: 
            print(f"Please take the change below.")
            print("   " + str(int(stock["quarters"])) + " quarters")
            change_q = q - stock["quarters"] 
            move_q = change_q * 25 + remain_q

        if move_q >= 10:
            d = move_q // 10
            remain_d = move_q % 10
            if d <= stock["dimes"]:
                print(f"   {int(d)} dimes") 
                stock["dimes"] -= d
                move_d = remain_d
            else: 
                print(str(int(stock["dimes"])) + " dimes")
                change_d = d - stock["dimes"] 
                move_d = change_d * 10 + remain_d

            if move_d >= 5:
                n = move_d // 5
                if n <= stock["nickels"]:
                    print(f"   {int(n)} nickels") 
                    stock["nickels"] -= n
                else: 
                    print(f"Machine is out of change.")
                    print(f"See store manager for remaining refund.")
                    print(f"Amount due is: {int(n * 5)}")
        elif move_q >= 5:
            n = move_q // 5
            if n <= stock["nickels"]:
                print(f"   {int(n)} nickels") 
                stock["nickels"] -= n
            else: 
                print(f"Machine is out of change.")
                print(f"See store manager for remaining refund.")
                print(f"Amount due is: {int(n * 5)}")
                
    elif z >= 10:
        d = z // 10
        remain_d = z % 10
        if d <= stock["dimes"]:
            print(f"Please take the change below.")
            print(f"   {int(d)} dimes") 
            stock["dimes"] -= d
            move_d = remain_d
        else: 
            print(f"Please take the change below.")
            print("   " + str(int(stock["dimes"])) + " dimes")
            change_d = d - stock["dimes"] 
            move_d = change_d * 10 + remain_d

        if move_d >= 5:
            n = move_d // 5
            if n <= stock["nickels"]:
                print(f"   {int(n)} nickels") 
                stock["nickels"] -= n
            else: 
                print(f"Machine is out of change.")
                print(f"See store manager for remaining refund.")
                print(f"Amount due is: {int(n * 5)}")

    elif z >= 5:
        n = z // 5
        if n <= stock["nickels"]:
                print(f"Please take the change below.")
                print(f"   {int(n)} nickels") 
                stock["nickels"] -= n
        else: 
            print(f"Machine is out of change.")
            print(f"See store manager for remaining refund.")
            print(f"Amount due is: {int(n * 5)}")
        
    else:
        print(f"Please take the change below.")
        print(f"  No change due.")

    print()

    stock["nickels"] = int(stock["nickels"] + count_5)
    stock["dimes"] = int(stock["dimes"] + count_10)
    stock["quarters"] = int(stock["quarters"] + count_25)
    stock["ones"] = int(stock["ones"] + count_100)
    stock["fives"] = int(stock["fives"] + count_500)

print()

print("Total:", int(total), "dollars and", int((total*100)%100), "cents")