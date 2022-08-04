## 02_web_homework.md



### 1. Semantic tag

- header
- section
- footer

[Semantic Elements in HTML](https://www.w3schools.com/html/html5_semantic_elements.asp)



### 2. input tag

```html
<form action="#">
  <label for="username">USERNAME : </label>
  <input id="username" type="text" placeholder="아이디를 입력 해 주세요."><br>
    
	<label for="password">PWD : </label>
	<input id="password" type="password">
  
	<input type="submit" value="로그인">
</form>
```



### 3. 크기 단위

- `rem`
  - `root em`의 약자.
  - html tag의 font-size를 base로 합니다.
  - html tag에 font-size가 정의되지 않았다면, 브라우저 기본 설정을 따라갑니다.




### 4. 선택자

- 자손 - `div p`
    - div의 모든 자식들 중에 p (깊이 상관 없음)
    - 손자 일 수도, 증손자 일 수도 있음!
- 자식 - `div > p`
    - div의 **바로 아래** 자식들 중에 p
    - 손자, 증손자는 해당 안됨.