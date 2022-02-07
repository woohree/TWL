# CSS Layout

- css 원칙
  - 모든 요소는 박스모델, 좌측상단에 배치(normal flow)
  - display에 따라 크기와 배치가 달라짐

## Float

- 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함한 인라인 요소들이 주변을 wrapping 하도록 함
- 요소가 normal flow를 벗어나게 함

### 속성

- none: 기본값
- left: 요소를 왼쪽에 띄움
- right: 요소를 오른쪽에 띄움

### Clearfix

```css
.clearfix::after {
  content: "";
  display: block;
  clear: both;
}

<!-- clearfix
1. float 요소의 부모로 div!
2. 부모에게 .clearfix -->
<h1>Float 실습</h1>
<div class="clearfix">
  <div class="box1 left">box1</div>
</div>
<div class="box2">box2</div>
```

- 부모요소(clearfix) 높이 = 0. 왜냐면, 자식요소(box1 left)가 float이라서.
- 그래서 float을 clear시킴.
- 반드시 부모요소에 특성 부여.

## Flexbox

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델

- ![](02-CSS_Layout.assets/flexbox.png)

- 축

  - main axis(메인)
  - cross axis(교차)

- ```css
  .flex-container {
    display: flex;
  }
  ```

### 구성 요소

- flex container(부모)
- flex item(자식)

## Bootstrap

## Bootstrap Grid System

기본 요소

- column: 실제 컨텐츠를 포함한 공간
- gutter: 칼럼과 칼럼 사이 공간
- container: 칼럼을 담고 있는 공간

- flexbox로 제작됨