## 파이썬(수 19:00 - 22:00)

### 차시별 커리큘럼

1. [오픈소스 프로그래밍?](documents/1.opensource+setting.md)
2. [깃과 함께 시작하는 파이썬](documents/2.git+datatypes.md)
3. [데이터를 저장하자 + 코드묶음 함수](documents/3.string+function+library+crawling.md)
4. [조건조건 + 반복반복](documents/4.condition+repetition.md)
5. [내 눈에 보이는 화면 + 마우스 없이 파일 다루자](documents/5.gui,cli+fileinput)
6. [안전하게 데이터를 저장하자 + 웹에서 데이터를 긁어오자](documents/6.db+crawling.md)
7. [남이 만든 코드를 재사용하자](documents/7.library,framework+flask.md)
8. [나만의 파이썬 프로젝트 제작](documents/8.pythonProjects.md)

필요한 예시 코드는 [구글 education의 `Computational thinking`](https://learn.iste.org/d2l/lor/search/search_results.d2l?ou=6606&lrepos=1006&d2l_change=0) 참고

참고 서적은 [Hello Coding 한입에 쏙 파이썬](http://m.hanbit.co.kr/store/books/book_view.html?p_code=B5915471368), [Hello Coding 쌩 초보의 처음 프로그래밍 파이썬](http://m.hanbit.co.kr/store/books/book_view.html?p_code=B8489740275)  


## 수업 시작할 때(Ice breaking) 사용할 등장인물
> 포켓몬스터 캐릭터 사용
* 사람 : 지우, 로켓단 로이, 로켓단 로사
* 지우 포켓몬 : 피카츄, 파이리, 꼬북이, 이상해씨, 잠만보, 이브이
* 로켓단 포켓몬 : 냐옹이, 마자용


### 자세히 자세히

1. 오픈소스 프로그래밍?
+ 오픈소스 프로그래밍(개념) + 개발환경설정(실습)
  - 프로그래밍 입문 및 `Computational thinking`
  - `Git` 개념부터 왜 써야하는지, 오픈소스 프로그래밍의 강점
  - `Pycharm`, `Python`, `Git Bash` 설치
  - `Pycharm`에 `Git bash` 연동

2. 깃과 함께 시작하는 파이썬
+ `Git`에 대한 이해(개념) + 직접 레포지토리 써보기(실습)
  - `.gitignore` 활용해 프로젝트 업로드
  - 마크다운 문법
  - 라면 끓이는법 or 카레 만들기 [`README.md`](http://readme.md) 문서 만들기

+ `Git`을 이용한 끝말잇기(실습) + 파이썬 데이터 자료형(개념 + 실습)
  - 친구랑 `Git`에서 협업하는 연습하기(`commit`, `push)`
  - 파이썬 데이터 자료형([숫자](2.git+datatypes/numbers.py), [문자열](2.git+datatypes/string.py)), [연산자](2.git+datatypes/operators.py)
  - 주석 개념 + 사용방법
  - 옛날 방식, `pyformat`, `f-string` 활용한 파이썬 문자열 ([`string_interpolation.py`](2.git+datatypes/string_interpolation.py))

전역변수 및 지역변수? ASCII 코드?

3. 데이터를 저장하자 + 코드묶음 함수
+ 변수란?([variables.py](3.string+function+library+crawling/variables.py))
  - 변수의 개념
  - 변수 선언 방법, 사용 방법
  - 변수 이름 짓기
  
+ 파이썬 문자열 입출력, 라이브러리 및 함수(개념 + 실습)
  - 파이썬 문자열 입출력([input+print.py](3.string+function+library+crawling/input+print.py))
  - 함수란?, 함수 사용하자([functions.py](3.string+function+library+crawling/functions.py))
  - 모듈 `random` 이용한 로또 뽑기([lotto.py](3.string+function+library+crawling/lotto.py))
  - 객체지향 개념 + 실습(아직 코드 못짬, 포켓몬 활용해 예제 만들어보자)
  


4. 조건조건 + 반복반복 
+ 조건문을 왜 쓰는지? 어디에 활용하는지?(개념) + 조건문 트레이닝(실습 - [condition.py](4.condition+repetition/condition.py))

  - 조건문 도입 - 컴퓨터처럼 생각하기(경우의 수)
  - 실제 사례에 쓰이는 예시 + 쓰면 좋은 점
  - 연습만이 살길 → 예제 짜보자

+ 반복문을 왜 쓰는지? 어디에 활용하는지?(개념) + 반복문 트레이닝(실습 - [repetition.py](4.condition+repetition/repetition.py))

  - 반복문 도입 - 귀찮은 일 대신하는 컴퓨터(매크로, 알람 등)
  - 실제 사례에 쓰이는 예시 + 쓰면 좋은 점
  - 연습만이 살길 → 예제 짜보자
+ 조건 + 반복 (실습 - [repetitionWithCondition.py](4.condition+repetition/repetitionWithCondition.py))
 
5. 내 눈에 보이는 화면 + 마우스 없이 파일 다루자 
+ GUI와 CLI의 비교 및 파일 열고닫기(개념) + `turtle`, `pygame`, `tkinter`(개념) + [`pysnake`](5.gui,cli+fileinput/pysnake.py) (실습)

  - GUI와 CLI의 비교
  - UX / UI 개념
  - `turtle` 이란?  
  [24. Program Frameworks - Python 3.3.7 documentation](https://docs.python.org/3.3/library/frameworks.html)

  - `pygame`이란?  
  [About - wiki](https://www.pygame.org/wiki/about)

  - `tkinter` 이란?  
  [tkinter - Python interface to Tcl/Tk - Python 3.8.1 documentation](https://docs.python.org/ko/3/library/tkinter.html)
  - [playsnake](https://python.bakyeono.net/chapter-12-1.html)를 통한 게임 만들기
    [파이썬으로 뱀 게임 만들기](https://python.bakyeono.net/chapter-12-1.html) 참조해 코드 완성하자

+ 파일 입출력,`csv`에 대한 이해(개념) + 파일 입출력(실습)

  - 파일 위치 및 경로([`directory.py`](5.gui,cli+fileinput/directory.py))
  - 파일 입력([`write_txt.py`](5.gui,cli+fileinput/write_txt.py)) + `with`(context manager)
  - 파일 출력(`read_txt.py`), 수정(`reverse_content.py`)
  - [`Escape Sequence`](5.gui,cli+fileinput/escape_sequence.py)
  - `csv` 파일 구조 방식
  - `csv`파일 출력(`write_csv.py`), `csv` 파일 입력(`read_csv.py`)
  - 멜론에서 실시간 차트 가져오기(`melon_rank.py`)

6. 안전하게 데이터를 저장하자 + 웹에서 데이터를 긁어오자 
+ 데이터베이스 및 정보, 일상에서 사용할 크롤링(개념) + 내 손으로 만져 보는 크롤링(실습)
  
  - 데이터베이스 → 정보사회에서 융합을 통한 새로운 개념 창출로 가치 증대
  - 귀찮은 일 자동화하기
  - 크롤링 예시 및 활용
  - 크롬 개발자 도구를 활용한 웹 정적 리버싱(네이버 실시간 검색어) → 웹 개발 및 디버깅
  - 네이버 실시간 검색어 가져오기(`naver_rank.py`)
  - melon 실시간 차트 가져오기(`melon_rank.py`)

  

7. 남이 만든 코드를 재사용하자 
+ 라이브러리와 프레임워크에 대한 이해(개념) + `flask` 입문(실습)

  - 라이브러리 vs 프레임워크
  - 실무에서 사용하는 파이썬을 활용한 여러 프레임워크들(`django`, `tensorflow`, `keras` 등)
  - 프레임워크를 사용할때의 장,단점 + 왜 사용하는지?
  - `flask` 실습  
    [kei01138/flaskIntroduction](https://github.com/kei01138/flaskIntroduction)


  
8. 나만의 파이썬 프로젝트 제작 
+ `python` 라이브러리 및 프레임워크 사용(`turtle`, `pygame`, `tkinter`)

  - 쓸만한 예제로 실습자료 만들자  
  [`turtle` 실습](https://www.notion.so/turtle-dca52e8aea724b1189763c7ababf4c17)
