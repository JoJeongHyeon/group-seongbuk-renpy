# Git 협업을 위한 필수 명령어 가이드

이 문서는 팀 프로젝트에서 Git을 사용하여 협업할 때 자주 사용하는 필수 명령어들을 정리한 가이드입니다.

---

### 1. 프로젝트 시작 및 동기화

원격 저장소의 코드를 가져오거나 최신 상태로 업데이트합니다.

-   `git clone [저장소 URL]`
    -   **설명**: 원격 저장소(GitHub 등)의 프로젝트를 내 컴퓨터로 처음 복제해올 때 사용합니다.

-   `git fetch origin`
    -   **설명**: 원격 저장소의 최신 변경 내역을 일단 가져오기만 합니다. 현재 작업 내용과 합치지 않으므로, 안전하게 원격의 변경 사항을 확인할 때 유용합니다.

-   `git pull origin [브랜치 이름]`
    -   **설명**: 원격 저장소의 최신 변경 내용을 내 컴퓨터로 가져와서 현재 브랜치에 즉시 합칩니다(merge). `fetch` + `merge`가 합쳐진 명령어입니다.

---

### 2. 브랜치 작업 (독립적인 기능 개발)

다른 작업에 영향을 주지 않고 독립적인 공간에서 새로운 기능을 개발하거나 버그를 수정합니다.

-   `git branch`
    -   **설명**: 내 컴퓨터(로컬)의 브랜치 목록을 보여줍니다. `*` 표시가 현재 작업 중인 브랜치입니다.

-   `git branch -a`
    -   **설명**: 로컬 브랜치와 원격 저장소의 모든 브랜치를 함께 보여줍니다.

-   `git checkout [브랜치 이름]`
    -   **설명**: 다른 브랜치로 작업을 전환합니다. 원격에만 있는 브랜치 이름으로 실행하면, 해당 브랜치를 로컬로 가져와 자동으로 전환해줍니다.

-   `git checkout -b [새 브랜치 이름]`
    -   **설명**: 새로운 브랜치를 생성하고 **바로 그 브랜치로 전환**까지 한 번에 처리합니다.

---

### 3. 변경 내용 저장 및 공유

수정한 코드를 저장하고 팀원들과 공유하기 위해 원격 저장소에 업로드합니다.

-   `git status`
    -   **설명**: 현재 작업 폴더의 파일 변경 상태(수정, 추가, 삭제 등)를 한눈에 보여줍니다.

-   `git add .`
    -   **설명**: 현재 폴더와 하위 폴더의 **모든 변경 사항**을 커밋할 목록(Staging Area)에 추가합니다. (`.`은 '모든 것'을 의미합니다.)

-   `git add [파일 이름]`
    -   **설명**: **특정 파일**의 변경 사항만 골라서 커밋할 목록에 추가합니다.

-   `git commit -m "커밋 메시지"`
    -   **설명**: 스테이징된 변경 사항들을 하나의 작업 단위(커밋)로 묶어 저장하고, 어떤 작업을 했는지 설명하는 메시지를 남깁니다.

-   `git push origin [브랜치 이름]`
    -   **설명**: 내 컴퓨터에 커밋된 내용을 원격 저장소(GitHub)에 업로드하여 팀원들과 공유합니다. **어디로(origin) 무엇을(브랜치 이름) 보낼지 명확히 지정하는 가장 안전한 방법입니다.**

---

### 4. 다른 사람의 브랜치 가져오기

팀원이 작업한 브랜치(예: `Feature-Jeonghyeon`)를 내 컴퓨터로 가져와서 확인하거나 함께 작업할 수 있습니다.

#### 방법 1: 처음 프로젝트를 받는 경우

```bash
# 1. 저장소를 처음 클론
git clone [저장소 URL]

# 2. 클론한 폴더로 이동
cd [프로젝트 폴더명]

# 3. 원격 브랜치 확인
git branch -a

# 4. 원하는 브랜치로 전환 (자동으로 로컬에 생성됨)
git checkout Feature-Jeonghyeon
```

#### 방법 2: 이미 프로젝트가 있는 경우

```bash
# 1. 원격 저장소의 최신 정보 가져오기
git fetch origin

# 2. 원격 브랜치 목록 확인
git branch -a

# 3. Feature-Jeonghyeon 브랜치로 전환
git checkout Feature-Jeonghyeon

# 또는 새로 생성하면서 원격 브랜치 추적
git checkout -b Feature-Jeonghyeon origin/Feature-Jeonghyeon
```

#### 최신 변경사항 받기

```bash
# 현재 브랜치가 Feature-Jeonghyeon일 때
git pull origin Feature-Jeonghyeon
```

---

### 5. 팀원의 작업 내용을 내 브랜치에 반영하기

다른 팀원의 작업이 `develop` 브랜치에 머지되었고, 그 변경사항을 내 Feature 브랜치에 가져오는 방법입니다.

#### 기본 흐름

```
팀원 작업 완료 → develop에 PR & 머지 → 내가 develop에서 받아오기
```

#### 실제 명령어

```bash
# 1. 현재 작업 중인 파일 커밋 (중요!)
git add .
git commit -m "내 작업 저장"

# 2. develop의 최신 변경사항을 내 브랜치에 가져오기
git pull origin develop

# 3. 충돌 없으면 완료!
# 충돌 있으면 아래 "충돌 해결" 섹션 참고

# 4. 작업 계속...
```

#### 예시 상황

**정현이 작업이 develop에 머지됨**
→ 민욱이 자기 브랜치(`Feature-Minwook`)에서 작업 중
→ 정현이 작업을 받아와야 함

```bash
# 민욱이 할 일
git checkout Feature-Minwook  # 내 브랜치 확인
git add .
git commit -m "민욱 루트 작업 중"
git pull origin develop  # develop의 최신 변경사항 가져오기
```

#### 작업 시작 전 습관화하기

```bash
# 매번 작업 시작 전에
git pull origin develop
```
이렇게 하면 항상 최신 develop 상태에서 작업할 수 있습니다!

---

### 6. Pull Request (PR) 생성

완료된 작업을 develop 브랜치에 합치기 위한 과정입니다.

#### GitHub에서 PR 생성 방법

**1단계: 작업 푸시**
```bash
git push origin Feature-Jeonghyeon
```

**2단계: GitHub에서 PR 생성**
1. GitHub 저장소 페이지로 이동
2. 상단에 `Compare & pull request` 버튼이 나타남 (최근 푸시한 경우)
3. 또는 `Pull requests` 탭 → `New pull request` 클릭
4. **Base 브랜치**: `develop` 선택
5. **Compare 브랜치**: `Feature-Jeonghyeon` 선택
6. PR 제목과 설명 작성:
   ```
   제목: 장혁 캐릭터 루트 구현
   
   설명:
   - 장혁 캐릭터 대화 스크립트 추가
   - 테이블 상호작용 구현
   - 관련 이미지 리소스 추가
   ```
7. 팀원을 **Reviewer**로 지정
8. `Create pull request` 클릭

**3단계: 리뷰 및 머지**
- 팀원이 코드 확인
- 필요시 수정 요청
- 승인 후 `Merge pull request` 클릭
