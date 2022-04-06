# Form

- ***사용자는 절대로 개발자가 요구한 형식에 맞추어 데이터를 입력해주지 않는다.***
- Form의 역할
  - 유효성 검사(Validation)
  - HTML 생성

- `forms.py` 파일 위치
  - 어느 위치에 두어도 상관x
    - 예시) `models.py` 안에 `class`작성해도 됨

  - 그러나, 뭐가 많아지면 `app폴더/forms.py`로 작성하는 것이 편함




## Django Form Class

- From은 Django의 유효성 검사 도구 중 하나로, 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단
- 검사의 단순화, 자동화
  - 렌더링을 위한 데이터 준비 및 재구성
  - 데이터에 대한 HTML Form 생성
  - 클라이언트로부터 받은 데이터 수신 및 처리

### Form Class

- Form 내 여러 변수들을 제어 및 반복코드를 줄여줌

### rendering options

ex) `{{ form.as_p }}`

1. `.as_p`
2. `.as_ul`
3. `.as_table`

### widget

- Django의 HTML input element 표현
- HTML 렌더링 처리



### form fields vs widget

- 전자는 input 유효성 검사를 처리
- 후자는 웹페이지에서 input element의 단순 raw한 렌더링 처리



```python
from random import choices
from django import forms


class ArticleForm(forms.Form):
    REGION_A = 'sl'             # value
    REGION_B = 'dj'
    REGION_C = 'gj'
    REGIONS_CHOICES = [
        (REGION_A, '서울'),     # 출력
        (REGION_B, '대전'),
        (REGION_C, '광주'),
    ]

    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
    region = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=REGIONS_CHOICES)
```

***결국 위젯과 필드로 속성 값들을 잘 조절해줘야함!***



## ModelForm

- Model에서 정의한 필드를 Form에서 재정의하는 행위가 중복될 수 있음

- **그래서 Model을 통해 Form class를 만들 수 있는 ModelForm을 제공**

- cf) Meta data란, 데이터에 대한 데이터
  - 예시) 사진에 대한 데이터, 찍은 시각, 위치 등이 Meta data에 해당

- ```python
  from .models import Article
  from django import forms
  
  
  # 모델 클래스의 필드를 그대로 받아옴
  class ArticleForm(forms.ModelForm):
  
      class Meta:
          model = Article
          fields = '__all__'
          # exclude = ('title',)	# 출력에서 제외할 변수, fields와 동시에 사용 불가능
  ```



### is_valid() method & save() method

- 유효성 검사 실행 및 유효 여부를 boolean으로 반환(is_valid)
- Form에 바인딩된 데이터에서 db 객체를 만들고 저장(save)
- Form의 유효성 검사(`.is_valid()`)를 하면, form에 에러 메시지 값이 추가, form.errors를 확인해 에러 확인 가능

```python
def create(request):
    if request.method == 'POST':    # create
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()   # save()에 반환 값이 존재
            return redirect('articles:detail', article.pk)
   	# print(form.errors)       # 에러 메시지(이유) 확인
    
    else:                           # new
        form = ArticleForm()

    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```

```python
def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)

    else:
        form = ArticleForm(instance=article)

    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```

### Widget

- Django의 HTML input element 표현

- ```python
  class ArticleForm(forms.ModelForm):
      title = forms.CharField(
          widget=forms.TextInput(
              attrs={
                  'class': 'my_class class_two',    # 스타일 만지기 위해, 클래스 생성
                  'placeholder': 'Enter the title', # 디폴트 입력 값
              }
          )
      )
  
      content = forms.CharField(
          widget=forms.Textarea(
              attrs={
                  'class': 'my_content',            # 클래스 생성
  
              }
          ),  # <<< 쉼표 주의!!
          error_messages={                          # 에러 메시지 수정
              'required': 'Please enter content!!',
          }
      )
  
      class Meta:
          model = Article
          fields = '__all__'
  ```



## Form vs ModelForm

- 전자는 db에 저장할 필요가 없는 데이터(Model이 없음)
  - 어떤 model에 저장할 지 모르므로, 유효성 검사 후 `.cleaned_data` 딕셔너리 생성
  - `.cleaned_data`에서 데이터를 뽑아와, `save()` 해야함 (p.40)

- 후자는 db에 저장할 데이터(Model이 존재)



## Rendering Fields Manually

- 수동으로 Form 작성하기

### Rendering Fields Manually

```html
  <h1>Rendering Fields Manually</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    <div>
      {{ form.title.errors }}
      {{ form.title.label_tag }}
      {{ form.title }}
    </div>
    <div>
      {{ form.content.errors }}
      {{ form.content.label_tag }}
      {{ form.content }}
    </div>
    <input type="submit">
  </form>
```



### Looping over the form's fields (`{% for %}`)

```html
  <h1>Looping over the form's fields</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {% for field in form %}
    <div>
      {% comment %} 에러가 있다면, {% endcomment %}
      {% if field.errors %}
        {% for error in field.errors %}
        {% comment %} 부트스트랩 클래스 지정하고, 그에 맞추어 출력 {% endcomment %}
          <div class="alert alert-danger">
            {{ error }}
          </div>
        {% endfor %}
      {% endif %}
      {{ field.erroes }}
      {{ field.label_tag }}
      {{ field }}
    </div>
    {% endfor %}
    <input type="submit">
  </form>
  <a href="{% url 'articles:index' %}">back</a>
{% endblock content %}
```

- 참고

  ```python
  # 아티클에 pk=pk인 값이 있으면, 그대로 진행하고, 없으면 404에러 페이지로 이동
  # pk를 받아와야하는 함수에서 사용
  article = get_object_or_404(Article, pk=pk)
  ```

  
