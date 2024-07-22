import tkinter as tk
import random

class WordSearchGame:
    def __init__(self, root):
        self.root = root
        self.root.title("단어 찾기 퍼즐")
        self.board_size = 10  # 보드 크기를 키움
        self.subjects_and_words = {
            "과일": ["사과", "바나나", "오렌지", "포도", "키위", "딸기", "복숭아", "수박", "참외", "멜론"],
            "동물": ["호랑이", "사자", "코끼리", "기린", "토끼", "강아지", "고양이", "곰", "판다", "여우"],
            "나라": ["한국", "미국", "중국", "일본", "독일", "프랑스", "브라질", "캐나다", "영국", "호주"],
            "음식": ["김치", "불고기", "비빔밥", "떡볶이", "만두", "갈비", "냉면", "된장찌개", "삼겹살", "라면"],
            "스포츠": ["축구", "농구", "야구", "배구", "테니스", "수영", "탁구", "골프", "스키", "펜싱"],
            "색깔": ["빨강", "파랑", "노랑", "초록", "검정", "흰색", "보라", "분홍", "주황", "회색"],
            "직업": ["의사", "간호사", "경찰", "소방관", "선생님", "요리사", "판사", "변호사", "기자", "과학자"],
            "교통수단": ["자동차", "자전거", "버스", "기차", "비행기", "배", "오토바이", "전동킥보드", "지하철", "트럭"],
            "악기": ["피아노", "기타", "바이올린", "드럼", "플루트", "트럼펫", "하프", "첼로", "클라리넷", "색소폰"],
            "날씨": ["맑음", "비", "눈", "바람", "태풍", "안개", "구름", "폭염", "한파", "번개"]
        }
        self.subject = random.choice(list(self.subjects_and_words.keys()))
        self.words = self.subjects_and_words[self.subject]
        self.board = [["" for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.found_words = []
        self.score = 0
        self.time_left = 90  # 1분 30초
        self.timer_running = True

        # 창 크기 조정
        self.root.geometry("1000x1000")
        self.root.configure(bg="#F0F0F0")  # 배경 색상 설정

        self.create_widgets()
        self.place_words()
        self.fill_board()
        self.update_timer()

    def create_widgets(self):
        # 제목
        title_label = tk.Label(self.root, text="단어 찾기 퍼즐", font=("Helvetica", 36, "bold"), bg="#F0F0F0", fg="#333333")
        title_label.pack(pady=20)

        # 주제, 점수, 남은 시간 프레임
        info_frame = tk.Frame(self.root, bg="#F0F0F0")
        info_frame.pack(pady=10)

        self.subject_label = tk.Label(info_frame, text=f"주제: {self.subject}", font=("Helvetica", 24), bg="#F0F0F0", fg="#333333")
        self.subject_label.grid(row=0, column=0, padx=20)

        self.score_label = tk.Label(info_frame, text=f"점수: {self.score}", font=("Helvetica", 24), bg="#F0F0F0", fg="#333333")
        self.score_label.grid(row=0, column=1, padx=20)

        self.timer_label = tk.Label(info_frame, text=f"남은 시간: {self.format_time(self.time_left)}", font=("Helvetica", 24), bg="#F0F0F0", fg="#333333")
        self.timer_label.grid(row=0, column=2, padx=20)

        # 단어 입력
        self.entry = tk.Entry(self.root, font=("Helvetica", 24))
        self.entry.pack(pady=20)
        self.entry.bind("<Return>", self.check_word)

        # 퍼즐 격자
        self.board_frame = tk.Frame(self.root, bg="#F0F0F0")
        self.board_frame.pack()

        self.board_labels = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        for i in range(self.board_size):
            for j in range(self.board_size):
                label = tk.Label(self.board_frame, text="", font=("Helvetica", 32), width=2, height=1, borderwidth=2, relief="solid", bg="#FFFFFF", fg="#000000")
                label.grid(row=i, column=j, padx=5, pady=5)
                self.board_labels[i][j] = label

    def place_words(self):
        self.board = [["" for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.word_positions = {}  # 단어의 위치를 저장하는 딕셔너리
        for word in self.words:
            placed = False
            while not placed:
                direction = random.choice(['horizontal', 'vertical'])
                if direction == 'horizontal':
                    row = random.randint(0, self.board_size - 1)
                    col = random.randint(0, self.board_size - len(word))
                    if all(self.board[row][col + i] in ("", word[i]) for i in range(len(word))):
                        for i in range(len(word)):
                            self.board[row][col + i] = word[i]
                        self.word_positions[word] = (row, col, direction)
                        placed = True
                else:
                    row = random.randint(0, self.board_size - len(word))
                    col = random.randint(0, self.board_size - 1)
                    if all(self.board[row + i][col] in ("", word[i]) for i in range(len(word))):
                        for i in range(len(word)):
                            self.board[row + i][col] = word[i]
                        self.word_positions[word] = (row, col, direction)
                        placed = True

    def fill_board(self):
        # '가'부터 '차'까지의 글자로 보드를 채우기
        hangul_chars = list("가나다라마바사아자차")
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == "":
                    self.board[i][j] = random.choice(hangul_chars)  # '가'부터 '차'까지의 랜덤 문자 선택
                self.board_labels[i][j].config(text=self.board[i][j], bg="#FFFFFF")

    def check_word(self, event):
        word = self.entry.get().strip()
        if word in self.words and word not in self.found_words:
            self.found_words.append(word)
            self.score += 10
            self.score_label.config(text=f"점수: {self.score}")
            self.highlight_word(word)
            if len(self.found_words) == len(self.words):
                self.show_completion_popup()
        self.entry.delete(0, tk.END)

    def highlight_word(self, word):
        # 단어를 하이라이트하는 로직
        if word in self.word_positions:
            row, col, direction = self.word_positions[word]
            for i in range(len(word)):
                if direction == 'horizontal':
                    self.board_labels[row][col + i].config(bg="#FF0000")  # 빨간색으로 하이라이트
                else:
                    self.board_labels[row + i][col].config(bg="#FF0000")  # 빨간색으로 하이라이트

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

    def update_timer(self):
        if self.timer_running:
            if self.time_left > 0:
                self.time_left -= 1
                self.timer_label.config(text=f"남은 시간: {self.format_time(self.time_left)}")
                self.root.after(1000, self.update_timer)
            else:
                self.end_game()

    def end_game(self):
        self.timer_running = False
        for row in self.board_labels:
            for label in row:
                label.config(bg="lightgrey")
        self.entry.config(state="disabled")
        self.show_end_game_popup()

    def show_end_game_popup(self):
        popup = tk.Toplevel(self.root)
        popup.title("게임 종료")
        popup.configure(bg="#F0F0F0")
        tk.Label(popup, text=f"게임 종료! 최종 점수: {self.score}", font=("Helvetica", 24), bg="#F0F0F0", fg="#333333").pack(pady=20)
        tk.Button(popup, text="다시 하기", font=("Helvetica", 24), command=lambda: [popup.destroy(), self.restart_game()]).pack(side="left", padx=20, pady=20)
        tk.Button(popup, text="종료하기", font=("Helvetica", 24), command=self.root.quit).pack(side="right", padx=20, pady=20)

    def show_completion_popup(self):
        popup = tk.Toplevel(self.root)
        popup.title("축하합니다!")
        popup.configure(bg="#F0F0F0")
        tk.Label(popup, text="모든 단어를 찾았습니다!", font=("Helvetica", 24), bg="#F0F0F0", fg="#333333").pack(pady=20)
        tk.Button(popup, text="다시 하기", font=("Helvetica", 24), command=lambda: [popup.destroy(), self.restart_game()]).pack(side="left", padx=20, pady=20)
        tk.Button(popup, text="종료하기", font=("Helvetica", 24), command=self.root.quit).pack(side="right", padx=20, pady=20)

    def restart_game(self):
        self.timer_running = False
        self.time_left = 90
        self.score = 0
        self.found_words = []

        self.subject = random.choice(list(self.subjects_and_words.keys()))
        self.words = self.subjects_and_words[self.subject]

        self.subject_label.config(text=f"주제: {self.subject}")
        self.score_label.config(text=f"점수: {self.score}")
        self.timer_label.config(text=f"남은 시간: {self.format_time(self.time_left)}")
        self.entry.config(state="normal")

        self.place_words()
        self.fill_board()

        self.timer_running = True
        self.update_timer()

if __name__ == "__main__":
    root = tk.Tk()
    game = WordSearchGame(root)
    root.mainloop()
