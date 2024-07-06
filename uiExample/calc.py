import tkinter as tk
from tkinter import messagebox

def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        label_result.config(text=f"결과: {result}")
    except ValueError:
        messagebox.showerror("입력 오류", "유효한 숫자를 입력하세요.")

root = tk.Tk()
root.title("숫자 더하기 예제")

# 첫 번째 숫자를 입력받는 Entry 위젯
entry1 = tk.Entry(root, width=10)
entry1.pack(pady=5)

# 두 번째 숫자를 입력받는 Entry 위젯
entry2 = tk.Entry(root, width=10)
entry2.pack(pady=5)

# Add 버튼
button = tk.Button(root, text="Add", command=add_numbers)
button.pack(pady=10)

# 결과를 출력하는 Label 위젯
label_result = tk.Label(root, text="결과: ")
label_result.pack(pady=5)

root.mainloop()
