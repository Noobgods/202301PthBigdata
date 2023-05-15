## 1. vscode에서 "Remote ssh extension" 설치
<br/>

- - -
## 2. 로컬 환경의 "Cloudflared connections" 설치
[DOWNLOAD LINK](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation)   
*아래로 조금 내려가면 Windows가 있고 64, 32bit중 컴퓨터에 맞는 환경 설치하면 됨*   
<br/>

- - -
## 3. Remote config 설정   
> 1. Ctrl + Shift + P 로 명령 팔레트로 이동
> 2. Remote-SSH: Open SSH Configuration file... 검색하고 선택
> 3. C:\Users\{사용자이름}\.ssh\config 선택
> 4. 아래의 설정 입력
```
Host *.trycloudflare.com
    HostName %h
    User roo택
    Port 22
    ProxyCommand {CloudlflaredPath}/{CloudflaredFile} access ssh --hostname %h
```
*{CloudflaredPath}는 2번에서 설치한 Cloudflared 파일이 저장되어 있는 경로*   
*{CloudflaredFile}은 2번에서 설치한 Cloudflared 파일의 이름(.exe확장자 포함)*   
<br/>

- - - 
## 4. colab의 코드셀 추가하고 아래 코드 입력하고 실행
```
!pip install colab-ssh --upgrade

from colab_ssh import launch_ssh_cloudflared, init_git_cloudflared
launch_ssh_cloudflared(password='PASSWORD')
```
! 추후에 패스워드 입력해야 되기 때문에 패스워드 임의로 정해서 기억해놓아야 함   
실행완료하면 아래의 창이 나오는데 오른쪽 아래 VSCode Remote SSH 부분 링크 Copy     
<img src="./_img/copykey.PNG" width="80%" height="80%" title="copykey" alt="copykey"></img>   

<br/>

- - - 
## 5. remote ssh 실행
> 1. Ctrl + Shift + P 로 명령 팔레트로 이동
> 2. Remote-SSH: Connect to Host 검색하고 선택
> 3. Add New SSH Host... 선택
> 4. 4번 과정에서 복사한 키 입력후 엔터
> 5. Config에 적용
> 6. 새로운 VSCode창이 실행

<br/>

- - -
## 6. 새로운 Vscode창에서의 조작
- Linux, Windows, MacOS 중 선택
- OpenFolder 하면 패스워드 입력 (코드에서 정한 패스워드 입력)
- /Content/Drive/MyDrive/ 에 저장하면 자동으로 드라이브랑 연동됨

<br/>

- - -
## 프로그램을 다시실행하거나 런타임 연결이 끊기고 다시 시작하여야 한다면 4번과정부터 6번과정까지 다시 실행하여야 한다.    
<br/>

- - -
## 추가: 구글드라이브로 코랩에 파일 임포트
```
import os, sys
GDRIVE_HOME = 'content/drive/MyDrive'
research_root = os.path.join(GDRIVE_HOME, 'research')
sys.path.append(research_root)
```
