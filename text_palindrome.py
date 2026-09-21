def is_palindrome(text):
  text=text.lower()
  left=0
  right=len(text)-1
  while(left<right):
    if(text[left]!= text[right]):
      return f"{text} is not palindrome"
    left +=1
    right -=1
    return f"{text} is a palindrome"

print(is_palindrome("abbcbba"))
