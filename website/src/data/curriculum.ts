export interface CodeFiles {
  [key: string]: string | undefined;
  concept?: string;
  practiceA?: string;
  practiceB?: string;
  challenge?: string;
  answer?: string;
}

export interface Lesson {
  id: number;
  title: string;
  description: string;
  codes: CodeFiles;
}

export interface Part {
  id: number;
  title: string;
  description: string;
  lessons: Lesson[];
}

export const curriculum: Part[] = [
  {
    id: 1,
    title: "Part 1. 파이썬 기초 문법",
    description: "파이썬의 기본 문법과 핵심 개념을 학습합니다.",
    lessons: [
      {
        id: 1,
        title: "파이썬의 이해와 설치",
        description: "파이썬을 이해하고 VS Code 개발 환경을 설정합니다.",
        codes: {}
      },
      {
        id: 2,
        title: "수치 자료형과 변수",
        description: "정수, 실수, 변수의 개념과 산술 연산을 배웁니다.",
        codes: {
          concept: "02-01-numbers_concept.py",
          practiceA: "02-02-practice_a_calc.py",
          practiceB: "02-03-practice_b_bmi.py",
          challenge: "02-04-challenge.py"
        }
      },
      {
        id: 3,
        title: "문자열",
        description: "텍스트 다루기, 인덱싱/슬라이싱을 배웁니다.",
        codes: {
          concept: "03-01-strings_concept.py",
          practiceA: "03-02-practice_a_introduce.py",
          challenge: "03-03-challenge.py"
        }
      },
      {
        id: 4,
        title: "군집 자료형",
        description: "리스트, 튜플 등 데이터 묶음을 다룹니다.",
        codes: {
          concept: "04-01-lists_tuples_concept.py",
          practiceA: "04-02-practice_a_friend_list.py",
          practiceB: "04-03-practice_b_random_menu.py",
          challenge: "04-04-challenge.py"
        }
      },
      {
        id: 5,
        title: "문자 입출력",
        description: "input, print 포맷팅을 배웁니다.",
        codes: {
          concept: "05-01-io_concept.py",
          practiceA: "05-02-practice_a_greeting.py",
          practiceB: "05-03-practice_b_receipt.py",
          challenge: "05-04-challenge.py"
        }
      },
      {
        id: 6,
        title: "조건문",
        description: "if, elif, else로 프로그램 흐름을 제어합니다.",
        codes: {
          concept: "06-01-if_concept.py",
          practiceA: "06-02-practice_a_grade_check.py",
          practiceB: "06-03-practice_b_even_odd.py",
          challenge: "06-04-challenge.py"
        }
      },
      {
        id: 7,
        title: "for 반복문",
        description: "횟수 제어 반복을 배웁니다.",
        codes: {
          concept: "07-01-for_concept.py",
          practiceA: "07-02-practice_a_sum_n.py",
          practiceB: "07-03-practice_b_multiplication_table.py",
          challenge: "07-04-challenge.py"
        }
      },
      {
        id: 8,
        title: "while 반복문",
        description: "조건 제어 반복을 배웁니다.",
        codes: {
          concept: "08-01-while_concept.py",
          practiceA: "08-02-practice_a_count_while.py",
          practiceB: "08-03-practice_b_collect_inputs.py",
          challenge: "08-04-challenge.py"
        }
      },
      {
        id: 9,
        title: "함수",
        description: "def 정의와 호출을 배웁니다.",
        codes: {
          concept: "09-01-function_concept.py",
          practiceA: "09-02-practice_a_calc_func.py",
          practiceB: "09-03-practice_b_greeting_func.py",
          challenge: "09-04-challenge.py"
        }
      },
      {
        id: 10,
        title: "개념 복습",
        description: "1~9차시 총정리 및 Q&A",
        codes: {
          practiceA: "10-01-mini_quiz.py",
          challenge: "10-02-challenge.py"
        }
      }
    ]
  },
  {
    id: 2,
    title: "Part 2. 파이썬 라이브러리 활용",
    description: "파이썬의 유용한 라이브러리들을 활용합니다.",
    lessons: [
      {
        id: 11,
        title: "운에 맡겨라 (random)",
        description: "random 모듈로 무작위 데이터를 만듭니다.",
        codes: {
          concept: "11-1-random.py",
          practiceA: "11-2-lunch.py",
          practiceB: "11-3-lotto.py",
          challenge: "11-4-challenge.py",
          answer: "11-5-answer.py"
        }
      },
      {
        id: 12,
        title: "시간은 금이다 (time)",
        description: "time, datetime 모듈을 배웁니다.",
        codes: {
          concept: "12-1-time.py",
          practiceA: "12-2-3countdown.py",
          practiceB: "12-3-10seconds.py",
          challenge: "12-4-challenge.py",
          answer: "12-5-answer.py"
        }
      },
      {
        id: 13,
        title: "거북이로 그림 그리기 (turtle)",
        description: "turtle 모듈로 그래픽을 그립니다.",
        codes: {
          concept: "13-1-turtle.py",
          practiceA: "13-2-triangleSquare.py",
          challenge: "13-3-challenge.py",
          answer: "13-4-answer.py"
        }
      },
      {
        id: 14,
        title: "거북이 예술 작품 (turtle 응용)",
        description: "turtle로 복잡한 패턴을 그립니다.",
        codes: {
          practiceA: "14-1-colorful.py",
          practiceB: "14-2-turtlemouse.py",
          challenge: "14-3-challenge.py",
          answer: "14-4-answer.py"
        }
      },
      {
        id: 15,
        title: "컴퓨터 비서 (webbrowser)",
        description: "webbrowser 모듈로 브라우저를 제어합니다.",
        codes: {
          concept: "15-1-webbrowser.py",
          practiceA: "15-2-searchgoogle.py",
          practiceB: "15-3-ceomode.py",
          challenge: "15-4-challenge.py",
          answer: "15-5-answer.py"
        }
      },
      {
        id: 16,
        title: "메모장 만들기 (file I/O)",
        description: "파일 입출력을 배웁니다.",
        codes: {
          concept: "16-1-fileio.py",
          practiceA: "16-2-diary.py",
          challenge: "16-3-challenge.py",
          answer: "16-4-answer.py"
        }
      },
      {
        id: 17,
        title: "미니 프로젝트: Up/Down 게임",
        description: "숫자 맞추기 게임을 만듭니다.",
        codes: {
          challenge: "17-1-challenge.py",
          answer: "17-2-answer.py"
        }
      },
      {
        id: 18,
        title: "미니 프로젝트: 타자 게임",
        description: "영어 단어 타자 게임을 만듭니다.",
        codes: {
          challenge: "18-1-chatgame.py",
          answer: "18-2-answer.py"
        }
      }
    ]
  },
  {
    id: 3,
    title: "Part 3. 웹사이트 만들기",
    description: "Streamlit으로 웹사이트를 만듭니다.",
    lessons: [
      {
        id: 19,
        title: "Streamlit 기초",
        description: "Streamlit 설치 및 기본 사용법을 배웁니다.",
        codes: {
          concept: "19-1-streamlit_setup.py",
          practiceA: "19-2-portfolio.py",
          challenge: "19-3-challenge.py",
          answer: "19-4-answer.py"
        }
      },
      {
        id: 20,
        title: "입력 위젯",
        description: "버튼, 슬라이더 등 입력 위젯을 배웁니다.",
        codes: {
          concept: "20-1-widgets.py",
          practiceA: "20-2-mbti_ui.py",
          challenge: "20-3-challenge.py",
          answer: "20-4-answer.py"
        }
      },
      {
        id: 21,
        title: "미니 프로젝트: 웹 앱 대시보드",
        description: "실제 동작하는 웹 앱을 완성합니다.",
        codes: {
          practiceA: "21-1-lunch_app.py",
          practiceB: "21-2-bmi_web.py",
          challenge: "21-3-challenge.py",
          answer: "21-4-answer.py"
        }
      }
    ]
  },
  {
    id: 4,
    title: "Part 4. 데이터 분석",
    description: "Pandas와 Matplotlib으로 데이터를 분석합니다.",
    lessons: [
      {
        id: 22,
        title: "Pandas 기초",
        description: "데이터프레임으로 데이터를 다룹니다.",
        codes: {
          concept: "22-1-pandas_basic.py",
          practiceA: "22-2-grade_analysis.py",
          challenge: "22-3-challenge.py",
          answer: "22-4-answer.py"
        }
      },
      {
        id: 23,
        title: "데이터 시각화 (Matplotlib)",
        description: "그래프로 데이터를 표현합니다.",
        codes: {
          concept: "23-1-plot_basic.py",
          practiceA: "23-2-weather_chart.py",
          challenge: "23-3-challenge.py",
          answer: "23-4-answer.py"
        }
      },
      {
        id: 24,
        title: "미니 프로젝트: 공공데이터 분석",
        description: "실제 공공데이터를 분석합니다.",
        codes: {
          practiceA: "24-1-birthday_weather.py",
          practiceB: "24-2-temp_diff.py",
          challenge: "24-3-challenge.py",
          answer: "24-4-answer.py"
        }
      }
    ]
  },
  {
    id: 5,
    title: "Part 5. 알고리즘 & 자료구조",
    description: "기초 알고리즘과 자료구조를 학습합니다.",
    lessons: [
      {
        id: 25,
        title: "알고리즘적 사고",
        description: "리스트 컴프리헨션을 배웁니다.",
        codes: {
          concept: "25-1-algorithm.py",
          practiceA: "25-2-evenodd.py",
          challenge: "25-3-challenge.py",
          answer: "25-4-answer.py"
        }
      },
      {
        id: 26,
        title: "스택 (Stack)",
        description: "LIFO 자료구조를 이해합니다.",
        codes: {
          concept: "26-1-stack.py",
          practiceA: "26-2-backward.py",
          challenge: "26-3-challenge.py",
          answer: "26-4-answer.py"
        }
      },
      {
        id: 27,
        title: "큐 (Queue)",
        description: "FIFO 자료구조를 이해합니다.",
        codes: {
          concept: "27-1-queue.py",
          practiceA: "27-2-dinningcode.py",
          challenge: "27-3-challenge.py",
          answer: "27-4-answer.py"
        }
      },
      {
        id: 28,
        title: "선형 탐색",
        description: "순차 탐색 알고리즘을 배웁니다.",
        codes: {
          concept: "28-1-linearSearch.py",
          practiceA: "28-2-findnumber.py",
          challenge: "28-3-challenge.py",
          answer: "28-4-answer.py"
        }
      },
      {
        id: 29,
        title: "이진 탐색",
        description: "효율적인 탐색 알고리즘을 배웁니다.",
        codes: {
          concept: "29-1-binarySearch.py",
          practiceA: "29-2-binarySearchDetail.py",
          challenge: "29-3-challenge.py",
          answer: "29-4-answer.py"
        }
      },
      {
        id: 30,
        title: "정렬 (Sorting)",
        description: "버블 정렬과 내장 함수를 배웁니다.",
        codes: {
          concept: "30-1-sorting.py",
          practiceA: "30-2-library.py",
          challenge: "30-3-challenge.py",
          answer: "30-4-answer.py"
        }
      },
      {
        id: 31,
        title: "알고리즘 챌린지",
        description: "종합 문제를 풀고 수료합니다.",
        codes: {
          practiceA: "31-1-voweldetect.py",
          practiceB: "31-2-369.py",
          challenge: "31-3-Palindrome.py",
          answer: "31-4-duplicationDetect.py"
        }
      }
    ]
  }
];

export function getLessonById(id: number): { part: Part; lesson: Lesson } | null {
  for (const part of curriculum) {
    const lesson = part.lessons.find(l => l.id === id);
    if (lesson) {
      return { part, lesson };
    }
  }
  return null;
}

export function getAllLessons(): Lesson[] {
  return curriculum.flatMap(part => part.lessons);
}
