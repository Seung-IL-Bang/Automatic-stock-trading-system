Automatic stock Trading system
===

# 1. Setting
 
 * 크레온 HTS 설치 ( + 계좌개설)
 * 파이썬 설치 *(32bit 필수)* & 라이브러리 세팅
 * 크레온 API 활용하기  *(주의 사항 : 윈도우 환경 필수)*
 
  
### API 사용을 위한 라이브러리 설치 & VSC 환경 설정

1. VSC 터미널 창을 cmd로 설정

2. 라이브러리 설치
```
$ pip install pywinauto
```
: pywinauto : 윈도우 작업을 자동화하는 파이썬 라이브러리

*(위 라이브러리를 설치 시 'jupyter' extension 문구에 대한 절차)*
1. Install and Reload 눌러주기
2. Select Python Interpreter 눌러주기
3. 윈도우 환경에서 설치한 파이썬 32 bit를 선택하기

---

# 2. SLACK (알림 봇 생성)

1. 새로운 워크 스페이스 생성하기
    * slack.com 홈페이지에서 회원 가입후 새 워크스페이스 생성
    
2. 새로운 app 만들기
    * api.slack.com 홈페이지에서 create app 
    * workspace를 이전에 생성한 워크스페이스로 선택
    
3. app 사용을 위한 설정
    * OAuth & Permissions 목록 -> Bot Token Scopes 탭 -> Add an OAuth Scope 눌르기
    * 봇이 채팅방에 글을 쓸 수 있도록 chat : write 권한을 부여
    * 권한 부여 후 위쪽에 'Install to Workspace' 버튼 눌르기 -> '허용' 버튼 눌르기
    
4. OAuth Token 
    * OAuth Token for your Team 탭에서 Bot User OAuth Access Token 복사하기
    * slcak.com 에서 사용할 워크스페이스로 이동
    * 사용하는 채널 우클릭 -> 세부 정보 열기 -> '통합' 설정 -> 앱 추가하기 -> api.slack.com 에서 만든 slack bot 추가
    
5. Slacker Lib 설치
    * slacker Lib install (VSC 작업 폴더에서 설치하기 /stockauto)
```
$ pip install slacker
```

6. Slacker VSC
    * 구글에 slacker 검색 -> 'slacker Github 접속
    * Examples에서 위에서 4번째 줄 까지만 복사
    * 아까 복사해둔 OAuth Token을 2번 째 줄 코드, Slacker 괄호 옆 따옴표 사이에 insert
    * 메시지를 보낼 채널명 변경 해주기 -> 4번 째 줄 코드 #general, 워크스페이스에서 사용하는 채널 이름으로 변경 #채널명
```
slack = Slacker('<your-slack-api-token-goes-here>')
slack.chat.post_message('#general', 'Hello fellow slackers!')
```

7. Slacker VSC 오류 해결 방안
    * requests Lib 설치
    * requests를 활용하여 slacker의 기능을 하는 아래의 코드를 그대로 복사 + 붙여넣기 합니다.
    * 마지막 줄의 post_message 함수의 인자를 변경해줍니다. 1번째 인자로 여러분의 bot 토큰을, 2번째 인자로 채널명을, 3번째 인자로 보내고자 하는 메시지를 작성합니다.
    * 코드를 실행하고 '<Response [200]>' 메시지가 표시되면 slack에 성공적으로 전송됩니다.
    ```
    # requests 라이브러리 설치
      $ pip install requests
    # slacker 기능의 코드
    import requests
    
    def post_message(token, channel, text):
        response = requests.post("https://slack.com/api/chat.postMessage",
            headers={"Authorization": "Bearer "+token},
            data={"channel": channel,"text": text}
        )
        print(response)
     
    myToken = "xoxb-123*****"
     
    post_message(myToken,"#stock","jocoding")
```


    
