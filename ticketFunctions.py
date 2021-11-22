import requests
import sys
# Ethan Hinman Zendesk coding Challenge

'''
Input: Void
Return: Void
Functionality: Print a welcome message with all commands to the user.
'''
def printWelcomeMessage()->None:

    # print the welcome message.
    welcomeMessage = """\n-----------------------------------------------------------------------------------------------------
    \nHello and welcome to Ethan Hinman's Support Ticket Displayer.\n\nCommands are listed below:\n\n-pAll
    This command will print all tickets.\n\n-p<space>'ticketNumber' ex. -p 2 #This will print ticket 2#
    This command will print an individual ticket\n\n-h
    This will print the welcome message again.\n\n-n
    If there are more than 25 tickets, it will look at the next 25 tickets.
    If you are at the end, it will wrap around to the beginning 25 tickets.\n\n-e
    This command will exit the program.\n
    \n-----------------------------------------------------------------------------------------------------\n"""
    print(welcomeMessage)


'''
Input: user's email, user's password and user's subdomain
Return: dictionary of user's tickets
Functionality: connects to the user's subdomain using Zendesk's API 
          and retrieves all tickets.
'''
def connectToAPI(email:str,password:str,subdomain:str) -> dict():
    
    
    # Request all tickets
    getResponse = requests.get(url=subdomain,auth=(email,password))

    # Check to make sure the API is up. If it is not, then let the user know.
    if getResponse.status_code == 404:
        print("API is down. Try again later. Exiting with error code:",getResponse.status_code)
        return []

    # Check to make sure the get request is valid. If it is invalid, we will print an error and exit.
    if getResponse.status_code != 200:
        print("The get request has responded with a non 200 value. Exiting with error code:",getResponse.status_code)
        return []

    # We got back a valid command. Convert response to json, print valid response, and return tickets.    
    else:
        tickets = getResponse.json()['tickets']
        print("\nYou have successfully connected to",subdomain,"and retrieved",len(tickets),"tickets.\n" )
        return tickets


'''
Input: Void
Return: Void
Functionality: Print all tickets gotten from connectToAPI() to the user.
'''  
def printAllTickets(tickets:dict)-> None:
    print('Tickets:\n')
    count = 0
    for ticket in tickets:

        # slice year, month ,and day accordingly
        year,month,day = ticket['created_at'][:4],ticket['created_at'][5:7],ticket['created_at'][8:10]

        # concate them into month/day/format
        date = month.strip() + '/' + day.strip() + '/'+ year.strip()

        # slice time accordingly.
        time = ticket['created_at'][11:-1]
        
        # print the ticket information
        print("Ticket ID:",ticket['id'] ,"\n  Subject:\n    ",ticket['subject'],"\n  Status:\n    ",
        ticket['status'],"\n  Submitter ID:\n    ",ticket['submitter_id'],"\n  Opened On:\n    ",
        date,"at",time.strip(),'\n')


'''
Input: ticket requested by the user
Return: Void
Functionality: Print details of the requested ticket.
'''
def printTicketDetails(ticket:dict)-> None:
    
    # slice year, month ,and day accordingly
    year,month,day = ticket['created_at'][:4],ticket['created_at'][5:7],ticket['created_at'][8:10]

    # concate them into month/day/format
    date = month.strip() + '/' + day.strip() + '/'+ year.strip()

    # slice time accordingly.
    time = ticket['created_at'][11:-1]

    # print the ticket information
    print("\n----------------------\nTicket ID:\n",ticket['id'],"\nSubject:\n"
    ,ticket['subject'],"\nDescription:\n",ticket['description'],
    "\nStatus:\n",ticket['status'],"\nDate Created:\n",date, 'at',time ,
    "\nRequester ID:\n",ticket['requester_id'],'\n----------------------\n')


'''
Input: a dictionary of all tickets, beginning index of current tickets we are viewing, end index of current tickets we are viewing
Return: list containing a new slice of tickets, updated beginning index to correspond with new slice, updated end index to correspond with new slice
Function: Take in all tickets and current slice of tickets we are viewing and update it to see the next slice.
'''
def pageTickets(allTickets:dict,beginTicket:int,endTicket:int) -> list():
    
    # if we are at the end of all our tickets, then wrap around.
    if len(allTickets) < 25:
        return [allTickets,0,len(allTickets)-1]
    elif endTicket+1 == len(allTickets):
        return [allTickets[0:25],0,24]
    # if slicing next 25 tickets would put us over our number of tickets, then we just
    # display until the last ticket.
    elif endTicket+1 + 25 > len(allTickets): 
        return [allTickets[endTicket+1:],endTicket+1,len(allTickets)-1]

    # Otherwise get the next 25 tickets
    else:
        return [allTickets[endTicket+1:endTicket+26],endTicket+1,endTicket+25]



