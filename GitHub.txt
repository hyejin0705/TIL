# Git이란?

- git? 분산버전관리 프로그램
  - 버전 : 컴퓨터 소프트웨어의 특정 상태
  - 중앙집중 ↔ 분산
- git 기반의 저장소 서비스 : GitLab(싸피), GitHub(일반적으로), bitbucket
  - GitHub : 마이크로소프트 (내부)서버에 저장
  - GitLab : 저장하는 서버를 마음대로 구축 가능 (삼성 내부 서버 이용)
          (버전관리는 Git이 해주는 거라 사용방법은 같음?)
  
- Github : 모든 사람들에게 공개 가능
        *하루에 한번 커밋하기*


# CLI

- CLI(명령어로 새로만들기) ↔ GUI(그래픽으로 새로만들기)
- CLI(Command Line Interface) : 경제적이고, GUI로는 못 하는 걸 많이 할 수 있음
- GUI(Graphic User Interface) : 그래픽을 통해 사용자와 컴퓨터가 상호작용하는 시스템
  - GUI는 CLI에 비해 사용하기 쉽지만 단계가 많고 컴퓨터의 성능을 더 많이 소모
  - 수많은 서버/개발 시스템이 CLI를 통한 조작 환경을 제공
- 기본적인 명령어
  - clear : 내용 삭제
  - touch : 파일을 생성하는 명령어
  - MKdir : 새 폴더를 생성하는 명령어      
      
  - ls : 현재 작업 중인 디렉토리의 폴더/파일 목록을 보여주는 명령어
  - cd : 현재 작업 중인 디렉토리를 변경하는 명령어
      
  
  - start(W), open(M) : 파일/폴더를 여는 명령
  - rm : 파일을 삭제하는 명령어
    - -r 옵션(폴더 안의 모든 파일들을 제거하고 폴더도 삭제)
              주면 폴더 삭제 가능

  - SSAFY@DESKTOP : 컴퓨터 이름
  - ~ : 현재 작업중인 위치/유저의 홈 디렉토리 (C:\Users\multicampus)

- cd .. : 상위폴더로 이동
  - .. (상위폴더)
 
  - . (현재 폴더)


# Git 기본

- README.md
  - 프로젝트에 대한 설명 문서
- Repository
  - 특정 디렉토리를 버전 관리하는 저장소
  - git init 명령어로 로컬 저장소를 생성  
    - .git(숨김파일로 생김)
    - (master) 생성됨.

  - git 디렉토리에 버전 관리에 필요한 모든 것이 들어 있음.

- [README.md](http://README.md) 생성하기
  - 새 폴더를 만들고 파일을 생성해주세요
  - 이 파일을 버전 관리하며  Git을 사용해 봅시다.
    - 특정 버전으로 남긴다 = 커밋(Commit)한다.  
      3가지 영역(working directory, staging area, repository)을 바탕으로 동작

      - Working directory : 내가 작업하고 있는 실제 디렉토리
      - Staging Area : 커밋(Commit)으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳
      - Repository : 커밋(Commit)들이 저장되는 곳


# Git 기본 명령어

- git add
  - untracked파일의 변경사항을 Staging Area에 올리는 명령어
  - untracked파일 → tracked(=staged)파일로 변경됨.

- git commit
  - Staging Area → Commit하기 위해
  - commited파일이 Repository에 저장

- 파일이 수정되면 modified 상태로 변함
  - 다시  git add → git commit 사이클이 돌아가면서 commit.

- git status
  - 현재 git으로 관리되고 있는 파일의 상태를 알 수 있음.
 
    - untracked files(저장이 안 됨.)
    - git add [README.m](http://README.md)d 하지 않음. 해야 한다.

- git commit -m “한줄설명”   


- git log : commit 내용을 확인가능

- github Repository 생성하기
  - git remote add origin {remote_repo 주소(url)}
      
  
  - 처음에 push 할 때에는 로그인해서 연결해야
      
  
  - git push -u origin master : origin과 repo가 붙음
      - origin : repo_name 별명
        
- git clone {remote_repo}
  - remote_repo를 local로 복사합니다.
      
  
  - VScode로 이동하기
      - git bash 버전 : code .