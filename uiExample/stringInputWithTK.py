import tkinter as tk

def display_text():
    input_text = entry.get()  # Entry 위젯에서 입력된 텍스트를 가져옵니다.
    label.config(text=input_text)  # 가져온 텍스트를 Label 위젯에 표시합니다.

root = tk.Tk()
root.title("문자열 입력받기 예제")

# Entry 위젯을 생성하고 윈도우에 배치합니다.
entry = tk.Entry(root, width=30)
entry.pack(pady=10)  # 약간의 여백을 추가합니다.

# 버튼 위젯을 생성하고 윈도우에 배치합니다.
button = tk.Button(root, text="입력된 텍스트 표시", command=display_text)
button.pack(pady=5)  # 약간의 여백을 추가합니다.

# Label 위젯을 생성하고 윈도우에 배치합니다.
label = tk.Label(root, text="")
label.pack(pady=10)  # 약간의 여백을 추가합니다.

root.mainloop()
