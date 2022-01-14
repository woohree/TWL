# Git 기초

## git이 관리 하는 폴더: 리포(repo.)

### git init: 

깃 시작 ('폴더' 에서 '리포'로 바꿈)

```
$ git init
```

### rm -r .git: 

잘못 설정한 경우 사용

but 작업한거 다 날아감 주의!!

```
$ rm -r .git/
```

### 서명하기: 

```
$ git config --global user.name " "  
$ git config --global user.email " "
```

## 파일 만들기:

```
$ touch <filename> 
```

## 지우기:

```
$ rm
$ rm -r #폴더
$ rm -rf #관리자 권한
```

## git 명령어

### add

파일을 스테이지에 올리기 위한 명령어

```
$ git add <filename> 
```

### commit

스테이지에 올라간 변경사항만 commit에 포함

```
$ git commit -m '1번'
```

1번이라고 메시지 남겨 버전을 바꿈

-m를 저장하지 않으면 vim 으로 넘어가게 됨. 코치왈) 아주 귀찮다고 함 (!q로 나가기)

### status

```
$ git status
```

상태 확인

### log

```
$ git log
```

로그 확인

### remote

깃허브와 내 리포를 연결(이라기 보다는 pointing)

```
$ git remote add origin https://
```

```
$ git remote -v #연결확인
```

```
$ git remote remove ~ #지우기
```



### origin 의미

origin이란 key값에 벨류를 넣겠다.

origin은 다른 단어로 바꾸어도 무방하고, 따라서 여러 주소를 지정 가능

### *촬영장 비유*

#### 스테이지

깃은 스테이지에 올라간 것만 사진을 찍음

#### 제작진(메모리카드)

commit

#### 분장실

대기실같은 느낌



## *저장을 해야 바뀐 것으로 인식*



## git hub

### *클라우드 비유*

#### 내컴(git) <-> 드라이브(github)

local repo - remote repo

폴더 두개 생성

내 리포의 commit 들은 github로 밀어서 보내기

```
$ git remote add origin https://
```

### 기존 깃허브 설정을 바꿀 경우

윈도우키 - 자격증명관리자 검색 - 윈도우 자격 증명 - github 찾아서 ID, PW 편집

### hub에 올리기

```
$ git push origin master
```

### README.md

내 git 대문 

### .gitignore (반드시 ignore부터 만들고 시작!!!!!!!!!)

업로드 되지 않았으면 하는 파일 혹은 폴더 등을 지정하여 push되지 않게 설정해주는 파일

gitignore.io 에 들어가서 windows, python, VScode 해서 생성하면 얘들이랑 관련해서 ignore 파일 자동으로 싹 만들어줌 

그 외

plan.md #파일, plan/ #폴더 등 

#### 만약 중요한 파일을 github에 올렸다면? 

파일 지우거나 / add 후 제외하고 반드시 다시 "push" 해 주어야 함

### 명령어

#### clone

리모트에 있는 내용 로컬로 복사해오기

```
$ git clone <URL>
```

new-repo-name으로 최상단 폴더 이름이 바뀌어서 가져옴

```
$ git clone <URL> new-repo-name 
```

#### pull

오리진의 내용 가져오기(push와 반대 개념이라 생각)

```
$ git pull origin master
```

### github에서 수정할 시 주의사항(팀워크 시 자주 발생)

github에서 수정을 한다면 반드시 커밋을 작성하고 로컬에서 반드시 pull을 해야함

만약 pull 이전에, 로컬에서 수정하고 push를 먼저 한다면 꼬여버림 혹은 거절당함 *넥서스 사건 안생기게 주의..*

그래서 다시 pull부터 하고 선택하면됨

### VS 명령어: ctrl + c, ctrl + l

c는 일단 취소! / l은 clear !

## *--help*

명령어 이후 무엇을 명령어로 써야할 지 모른다면 쓰기

그 자리에 쓸 수 있는 여러 명령어를 보여줌

