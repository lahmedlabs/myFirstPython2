#score = 30
# 점수를 입력 받아서 정수형으로 변환 합니다.
score = int(input("점수를 입력해주세요..."))

# 합격여부를 판단하고 결과를 출력합니다.
if score > 64:
    print("축하합니다! 합격입니다.")
elif score >85:
    print("B")
else:
    print("아쉽게도 불합격입니다.")

