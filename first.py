#
#Account is the name of the dictionary that we are going to store data 
accounts = {}

#Menu is the string we are choosing from i.e. the choices we have 
menu_str = "Please select an option: \n 1: Create account \n 2: Edit Account \n 3: Deposit Funds \n 4: Withdraw Funds \n 5: Check Balance \n 6: Exit \n : "
#We put the choice int format
choice = int(input(menu_str))
while choice != 6:

   if choice == 1:
        #create account
        #name and id are the two variables in string
        #Create the two variables
        name = input("Please add your name: ")
        id = int(input ("Please add your id: "))
        #This line checks if the name is in the dictionary if it is, its prints
        if name in accounts:
            print ("That account exist")
            print(accounts)
            

        #if its not it added and given 0 for balance 
        else:
            accounts[name]= [id,0]
            print(accounts)
   elif choice == 2:
        #Edit account
        #name and id are the two variables in string
        name = input ("Please enter your name: ")
        
        #This line checks if the name is in the dictionary if it is, its there it add the balance id not
        if name in accounts:
            #If its there it add the balance to the dict considering the name as the key
            id = int(input ("Please add your id: "))
            accounts[name][0] = id

        else:
            print ("That account does not exist")
        
   elif choice == 3:
        #Deposit Funds
        name = input ("Please add your name: ")

        if name in accounts:

            #If its there it add the balance to the dict considering the name as the key
            deposit = int(input ("Please enter the amount you want to deposit: "))
            accounts[name][1] += deposit
            print (accounts)
        else:
            print ("That account does not exist")
    
   elif choice == 4:
        #Withdraw Funds
        name = input ("Please add your name: ")
        if name in accounts:
        #If its there it add the balance to the dict considering the name as the key
            Withdraw = input ("Please enter the amount you want to withdraw: ")
            if Withdraw > accounts[name][1]:
                print ("You have insufficient funds")   
            else:
                accounts[name][1] -= Withdraw
        else:
            
            print ("That account does not exist")
   elif choice == 5:
        #Check balance
        name = input ("Please add your name: ")
        if name in accounts:
            print (accounts[name][1])
        else:
            
            print ("That account does not exist")

   choice = int(input(menu_str))
print (accounts)
