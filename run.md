# LangChain LLM 호출 방식 정리

## ✅ 1. `invoke()`
### 기능
- 단일 입력을 받아 LLM을 호출하고 응답을 반환
- 체인(`|`)을 사용하거나 직접 모델을 호출할 때 사용
- **비동기 처리 X** (동기 방식)

### 🔹 예제 (체인 사용)
```python
response = chain.invoke({"input": "자연어처리란?"})
print(response.content)
```

### 🔹 예제 (직접 LLM 호출)
```python
response = llm.invoke("자연어처리란?")
print(response.content)
```

### 📌 언제 사용해야 할까?
✅ 단일 입력을 처리할 때
✅ 체인을 사용할 때

---

## ✅ 2. `stream()`
### 기능
- LLM 응답을 **스트리밍 방식**으로 받아옴
- 부분적으로 생성된 응답을 실시간으로 처리 가능
- **예: 채팅 앱, 실시간 응답이 필요한 경우**

### 🔹 예제
```python
for chunk in chain.stream({"input": "자연어처리란?"}):
    print(chunk.content, end="")
```

➡️ **모델의 응답을 한 번에 받는 것이 아니라, 토큰 단위로 부분 출력됨**

### 📌 언제 사용해야 할까?
✅ **실시간 스트리밍 출력이 필요할 때**
✅ **대화형 인터페이스 (챗봇 등)**에서 활용

---

## ✅ 3. `batch()`
### 기능
- **여러 개의 입력을 한 번에 처리** (배치 처리)
- 입력을 리스트로 받아 일괄 실행

### 🔹 예제
```python
responses = chain.batch([
    {"input": "자연어처리란?"},
    {"input": "머신러닝이란?"}
])

for res in responses:
    print(res.content)
```

### 📌 언제 사용해야 할까?
✅ 여러 개의 요청을 한 번에 실행할 때 (효율적인 처리)
✅ API 호출 횟수를 줄이고 싶을 때

---

## ✅ 4. `ainvoke()`
### 기능
- `invoke()`의 **비동기(async) 버전**
- `await`을 사용하여 실행 가능 (비동기 코드에서 사용)

### 🔹 예제
```python
import asyncio

response = await chain.ainvoke({"input": "자연어처리란?"})
print(response.content)
```

### 📌 언제 사용해야 할까?
✅ **비동기 환경 (FastAPI, AsyncIO 등)에서 사용**
✅ **여러 개의 LLM 호출을 병렬 처리할 때**

---

## ✅ 5. `astream()`
### 기능
- `stream()`의 **비동기(async) 버전**
- `await`과 함께 사용 가능

### 🔹 예제
```python
async for chunk in chain.astream({"input": "자연어처리란?"}):
    print(chunk.content, end="")
```

### 📌 언제 사용해야 할까?
✅ **비동기 환경에서 실시간 스트리밍 응답이 필요할 때**
✅ **웹소켓 기반 실시간 애플리케이션 (예: FastAPI WebSocket)**

---

## 🚀 **전체 정리**
| 메서드 | 동기/비동기 | 기능 | 사용 예제 |
|--------|------------|------|----------|
| `invoke()` | 동기 | 단일 요청 처리 | `chain.invoke({"input": "질문"})` |
| `stream()` | 동기 | 실시간 스트리밍 응답 | `for chunk in chain.stream({"input": "질문"}): print(chunk.content)` |
| `batch()` | 동기 | 여러 개의 요청 처리 (배치) | `chain.batch([{ "input": "A" }, { "input": "B" }])` |
| `ainvoke()` | 비동기 | 단일 요청 처리 (async) | `await chain.ainvoke({"input": "질문"})` |
| `astream()` | 비동기 | 실시간 스트리밍 응답 (async) | `async for chunk in chain.astream({"input": "질문"}): print(chunk.content)` |

---

## 🔥 **어떤 걸 써야 할까?**
- **단일 요청 실행** → `invoke()`
- **여러 개의 요청을 한 번에 실행 (배치)** → `batch()`
- **실시간 응답 (스트리밍)** → `stream()`
- **비동기 단일 요청 (FastAPI 등)** → `ainvoke()`
- **비동기 실시간 스트리밍 응답** → `astream()`

📌 **비동기 환경이 아니라면 `invoke()`와 `stream()`을 주로 사용하면 됩니다!** 🚀🔥

