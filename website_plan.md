# EBS 파이썬 교육 웹사이트 계획서

> **최종 업데이트**: 2026-02-08

## 개요
- **프로젝트명**: 해달에듀 파이썬 (EBS 이솦과 함께하는 파이썬)
- **대상**: 파이썬을 공부하려는 초중고 학생
- **목적**: 교육과정 안내 및 차시별 코드 학습 제공
- **현재 상태**: Phase 1~2 완료, Phase 3 진행 중

---

## 사이트 구조

```
홈페이지
├── 메인 페이지 (교육과정 개요)
├── Part 1. 파이썬 기초 문법 (1~10차시)
│   ├── 1차시. 파이썬의 이해와 설치
│   ├── 2차시. 수치 자료형과 변수
│   ├── ...
│   └── 10차시. 개념 복습
├── Part 2. 파이썬 라이브러리 활용 (11~18차시)
│   ├── 11차시. random 모듈
│   ├── ...
│   └── 18차시. 미니 프로젝트 - 타자 게임
├── Part 3. 웹사이트 만들기 (19~21차시)
├── Part 4. 데이터 분석 (22~24차시)
└── Part 5. 알고리즘 & 자료구조 (25~31차시)
```

---

## 페이지별 구성

### 1. 메인 페이지 (`/`)
- 교육과정 소개 (타겟, 구성, 학습 목표)
- 전체 커리큘럼 요약 (5개 Part)
- 각 Part로 빠르게 이동하는 네비게이션 카드

### 2. 차시별 상세 페이지 (`/lesson/{차시번호}`)
- **차시 제목 및 설명**
- **학습 목표**
- **코드 뷰어** (탭 구조)
  - 개념 학습 코드
  - 실습 코드 A
  - 실습 코드 B (있는 경우)
  - 도전 과제
  - 정답 (토글로 숨김 처리)
- **코드 복사 버튼**
- **구문 하이라이팅** (Python)

---

## 기술 스택 (확정)

- **프레임워크**: Next.js 16.1.6 (App Router)
- **언어**: TypeScript
- **React**: 19.2.3
- **스타일링**: Tailwind CSS 4
- **코드 하이라이팅**: react-syntax-highlighter (Prism 기반, oneDark 테마)
- **배포**: Vercel (예정)

---

## 주요 기능

### 필수 기능
1. ~~**반응형 디자인**~~ - 모바일/태블릿/데스크톱 지원 ✅ 구현 완료 (1~3컬럼 반응형 그리드)
2. ~~**코드 뷰어**~~ - 구문 하이라이팅, 줄 번호 표시 ✅ 구현 완료 (Prism oneDark 테마)
3. ~~**코드 복사**~~ - 클립보드 복사 버튼 ✅ 구현 완료 (복사 피드백 포함)
4. ~~**네비게이션**~~ - Part/차시별 이동 ✅ 구현 완료 (사이드바 + 이전/다음 + 브레드크럼)
5. **진행률 표시** - 현재 차시 위치 표시 ❌ 미구현

### 선택 기능 (확장)
1. **다크 모드** - 학습 환경에 따른 테마 전환 ❌ 미구현
2. **검색 기능** - 키워드로 차시/코드 검색 ❌ 미구현
3. **북마크** - 학습 중인 차시 저장 (로컬스토리지) ❌ 미구현
4. **코드 실행** - Python 온라인 실행 연동 (Replit 등) ❌ 미구현

---

## 디자인 가이드

### 컬러 팔레트 (확정)
- **Primary**: #7232d8 (해달 퍼플)
- **CTA 버튼**: #ffd506 (해달 옐로우)
- **Part별 액센트 컬러**:
  - Part 1: #ffd506 (옐로우)
  - Part 2: #7232d8 (퍼플)
  - Part 3: #50a5dc (블루)
  - Part 4: #d069a9 (핑크)
  - Part 5: #4d2c77 (다크 퍼플)
- **Code Block**: oneDark 테마 (다크 배경)

### 레이아웃
```
┌─────────────────────────────────────────┐
│  헤더 (로고, 네비게이션)                 │
├─────────────────────────────────────────┤
│  사이드바      │     메인 컨텐츠         │
│  - Part 목록   │     - 차시 제목         │
│  - 차시 목록   │     - 설명              │
│               │     - 코드 탭 뷰어       │
│               │     - 이전/다음 버튼     │
├─────────────────────────────────────────┤
│  푸터 (저작권, EBS 링크)                 │
└─────────────────────────────────────────┘
```

---

## 파일 구조 (현재)

```
website/
├── public/
│   ├── file.svg               # Next.js 기본 에셋
│   ├── globe.svg
│   ├── next.svg
│   ├── vercel.svg
│   └── window.svg
├── src/
│   ├── app/
│   │   ├── layout.tsx         # 루트 레이아웃 (메타데이터, 폰트, 헤더)
│   │   ├── page.tsx           # 메인 페이지 (히어로, 기능소개, 커리큘럼)
│   │   ├── globals.css        # 글로벌 스타일 (Tailwind)
│   │   ├── robots.ts          # 검색엔진 크롤러 안내 (/robots.txt)
│   │   ├── sitemap.ts         # 동적 사이트맵 생성 (/sitemap.xml)
│   │   └── lesson/
│   │       └── [id]/
│   │           └── page.tsx   # 차시별 동적 페이지 (SSG + generateMetadata)
│   ├── components/
│   │   ├── Header.tsx         # 스티키 헤더 (로고, 네비게이션)
│   │   ├── Sidebar.tsx        # 아코디언 사이드바 (Part/차시 목록)
│   │   ├── CodeViewer.tsx     # 탭 기반 코드 뷰어 (구문 하이라이팅)
│   │   └── LessonCard.tsx     # Part 카드 컴포넌트 (홈페이지용)
│   └── data/
│       └── curriculum.ts      # 전체 커리큘럼 데이터 (5파트, 31차시)
├── package.json
├── next.config.ts
├── postcss.config.mjs
├── eslint.config.mjs
└── tsconfig.json
```

---

## 개발 단계

### Phase 1: 기본 구조 ✅ 완료
- [x] 프로젝트 세팅 (Next.js 16 + Tailwind CSS 4 + TypeScript)
- [x] 커리큘럼 데이터 구조화 (TypeScript - 5파트, 31차시 전체 정의)
- [x] 기본 레이아웃 (스티키 헤더, 아코디언 사이드바, 푸터)
- [x] 메인 페이지 구현 (히어로 섹션, 기능 카드 3개, Part별 커리큘럼 카드)

### Phase 2: 핵심 기능 ✅ 완료
- [x] 차시별 상세 페이지 구현 (동적 라우팅 + SSG `generateStaticParams`)
- [x] 코드 뷰어 컴포넌트 (Prism 구문 하이라이팅, 줄 번호 표시)
- [x] 코드 탭 전환 기능 (개념/실습A/실습B/도전/정답 5개 탭)
- [x] 코드 복사 기능 (클립보드 복사 + 시각적 피드백)
- [x] 정답 숨김 처리 (버튼 클릭 시 정답 코드 공개)
- [x] 빌드 타임에 .py 파일 읽기 (서버 컴포넌트에서 `fs.readFile`)

### Phase 3: 완성 및 배포 🔧 진행 중
- [x] 반응형 디자인 최적화 (1~3컬럼 반응형 그리드)
- [x] 이전/다음 차시 네비게이션
- [x] 브레드크럼 네비게이션
- [x] SEO 최적화
  - [x] 메타데이터 템플릿 (title template, OG, Twitter Card, keywords, canonical)
  - [x] 차시별 동적 메타데이터 (`generateMetadata`)
  - [x] robots.txt (`/robots.txt`)
  - [x] 사이트맵 (`/sitemap.xml` - 홈 + 31차시 동적 생성)
- [x] Vercel 배포 (`https://python.haedal.io`)
- [ ] Part 2~5 콘텐츠 활성화 (현재 "준비중" 상태)

---

## 커리큘럼 데이터 예시

```typescript
// data/curriculum.ts
export const curriculum = {
  parts: [
    {
      id: 1,
      title: "Part 1. 파이썬 기초 문법",
      description: "파이썬의 기본 문법과 핵심 개념을 학습합니다.",
      lessons: [
        {
          id: 2,
          title: "수치 자료형과 변수",
          description: "정수, 실수, 변수의 개념과 산술 연산을 배웁니다.",
          codes: {
            concept: "02-01-numbers_concept.py",
            practiceA: "02-02-practice_a_calc.py",
            practiceB: "02-03-practice_b_bmi.py",
            challenge: "02-04-challenge.py",
            answer: "02-05-answer.py"
          }
        },
        // ...
      ]
    },
    // ...
  ]
};
```

---

## 배포 (Vercel 확정)

| 항목 | 값 |
|------|-----|
| **플랫폼** | Vercel (무료) |
| **Framework Preset** | Next.js |
| **Root Directory** | `website` |
| **Build Command** | `npm run build` |
| **Output Directory** | `.next` |
| **Node.js Version** | 20.x |

---

## 구현된 주요 컴포넌트 상세

### Header (`Header.tsx`)
- 스티키 헤더 + backdrop blur 효과
- 🐍 로고 + "해달에듀 파이썬" 브랜딩
- "시작하기" CTA 버튼 (#ffd506)

### Sidebar (`Sidebar.tsx`)
- 클라이언트 컴포넌트 (상태 관리)
- 5개 Part 아코디언 펼침/접기
- 현재 차시 하이라이트 (옐로우 배경)
- Part 1 기본 펼침 상태

### CodeViewer (`CodeViewer.tsx`)
- 5개 탭 (개념/실습A/실습B/도전/정답)
- Prism oneDark 테마 구문 하이라이팅
- 줄 번호 표시
- 클립보드 복사 (피드백 포함)
- 정답 탭 숨김 → 클릭 시 공개

### LessonCard (`LessonCard.tsx`)
- Part별 아이콘 (📚🧰🌐📊🧠)
- Part별 고유 액센트 컬러
- Part 1만 클릭 가능, 나머지 "준비중" 표시

---

## 참고사항

- 기존 `code/` 폴더의 .py 파일들을 빌드 타임에 서버 컴포넌트에서 직접 읽어 활용
- `curriculum.ts`에 31차시 전체 데이터 구조화 완료
- `generateStaticParams()`로 전체 차시 SSG 생성
- 학생 친화적인 UI/UX 구현 (직관적인 네비게이션, 컬러 코딩)
- Part 2~5는 데이터 정의 완료, UI에서 "준비중" 상태로 비활성화
