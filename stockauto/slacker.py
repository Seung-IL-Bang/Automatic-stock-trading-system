import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2342626884407-2369989189297-Re21kmP8HOyMLI7d68oCMEvs"
 
post_message(myToken,"#stockbot","안녕하세요 스톡봇입니다.")
