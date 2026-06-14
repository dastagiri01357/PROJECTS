# login details
owner_name = 'Dastagiri'
password = 'giri@2468'

#inventory
item = ['tomato','onion','ladyfinger','carrot','beetroot','drum stick','brinjal','beans','potato']
quantity = [30,35,10,20,15,10,20,10,10]
selling_price = [35,25,40,50,40,45,30,20,15]
cost_price = [25,20,30,40,35,40,25,10,10]
sales_amt = [0]*len(item)

purchase_amt=[]
for q,c in zip(quantity,cost_price):
    b=q*c
    purchase_amt.append(b)

total_amt=0
for i in purchase_amt:
    total_amt+=i
    
total_sales = 0

user_names=[]
user_phn_no=[]
user_bill=[]


while True:
    print("\n1.Owner \n2.Customer")
    section = input("Enter login section number: ")

    # ================= OWNER SECTION =================
    if section == '1':

        attempt = 1
        while attempt <= 3:
            o_n = input("Enter user name: ")
            pw = input("Enter password: ")

            if o_n == owner_name and pw == password:
                print("Login Successful")
                break
            elif o_n!=owner_name and pw == password:
                print("Incorrect User name")
            elif pw!=password and o_n == owner_name:
                print("Incorrect Password")
            else:
                print("Incorrect login details")
            attempt += 1
        else:
            print("You are not the owner")
            continue

        while True:
            print("\n1.Add item")
            print("2.Remove item")
            print("3.Update item")
            print("4.View inventory")
            print("5.View report")
            print("6.User Details")
            print("7.Exit")

            menu = input("Enter menu number: ")

            # Add item
            if menu == '1':
                while True:
                    veg = input("Enter new vegetable name: ")

                    if veg in item:
                        print("Item already exists")
                    else:
                        q = float(input("Enter quantity: "))
                        sp = float(input("Enter selling price: "))
                        cp = float(input("Enter cost price: "))

                        item.append(veg)
                        quantity.append(q)
                        selling_price.append(sp)
                        cost_price.append(cp)
                        sales_amt.append(0)

                        print(veg, "added successfully")
                    
                    ch=input("Do you want to add another item in the shop(yes/no):")

                    if ch=='no' or ch=='NO' or ch=='No':
                        break
                    elif ch=='yes' or ch=='YES' or ch=='Yes':
                         continue
                    else:
                        print("Wrong input")
                        while True:
                            ch=input("Enter correct choice(yes/no):")
                            if ch=='no' or ch=='NO' or ch=='No':
                                break
                            elif ch=='yes' or ch=='YES' or ch=='Yes':
                                break
                            else:
                                print("ENter correct option")
                        if ch=='no' or ch=='NO' or ch=='No':
                            break
                               
                        
            # Remove item
            elif menu == '2':
                while True:
                
                    veg = input("Enter vegetable to remove: ")

                    if veg in item:
                        idx = item.index(veg)

                        item.remove(item[idx])
                        quantity.remove(quantity[idx])
                        selling_price.remove(selling_price[idx])
                        cost_price.remove(cost_price[idx])
                        sales_amt.remove(sales_amt[idx])

                        print(veg, "removed successfully")
                    else:
                        print("Item not found")

                    ch=input("Do you want to remove another item in the shop(yes/no):")

                    if ch=='no' or ch=='NO' or ch=='No':
                        break
                    elif ch=='yes' or ch=='YES' or ch=='Yes':
                         continue
                    else:
                        print("Wrong input")
                        while True:
                            ch=input("Enter correct choice(yes/no):")
                            if ch=='no' or ch=='NO' or ch=='No':
                                break
                            elif ch=='yes' or ch=='YES' or ch=='Yes':
                                break
                            else:
                                print("ENter correct option")
                        if ch=='no' or ch=='NO' or ch=='No':
                            break
                       
                        
            # Update item
            elif menu == '3':
                while True:
                
                    veg = input("Enter vegetable to update: ")

                    if veg in item:
                        idx = item.index(veg)

                        print("1.Update quantity")
                        print("2.Update selling price")
                        print("3.Update cost price")

                        ch = input("Enter choice: ")

                        if ch == '1':
                            qty = float(input("Enter quantity to add: "))
                            quantity[idx] += qty

                        elif ch == '2':
                            sp = float(input("Enter new selling price: "))
                            selling_price[idx] = sp

                        elif ch == '3':
                            cp = float(input("Enter new cost price: "))
                            cost_price[idx] = cp

                        else:
                            print("Invalid choice")

                    else:
                        print("Item not available")

                    ch=input("Do you want to update another item(yes/no):")

                    if ch=='no' or ch=='NO' or ch=='No':
                        break
                    elif ch=='yes' or ch=='YES' or ch=='Yes':
                         continue
                    else:
                        print("Wrong input")
                        while True:
                            ch=input("Enter correct choice(yes/no):")
                            if ch=='no' or ch=='NO' or ch=='No':
                                break
                            elif ch=='yes' or ch=='YES' or ch=='Yes':
                                break
                            else:
                                print("ENter correct option")
                        if ch=='no' or ch=='NO' or ch=='No':
                            break
                       
                        
            #  View inventory using zip
            elif menu == '4':

                print("Vegetables\tQuantity   Selling price\tCostPrice")

                
                for i, q, sp, cp in zip(item, quantity, selling_price, cost_price):
                    print(f'{i:<15} {q:<10} {sp:<20} {cp:<4}')
                   

            #  View report using zip
            elif menu == '5':
                
                profit = total_sales - total_amt

                print("\nTotal Sales:", total_sales)
                print("Total Purchase Value:", total_amt)

                if profit > 0:
                    print("Profit:", profit)
                else:
                    print("Loss:", profit)

                print("\nSales Per Item:")
                for i, s in zip(item, sales_amt):
                    print(f'{i:<15} {s:<4}Rs')

                print("\n Items left in the shop are:")
                for i,q in zip(item,quantity):
                    print(f'{i:<15} {q:<4}KGs')

                print("\n Item wise profit or loss")
                for i,p,s in zip(item,purchase_amt,sales_amt):
                    print(f'{i:<15} {s-p:<6}Rs')
                    
            #USer Details
            elif menu=='6':
                if len(user_names)==0:
                    print("No Customers are arrived in the shop")
                else:
                    for n,p,b in zip(user_names,user_phn_no,user_bill):
                        print(f'{n:<15}--   {p:<12}--   {b:<6}Rs')
                        
            #Out of the Owner Section
            elif menu == '7':
                print("Logging out from owner section")
                break

            else:
                print("Invalid menu")

                
        close = input("\nDo you want to close the shop (yes/no): ")
        if close == 'yes' or  close=='YES' or close=='Yes':
            print("Shop Closed")
            break
    
        elif close == 'no' or close=='NO' or close=='No':
            continue
    
        else:
            print("Wrong input")
        
            while True:
                close=input("Enter Correct option (yes/no):")
                if close=='yes' or close=='YES' or close=='Yes':
                    break
            
                elif close=='no' or close=='NO' or close=='No':
                    break
            
                else:
                    print("Choose correct option")
                
            if close=='yes':
                print("Shop Closed")
                break

    # ================= CUSTOMER SECTION =================
    elif section == '2':

        u_n=input("Enter Customer name")
        user_names.append(u_n)
        while True:
            phn=input("Enter Customer phone number:")
            if len(phn)==10 and (int(phn[0])>=6 and int(phn[0])<=9):
                for i in phn:
                    if i not in['0','1','2','3','4','5','6','7','8','9']:
                        break
                else:
                    #temp=int(phn)
                    user_phn_no.append(phn)
                    break
                    
                    '''while temp>0:
                            d=temp%10
                            temp//=10
                            
                    if d>=6 and d<=9:
                          user_phn_no.append(phn)
                          break
                    else:
                        print("Correct number")
                        continue'''                                                                 
            print("Enter Correct number")
        else:
            print("Enter 10 digit number")
        
        
        cart = []
        cart_qty = []
        cart_price = []

        while True:
            print("\n1.Add to cart")
            print("2.Remove from cart")
            print("3.Modify Cart")
            print("4.View cart")
            print("5.Billing")
            

            ch = input("Enter choice: ")

            # Add to cart
            if ch == '1':
                print("\nAvailable items:")
                print("Vegetables\tQuantity\tSellingPrice")
                for i, q, sp in zip(item, quantity, selling_price):
                    print(f'{i:<15} KGs  {q:<14}   {sp:<4}Rs')
                    

                while True:
                    veg = input("Enter vegetable name: ")
                    if veg in cart:
                        print(veg,"is already in the cart")

                    else:

                        if veg in item:
                            idx = item.index(veg)

                            q = float(input("Enter quantity: "))

                            if q <= quantity[idx]:
                                quantity[idx] -= q
                                price = q * selling_price[idx]

                                cart.append(veg)
                                cart_qty.append(q)
                                cart_price.append(price)

                                sales_amt[idx] += price
                                print("Added to cart")

                            else:
                                print("Not enough stock")

                        else:
                            print("Item not found")
                        
                    ch=input("Do you want add another item into the cart(yes/no):")
                    
                    if ch=='no' or ch=='NO' or ch=='No':
                        break
                    elif ch=='yes' or ch=='YES' or ch=='Yes':
                         continue
                    else:
                        print("Wrong input")
                        while True:
                            ch=input("Enter correct choice(yes/no):")
                            if ch=='no' or ch=='NO' or ch=='No':
                                break
                            elif ch=='yes' or ch=='YES' or ch=='Yes':
                                break
                            else:
                                print("ENter correct option")
                        if ch=='no' or ch=='NO' or ch=='No':
                            break
                       
                        
            # Remove from cart
            elif ch == '2':
                if len(cart)==0:
                    print("Cart is Empty")
                else:
                    while True:
                        
                        veg = input("Enter item to remove: ")

                        if veg in cart:
                            idx = cart.index(veg)
                            ind=item.index(veg)
                            
                            prs=cart_qty[idx]
                            cart.remove(cart[idx])
                            cart_qty.remove(cart_qty[idx])
                            cart_price.remove(cart_price[idx])
                            sales_amt[ind]=0
                            quantity[ind]=quantity[ind]+prs

                            print("Removed from cart")
                        else:
                            print("Item not in cart")

                        ch=input("Do you want to remove another item in the cart(yes/no):")
                        if ch=='no' or ch=='NO' or ch=='No':
                            break
                        elif ch=='yes' or ch=='YES' or ch=='Yes':
                             continue
                        else:
                            print("Wrong input")
                            while True:
                                ch=input("Enter correct choice(yes/no):")
                                if ch=='no' or ch=='NO' or ch=='No':
                                    break
                                elif ch=='yes' or ch=='YES' or ch=='Yes':
                                    break
                                else:
                                    print("ENter correct option")
                            if ch=='no' or ch=='NO' or ch=='No':
                                break

            #Modify Cart
            elif ch=='3':
                if len(cart)==0:
                    print("Nothing to modify in the cart")
                    print("Cart is empty")
                else:
                    while True:
                        veg = input("What vegetable do you want to modify in the cart:")
                        if veg in cart:
                            
                            idx=cart.index(veg)
                            ind=item.index(veg)
                            
                            print("1.Increase Quantity")
                            print("2.Decrease Quantity")
                            
                            while True:
                                
                                ch=int(input("what do you want to modify:"))
                                if ch==1:
                                    
                                    iq=float(input("How much quantity do you want to modify:"))
                                    if iq<=quantity[idx]:
                                        cart_qty[idx]+=iq
                                        p=cart_qty[idx]*selling_price[idx]
                                        cart_price[idx]=p
                                        quantity[ind]-=iq
                                        break

                                    else:
                                        print("Insufficient Stock")

                                elif ch==2:
                                    
                                    dq=float(input("How much quantity do you want to remove from the cart:"))
                                    if dq<=cart_qty[idx]:
                                        cart_qty[idx]-=dq
                                        p=cart_qty[idx]*selling_price[idx]
                                        cart_price[idx]=p
                                        quantity[ind]+=dq
                                        break
                                        
                                    else:
                                        print("Decreasing of quantity is not possible")
                                        print("The decrease input is greater than the actual quantity in the cart")

                                        
                                    if cart_qty[idx]==0:
                                        cart.remove(cart[idx])
                                        cart_quantity.remove(cart_qty[idx])
                                        cart_price.remove(cart_price[idx])

                                else:
                                    print("Wrong input")
                                    print("ENter Correct input")
                                    
                            
                        else:
                            print(veg,"is not available in the cart")

                        ch=input("Do You want to modify another vegetable(yes/no):")
                        if ch=='no' or ch=='NO' or ch=='No':
                            break
                        elif ch=='yes' or ch=='YES' or ch=='Yes':
                         continue
                        else:
                            print("Wrong input")
                            while True:
                                ch=input("Enter correct choice(yes/no):")
                                if ch=='no' or ch=='NO' or ch=='No':
                                    break
                                elif ch=='yes' or ch=='YES' or ch=='Yes':
                                    break
                                else:
                                    print("ENter correct option")
                            if ch=='no' or ch=='NO' or ch=='No':
                                break                    

            # View cart using zip
            elif ch == '4':
                if len(cart)==0:
                    print("Cart is empty")
                else:
                    print("\nCart items:")
                    for c, q, p in zip(cart, cart_qty, cart_price):
                        print(f'{c:<15} {q:<4}KGs  -- {p:<4}Rs')
                        

            # Billing
            elif ch == '5':
                if len(cart)==0:
                    print("Cart is empty")
                else:
                    bill = 0
                    for p in cart_price:
                        bill += p

                    for c, q, p in zip(cart, cart_qty, cart_price):
                        print(f'{c:<12} KGs{q:<7}  -- {p:<4}Rs')
                    
                    print("Total amount to be payable:", bill)
                    total_sales += bill
                    print("Thank you for shopping!")
                    user_bill.append(bill)
                    break

            

            else:
                print("Invalid choice")

    else:
        print("Invalid login number")
        continue
        

    
        
