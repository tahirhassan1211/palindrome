def istext_palindrome(text):
    text=text.lower()
    original_text=text
    reverse_text=""
    for i in text:
        reverse_text= i + reverse_text
    if(reverse_text==original_text):
        return f"{original_text} is palindrome..!"
    else:
        return f"{original_text} is not palindrome"

print(istext_palindrome("abcxba"))
