# 🌏 부산대 교환학생 필터: 100% 무료 배포 & Supabase 연동 완벽 가이드

이 프로젝트는 **Cloudflare Pages / GitHub Pages (정적 호스팅)**와 **Supabase (BaaS)**의 무료 티어만을 사용하여 **유지비 0원(완전 무료)**으로 평생 운영할 수 있도록 제작되었습니다.

---

## 📁 프로젝트 파일 구성

- **`index.html`**: 129개 해외 대학 정제 데이터와 고품질 모던 UI(Pretendard 폰트, 실시간 키워드 검색, 국기 뱃지, 테이블/카드 뷰 전환, 찜하기, 상세 모달, 운영자 콘솔)가 포함된 단일 파일 완성본
- **`supabase_schema.sql`**: Supabase에 실행하여 검색 로그 테이블 및 관리자 보안 함수를 생성하는 SQL
- **`run_local.sh`**: 로컬 컴퓨터에서 브라우저를 자동 실행해 주는 원클릭 스크립트 (`./run_local.sh`)
- **`test_server.py`**: 로컬 테스트용 간이 파이썬 웹 서버 (`python3 test_server.py`)
- **`DEPLOY_GUIDE.md`**: 본 배포 설명서

---

## ✨ 원본 대비 대폭 개선 및 수정된 사항
1. **데이터 파싱 버그 수정 (어학 요건 누락 해결)**:
   - 노르웨이과학기술대학(NTNU): TOEFL iBT 90 / IELTS 6.5 정상 복구 (기존 원본에서 누락)
   - 브레멘응용과학대학: TOEFL iBT 71 / IELTS 5.5 정상 복구 (기존 원본에서 누락)
   - 칸세이가쿠인대학: TOEFL iBT 71 정상 복구 (기존 원본에서 누락)
   - 중국인민대학: TOEFL iBT 90 / IELTS 6.0 정상 복구 (기존 원본에서 누락)
   - 국가명 줄바꿈 오류(`영국\n(웨일스)`, `중국\n(홍콩)`) 정규화로 필터 드롭다운 깨짐 해결
2. **고급 UI/UX 추가**:
   - **실시간 통합 검색바**: 대학명(국문/영문), 국가, 도시 즉시 검색 지원
   - **국기 이모지(🇳🇱, 🇺🇸, 🇯🇵 등)** 자동 표시
   - **⭐ 나만의 찜하기(즐겨찾기)** 기능: `localStorage`에 자동 저장되어 나만의 파견 희망 리스트 필터링 가능
   - **테이블 뷰 ↔ 카드 뷰 원클릭 전환**: 스마트폰 및 태블릿에서도 시각적으로 편리하게 탐색 가능
   - **대학명 원클릭 복사 버튼**: 클립보드 복사 및 슬라이드 토스트 메시지 안내

---

## STEP 1. Supabase 데이터베이스 세팅 (SQL 1번 실행)

사용자분의 프로젝트(`ihbpjyjpvcwhqqmgadvr`)와 `anon key`가 이미 `index.html`에 연동 완료되었습니다!
이제 Supabase에서 테이블만 생성해 주시면 됩니다:

1. [Supabase 대시보드 (ihbpjyjpvcwhqqmgadvr)](https://supabase.com/dashboard/project/ihbpjyjpvcwhqqmgadvr)에 접속합니다.
2. 왼쪽 메뉴 바에서 **[SQL Editor]** 아이콘을 클릭합니다.
3. **[+ New query]** 버튼을 누르고, 프로젝트 폴더의 `supabase_schema.sql` 파일 내용을 **전체 복사하여 붙여넣은 뒤 [Run (실행)]**을 클릭합니다.
   - `Success. No rows returned` 메시지가 나오면 `search_logs` 테이블 및 보안 정책 생성이 100% 완료됩니다!

---

## STEP 2. `index.html` 설정 (이미 완료됨!)

사용자분의 Supabase Project URL 및 anon 키가 이미 코드에 안전하게 삽입되었습니다:
- **Project URL**: `https://ihbpjyjpvcwhqqmgadvr.supabase.co`
- **anon Key**: `eyJhbGciOiJIUzI1Ni...` (적용 완료)

---

## STEP 3. 무료 클라우드 배포 (택 1, 소요시간: 1분)

### 방법 A. Cloudflare Pages로 배포 (⭐ 가장 추천: 초고속, 무제한 대역폭, 파일 드래그앤드롭)

1. [Cloudflare](https://dash.cloudflare.com/)에 회원가입/로그인합니다.
2. 왼쪽 메뉴에서 **Workers & Pages** -> **Create application** -> **Pages** 탭 클릭
3. **[Upload assets]** (직접 업로드) 선택
4. Project name 입력 (예: `pusan-exchange`)
5. `index.html`이 있는 `pusan-exchange-clone` 폴더 전체를 브라우저 드래그 영역에 끌어다 놓습니다.
6. **[Deploy site]** 버튼을 누르면 **10초 만에 `https://pusan-exchange.pages.dev` 주소로 즉시 전 세계 무료 라이브 배포**됩니다!
   *(개인 도메인이 있다면 무료로 커스텀 도메인 연결도 가능합니다)*

---

### 방법 B. GitHub Pages로 배포 (원본 사이트와 동일한 방식)

1. [GitHub](https://github.com)에 로그인 후 새 Repository를 생성합니다 (예: `exchange-filter`).
2. `index.html`을 레포지토리의 메인 브랜치 루트에 업로드(푸시)합니다.
3. 레포지토리 상단의 **Settings** -> 왼쪽 메뉴 **Pages** 클릭
4. **Build and deployment** 항목에서:
   - Source: `Deploy from a branch`
   - Branch: `main` / Folder: `/ (root)` 선택 후 **[Save]** 클릭
5. 1분 뒤 `https://<내깃허브아이디>.github.io/exchange-filter/` 주소로 무료 배포 완료!

---

## ⚙️ 운영자 콘솔(관리자 페이지) 사용 방법

1. 배포된 사이트 최하단으로 스크롤하면 작고 은은한 **⚙** 아이콘 버튼이 있습니다.
2. 클릭하면 관리자 로그인 모달이 열립니다.
3. 초기 기본 비밀번호는 **`admin1234`** 입니다.
4. 로그인 시 다음과 같은 기능을 이용할 수 있습니다:
   - **실시간 검색자 통계**: 총 검색 건수 및 학생(익명 ID)별 검색 횟수
   - **세부 검색 조건 조회**: 학생들이 어떤 전공, 어떤 국가, 몇 점의 iBT를 설정했는지 열람
   - **엑셀 다운로드 (⬇ 엑셀 .xlsx)**: 검색 로그 전체와 요약본을 엑셀 파일로 원클릭 다운로드
   - **마크다운 다운로드 (⬇ 마크다운 .md)**: 보고서용 마크다운 형식 다운로드
   - **비밀번호 변경 (🔑 비번변경)**: 원하는 새 관리자 비밀번호로 변경 가능
   - **특정 사용자 기록 삭제 / 전체 초기화**
