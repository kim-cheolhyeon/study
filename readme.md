# 폴더 구조

```text
study/
├── DataAnalysis_with_python/
├── DataStructure/
├── Algorithm/
├── .gitignore
└── readme.md
```

- `DataAnalysis_with_python/`: Do it! 파이썬 데이터 분석 실습 노트북과 데이터
- `DataStructure/`: 자료구조 실습 코드

# Commit Message Convention

실습 코드의 변경 사항을 명확하게 기록하고, 여러 기기에서 학습 작업을 이어서 진행하기 위해 아래 커밋 메시지 규칙을 사용한다.

## 형식

```text
<type>(<scope>): <내용>
```

### 예시

```text
practice(DataStructure): 배열 기반 스택 구현
fix(DataStructure): 큐 dequeue 예외 처리 수정
refactor(DataStructure): 연결 리스트 코드 구조 개선
docs(DataStructure): 실행 방법 README 추가
chore: gitignore 설정
wip(DataAnalysis_with_python): 데이터 전처리 실습 진행 중
```

## Type

| Type | 설명 |
| --- | --- |
| `practice` | 학습한 내용을 직접 구현하거나 문제 풀이를 완료한 경우 |
| `wip` | 작업이 완료되지 않았지만 진행 상황을 저장하거나 다른 기기에서 이어서 작업하기 위해 커밋하는 경우 |
| `fix` | 기존 실습 코드의 오류를 수정한 경우 |
| `refactor` | 기능 변경 없이 코드 구조를 개선한 경우 |
| `docs` | README, 주석 등 문서를 추가하거나 수정한 경우 |
| `chore` | 폴더 구성, 설정 파일 등 코드 외 작업을 한 경우 |

## Scope

`scope`에는 실제 학습 분야의 폴더명을 대소문자와 밑줄까지 그대로 작성한다.

```text
DataStructure
DataAnalysis_with_python
Algorithm
```

`scope`가 필요하지 않은 작업은 생략할 수 있다.

```text
chore: gitignore 설정
docs: README 수정
```

## WIP 커밋

`wip`는 작업 중간에 진행 상황을 저장하기 위한 커밋에 사용한다.

- 실습이나 구현이 완료되지 않은 상태에서 사용한다.
- 다른 기기에서 작업을 이어서 진행하기 위한 커밋에도 사용한다.
- 메시지에는 현재 진행 중인 작업 내용을 작성한다.
- 작업이 완료되면 `practice` 등 적절한 타입으로 커밋한다.

### 예시

```text
wip(DataStructure): 이진 탐색 트리 구현 중
wip(Algorithm): 다익스트라 알고리즘 구현 중
wip(DataAnalysis_with_python): 데이터 시각화 실습 진행 중
```

## 규칙

- 커밋 메시지는 `type(scope): 내용` 형식을 따른다.
- `type`은 영문 소문자로 작성한다.
- `scope`는 실제 학습 폴더명의 대소문자와 밑줄을 그대로 사용한다.
- 커밋 하나에는 하나의 작업 단위를 담는다. 단, `wip`는 진행 중인 작업의 중간 상태를 저장할 수 있다.
- 메시지만 보고 어떤 작업을 했는지 알 수 있도록 작성한다.
- 작업 환경이나 기기 이름보다는 실제 변경된 내용을 중심으로 작성한다.