def cel_to_fahr(celsius):
    return celsius * 9/5 + 32

def fahr_to_cel(fahrenheit):
    return (fahrenheit - 32) * 5/9

# test code

print("섭씨 25도는 화씨로 " + f"{cel_to_fahr(25)}")
print("화씨 60도는 섭씨로 " + f"{fahr_to_cel(60)}")
