# Zendesk-Coding-Challenge-Ethan-Hinman-
***
# Description
This is the coding challenge for Zendesk 2022 intern program. It was written in Python and utilizes Zendesk's API.
It will fetch and display tickets from a user's Zendesk subdomain. It also contains a basic CLI that responds to commands and output error messages, if neccesary.
It also contains standard unit tests using the unittest python library. 

# Installation
    Clone the repository using git or download the zipped files via the download button.
# Running
#### Step 1:
    Open up ticketDisplayer.py using any basic text editor and go to line 12. 
        Change:
            - "exampleEmail@gmail.com" to your email attached with your Zendesk account.
            - "ThisIsAPassword" to your password for your Zendesk account.
            - "https://'<yourSubdomain>'.zendesk.com/api/v2/tickets.json" replace <yourSubdomain>, with your subdomain for 
               your Zendesk.com.
#### Step 2:
    Open up any terminal where you have python installed and navigate to where you have ticketDisplayer.py installed..
        Type and enter the command below:
            Linux/Mac - $python3 ticketDisplayer.py
            Windows - python ticketDisplayer.py
#### Step 3:
    Follow commands given and type -e when ready to exit.
# Running Tests
#### Step 1:
    Open up any terminal where you have python installed and navigate to where you have testScript.py installed.
#### Step 2:
    Change email,password, and replace <yourSubdomain>, with your subdomain for your Zendesk.com in testConnectToAPI.
#### Step 3:
    Run testScript.py
