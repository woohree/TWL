# 인증

## Authentication System part.1

### The Django Authentication System

- django.contrib.auth와 django.contrib.contenttypes로 이미 인스톨드앱에 제공
- 전자는 인증, 후자는 권한

#### 인증(Authentication) & 권한(Authorization)

- 인증
  - 신원 확인
  - 사용자가 누군지 확인
- 권한
  - 권한 부여
  - 인증된 사용자가 수행할 수 있는 작업을 결정

```bash
$ python manage.py startapp accounts
```



### 쿠키와 세션

#### 쿠키

- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
- 사용자가 웹사이트를 방문할 경우, 해당 웹의 서버를 통해 사용자의 pc에 배치하는 작은 기록 정보 파일
  - key-value 데이터 형식으로 저장
  - 동일한 서버에 재 요청 시, 저장된 쿠키를 함께 전송
- http 쿠키는 상태가 있는 세션을 만들어줌
- 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 여부를 판단할 때 주로 사용

=> 웹 페이지에 접속하면 요청한 웹 페이지와 쿠키를 함께 저장하고, 클라이언트가 같은 서버에 재요청 시, 요청과 함께 쿠키도 함께 전송

##### 쿠키 사용 목적

1. 세션 관리
   - 로그인, 아이디 자동 완성, 공지 하루 안보기, 팝업체크, 장바구니 등의 정보 관리
2. 개인화
   - 사용자 선호, 테마 등의 설정
3. 트래킹
   - 사용자 행동 기록 및 분석

#### 세션

- 사이트와 특정 브라우저 사이의 상태를 유지시키는 것
- 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고 클라이언트는 발급받은 session id를 쿠키에 저장
- id는 세션을 구별하기 위해 필요하며, 쿠키에는 id만 저장함

#### 쿠키 수명

1. session 쿠키
   - 현재 세션이 종료되면 삭제됨
   - 브라우저가 현재 세션이 종료되는 시기를 정의
2. persistent(or permanent) 쿠키
   - expires 속성에 지정된 날짜 혹은 max-age 속성에 지정된 기간이 지나면 삭제

#### session in django

- 장고의 세션은 미들웨어를 통해 구현됨
- database-backed sessions 저장 방식을 기본 값으로 사용
- 장고는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 세션을 알아냄
  - 세션 정보는 장고db의 django_session 테이블에 저장됨
- 다 세션으로 사용하려하면 사용자가 많을 때, 서버에 큰 부하가 걸릴 수 있음

#### cf) 미들웨어

- http 요청과 응답 처리 중간에서 작동하는 시스템(hooks)
- 장고는 http 요청이 오면 미들웨어를 거쳐 해당 url에 등록되어 있는 view로 연결해주고, http 응답 역시 미들웨어를 거쳐 내보냄
- 주로 데이터 관리, 앱 서비스, 메시징, 인증 및 api 관리를 담당



### 로그인

- 로그인은 **session을 create**하는 로직과 같음
- 장고는 인증에 관한 built-in forms를 제공

#### AuthenticationForm

- 사용자 로그인을 위한 form
- request를 첫번째 인자로 취함

#### login 함수

- 현재 세션에 연결하려는 인증된 사용자가 있는 경우, login() 함수가 필요
- HttpRequest 객체와 user 객체가 필요
- session에 user의 id를 저장(=로그인)

```python
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```



### 로그아웃

- 로그아웃은 **session을 delete**하는 로직과 같음

#### logout 함수

- HttpRequest 객체를 인자로 받고 반환 값이 없음
- 사용자가 로그인하지 않은 경우, 오류발생x
- 현재 요청에 대한 session data를 db에서 완전히 삭제하고, 클라이언트의 쿠키에서도 session id가 삭제됨
  - 이전 사용자의 세션 데이터에 액세스하는 것을 방지

```python
@require_POST
def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```



### 로그인 사용자에 대한 접근 제한

#### The raw way

- is_authenticated attribute
  - user model 속성 중 하나
  - 모든 user 인스턴스에 대해 항상 True인 읽기 전용 속성
  - 사용자가 인증되었는지 여부만 알 수 있는 방법(T/F)
  - 권한과 관련x, 또한, 사용자가 활성화 상태이거나 유효한 세션을 갖고 있는지도 확인x

```django
<!-- base.html -->
<body>
  <div class="container">
    {% if request.user.is_authenticated %}
      <h3> Hello, {{ user }}</h3>
      <form action="{% url 'accounts:logout' %}" method="post">
        {% csrf_token %}
        <input type="submit" value="logout">
      </form>
    {% else %}
      <a href="{% url 'accounts:login' %}">login</a>
    {% endif %}
    {% block content %}
    {% endblock content %}
  </div>
```

```python
if request.user.is_authenticated:
    return redirect('articles:index')
```



#### The login_required decorator

- 사용자가 로그인되어 있지 않으면, setting.LOGIN_URL에 설정된 문자열 기반 절대 경로로 redirect함
  - 기본 값은 '/accounts/login'
- 사용자가 로그인되어 있으면, 정상적으로 view 함수를 실행
- 인증 성공 시, 사용자가 redirect되어야 하는 경로는 'next'라는 쿼리 문자열 매개변수에 저장됨
  - 예시) /account/login/?next=/articles/create/

```python
@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect('articles:index')
```



## Authentication System part.2

### 회원가입

- UserCreationForm
  - 주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm

```python
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```



### 회원탈퇴

- db에서 사용자를 삭제하는 것과 같음

```python
@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete() # 순서바뀌면 안됨, request에서 유저정보 사라짐
        auth_logout(request)  # 쿠키에 남은 세션id 삭제
    return redirect('articles:index')
```



### 회원정보 수정

- UserChangeForm
  - 사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm

```python
# forms.py
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):

    password = None  # 패스워드 어쩌고 하는 내용 없애기 => UserChangeForm 들어가서 보면 인자가 보임, 그거 없애버린것 => 비번 바꾸는 링크 새로 삽입해줘야함

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')
```

```python
# views.py
@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)
```



### 비밀번호 변경

- PasswordChangeForm
  - 사용자가 비밀번호를 변경할 수 있도록 하는 Form
  - 이전 비밀번호를 입력해 비밀번호를 변경할 수 있도록 함
  - 이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 SetPasswordForm을 상속받는 클래스
- update_session_auth_hash
  - 비밀번호가 변경되면 기존 세션과의 인증 정보가 달라져, 로그인 상태를 유지할 수 없게됨
  - 새로운 password hash로 session을 업데이트함

```python
@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
```

