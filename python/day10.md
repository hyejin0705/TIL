1. import에서는 모듈(파일, 함수) 형태를 호출해야 한다.
2. __init__의 기능 : 폴더가 실행되면 자동으로 실행됨.
                     패키지를 초기화시켜주는 기능을 가짐.
            from .(현재위치) import 하위폴더(모듈) 적어주면

    ```python
    import my_pac
    
    print(my_pac.math.test.name)  # name
    ```