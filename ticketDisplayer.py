from ticketFunctions import * # This is the header file. It contains all of our functions used in main.

if __name__ == "__main__":
    # Ethan Hinman Zendesk coding Challenge
    # print a welcome message to the user.
    printWelcomeMessage()
    
    

    ################################################################################################################
    ### Change the email, password, and subdomain to your Zendesk agent account accordingly before running this. ###
    ################################################################################################################
    email,password,subdomain =  "exampleEmail@gmail.com","ThisIsAPassword","https://yourSubdomain.zendesk.com/api/v2/tickets.json"

    # connect to the api and retreive all tickets.
    allTickets = connectToAPI(email,password,subdomain)
    tickets,beginTicket,endTicket = [], 0,len(allTickets)

    # the user can only view 25 tickets at one time.
    if len(allTickets) > 24:
        tickets = allTickets[:25]
        endTicket = 24
        print("\nYou are currently viewing tickets",beginTicket+1, " through ",endTicket+1,'\n')
    # if there are less than 25 tickets
    elif len(allTickets) >0:
        tickets = allTickets
        print("\nYou are currently viewing tickets",beginTicket+1, " through ",endTicket,'\n')
    
    # run the loop until the user enters -e (exit)
    command = ['']
    while command[0] != '-e' and len(tickets) > 0:
        command = input('Please input a command:').strip().split()


        # If the user wants to see an individual ticket.
        if command[0] == '-p':

            # the user must enter what ticket number they want to print.
            if len(command) == 1: 
                print("\nPlease enter ticket number desired.\n")
            
            # the user did not enter a valid ticket number.
            elif command[1].isdigit() == False or (command[1].isdigit() and
              ((int(command[1]) < 1) or int(command[1]) > len(tickets))):
                print("\nPlease enter a Ticket number that is a positive number no greater than current tickets. Example: '1','2','3'...\n")
                
            # everything is valid. Print the ticket.
            else:
                printTicketDetails(tickets[int(command[1])-1])
        

        # If the user wants to see all tickets.
        elif command[0] == '-pAll':
            printAllTickets(tickets)


        # If the user wants to see the next 25 tickets.
        elif command[0] == '-n':
            pagedTicket = pageTickets(allTickets,beginTicket,endTicket)
            tickets,beginTicket,endTicket = pagedTicket[0],pagedTicket[1],pagedTicket[2]
            print("\nYou are currently viewing tickets",beginTicket+1, " through ",endTicket+1,'\n')


        # If the user wants to reprint the help message.
        elif command[0] == '-h':
            printWelcomeMessage()


        # The user has either entered an invalid command or entered the exit command.
        else:

            # if they didn't enter the exit command, tell them they entered an invalid command.
            if command[0] != '-e':
                print("\nInvalid command. Please try again.\n")
    
    print("\n\nExiting Ethan Hinman's Support Ticket Displayer.\n")