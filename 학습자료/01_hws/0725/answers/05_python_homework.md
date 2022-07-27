### 05_python_homework.md

1. 모음은 몇 개나 있을까?

   ```python
   def count_vowels(word):
       vowels = 'aeiou'
       result = 0
       for vowel in vowels:
           result += word.count(vowel)
       return result
   ```

```python
count_vowels('apple')   # => 2
```

```python
count_vowels('banana')  # => 3
```

2. 문자열 조작

   > 답: 4	

   - 특정한 문자를 지정하지 않으면 공백 및 개행 문자를 제거한다.
   
   ```python
   # (1)
   'jurassic'.find('k') # -1 
   'jurassic'.find('s') # 4 
   
   # (2)
   'jurassic'.split('s') # ['jura', '', 'ic']
   'jurassic'.split('r')# ['ju', 'assic']
   
   # (3)
   'jurassic'.replace('j', 'k') # 'kurassic'
   'jurassic'.replace('s', 'k', 1) # 'juraksic'
   'jurassic'.replace('s', 'k', 2) # 'jurakkic'
   
   # (4)
   '   jurassic   '.strip() # 'jurassic'
   '   jur  assic   '.strip() # 'jur  assic'
   'www.jurassic.net'.strip('w.ten') # 'jurassic'
   ```
   
   



3. 정사각형만 만들기

   ```python
   # 1. basic
   
   def only_square_area(widths, heights):
       sqaure_combination = []
   
       for width in widths:
           for height in heights:
               if width == height:
                   sqaure_combination.append(width * height)
   	
       return sqaure_combination
   ```

   ```python
   # 2. list comprehension
   
   def only_square_area(widths, heights):
       sqaure_combination = [width * height for width in widths for height in heights if width == height]
       return sqaure_combination
   ```

   



