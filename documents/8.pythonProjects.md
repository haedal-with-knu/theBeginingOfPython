# 나만의 파이썬 프로젝트 제작 
+ `python` 라이브러리 및 프레임워크 사용(`turtle`, `pygame`, `tkinter`)
## 1. 기본적인 코드 모음
['turtle' 기본 코드](https://python.flowdas.com/library/turtle.html)

['pygame' 기본 코드](https://python101.readthedocs.io/pl/latest/_downloads/pygame192.pdf)

['tkinter' 기본 코드](https://www.tutorialspoint.com/python/python_gui_programming.htm)

## 2. 쓸만한 예제로 실습자료 만들기
  - 쓸만한 예제로 실습자료 만들자(turtle)
  
  [`turtle` 실습1](https://trinket.io/python/efc940a414)
  [`turtle` 실습2](https://trinket.io/python/88dd6c94d1)
  [`turtle` 실습3](https://trinket.io/python/64577872dd)
  - 쓸만한 예제로 실습자료 만들자(pygame)
  
  [`pygame` 실습1](http://programarcadegames.com/python_examples/f.php?file=snake.py)
  [`pygame` 실습2](http://programarcadegames.com/python_examples/show_file.php?file=move_sprite_keyboard_smooth.py)
  [`pygame` 실습3](http://programarcadegames.com/python_examples/show_file.php?file=bullets.py)
  - 쓸만한 예제로 실습자료 만들자(tkinter) 
  
  [`tkinter` 실습1](https://www.crocus.co.kr/1520)
  [`tkinter` 실습2](https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python)
  [`tkinter` 실습3](https://printed.tistory.com/10)

## 3. 실습 예제들 같이 풀어보기
예제코드들이 각 주제당 3개가 있기 때문에 보고 취향에 맞는 것 골라서 참고하시면 될 것 같습니다. <br>우선 각 주제들의 첫번째 코드들만 같이 해석하도록 하겠습니다. (다 해석하면 날샙니다..)

### 3.1 'turtle' 실습1
 ```python
   import turtle
   import math
   import random

```
우선 여기서는 turtle을 쓰기에 turtle묘듈과 math, random묘듈을 가져옵니다. 
```python
  wn = turtle.Screen()
  wn.bgcolor('black')
  Albert = turtle.Turtle()
  Albert.speed(0)
  Albert.color('white')
  rotate=int(360)
```
turtle 클래스의 Screen을 "wn"이라 지정합니다.<br>(이렇게 하는 이유 : 이렇게 지정한 이후 turtle.Screen()이라고 쓸 것을 wn 한 단어로 쓸 수 있습니다.)<br>
배경색을 검은색으로 지정 후 "Albert"라는 것을 turtle.Turtle로 지정합니다.(위 이유와 마친가지)<br>
Albert를 정지로 해놓고(speed(0)) 색은 흰색으로 지정합니다.
```python
def drawCircles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def drawSpecial(t,size,repeat):
  for i in range (repeat):
    drawCircles(t,size)
    t.right(360/repeat)
drawSpecial(Albert,100,10)

```
"drawCircles"와 "drawSpecial"함수를 만든 후 함수를 실행합니다.<br> 
"drawCircles"함수에서는 원의 크기를 점점 작게 "drawSpecial"함수에서는 "drawCircles"함수가 끝난후 오른쪽으로 얼만큼 회전할지를 지정하여 그립니다.<br>
이후에는 Steve(노란색), Barry(파란색), Terry(주황색), Will(분홍색)을 Albert(하얀색)과 형식을 똑같이 맞춰주면 그림은 완성이 됩니다.
### 3.2 'pygame' 실습 1
```python
import pygame

```
pygame묘듈을 가져옵니다.
```python
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
segment_width = 15
segment_height = 15
segment_margin = 3
x_change = segment_width + segment_margin
y_change = 0

```
전역변수로 BLACK와WHITE를 지정한 후 snake게임의 높이와 너비, 그리고 그 부분 사이의 여백을 지정합니다. <br>그후 snake의 x축으로의 변화와 y축으로의 변화(속도)를 지정합니다.
```python
class Segment(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

```
snake게임의 객체들의 일부분을 표현하는 Segment클래스로 객체의 이미지의 높이, 너비, 색, 그리고 객체의 사각형을 만든 후 x축, y축으로를 표현하고 있습니다.<br>
그리고 Sprite의 개념을 이해해야 이 게임을 만들 수 있는데 다른 이미지와 합성하기 위해 사용하는 이미지나 애니메이션을 말합니다. “게임 화면 내에서 움직이는 물체”라고 생각해도 됩니다.
```python
pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('Snake Example')
allspriteslist = pygame.sprite.Group() 

```
pygame을 시작하고 창너비 ,높이와 표시될 프로그램이름을 지정한후 pygame.sprite.Group()을 allspriteslist로 지정하고 있습니다.<br> 이후에는 pygame.sprite.Group()의 메소드를 쓸 때 allspriteslist로 더 간편하게 쓸 수 있습니다.
```python
snake_segments = []
for i in range(15):
    x = 250 - (segment_width + segment_margin) * i
    y = 30
    segment = Segment(x, y)
    snake_segments.append(segment)
    allspriteslist.add(segment)

```
 snake_segments라는 빈 배열을 만든 후 위에서 만든 클래스를 이용하여 만든 값들을 빈 배열과 스프라이트 그룹에 추가하여 snake게임의 초기상태를 만듭니다.
```python
if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (segment_width + segment_margin) * -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (segment_width + segment_margin)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (segment_height + segment_margin) * -1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (segment_height + segment_margin)


```
키 누르는 것에 따라 x축으로의 그리고 y축으로의 변화가 어떻게 변하는지 설정합니다.
```python
   old_segment = snake_segments.pop()
   allspriteslist.remove(old_segment)
 
   x = snake_segments[0].rect.x + x_change
   y = snake_segments[0].rect.y + y_change
   segment = Segment(x, y)
   snake_segments.insert(0, segment)
   allspriteslist.add(segment)

```
 마지막 요소를 배열과 스프라이트 그룹에서 제거합니다. 그리고 새로운 요소가 어디있을지 알아낸 뒤 배열과 스프라이트 그룹에 추가합니다.
```python
    screen.fill(BLACK)
    allspriteslist.draw(screen)
    pygame.display.flip()
    clock.tick(5)
pygame.quit()

```
화면이 어두운색으로 바뀌고 스프라이트 그룹에 요소들을 다 보여준후 시간을 멈추고 pygame은 종료됩니다.
### 3.3 'tkinter' 실습1
```python
from tkinter import*
window=Tk()
sum=100

```
tkinter에서 묘듈 전체를 가져와주고 윈도우창을 생성한후 전역변수 sum을 생성합니다.
```python
def pocess1():
	global sum
	sum=sum+float(e1.get())
	l2=Label(window,text=sum)
	l2.grid(row=0,column=2)


```
전역변수 sum을 가져와 입력한 값(e1)을 더하여 더한결과를 가로로 0 세로로 2인 곳에 표시합니다.
```python
def process2():
	global sum
	sum=sum-float(e1.get())
	l2=Label(window,text=sum)
	l2.grid(row=0,column=2)

```
전역변수 sum을 가져와 입력한 값(e1)을 빼서 뺀 결과를 가로로 0 세로로 2인 곳에 표시합니다.
```python
def process3():
	global sum
	sum=100
	l2=Label(window,text=sum)
	l2.grid(row=0,column=2)

```
전역변수 sum을 가져와 초기화(다시 100으로)한후 가로로 0 세로로 2인 곳에 표시합니다.
```python
e1=Entry(window)
e1.grid(row=1,column=0,columnspan=3)


```
숫자를 입력할 곳을 만든 후 배치합니다.
```python
b1=Button(window,text=”더하기(+)”,command=process1)
b2=Button(window,text=”빼기(-)”,command=process2)
b3=Button(window,text=”초기화”,command=process3)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)

```
이전에 만든 함수들을 이용하여 더하기, 빼기, 초기화 버튼을 생성한 후 배치합니다.
```python
window.mainloop()
```
tkinter가 계속 실행할 수 있도록 mainloop를 지정합니다. (지정안하면 꺼집니다.)
