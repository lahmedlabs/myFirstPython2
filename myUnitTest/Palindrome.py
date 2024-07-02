def is_palindrome(str):
    cleaned = ''.join(char.lower() for char in str if char.isalnum())
    return cleaned == cleaned[::-1]

    # # 1단계: 알파벳과 숫자만 남기기
    # alphanumeric_chars = [char for char in s if char.isalnum()]
    # # 2단계: 남긴 문자들을 소문자로 변환하기
    # lowercased_chars = [char.lower() for char in alphanumeric_chars]
    # # 3단계: 리스트를 문자열로 결합하기
    # cleaned = ''.join(lowercased_chars)
    # # 4단계: 문자열이 팔린드롬인지 확인하기
    # return cleaned == cleaned[::-1]

# # 테스트 케이스
# print(is_palindrome("A man, a plan, a canal, Panama"))  # True
# print(is_palindrome("racecar"))  # True
# print(is_palindrome("hello"))  # False
# print(is_palindrome("12321"))  # True
# print(is_palindrome("No lemon, no melon"))  # True
