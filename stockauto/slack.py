import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2342626884407-2369989189297-szr194sQceEm6WR8eXiWpyYu"
 
post_message(myToken,"#stockbot","hello stock bot")