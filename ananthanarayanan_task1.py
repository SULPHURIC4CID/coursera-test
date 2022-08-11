#####################################
#   GUVI-IITM Data Science Task 1   #
#   Name : Ananthanarayanan R       #
#   Batch : DW22                    #
#   Module : MAIN                   #
#####################################

#importing necessary libraries
import registration_module;
import login_module;

#Welcome message of the portal
print("***********************************************");
print("*  WELCOME TO THE LOGIN/REGISTRATION PORTAL   *");
print("***********************************************");
print("\nMAIN MENU.\n");
while(True):
    #List of features provided by the portal
    print("What do you want to do?");
    print("New users choose register (R).");
    print("Registered users choose login (L).");
    print("Choose (Q) to quit the portal.\n");
    
    #Accepting the functionality option as input from the user
    user_input = input("Enter your input R/L/Q : ");

    #Checking the user input
    if (user_input.upper() == 'Q'):         #Quitting the PORTAL
        print("\nThank you for using the Portal.");     
        break;
    elif (user_input.upper() == 'L'):       #Login Page
        login_module.login();
    elif (user_input.upper() == 'R'):       #Registration Page
        registration_module.register();
    else:
        print("\nInvalid input, please choose a value from R/L/Q.\n");
        
    
    
