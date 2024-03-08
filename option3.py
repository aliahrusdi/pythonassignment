import requests

def getDataOption3(tokeninput):
    try:
        url = 'https://webexapis.com/v1/rooms'
        headers = {
            'Authorization' : 'Bearer {}'.format(tokeninput)
        }

        response = requests.get(url, headers = headers)
        
        if(response.status_code != 200):
            print("invalid token or error occurred. please try again")
        else:
            datawebex = response.json()
            for eachroom in datawebex["items"]:
                print("")
                print("Room ID : " + eachroom["id"])
                print("Room Title : " + eachroom["title"])
                print("Date Created : " + eachroom["created"])
                print("Last Activity : " + eachroom["lastActivity"])
            # print(response.json()

    except:
        print("Error occurred")
