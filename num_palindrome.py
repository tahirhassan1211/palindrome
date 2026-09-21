def isnum_palindrome(num):
  original=num
  reversenum=0
  while(num>0):
    digit=num %10
    reversenum=(reversenum*10)+digit
    num=num//10
  if(original==reversenum):
    print(f"{original} is palindrome")
  else:
    print(f"{original} is not palindrome")

isnum_palindrome(12321)
