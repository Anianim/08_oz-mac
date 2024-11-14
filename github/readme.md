### OZ Coding Backend
1. [Github]


### Day 1

ctrl + ` //터미널 단축키 상위터미널 클릭후 새 터미널 로도 가능
claer //터미널 지우기

mkdir " " // 디렉토리 생성 
cd " " // 디렉토리 이동
pwd //현재 디렉토리 확인


Git파일 commit하는 순서
git init 으로 초기화 // 상위 디렉토리에서 권한 설정을 해야함 

git config // 이용해서 기본 설정 
 - git config user.name " "
 - git config user.email " "
 - git config --list // config 확인하가능 

git config --global //전역 설정 
 - git config --global user.name " "
 - git config --global user.email " "
 - git config --global --list // global config 확인하가능 

git add " " //커밋할 대상추가
git resert " " //커밋할 대상 취소
git add . //*이전? 전체? 커밋 대상 추가*
git status //현재 git 상태 확인
git commit -m " " // 커밋시 메세지
git branch -M main // main대신 master 가 최상위일때 변경필요 일부 운영체제 버전따라 수정필요 
git remote add origin https://github/"닉네임"/"리파지토리명.git"  // origin 에 리파지토리 지정
git remote origin //
git remote -v //상세 origin 주소확인가능


git log //로그 확인가능 
git push -u origin main // commit 파일 push  

*git init 을 잘못할경우 repositories에 제대로된 디렉토리가 생성 되지 않고 commit , push 되지 않을 수 있다.*


