# 📝 Python 코딩테스트 팀 스터디 가이드라인 🚀

## 1️⃣ 개요
### 📅 진행 일정
- **기간**: 2025.03.07 ~ 2025.06.07
- **목표**: 백준 문제 풀이를 통해 코딩테스트 대비
- **방식**: 주별 문제 풀이 & 코드 리뷰

### 📂 폴더 구조
```
📂 coding-test-study
 ├── 📂 week01  # 1주차 문제 풀이
 │   ├── README.md  # 1주차 문제 설명
 │   ├── problem_1000_박민용.py  # A+B 문제 풀이
 │   ├── problem_2557_박민용.py  # Hello World 문제 풀이
 │   └── ...
 ├── 📂 week02  # 2주차 문제 풀이
 ├── 📂 solutions  # 참고 풀이 모음
 │   ├── optimized_solutions.md  # 최적화된 풀이 정리
 │   ├── best_practices.md  # 코드 스타일 및 모범 사례
 │   ├── common_mistakes.md  # 자주 하는 실수 모음
 ├── 📂 docs  # 스터디 규칙 및 계획
 │   ├── RULES.md  # 스터디 운영 규칙
 │   │   ├── 참여 방식, 코드 리뷰 기준, 주별 목표
 │   ├── PLAN.md  # 전체 스터디 계획
 │   │   ├── 주차별 학습 목표 및 문제 리스트
 │   │   ├── GitHub 사용법 & PR 작성 가이드
 ├── 📂 .github  # GitHub Actions (자동화)
 │   ├── workflows
 │   │   ├── ci.yml  # 코드 테스트 자동 실행
 │   │   │   ├── 문제 풀이 코드 자동 테스트 실행
 │   │   │   ├── PR 생성 시 테스트 실행 및 결과 확인
 ├── README.md  # 메인 소개 페이지
 ├── .gitignore  # 불필요한 파일 제외
 ├── requirements.txt  # 필요한 패키지 리스트

## 2️⃣ GitHub 스터디 진행 방법

### 📌 1. 레포지토리 클론하기
```sh
git clone https://github.com/yamewrong/coding-test-study.git
cd coding-test-study
```

### 📌 2. 본인 브랜치 생성
```
git checkout -b feature/{이름}/week{번호}
```
✅ 예시:
```sh
git checkout -b feature/yamewrong/week01
```

### 📌 3. 문제 풀이 후 코드 업로드
```sh
git add problem_1000_박민용.py
git commit -m "[Week01] A+B 문제 풀이 - 박민용"
git push origin feature/계정명/week01
```

### 📌 4. PR(Pull Request) 생성 & 코드 리뷰
1. GitHub에서 `Pull Request` 생성
2. 팀원들 코드 리뷰 진행
3. `main` 브랜치에 병합(Merge)

### 📌 5. 브랜치 삭제 (정리)
```sh
git branch -d feature/이름/week01
```

## 3️⃣ Git 커밋 & PR 규칙
### 📌 커밋 메시지 규칙
```
[Week{번호}] 문제이름 - {이름}
```
✅ 예시:
```sh
git commit -m "[Week01] DFS 문제 풀이 - 박민용"
```

### 📌 PR 제목 & 내용 예시
**PR 제목**
```
[Week01] 문제이름 - 박민용
```

**PR 내용**
```md
### 문제 설명
- A+B 문제 풀이

### 풀이 방법
- 입력값을 받아 두 수를 더한 후 출력
- 시간복잡도: O(1)

### 리뷰 요청 사항
- 더 나은 코드 개선 방법이 있을까요?
```

## 4️⃣ 자동화 기능 (GitHub Actions)
📌 **자동 코드 테스트 (`.github/workflows/ci.yml`)**
```yaml
name: Python CI

on:
  pull_request:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8
      - name: Install Dependencies
        run: pip install -r requirements.txt
      - name: Run Tests
        run: pytest
```
✅ PR을 올릴 때 자동으로 코드 테스트 실행됨!

---

## 📌 마무리
✅ GitHub 스터디 **폴더 & 브랜치** 체계적으로 정리  
✅ **Git 커밋 & PR 규칙** 통일 → 코드 관리 깔끔하게!  
✅ GitHub **자동화(CI/CD) 설정**으로 코드 품질 유지  


