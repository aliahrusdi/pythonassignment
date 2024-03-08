import requests

def getDataOption4(tokeninput):
    try:
        url = 'https://webexapis.com/v1/rooms'
        headers = {
            'Authorization' : 'Bearer {}'.format(tokeninput),
            'Content-Type': 'application/json'
        }

        print("Enter room name :")
        roomname = input()

        params = { 'title' : roomname }
        response = requests.post(url, headers = headers, json=params)
        
        if(response.status_code != 200):
            print("invalid token or error occurred. please try again")
        else:
            print("")
            print("Room Successfully Created !")
    except:
        print("Error occurred")
