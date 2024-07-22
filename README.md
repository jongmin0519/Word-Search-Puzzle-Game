
# 🧩 단어 찾기 퍼즐 게임 🎉

이 프로젝트는 파이썬과 Tkinter를 사용하여 만든 단어 찾기 퍼즐 게임입니다. 다양한 주제와 단어를 포함하며, 각 게임에서 주제와 단어가 무작위로 선택되어 새로운 퍼즐을 제공합니다.

## 주요 기능 ✨

- **다양한 주제**: 과일, 동물, 나라, 음식, 스포츠, 색깔, 직업, 교통수단, 악기, 날씨 등 10가지 주제를 제공합니다.
- **무작위 퍼즐 생성**: 각 게임마다 무작위로 주제와 단어가 선택되어 새로운 퍼즐을 제공합니다.
- **단어 찾기**: 사용자가 단어를 찾으면 해당 단어가 퍼즐에서 빨간색으로 하이라이트됩니다.
- **타이머**: 1분 30초의 제한 시간 내에 단어를 모두 찾는 도전 과제를 제공합니다.
- **점수 시스템**: 각 단어를 찾으면 10점이 추가됩니다.
- **재시작 기능**: 게임 종료 후 다시 시작할 수 있습니다.

## 설치 및 실행 방법 🛠

### 1. 파이썬 설치
프로그램을 실행하기 위해 [Python](https://www.python.org/)이 설치되어 있어야 합니다.

### 2. 코드 클론
GitHub 레포지토리에서 코드를 클론합니다:
```bash
git clone https://github.com/your-username/word-search-puzzle.git
cd word-search-puzzle
```

### 3. 필요 패키지 설치
이 프로젝트는 Tkinter를 사용합니다. Tkinter는 대부분의 파이썬 배포판에 기본적으로 포함되어 있습니다.

### 4. 게임 실행
아래 명령어를 통해 게임을 실행합니다:
```bash
python game.py
```

## 게임 화면 🎮
![image](https://github.com/user-attachments/assets/870bb903-876e-41e2-8a68-74d3535c7ddb)
![image](https://github.com/user-attachments/assets/612e590b-02ba-4f91-bd8a-0f51579f7926)

## 코드 설명 📝

- `WordSearchGame` 클래스: 게임의 주요 로직을 포함합니다.
- `create_widgets` 메서드: Tkinter 위젯을 생성하고 배치합니다.
- `place_words` 메서드: 단어를 퍼즐 보드에 무작위로 배치합니다.
- `fill_board` 메서드: 빈 공간을 무작위 한글 글자로 채웁니다.
- `check_word` 메서드: 사용자가 입력한 단어가 퍼즐에 있는지 확인합니다.
- `highlight_word` 메서드: 찾은 단어를 빨간색으로 하이라이트합니다.
- `update_timer` 메서드: 게임 타이머를 업데이트합니다.
- `end_game` 및 `show_end_game_popup` 메서드: 게임 종료 시 호출됩니다.
- `show_completion_popup` 메서드: 모든 단어를 찾았을 때 호출됩니다.
- `restart_game` 메서드: 게임을 다시 시작합니다.

## 주제와 단어 🧠

### 과일 🍎
- 사과, 바나나, 오렌지, 포도, 키위, 딸기, 복숭아, 수박, 참외, 멜론

### 동물 🐶
- 호랑이, 사자, 코끼리, 기린, 토끼, 강아지, 고양이, 곰, 판다, 여우

### 나라 🌏
- 한국, 미국, 중국, 일본, 독일, 프랑스, 브라질, 캐나다, 영국, 호주

### 음식 🍔
- 김치, 불고기, 비빔밥, 떡볶이, 만두, 갈비, 냉면, 된장찌개, 삼겹살, 라면

### 스포츠 ⚽
- 축구, 농구, 야구, 배구, 테니스, 수영, 탁구, 골프, 스키, 펜싱

### 색깔 🎨
- 빨강, 파랑, 노랑, 초록, 검정, 흰색, 보라, 분홍, 주황, 회색

### 직업 👩‍⚕️
- 의사, 간호사, 경찰, 소방관, 선생님, 요리사, 판사, 변호사, 기자, 과학자

### 교통수단 🚗
- 자동차, 자전거, 버스, 기차, 비행기, 배, 오토바이, 전동킥보드, 지하철, 트럭

### 악기 🎻
- 피아노, 기타, 바이올린, 드럼, 플루트, 트럼펫, 하프, 첼로, 클라리넷, 색소폰

### 날씨 ☀️
- 맑음, 비, 눈, 바람, 태풍, 안개, 구름, 폭염, 한파, 번개

## 기여 방법 🤝

1. **포크(Fork)**: 이 레포지토리를 포크하세요.
2. **브랜치 생성**: 새로운 기능을 추가할 브랜치를 생성하세요.
    ```bash
    git checkout -b feature/AmazingFeature
    ```
3. **커밋**: 변경 사항을 커밋하세요.
    ```bash
    git commit -m 'Add some AmazingFeature'
    ```
4. **푸시**: 브랜치에 푸시하세요.
    ```bash
    git push origin feature/AmazingFeature
    ```
5. **풀 리퀘스트**: 풀 리퀘스트를 생성하세요.

## 라이선스 📄

이 프로젝트는 MIT 라이선스를 따릅니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.
