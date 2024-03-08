import requests

def getDataOption5(tokeninput):
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
            roomnumber = 0
            for eachroom in datawebex["items"]:
                roomnumber = roomnumber + 1

                print("")
                print(roomnumber)
                print("Room ID : " + eachroom["id"])
                print("Room Title : " + eachroom["title"])
                print("Date Created : " + eachroom["created"])
                print("Last Activity : " + eachroom["lastActivity"])
            # print(response.json()

            print("choose room by number to send message")
            roomnumber = int(input())   
            
            print("")
            print("enter the message")
            message = input()

            url2 = 'https://webexapis.com/v1/messages'

            headers2 = {
            'Authorization': 'Bearer {}'.format(tokeninput),
             'Content-Type': 'application/json'
            }

            room_id = datawebex["items"][roomnumber - 1]["id"]
            params = {'roomId': room_id, 'markdown': message}
            response2 = requests.post(url2, headers=headers2, json=params)

            if(response2.status_code != 200):
                print("invalid token or error occurred. please try again")
                print(response2.json())
            else:
                print("Successfully send message")
    except:
        print("Error occurred")
