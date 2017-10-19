# 서버 설정하기
google cloud 이용해 서버 설정하기 등등 (명령어 기록용 파일)

#### 인스턴스 생성
- 이름(instance-project) 외 기본 설정
- 부팅디스크: CentOS 7
- 모든 Cloud API에 대한 전체 엑세스 허용
- 방화벽: HTTP/HTTPS 트래픽 허용(둘다 체크)

## 1. python 3.x 설치하기
#### python 3.4 설치
`$ sudo yum install python34`
#### python 개발 패키지 설치
`$ sudo yum install python34-devel`  
`$ sudo yum install python34-setuptools`
> 결과
```
[g5eo1ab@instance-project ~]$ python3 --version
Python 3.4.5
```  

#### pip 설치
`$ cd /usr/lib/python3.4/site-packages/`  
`$ sudo python3 easy_install.py pip`
> 결과
```
... Finished processing dependencies for pip
[g5eo1ab@instance-project site-packages]$ pip3 --version
pip 9.0.1 from /usr/lib/python3.4/site-packages/pip-9.0.1-py3.4.egg (python 3.4)
```

## 2. git 설치 및 clone repository
#### git 설치
`$ sudo yum install git`
#### clone repository
`$ git clone https://github.com/5eo1ab/trading-bot`  
`$ cd trading-bot`

## 3. Java 설치 및 경로 설정
#### Java 설치
`$ sudo yum install java`
#### Java 설치 경로 찾기
`$ which java`  
`$ ls -al [경로]`  
처음 명령어를 입력했을 때 java 설치 경로를 반환한다. 근데 이거 fake path  
반환하는 주소의 진짜 주소를 찾아 가야하는데, 아래 명령어를 입력했을 떄 반환하는 주소를 다시 반복해서 입력  
더이상 redirect 경로가 없을떄 그 경로를 복사해둔다.
> 반복 과정(결과)
```
[g5eo1ab@instance-project ~]$ which java
/usr/bin/java
[g5eo1ab@instance-project ~]$ ls -al /usr/bin/java
lrwxrwxrwx. 1 root root 22 Oct 17 15:17 /usr/bin/java -> /etc/alternatives/java
[g5eo1ab@instance-project ~]$ ls -al /etc/alternatives/java
lrwxrwxrwx. 1 root root 73 Oct 17 15:17 /etc/alternatives/java -> /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.144-0.b01.e
l7_4.x86_64/jre/bin/java
[g5eo1ab@instance-project ~]$ ls -al /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.144-0.b01.el7_4.x86_64/jre/bin/java
-rwxr-xr-x. 1 root root 7304 Sep  6 15:35 /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.144-0.b01.el7_4.x86_64/jre/bin/java
[g5eo1ab@instance-project ~]$
```

#### JAVA_HOME 환경변수에 추가
`$ cd ~`  
`$ vi .bash_profile`  
아래와 같이 기존 PATH 설정 아래에 JAVA_HOME 경로를 추가한다.  
```
@ vi editor  
PATH=$PATH:/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.144-0.b01.el7_4.x86_64/jre/bin/java # JAVA_HOME
```

#### 설정 활성화
`$ source .bash_profile`
