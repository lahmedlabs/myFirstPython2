import tkinter as tk
from tkinter import messagebox

def display_add():
    try:
        n1 = int(num1.get())
        n2 = int(num2.get())
        result = n1 + n2
        label_result.config(text=f"Result : {result}")
    except ValueError:
        #print("입력 오류")
        messagebox.showerror("입력 오류", "유효한 숫자를 입력하세요.")

def display_sub():
    result = int(num1.get()) - int(num2.get())
    label_result.config(text=f"Result : {result}")


root = tk.Tk()
root.title("계산기 예제")

label_title = tk.Label(root, text="계산기")
label_title.pack(pady=5)

# Entry 위젯을 생성하고 윈도우에 배치합니다.
num1 = tk.Entry(root, width=10)
num1.pack(pady=5)  # 약간의 여백을 추가합니다.

# Entry 위젯을 생성하고 윈도우에 배치합니다.
num2 = tk.Entry(root, width=10)
num2.pack(pady=5)  # 약간의 여백을 추가합니다.

# 버튼을 담을 프레임 생성
frame = tk.Frame(root)
frame.pack(pady=10)

# 버튼 위젯을 생성하고 윈도우에 배치합니다.
#buttonAdd = tk.Button(root, text=" + ", command=display_add)
#buttonAdd.pack(pady=5)  # 약간의 여백을 추가합니다.
buttonAdd = tk.Button(frame, text=" + ", command=display_add)
buttonAdd.pack(side="left", padx=5)  # 가로 배치

# 버튼 위젯을 생성하고 윈도우에 배치합니다.
#buttonSub = tk.Button(root, text=" - ", command=display_sub)
#buttonSub.pack(pady=5)  # 약간의 여백을 추가합니다.
buttonSub = tk.Button(frame, text=" - ", command=display_sub)
buttonSub.pack(side="left", padx=5)

# Label 위젯을 생성하고 결과를 출력합니다.
label_result = tk.Label(root, text="result: ")
label_result.pack(pady=5)  # 약간의 여백을 추가합니다.

root.mainloop()