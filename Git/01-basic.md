# 01-13. git 기초

## 깃이 관리 하는 폴더: 리포(repo.)

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

### *cf촬영장 비유*

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

### 기존의 깃허브를 바꿀 경우

윈도우키 - 자격증명관리자 검색 - 윈도우 자격 증명 - github 찾기 - 이후 구글링해야겠다

### hub에 올리기

```
$ git push origin master
```



## *--help*

명령어 이후 무엇을 명령어로 써야할 지 모른다면 쓰기

그 자리에 쓸 수 있는 여러 명령어를 보여줌