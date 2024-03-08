import requests

def getDataOption1(tokeninput):
    try:
        url = 'https://webexapis.com/v1/people/me'
        headers = {
            'Authorization' : 'Bearer {}'.format(tokeninput)
        }

        response = requests.get(url, headers = headers)
        
        if(response.status_code != 200):
            print("invalid token or error occurred. please try again")
        else:
            print("")
            print("Test Successfully")

    except:
        print("Error occurred")
