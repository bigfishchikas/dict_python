#Dictionary And Function
#David Ger
#
global customer
global sales
global choice
global pname



customer = {}
sales = {}

def mainmenu():
    print "\n Welcome to David Ger Application :::: To exit Press EXit"
    print  "\n ======================================================="
    return "\n Please select an option \n 1: Create an account \n 2: Create a product \n 3: Deposit Funds \n 4: Buy a product \n 5: Withdraw funds \n 6: Edit product \n 7: Check sales \n 8: Check balance \n 9: Exit \n"

 # Create an create account
def create_account():# Create a create account

    user = "Please select an account \n 1: Vender \n 2: Customer \n  "
    vs = input (user)
    ids = input ("Please your id: ")
    
    #This line checks if the name is in the dictionary if it is, its prints     
    if customer.has_key(ids) :
    
        print "The account exists"
        
    #if its not it added and given 0 for balance 
    else:
        name = raw_input ("Please add your name: ")
        customer[ids]=[name,vs,0]
        return customer
    #Go Back to the menu  
    return mainmenu()

def create_a_product():#create product
    
        #product name and id are the two variables in string price
        #Create the two variables
        ids = input ("Please your id: ")
       
        #This line checks if the name is in the dictionary if it is, its prints 
        if customer.has_key(ids) and customer[ids][1] == 1:
                pids = input ("Please Product id: ")
                pname = raw_input ("Please Product name: ")
                price = input ("Product Price: ")
                if sales.has_key(pids):
                    print "The product exists"
                    return mainmenu()
                else:
                    sales[pids]= [pname,price,0]
                    return sales
        else:
            print "You are not a vendor " 
        return  mainmenu()

def deposit_funds():#Deposit Funds
       #To deposit funds on customer account
        ids = input ("Please put your id: ")
        
        if customer.has_key(ids) and customer[ids][1] == 2:

            #If its there it add the balance to the dict considering the name as the key
            deposit = input ("Please enter the amount you want to deposit: ")
            if deposit >= 0:
                customer[ids][2] += deposit
                return "Amount deposited : %s New Amount: %s " % (deposit,customer[ids][2])
            else:
                return "You cant enter a negative value"
            
        else:
            return "You are not a customer or the account does not exist"
    
def buy_a_product():#To buy a product debit seller and credit seller
     #To buy a product check customer id and product id
        ids = input ("Please put your id: ")
        
        if customer.has_key(ids) and sales.has_key(pids) and sales[pids][2] >= 0:
            totalbought = sales[pids][1]* quantity 
            creditcustomer = customer[ids][1]==2
            debitvender = customer[ids][1]==1
            customer_name = customer[ids][1]
            print "Welcome:  %s " % (customer_name)
            #Check the deposited amount minus the buying 
            pids = input ("Please put your product id: ")
            quantity = input ("Number of goods to buy: ")
            
            if creditcustomer and debitvender and (creditcustomer < totalbought) and sales[pids][2] < quantity :
                return "You have insufficient balance and less quantity"
            else:
                if creditcustomer and debitvender:
                    #Customer purchase i.e. number of goods and price
                    customer_balance = customer[ids][2] - totalbought
                    return "The amount left in the customer account is: %s " % (customer_balance)
                    quantity_remains = sales[pids][2] - quantity
                
                    sales[pids][2]= quantity_remains
                    customer[ids][2]= customer_balance
                
                    vender_balance = customer[ids][2] + totalbought
                    print "The amount deposited in the vender account is: %s" % (vender_balance)
                    customer[ids][2]= vender_balance
                
                else:
                    return "You are doomed"
                          
        else:
            return "customer or product does not exist"
        
def withdraw_funds():#Withdraw Funds
    #Withdraw Funds
        ids = input ("Please put your id: ")
        if customer.has_key(ids):
        #If its there it add the balance to the dict considering the name as the key
            Withdraw = input ("Please enter the amount you want to withdraw: ")
        
            if Withdraw < (customer[ids][2] and customer[ids][2] >= 0):
                print "You have insufficient funds"   
            else:
                customer[ids][2] -= Withdraw
                print "Amount withdrawn: %s Balance: %s " %(Withdraw,customer[ids][2])
        else:
            
            return "That account does not exist"

def edit_product():#Edit Product
            #Create the two variables
        ids = input ("Please Vender id: ")
        pids = input ("Please Product id: ")
       
        #This line checks if the name is in the dictionary if it is, its prints 
        if customer.has_key(ids) and sales.has_key(pids) and customer[ids][1] == 1:
            
            quantity = input ("Please put the quantity: ")

            sales[pids]= [pname,price,quantity]

            return sales
        else:
            
            return "You are not a vendor or the product does not exist"

def check_sales():#Check Sales
    ids = input ("Please put your id: ")

    if customer.has_key(ids) and customer[ids][1] == 1:
        return sales
    else:
        return "The account doesnt exit"

def check_balance():#Check Balance
    ids = input ("Please put your id: ")

    if customer.has_key(ids):

        return customer[ids][2]
    
    else:
        return "The account does not exist"




#imports 


#functions


#Entry Point
if __name__ == '__main__':
    while True:
        print mainmenu()
        choice = raw_input("Choose your option: ")
        if choice == "1":
            print create_account()
        elif choice == "2":
            print create_a_product()
        elif choice == "3":
            print deposit_funds()
        elif choice == "4":
            print buy_a_product()
        elif choice == "5":
            print withdraw_funds()
        elif choice == "6":
            print edit_product()
        elif choice == "7":
            print check_sales()
        elif choice == "8":
            print check_balance()
        elif choice == "9":
            print exit()
            break
        elif choice == "exit()":
            print exit()
            break
        else:
            print "Invalid choice"
