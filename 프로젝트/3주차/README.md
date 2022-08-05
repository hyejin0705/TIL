# pjt03

### 이번 plt를 통해 배운 내용
- 반응형 웹(Grid system) 방식을 활용하여 나만의 영화 사이트를 만듦.

- Bootstrap의 여러가지 기능들(list, card, pagination, navbar 등)을 활용하여 완성도 있는 웹 사이트를 만들었음. 

- 화면의 크기에 따라 내용들의 크기가 달라지는 방법 외에도 보여지는 내용의 종류가 달라지는 방법도 배움.

- 이전까지는 데이터를 가공하는 방법을 배웠다고, 이번 프로젝트를 통해 영화 데이터들을 어떻게 시각적으로 보여줄 수 있는지를 배웠음.


## A. nav_footer.html
- 요구 사항 
    1. Navigation Bar
        - Bootstrap Navbar Component를 참고합니다.

        - 스크롤을 하더라도 항상 화면 상단에 고정되어 있습니다.
        
        - 로고 이미지는 제공된 logo.png를 사용합니다.
        
        - 로고 이미지는 하이퍼링크 역할도 가능하며 클릭 시 02_home.html로 이동해야 합니다.

        - 내비게이션 메뉴 중 Home, Community는 하이퍼링크 역할도 가능하며 클릭 시 각각 02_home.html, 03_community.html로 이동해야 합니다.

        ![](README.assets/result.png)
        


        - 내비게이션 메뉴 중 Login은 클릭 시 Bootstrap Modal Component가 나타납니다.
            -  Modal Component 내부에는 HTML form 요소를 배치합니다.
        
        ![](README.assets/result2.png)

        
        - Viewport의 가로 크기 별 반응형 디자인은 스크린 샷 예시를 참고하여 일치하도록 합니다.

    
    2. Footer
        - 스크롤을 하더라도 항상 화면 하단에 고정되어 있습니다.
        - Footer에 작성된 내용은 수직·수평 가운데 정렬되어 있습니다.


        ![](README.assets/result3.png)





- 문제 접근 방법 및 코드 설명:
    ```html
    
    <body>
    <!-- 스크롤을 하더라도 항상 화면 상단에 고정, sticky-top -->
    <!-- Bootstrap Navbar Component 활용, toggler는 width 768px 미만일 때 활성화, navbar-expand-md -->
    <nav class="navbar navbar-expand-md bg-dark navbar-dark sticky-top">

        <div class="container-fluid d-flex justify-content-between">
    
        <!-- 로고 이미지는 클릭 시 02_home.html로 이동 -->
        <a class="navbar-brand" href="02_home.html">
            <img src="images/logo.png" alt="Logo_image" width="150" height="50">
        </a>

        <!-- toggler : 햄버거 모양 -->
        <button class="navbar-toggler col-" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
            <!-- Home, Community는 클릭 시 각각 02_home.html, 03_community.html로 이동 -->
            <li class="nav-item">
                <a class="nav-link active" href="02_home.html">Home</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="03_community.html">Community</a>
            </li>
            <li class="nav-item">
                <!-- <a class="nav-link text-white" href="#">Login</a>-->
                <a class="nav-link" href="#exampleModal" data-bs-toggle="modal">Login</a>
                
            </li>
            </ul>

        </div>
        </div>
    </nav>
    

    <!-- Modal 실행은 nav 밖에서 실행해야 활성화가 됨. -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
            <form>
                <div class="mb-3">
                <label for="email" class="col-form-label">Email address</label>
                <input type="email" class="form-control" id="email">
                <!-- 회색으로 이메일 작성시 주의사항 달기 -->
                <p style="font-size: small; color: grey;">We'll never share your email with anyone else.</p>
                </div>
                <div class="mb-3">
                <label for="password" class="col-form-label">password</label>
                <input type="password" class="form-control" id="password">
                </div>

                <div class="mb-3">
                <input type="checkbox" value="Check me out" id="checkbox">
                <label for="checkbox" class="col-form-label">Check me out</label>
                </div>
            </form>

            </div>
            <!-- close 누르면 취소, submit 누르면 제출 -->
            <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary">Submit</button>
            </div>
        </div>
        </div>
    </div>

    <!-- 스크롤을 하더라도 항상 화면 하단에 고정, fixed-bottom -->
    <!-- fixed랑 sticky의 차이점, fixed-bottom은 스크롤 하더라도 항상 하단에 나타남
            단, sticky-bottom은 그냥 하단에 고정 왜??? top은 스크롤 하더라고 항상 상단에 고정인데.... -->
    <footer class="fixed-bottom">
        <!-- 내용은 수직·수평 가운데 정렬, text-center -->
        <p class="text-center">Web-booststrap PJT, by hyejin</p>
    </footer>

    ```


- 어려웠던 점 및 문제의 포인트
- 어려웠던 점

    1. toggler가 햄버거 모양의 메뉴 축소판인 줄 모르고 지웠다가 다시 생성하는 번거로운 일이 있었음.

    2. modal의 코드를 가져와서 실행시키는데, 
        nav태그 안에 넣으니, modal이 비활성화가 됨.
        
        - 해결방안 : nav를 닫고 그 뒤에 코드를 넣기

- 문제의 포인트 
    1. bootstrap의 navbar를 활용하여 사이트의 상단를 완성하기

    2. 또한, modal 기능을 활용하여, 클릭하면 가입하는 창이 나타나는 기능 구현하기

    3. 스크롤을 하더라도 항상 화면 상단, 하단에 있도록 고정하기
        - fixed, sticky의 차이점을 파악하고 활용하기



## B. home.html
- 요구 사항 
    1. Header
        - Bootstrap Carousel Component로 구성합니다.
        - 이미지는 최소 3장 이상 사용하며 자동으로 전환됩니다.

        ![](README.assets/result4.png)


    2. Section
        - Section 내부의 개별 요소(article)들은 Bootstrap Card Component로 구성합니다.
            - 이미지, 제목, 설명을 포함합니다.
            - 이미지는 제공된 영화 포스터 이미지를 사용합니다.
        - 개별 요소들은 좌우 일정한 간격을 가집니다. (간격은 자유롭게 설정 가능)
        - Viewport의 가로 크기가 576px 미만일 경우 한 행에 1개씩 표시됩니다.

            ![](README.assets/result6.png)

        - Viewport의 가로 크기가 576px 이상일 경우 한 행에 2개 이상 표시됩니다. (자유롭게 설정 가능)

            ![](README.assets/result5.png)



- 문제 접근 방법 및 코드 설명
    ```html
    <body>
    <!-- 01_nav_footer에서 완성한 Navigation bar & Modal & Footer 코드를 적절한 위치에 사용합니다. -->


    <!-- 02_home.html -->
    <header>
        <!-- Bootstrap Carousel Component 활용, 최소 3장 이상 사용하며 자동으로 전환 -->
        <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
            <div class="carousel-item active">
            <img src="images/header1.jpg" class="d-block w-100" alt="...">
            </div>
            <div class="carousel-item">
            <img src="images/header2.jpg" class="d-block w-100" alt="...">
            </div>
            <div class="carousel-item">
            <img src="images/header3.jpg" class="d-block w-100" alt="...">
            </div>
        </div>
        </div>
    </header>

    <!-- 중앙정렬 -->
    <h1 class="text-center">Boxoffice</h1>

    <div>
        <!-- Bootstrap Card Component 활용 -->
        <!-- 가로 크기가 576px 미만일 경우 한 행에 1개씩 표시, 이상일 경우 한 행에 2개 표시
            758px 이상일 경우 3개 표시 -->
        <section class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-4">
        <article class="col">
            
            <!-- 길이는 100으로 고정 -->
            <div class="card h-100">
            <img src="images/movie1.jpg" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>

            </div>
            </div>
        </article>

        <article class="col">
            <div class="card h-100">
            <img src="images/movie2.jpg" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>

            </div>
            </div>
        </article>

        <article class="col">
            <div class="card h-100">
            <img src="images/movie3.jpg" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>

            </div>
            </div>
        </article>
        
        <article class="col">
            <div class="card h-100">
            <img src="images/movie4.jpg" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>

            </div>
            </div>
        </article>
        
        <article class="col">
            <div class="card h-100">
            <img src="images/movie5.jpg" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>

            </div>
            </div>
        </article>

        <article class="col">
            <div class="card h-100">
            <img src="images/movie6.jpg" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>

            </div>
            </div>
        </article>

        </section>
    </div>

    ```


- 어려웠던 점 및 문제의 포인트
- 어려웠던 점
    - Grid system를 활용하기 위해서는 container를 선언해줘야 하는데
    card에서는 `<section class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-4">` 이런 식으로 Grid system를 활용함.
        - `row-cols-1` : 화면이 576px미만일 때, 1개의 카드만 나옴.
        - `row-cols-sm-2` : 화면이 576px 이상이면, 2개의 카드만 나옴.


- 문제의 포인트
    1. Bootstrap Carousel 활용하여 이미지가 자동으로 변경되는 기능을 구현하기

    2. Bootstrap Card를 활용하여, 이미지 밑에 제목과 설명이 나오도록 구현하기

    3. Grid System(반응형 웹)를 활용하여 화면 크기에 따라 이미지 카드의 수가 달라지는 기능을 구현하기



## C. community.html
- 요구 사항 
    1. Aside (게시판 목록)
        - HTML aside 요소로 이루어져 있습니다.
        - Bootstrap List group Component로 구성합니다.
        - 내부의 각 항목은 클릭이 가능한 하이퍼링크이지만, URL은 별도로 없습니다.
        - Viewport의 가로 크기가 992px 미만일 경우 HTML main 요소 영역 전체만큼의 너비를 가집니다.
        - Viewport의 가로 크기가 992px 이상일 경우 HTML main 요소 영역 기준으로 좌측 1/6 만큼의 너비를 가집니다.
        - Viewport의 가로 크기 별 반응형 디자인은 스크린 샷 예시를 참고하여 일치하도록 합니다.

    2. Section (게시판)
        - 게시판은 HTML section 요소로 이루어져 있습니다.
        - 게시판은 Viewport의 가로 크기에 따라 전혀 다른 요소를 표시합니다.
            - Viewport의 가로 크기가 992px 미만일 경우 게시판은 HTML article 요소의 집합으로 표시되며, HTML main 요소 영역 전체만큼의 너비를 가집니다.

            - Viewport의 가로 크기가 992px 이상일 경우 게시판은 Bootstrap Tables Content로 구성되며, HTML main 요소 영역 기준으로 우측 5/6 만큼의 너비를 가집니다.


    3. Pagination
        - Bootstrap Pagination Component로 구성합니다.
        - 게시판 하단에 위치하며 너비는 자유롭게 설정합니다.
        - 자신의 영역 안에서 수평 중앙 정렬되어 있습니다.
        - 내부의 각 항목은 클릭이 가능한 하이퍼링크이지만, URL은 별도로 없습니다.



- 결과
    1. 992px 미만일 경우 

        ![](README.assets/result7.png)

    2. 992px 이상일 경우 

        ![](README.assets/result8.png)


- 문제 접근 방법 및 코드 설명
    ```html 
    <!-- 03_community.html -->
    <main>
        <!-- Aside - 게시판 목록 -->

        <!-- 반응형 웹 호출 -->
        <div class="container">
        <h1>Community</h1>

        <div class="row">
            <!-- 992px 미만일 경우 HTML main 요소 영역 전체만큼의 너비, 12사이즈 -->
            <!-- 992px 이상일 경우 HTML main 요소 영역 기준으로 좌측 1/6 만큼의 너비, 2사이즈 -->
            <aside class="col-12 col-lg-2">

            <!-- Bootstrap List group Component 활용 -->
            <!-- 내부의 각 항목은 클릭이 가능한 하이퍼링크, a태그 활용 -->
            <ul class="list-group">
                <li class="list-group-item"><a href="#" class="text-decoration-none">Boxoffice</a></li>
                <li class="list-group-item"><a href="#" class="text-decoration-none">Movies</a></li>
                <li class="list-group-item"><a href="#" class="text-decoration-none">Genres</a></li>
                <li class="list-group-item"><a href="#" class="text-decoration-none">Actors</a></li>
            </ul>
            </aside>
        

            <!-- Section - 게시판 -->
            <!-- 게시판은 Viewport의 가로 크기에 따라 전혀 다른 요소를 표시, d-None를 활용 -->

            <!-- 992px 미만일 경우 전체만큼의 너비, 992px 이상일 경우 우측 5/6 만큼의 너비 -->
            <section class="col-12 col-lg-10">

            <!-- 일반적으로 없다가 (d-none), 992px 이상일 경우 블록형식으로 나타남 (d-lg-block) -->
            <div class="d-none d-lg-block">

                <!-- 992px 이상일 경우 게시판은 Bootstrap Tables Content로 구성 -->
                <table class="table table-striped">
                <thead>
                    <tr class="table-dark">
                    <th scope="col">영화 제목</th>
                    <th scope="col">글 제목</th>
                    <th scope="col">작성자</th>
                    <th scope="col">작성 시간</th>
                    </tr>
                </thead>
                
                <tbody>
                    <tr>
                    <td>Great Movie title</td>
                    <td>Best Movie Ever</td>
                    <td>user</td>
                    <td>1 minute ago</td>
                    </tr>

                    <tr>
                    <td>Great Movie title</td>
                    <td>Movie Test</td>
                    <td>user</td>
                    <td>1 minute ago</td>
                    </tr>

                    <tr>
                    <td>Great Movie title</td>
                    <td>Movie Test</td>
                    <td>user</td>
                    <td>1 minute ago</td>
                    </tr>

                    <tr>
                    <td>Great Movie title</td>
                    <td>Movie Test</td>
                    <td>user</td>
                    <td>1 minute ago</td>
                    </tr>

                </tbody>
                
                </table>
            </div>


            <div>
                <!-- 992px 미만일 경우 전체만큼의 너비만큼 생성, 이상이면, 사라짐 -->
                <article class="col-12 d-lg-none">
                <hr class="m-3">

                <!-- Bootstrap List group Component 활용 -->
                <ul class="list-group list-group-flush">
                    <li class="list-group-item">
                    <h2>Best Movie Ever</h2>
                    <h5>Great Movie Title</h5>
                    <p>user</p>
                    <p>1 minute ago</p>
                    </li>

                    <li class="list-group-item">
                    <h2>Movie Test</h2>
                    <h5>Great Movie Title</h5>
                    <p>user</p>
                    <p>1 minute ago</p>
                    </li>

                    <li class="list-group-item">
                    <h2>Movie Test</h2>
                    <h5>Great Movie Title</h5>
                    <p>user</p>
                    <p>1 minute ago</p>
                    </li>

                </ul>
                <hr class="m-3">

                </article>
            </div>


            <!-- Bootstrap Pagination Component 활용 -->
            <!-- 자신의 영역 안에서 수평 중앙 정렬, d-flex justify-content-center -->
            <nav aria-label="Page navigation example" class="d-flex justify-content-center">
                <ul class="pagination">
                <li class="page-item"><a class="page-link" href="#">Previous</a></li>
                <li class="page-item"><a class="page-link" href="#">1</a></li>
                <li class="page-item"><a class="page-link" href="#">2</a></li>
                <li class="page-item"><a class="page-link" href="#">3</a></li>
                <li class="page-item"><a class="page-link" href="#">Next</a></li>
                </ul>
            </nav>
            </section>
        
        </div>
        </div>
    </main>
    ```


- 어려웠던 점 및 문제의 포인트
    - 어려웠던 점
        1. Grid system이 블록인 형태에서 사용가능하다는 점을 알았음.
        즉, 인라인 요소로 되어 있을 경우, block 형태로 변환을 해줘야 grid system를 사용할 수 있음.

        2. 992px 미만일 때, list와 표가 수평적으로 배치하는 부분에서, 태그들이 꼬여서 디버깅.
            - Grid system를 불러오는 과정에서 div를 생성하고 닫는 과정에서 중간에 div의 닫는 태그가 하나더 발생.
            - 🌟 태그 관리를 제대로 하지 않으면 멀쩡한 코드도 제대로 작동하지 않음.

        3. 992px 미만일 때는 표가, 992px 이상일 때에는 리스트형식의 내용이 나오게 하는 부분
            - 크기에 따른 내용 크기를 설정하는 부분만 배웠는데, 크기에 따라 내용의 형식이 달라지는 것은 배우지 않아서 막막했음.

            - 🌟 d-none를 활용하여, 일정한 상태가 되면, 보이지 않게 함.
            `<div class="d-none d-lg-block">` : 992px 미만일 경우 사라졌다가 (d-none), 992px 이상일 경우 블록형식으로 나타남 (d-lg-block)


    - 문제의 포인트
        1. 표형식과, 리스트 형식으로 내용을 나타내기

        2. Grid System를 활용하여, 화면의 크기에 따라 전혀 다른 요소를 표시하기 🌟🌟🌟 

        3. Bootstrap Pagination 활용하여 다음 장으로 넘어가는 버튼을 만들기

