import requests

def getDataOption2(tokeninput):
    try:
        url = 'https://webexapis.com/v1/people/me'
        headers = {
            'Authorization' : 'Bearer {}'.format(tokeninput)
        }

        response = requests.get(url, headers = headers)
        
        if(response.status_code != 200):
            print("invalid token or error occurred. please try again")
        else:
            datawebex = response.json()
            print("")
            print("Displayed Name : " + datawebex["displayName"])
            print("Nick Name : " + datawebex["nickName"])
            print("Email : " + datawebex["emails"][0])
            # print(response.json()

    except:
        print("Error occurred")
