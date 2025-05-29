s = "nitin"

char_list = list(s)

print("Original String:", s)


def ReverseList(char_list, left, right):
    if left >= right:
        return
    char_list[left], char_list[right] = char_list[right], char_list[left]
    ReverseList(char_list, left + 1, right - 1)


ReverseList(char_list, 0, len(char_list) - 1)


reversed_s = ''.join(char_list)
print("Reversed String:", reversed_s)


if s == reversed_s:
    print("String is Palindrome")
else:
    print("String is not Palindrome")
