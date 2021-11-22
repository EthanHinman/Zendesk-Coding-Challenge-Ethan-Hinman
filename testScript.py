import unittest
import json
import io
from contextlib import redirect_stdout
# documentation: https://docs.python.org/3/library/unittest.html
from ticketFunctions import * # This is the header file. It contains all of our functions that we will test. 

class TestTicketDisplayer(unittest.TestCase):
    # test the connectToAPI()  
    def testConnectToAPI(self):
        # attempt to connect to a valid API
        email,password,subdomain =  "exampleEmail@gmail.com","ThisIsAPassword","https://yourSubdomain.zendesk.com/api/v2/tickets.json"
        tickets = connectToAPI(email,password,subdomain)
        moreThanZeroTickets = len(tickets) > 0
        self.assertEqual(moreThanZeroTickets,True) # check to make sure there are tickets returned.


        # attempt to connect to a non-valid api. Should print error.
        email,password,subdomain =  "nonValidEmail@gmail.com","ThisIsAFalsePassword","https://invalidSubdomain.zendesk.com/api/v2/tickets.json"
        self.assertEqual(connectToAPI(email,password,subdomain),[])
    
    # test the printAll()  
    def testPrintAll(self):
        data = dict()
        # get all data from "smallTickets.json"
        with open("Tests/smallTickets.json") as f:
            data = json.load(f)
        
        
        with open("Tests/testPrintAllOutput.txt", 'w+') as allTicketsOutput:
            with redirect_stdout(allTicketsOutput):
                printAllTickets(data['tickets'])
                # check to make sure the output is correct.
            
        correctTicketOutput = io.open("Tests/smallTicketsCorrectOutput.txt",'r')
        allTicketsOutput = io.open("Tests/testPrintAllOutput.txt",'r')
        self.assertListEqual(list(allTicketsOutput),list(correctTicketOutput))

        # close file
        correctTicketOutput.close(),allTicketsOutput.close()

    # test the printIndividual()  
    def testPrintIndividual(self):
        # attempt to print a valid ticket
   
        data = dict()

    
        # get all data from "smallTickets.json"
        with open("Tests/smallTickets.json") as f:
            data = json.load(f)
        
        
        # change output to "smallTicketsOutput.txt" and run functions

        with open("Tests/testDetailOutput.txt", 'w+') as detailTicketsOutput:
            with redirect_stdout(detailTicketsOutput):
                printTicketDetails(data['tickets'][1])
                
        correctTicketOutput = io.open("Tests/ticketDetailCorrectOutput.txt",'r')
        detailTicketsOutput = io.open("Tests/testDetailOutput.txt",'r')
        self.assertListEqual(list(detailTicketsOutput),list(correctTicketOutput))

        # close file
        correctTicketOutput.close(),detailTicketsOutput.close()
        
    # test the printWelcomeMessage()  
    def testHelp(self):
        # print the help message and make sure it prints the correct output.
        # attempt to print all valid tickets from smallTickets.json

       
       
        with open("Tests/testHelpOutput.txt", 'w+') as helpOutput:
            with redirect_stdout(helpOutput):
                printWelcomeMessage()
                # check to make sure the output is correct.
            
        correctHelp = io.open("Tests/helpCorrectOutput.txt",'r') 
        helpOutput = io.open("Tests/testHelpOutput.txt",'r') 
        self.assertListEqual(list(correctHelp),list(helpOutput))

        # close file
        correctHelp.close(),helpOutput.close()
    
    # test the pageTickets()
    def testPage(self):
        # See if test to see if can slice [0-24] to [25-49]
        lotsOfTickets = []
        with open("Tests/tickets.json") as f:
            lotsOfTickets = json.load(f)
        pageList = pageTickets(lotsOfTickets['tickets'],0,24)
        correctList,outputList = [25,49],[pageList[1],pageList[2]]
        self.assertEqual(outputList,correctList)

        # see if test will go until the end when slicing would be out of bounds.
        # ex. [0-24] to [24:30]
        pageList = pageTickets(lotsOfTickets['tickets'],70,79)
        correctList,outputList = [80,99],[pageList[1],pageList[2]]
        self.assertEqual(outputList,correctList)
        
        # see if the test will wrap around when it is at the end of tickets.
        with open("Tests/smallTickets.json") as f:
            lotsOfTickets = json.load(f)
        pageList = pageTickets(lotsOfTickets['tickets'],0,2)
        correctList,outputList = [0,2],[pageList[1],pageList[2]]
        self.assertEqual(outputList,correctList)


# run the test
unittest.main()