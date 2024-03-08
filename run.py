import requests, os

# call file
import option1
import option2
import option3
import option4
import option5

# menu button
print("=== WELCOME TO WEBEX ===")
print("")
try:
    tokeninput = ""
    
    while True:
        # insert token
        print("please enter your token : ")
        tokeninput = input()

        # url
        url = 'https://webexapis.com/v1/people/me'
        headers = {
            'Authorization' : 'Bearer {}'.format(tokeninput)
        }

        response = requests.get(url, headers = headers)

        # check status
        if(response.status_code == 200):
            break
        else:
            print("invalid token or error occurred. please try again")
            print("")
    
    while True:
        print("")
        print("")

        # menu button
        print("- choose one of the menu that you want  to use -")
        print("option 1 ( test connection to webex )")
        print("option 2 ( user information )")
        print("option 3 ( list room )")
        print("option 4 ( create room )")
        print("option 5 ( send message )")
        print("option 6 ( exit )")
        chooseoption = int(input())

        # user choose option 1
        if(chooseoption == 1):
            option1.getDataOption1(tokeninput)

        # user choose option 2
        if(chooseoption == 2):
            option2.getDataOption2(tokeninput)

        # user choose option 3
        if(chooseoption == 3):
            option3.getDataOption3(tokeninput)

        # user choose option 4
        if(chooseoption == 4):
            option4.getDataOption4(tokeninput)

        # user choose option 5
        if(chooseoption == 5):
            option5.getDataOption5(tokeninput)

        # user choose option 6
        if(chooseoption == 6):
            os._exit(1)

except:
    print("Error occurred")