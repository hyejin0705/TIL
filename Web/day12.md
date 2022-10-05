## CSS Layout

- CSS layout techniques
    - display
    - position
    - float
    - flexbox
    - grid
    - 기타
        - Responsive Web Design, Media Queries
        
- float
    - 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인요소들이 주변을 wrapping하도록 함.
    - 요소가 Normal flow를 벗어나도록 함.
    - float 속성
        - none : 기본값
        - left : 요소를 왼쪽으로 띄움
        - right : 요소를 오른쪽으로 띄움
            
            ```html
            <style>
            	/* CSS 작성 */
            	.box{
            		width: 150px;
            		height: 150px;
            		border: 1px solid black;
            		background-color: crimson;
            		margin: 20px;
            	}
            
            	.left{
            		float: left;
            	}
            
            	.right{
            		float: right;
            	}
            </style>
            
            <body>
            	<!-- 클래스 선택자  div.class*3 -->
            	<div class="box left">float left</div>
            	<div class="box left">float left</div>
            	<div class="box right">float right</div>
              <p>lorem
            		lorem
            		lorem
            	</p>
            </body>
            ```
            

- flexbox
    - CSS Flexible Box Layout (ie 부분지원)
        - 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
        - 축
            - main axis(메인 축) : 꼬치
            - cross axis(교차 축) : 먹는 방향?
  
        
        - 구성요소
            - flex container (부모 요소) : flex를 적용시켜야 함.
            - flex item (자식 요소)
            
        - Flexbox 구성요소
            - Flex Container (부모요소)
                - flexbox 레이아웃을 형성하는 가장 기본적인 모델
                - flex item들이 놓여있는 영역
                - display 속성을 flex 혹은 inline-flex로 지정
            - flex item (자식요소)
                - 컨테이너에 속해 있는 컨텐츠(박스)
            
        - flex-direction: row : 인라인요소(내용물의 크기만큼)처럼 변함
            

        - flex-direction: row-reverse : 역순으로
            

        - flex-direction: column; : block요소(한 줄을 다 차지)처럼 변함
        - flex-direction: column-reverse; 역순
            
          
        
        - display : flex;
            

        - display : inline-flex;  테두리가 줄어듦
           
        
        - 실습 자료들
            
            [SSAFY](https://lab.ssafy.com/s08/python/web)
            
        
    - CSS Flexible Box Layout 사용하는 이유
        - 이전까지 Normal Flow를 벗어나는 수단은 Float 혹은 Position밖에 없었음
        - (수동값 부여 없이)
            1. 수직 정렬
            2. 아이템의 너비와 높이 혹은 간격을 동일하게 배치
    
    - Flex 속성
        - 배치 설정
            - flex-direction
                - main axis 기준 방향 설정
                - 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의(웹 접근성에 영향)
                    

            - flex-wrap
                - 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
                - 즉, 기본적으로 컨테이너 영역을 벗어나지 않도록 함.
                    
             
                - 요소들이 강제로 한 줄에 배치되게 할 것인지 여부 설정
                    - flex-wrap : nowrap(기본값) (한 줄 안에 다 집어넣기, 한 줄에 배치)
                    - flex-wrap : wrap (줄바꿈, 넘치면 다음 줄로 배치)
                    - flex-wrap : wrap-reverse
                        
                       
                
            - flex-flow
                - flex-direction과 flex-wrap의 shorthand
                - flex-direction과 flex-wrap에 대한 설정 값을 차례로 작성
                - 예시 ) flex-flow: row nowrap;
                
        - 공간 나누기
            
            - justify-content (main axis)
                - main axis를 기준으로 공간 배분
                    
                    
            
            - align-content (cross axis)
                - cross axis를 기준으로 공간 배분 (아이템이 한 줄로 배치되는 경우 확인할 수 없음)
                   
            
            - 속성
                - flex-start (기본값) : 아이템들을 axis 시작점으로
             
                - flex-end : 아이템들을 axis 끝 쪽으로
                
                - center :  아이템들을 axis 중앙으로
                                   
                - space-between :  아이템 사이의 간격을 균일하게 분배

                - space-around : 아이템을 둘러싼 영역을 균일하게 분배 (가질 수 있는 영역을 반으로 나눠서 양쪽에)
                                    
                - space-evenly : 전체 영역에서 아이템 간 간격을 균일하게 분배


        - 정렬
            - align-items (모든 아이템을 cross axis 기준으로)
 
                - align-items: stretch
                
                - align-items: flex-start
                    
                - align-items: flex-end
                                    
                - align-items: center
             
                - align-items: baseline
                   
                
            - align-self (개별 아이템)
                - 개별 아이템을 cross axis 기준으로 정렬
                    
                    주의! 해당 속성은 컨테이너에 적용하는 것이 아니라 개별 아이템에 적용


                
                - align-self: flex-start
                - align-self: centet
                - align-self: flex-end
                - align-self: stretch
                    
                 
                
                - 속성
                    - stretch(기본값) : 컨테이너를 가득 채움
                    - flex-start : 위
                    - flex-end : 아래
                    - center : 가운데
                    - baseline: 텍스트 baseline에 기준선을 맞춤
            
            - Flex에 적용하는 속성
                - 기타 속성
                    - flex-grow: 남은 영역을 아이템으로 분배
                        
                    
                    - order: 배치 순서
                        
                

- grid

## bootstrap

- Build fast, reponsive sites with Bootstrap
- CDN
    - Content Delivery Network
    - 컨텐츠을 효율적으로 전달하기 위해 여러 모드에 가진 네트워크에 데이터를 제공하는 시스템.
    - 개발 end-user의 가까운 서버를 통해 빠르게 전달 가능(지리적 이점)
    - 외부 서버를 활용함으로써 본인 서버의 부하가 적어짐.
        
      

- Bootstrap 기본원리
    - spacing (Margin and padding)
        - {property}{sides}-{size}
        - mt-3
        
        - property
            - m - for classes that set margin
            - p - for classes that set padding
        - sides
            - t : top
            - b: bottom
            - s: start(left)
            - e: end(right)
            - x: 좌우
            - y: 상하
            - blank: 4방향 다
        
        - size
            - 0~5 : 0, 0.25, 0.5, 1.5, 3 (rem)
            - : 4, 8, 16, 24, 48 (px)
        - .mx-auto
            - 수평 중앙 정렬
            - 가운데 정렬



    - color (bg-, text-)
        - primary(blue), secondary(grey), success(green), info(skyblue), warning(yellow), danger(red)


    
    - Text
        - text-decoration-none : 밑줄 없어짐.
        


    - display, position
        - 부모클래스에 relative설정해야 자식클래스에서 absolute가 가능.
        - 아니면, 웹을 기준으로 설정됨.

    - components
        - boostrap의 다양한 ui 요소를 활용할 수 있음
        - 아래 components 탭 및 검색으로 원하는 ui요소를 찾을 수 있음
        
        - 종류
            - button
            - dropdowns
            - form
            - caroucel
            - modal
                - 중첩되어 들어가 있으면 안 됨.
            - flex
            - cards
                - grid cards
    
    - Responsive Web Design
        - 다양한 화면 크기를 가진 디바이스들이 등장함에 따라 reponsive web design 개념이 등장
        - 반응형 웹은 별도의 기술 이름이 아닌 웹 디자인에 대한 접근방식, 반응형 레이아웃 작성에 도움이 되는 사례들의 모음 등을 기술하는데 사용되는 용어
        
        - breakpoints
            
     
        - bootstrap grid system
        
- bootstrap grid system
    - 요소들의 디자인과 배치에 도움을 주는 시스템
    - 기본 요소
        - column : 실제 컨텐츠를 포함하는 부분
        - gutter: 칼럼과 칼럼 사이의 공간 (사이 간격)
        - container: column들을 담고 있는 공간
    - booststrap grid system은 flexbox로 제작됨
    - container, rows, column으로 컨텐츠를 배치하고 정렬
    - 반드시 기억해야 할 2가지
        - 12개의 column
        - 6개의 grid breakpoints
            
           
    
    - Grid system breakpoints
        - .col-{breakpoint}-
        - 옵션
            - extra small (xs)
            - small (sm)
            - large (lg)
            - extra large (xl)
            - extra extra large (xxl)
            
        - 크기에 따라 비율이 변경되도록 설정
           
        
        - nesting
            
                
        - offset

