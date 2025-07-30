def alphabet_index(word):
    result = []
    for i in range(26):
        char = chr(ord('a') + i)
        result.append(word.find(char))
    return result

# 사용 예시
word = input().strip()
print(alphabet_index(word))
