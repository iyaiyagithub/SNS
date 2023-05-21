# AI-5_A5_SNS
# Django-rest-framework-Project-Newsfeed
DRF를 이용한 Newsfeed 사이트 만들기!

## 🖥️ 프로젝트 소개
인스타그램이나 페이스북 같은 SNS를 직접 만들어 보고자 하는 목표를 가지고 일상을 공유할 수 있는 SNS 사이트를 제작하였습니다.

## 🕰️ 개발 기간
* 23.04.10 - 23.04.18

### 🧑‍🤝‍🧑 팀원 구성 및 역할 분담
- 팀장😄  : 조혜민 - 게시물 수정, 삭제 / 태그
- 팀원😄1 : <a href="https://guco.tistory.com/">구민정</a> - 게시물 작성 / 좋아요
- 팀원😄2 : 김은수 - 피드페이지 및 마이페이지 조회 / 팔로우(미구현)
- 팀원😄3 : 윤찬효 - 로그인 / 회원가입 / 좋아요
- 팀원😄4 : 임라온 - 프로필 조회 및 수정

### ⚙️ 개발 환경
- `Python 3.11`
- **IDE** : `visual studio code`
- **Framework** : `Django-Rest-Framework`
- **Database** : `sqllit3`
- **requirements.txt** : `requirements.txt`

### 🔑 프로젝트 설치 및 실행 방법
#### 깃허브 클론하기
```
$ git init
$ git clone git@github.com:goodminjeong/AI-5_A5_SNS.git
```
#### 패키지 밎 라이브러리 설치
```
$ pip install -r requirements.txt
```
#### DB 연동
```
$ python manage.py makemigrations
$ python manage.py migrate
```
#### 서버 실행
```
$ python manage.py runserver
```

## 📌 주요 기능
### 목차
#### [1. 로그인](#로그인)
#### [2. 회원가입](#회원가입)
#### [3. 홈](#홈)
#### [4. 마이페이지](#마이페이지)
#### [5. 게시글](#게시글)
#### [6. 댓글](#댓글)
#### [7. 글쓰기](#글쓰기)
#### [8. 검색](#검색)
#### [9. 태그 모음](#태그-모음)
#### [10. 로그아웃](#로그아웃)
#### [11. 프로필 수정](#프로필-수정)
------------
#### 로그인 
- DB값 검증
- 로그인 시 로그인 시 쿠키(Cookie) 생성
![image](https://github.com/goodminjeong/algorithm/assets/125722304/765d9d79-9da0-4ee4-8661-8e8f1025fa2a)

#### 회원가입 
- 회원가입 시 자동 로그인 되어 메인페이지로 이동
- 이미 존재하는 아이디 입력할 경우 안내 문구 뜸
![image](https://github.com/goodminjeong/algorithm/assets/125722304/6c9d4eb4-3c98-44ab-857b-d007acbf6334)
![image](https://github.com/goodminjeong/algorithm/assets/125722304/c5655ee4-aa80-4150-9283-f17b6b517af6)
![image](https://github.com/goodminjeong/algorithm/assets/125722304/680b4668-f6a8-4e63-ba2e-1bfa2e2fdedf)
![image](https://github.com/goodminjeong/algorithm/assets/125722304/fa35782e-7eab-4110-83c4-0292c4be3fd7)

#### 홈
- 유저들이 작성한 게시글들이 최신순으로 일자로 나열됨(인스타그램과 비슷한 형식)
![image](https://github.com/goodminjeong/algorithm/assets/125722304/51243292-257f-4d19-ab46-8ad078578567)

#### 마이페이지 
- 자신이 쓴 게시글 모아보기
![image](https://github.com/goodminjeong/algorithm/assets/125722304/dc816d77-399a-4c00-a9d8-f97928d605ba)

#### 게시글
- 유저 아이디 옆에 유저가 설정한 프로필 이미지가 보임(프로필 이미지 미설정 시 기본 이미지가 보임)
- 이미지 없는 게시글의 경우 기본 로고 이미지가 보이게 함
- 자신이 작성한 게시글에는 수정, 삭제 버튼이 있고, 타인이 작성한 게시글은 수정, 삭제 버튼이 보이지 않음
![image](https://github.com/goodminjeong/algorithm/assets/125722304/f6591aac-2455-4554-9c53-793a35b63e83)
- 글 수정 시 원래 있던 내용, 이미지, 태그가 채워져 있음
![image](https://github.com/goodminjeong/algorithm/assets/125722304/db68e54c-d8f3-4005-8c71-e40410b112ec)
- 글 삭제 시 "삭제할까요?" 확인창 띄운 후 확인 클릭 시 삭제, 취소 시 삭제 안 됨
![image](https://github.com/goodminjeong/algorithm/assets/125722304/2658ecf0-d351-427c-81e5-a4e6142f3b26)
![image](https://github.com/goodminjeong/algorithm/assets/125722304/6b46c412-13be-4f9f-a33e-ad8603f1c973)
- 좋아요 클릭 시 하트색 및 좋아요 개수 변경
![image](https://github.com/goodminjeong/algorithm/assets/125722304/9ee8b259-c618-4afc-a521-4633f1fbb6bc)
![image](https://github.com/goodminjeong/algorithm/assets/125722304/26858bba-cba6-4b99-8aec-578171f8602a)
- 태그 클릭 시 해당 태그가 포함된 게시글 모아볼 수 있음
![image](https://github.com/goodminjeong/algorithm/assets/125722304/36277a5a-59a3-4a82-b925-7aab82312f46)
![image](https://github.com/goodminjeong/algorithm/assets/125722304/f5427328-c2d1-4353-a7fb-e2fe4ab0a7b4)

#### 댓글
- 댓글 작성 후 엔터 누르면 댓글 작성됨
![image](https://github.com/goodminjeong/algorithm/assets/125722304/860c7f8f-3f0b-49cf-a86f-2672a541c28e)
![image](https://github.com/goodminjeong/algorithm/assets/125722304/73b6ad47-5557-405b-adcc-32384f59f6f4)
![image](https://github.com/goodminjeong/algorithm/assets/125722304/8febcea9-f10c-4406-b3d2-10e68456c8a5)
- 작성자만 본인 댓글을 삭제 가능
- 삭제 시 "삭제하시겠습니까?" 확인창 띄운 후 확인 클릭 시 삭제, 취소 시 삭제 안 됨
![image](https://github.com/goodminjeong/algorithm/assets/125722304/67656a1b-2809-465e-8430-e44614fd21fd)
![image](https://github.com/goodminjeong/algorithm/assets/125722304/7879c7a7-0797-4b88-b95e-b72ce6863b7c)

#### 글쓰기
- 글 내용, 이미지, 태그를 채워 넣을 수 있음
- 글 내용은 필수, 이미지와 태그는 선택사항
![image](https://github.com/goodminjeong/algorithm/assets/125722304/27d86681-7a56-4f02-8002-d946d0aeaa9c)
![image](https://github.com/goodminjeong/algorithm/assets/125722304/88b6915b-7f5a-4678-877c-be7bdcec23da)
![image](https://github.com/goodminjeong/algorithm/assets/125722304/7fce38ce-a30e-46b1-ae3e-21b0aed22ac4)

#### 검색
- 유저의 아이디나 게시글 내용으로 검색 가능함
![image](https://github.com/goodminjeong/algorithm/assets/125722304/3ea125d7-bfc2-4a1d-8afb-088748397d13)
![image](https://github.com/goodminjeong/algorithm/assets/125722304/85ca960c-4186-4903-9c74-052b516f9d26)
![image](https://github.com/goodminjeong/algorithm/assets/125722304/c6347ec6-2a4a-427f-a974-c7caf3ccbf9c)
![image](https://github.com/goodminjeong/algorithm/assets/125722304/55b211b9-d47f-48ff-8d8a-a48473bc8de4)

#### 태그 모음
- SNS 페이지에 작성된 게시글의 모든 태그들을 모아보는 기능
- 태그 클릭 시 해당 태그가 포함된 게시글들이 나옴
![image](https://github.com/goodminjeong/algorithm/assets/125722304/1b0331e7-8bec-4b7f-ac47-30c429ee0d03)
![image](https://github.com/goodminjeong/algorithm/assets/125722304/ce4301b7-3307-4891-83b0-5bce2573e63a)

#### 로그아웃
- 로그아웃 시 로그인 페이지로 이동함
![image](https://github.com/goodminjeong/algorithm/assets/125722304/59a96988-eeae-419c-9edd-d6c4f21d0754)
![image](https://github.com/goodminjeong/algorithm/assets/125722304/72f4ec39-157e-46c0-aaaf-675c6a86dfb5)

#### 프로필 수정
- 처음 회원가입 시 프로필 이미지는 기본 이미지로 보임
- 프로필 이미지를 추가하면 추가한 이미지가 보임
- 이름, 닉네임, 소개, 이메일 수정 가능함
- 아이디는 수정할 수 없도록 인풋박스를 만들지 않음
- DB에 저장된 데이터가 있다면 프로필 수정 시 그 데이터가 나오도록 함
- 이름, 닉네임, 소개, 이메일 칸을 비우면 DB에 데이터가 사라짐
![image](https://github.com/goodminjeong/algorithm/assets/125722304/87d21235-2e93-4997-a715-c23f4ca498be)
![image](https://github.com/goodminjeong/algorithm/assets/125722304/4d35a5a8-be80-42a7-ac64-5d5906f06cb1)
![image](https://github.com/goodminjeong/algorithm/assets/125722304/f1c432a5-8ee3-4260-bf47-7a9a1879d8f3)
![image](https://github.com/goodminjeong/algorithm/assets/125722304/bb3bd26a-a5be-4f3f-98f5-4abb930c5f3c)
