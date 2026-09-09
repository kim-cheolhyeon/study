# 폴더 구조

```text
study/
├── DataAnalysis_with_python/
│   ├── CH5_데이터분석기초.ipynb
│   ├── CH6_자유자재로데이터가공하기.ipynb
│   └── data/
│       ├── exam.csv
│       ├── midwest.csv
│       └── mpg.csv
├── DataStructure/
│   └── lists.py
├── .gitignore
└── readme.md
```

- `DataAnalysis_with_python/`: Do it! 파이썬 데이터 분석 실습 노트북과 데이터
- `DataStructure/`: 자료구조 실습 코드

# Commit Message Convention

실습 코드의 변경 사항을 명확하게 기록하기 위해 아래 커밋 메시지 규칙을 사용한다.

## 형식

```text
<type>(<scope>): <내용>
```

### 예시

```text
practice(data-structures): 배열 기반 스택 구현
fix(data-structures): 큐 dequeue 예외 처리 수정
refactor(data-structures): 연결 리스트 코드 구조 개선
docs(data-structures): 실행 방법 README 추가
chore: gitignore 설정
```

## Type

| Type | 설명 |
| --- | --- |
| `practice` | 학습한 내용을 직접 구현하거나 문제를 풀이한 경우 |
| `fix` | 기존 실습 코드의 오류를 수정한 경우 |
| `refactor` | 기능 변경 없이 코드 구조를 개선한 경우 |
| `docs` | README, 주석 등 문서를 추가하거나 수정한 경우 |
| `chore` | 폴더 구성, 설정 파일 등 코드 외 작업을 한 경우 |

## Scope

`scope`에는 학습 분야의 폴더명을 작성한다.

```text
data-structures
algorithms
database
operating-systems
network
```

`scope`가 필요하지 않은 작업은 생략할 수 있다.

```text
chore: gitignore 설정
docs: README 수정
```

## 규칙

- 커밋 메시지는 `type(scope): 내용` 형식을 따른다.
- `type`과 `scope`는 영문 소문자로 작성한다.
- `scope`는 실제 학습 폴더명을 사용한다.
- 커밋 하나에는 하나의 작업 단위를 담는다.
- 메시지만 보고 어떤 작업을 했는지 알 수 있도록 작성한다.