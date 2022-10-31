
stocks=[25,25,25,0,0] #nickels, dimes, quarters, ones, fives
check=["0","1","2","3","4","5","6","7","8","9"]
check_selection=["n","d","q","o","f","c"]
print(f"Welcome to the vending machine change maker program\nChange maker initialized.\nStock contains:\n   {stocks[0]} nickels\n   {stocks[1]} dimes\n   {stocks[2]} quarters\n   {stocks[3]} ones\n   {stocks[4]} fives\n")

price=input("Enter the purchase price (xx.xx) or `q' to quit:")

while price!='q':
    ask=False
    a=list(price)
    for i in a:
        if i=="." or i=="-":
            a.remove(i)
    if price=='.':
        print()
        print("Invalid purchase price. Try again\n")
        ask=True
    next=True
    for i in a:
        if i not in check:
            print()
            print("Invalid purchase price. Try again\n")
            next=False
            ask=True
            break
    if next:
        if (float(price)<0 or round(float(price)*100)%5!=0):
            print()
            print("Illegal price: Must be a non-negative multiple of 5 cents.\n")
            ask=True
    if ask:
        price=input("Enter the purchase price (xx.xx) or `q' to quit:")
        
    else:
        print("\n")
        print("Menu for deposits:\n  'n' - deposit a nickel\n  'd' - deposit a dime\n  'q' - deposit a quarter\n  'o' - deposit a one dollar bill\n  'f' - deposit a five dollar bill\n  'c' - cancel the purchase\n")
        amount=round(float(price)*100)
        if amount<100:
            print(f"Payment due: {amount} cents")
        else:
            print(f"Payment due: {amount//100} dollars and {amount%100} cents")
        task=input("Indicate your deposit:")
        print()
        temp_amount=amount
        while task!="c" and temp_amount>0:
            if temp_amount>0:
                if task=="n":
                    temp_amount-=5
                    stocks[0]+=1
                elif task=="d":
                    temp_amount-=10
                    stocks[1]+=1
                elif task=="q":
                    temp_amount-=25
                    stocks[2]+=1
                elif task=="o":
                    temp_amount-=100
                    stocks[3]+=1
                elif task=="f":
                    temp_amount-=500
                    stocks[4]+=1
                elif task not in check_selection:
                    print(f"Illegal selection: {task}")
            if temp_amount<100 and temp_amount>0:
                print(f"Payment due: {temp_amount} cents")
                task=input("Indicate your deposit:")
                print()
            elif temp_amount>=100:
                print(f"Payment due: {temp_amount//100} dollars and {temp_amount%100} cents")
                task=input("Indicate your deposit:")
                print()
        if task=="c":
            change_amount=amount-temp_amount
            change=[0,0,0]
            """if change_amount//500>0:
                if stocks[4]>=(change_amount//500):
                    change[4]+=(change_amount//500)
                    stocks[4]-=(change_amount//500)
                    change_amount-=(500*(change_amount//500))
            if change_amount//100>0:
                if stocks[3]>=(change_amount//100):
                    change[3]+=(change_amount//100)
                    stocks[3]-=(change_amount//100)
                    change_amount-=(100*(change_amount//100))"""
            if change_amount//25>0:
                if stocks[2]>=(change_amount//25):
                    change[2]+=(change_amount//25)
                    stocks[2]-=(change_amount//25)
                    change_amount-=(25*(change_amount//25))
            if change_amount//10>0:
                if stocks[1]>=(change_amount//10):
                    change[1]+=(change_amount//10)
                    stocks[1]-=(change_amount//10)
                    change_amount-=(10*(change_amount//10))
            if change_amount//5>0:
                if stocks[0]>=(change_amount//5):
                    change[0]+=(change_amount//5)
                    stocks[0]-=(change_amount//5)
                    change_amount-=(5*(change_amount//5))
            print("")
            print(f"Please take the change below.")
            """if change[4]>0:
                print(f"   {change[4]} fives")
            if change[3]>0:
                print(f"   {change[3]} ones")"""
            if change[2]>0:
                print(f"   {change[2]} quarters")
            if change[1]>0:
                print(f"   {change[1]} dimes")
            if change[0]>0:
                print(f"   {change[0]} nickels")
            if change_amount>0:
                print("Machine is out of change.\nSee store manager for remaining refund.")
                if change_amount>=100:
                    print(f"Amount due is: {(change_amount//100)} dollars and {(change_amount%100)} cents")
                else:
                    print(f"Amount due is: {(change_amount)} cents")
            elif change_amount==0:
                #print("  No change due.")
                print()
                print(f"Stock contains:\n   {stocks[0]} nickels\n   {stocks[1]} dimes\n   {stocks[2]} quarters\n   {stocks[3]} ones\n   {stocks[4]} fives\n")
            price=input("Enter the purchase price (xx.xx) or `q' to quit:")
            ask=False
            
        elif temp_amount<0:
            change2=[0,0,0,0,0]
            temp_amount*=(-1)
            """if temp_amount//500>0:
                if stocks[4]>=(temp_amount//500):
                    change2[4]+=(temp_amount//500)
                    stocks[4]-=(temp_amount//500)
                    temp_amount-=500*(temp_amount//500)
            if temp_amount//100>0:
                if stocks[3]>=(temp_amount//100):
                    change2[3]+=(temp_amount//100)
                    stocks[3]-=(temp_amount//100)
                    temp_amount-=100*(temp_amount//100)"""
            if temp_amount//25>0:
                if stocks[2]>=(temp_amount//25):
                    change2[2]+=(temp_amount//25)
                    stocks[2]-=(temp_amount//25)
                    temp_amount-=25*(temp_amount//25)
            if temp_amount//10>0:
                if stocks[1]>=(temp_amount//10):
                    change2[1]+=(temp_amount//10)
                    stocks[1]-=(temp_amount//10)
                    temp_amount-=10*(temp_amount//10)
            if temp_amount//5>0:
                if stocks[0]>=(temp_amount//5):
                    change2[0]+=(temp_amount//5)
                    stocks[0]-=(temp_amount//5)
                    temp_amount-=5*(temp_amount//5)
            print("")
            print(f"Please take the change below.")
            """if change2[4]>0:
                print(f"   {change2[4]} fives")
            if change2[3]>0:
                print(f"   {change2[3]} ones")"""
            if change2[2]>0:
                print(f"   {change2[2]} quarters")
            if change2[1]>0:
                print(f"   {change2[1]} dimes")
            if change2[0]>0:
                print(f"   {change2[0]} nickels")
            if temp_amount>0:
                print("Machine is out of change.\nSee store manager for remaining refund.")
                if temp_amount>=100:
                    print(f"Amount due is: {(temp_amount//100)} dollars and {(temp_amount%100)} cents")
                else:
                    print(f"Amount due is: {(temp_amount)} cents")
            print()
            print(f"Stock contains:\n   {stocks[0]} nickels\n   {stocks[1]} dimes\n   {stocks[2]} quarters\n   {stocks[3]} ones\n   {stocks[4]} fives\n")
            price=input("Enter the purchase price (xx.xx) or `q' to quit:")
            ask=False
        else:
            print()
            print(f"Stock contains:\n   {stocks[0]} nickels\n   {stocks[1]} dimes\n   {stocks[2]} quarters\n   {stocks[3]} ones\n   {stocks[4]} fives\n")
            price=input("Enter the purchase price (xx.xx) or `q' to quit:")
            ask=False
print()
print(f"Total: {stocks[4]*5+stocks[3]+(stocks[2]*25+stocks[1]*10+stocks[0]*5)//100} dollars and {(stocks[2]*25+stocks[1]*10+stocks[0]*5)%100} cents")

            



            
               





        
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


        

