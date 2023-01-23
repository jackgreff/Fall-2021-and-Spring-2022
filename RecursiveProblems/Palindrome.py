
import doctest

def is_palindrome(letters :str) -> bool:
   """
   checks if a string is a palindrome

	:param letters: term checked to be a palindrome. Must be string or character
	:return: True or false whether its a a palindrome. Will be boolean

	:examples:
	>>> is_palindrome('')
	True

	>>> is_palindrome('s')
	True

	>>> is_palindrome('bb')
	True

	>>> is_palindrome('ab')
	False

	>>> is_palindrome('This is not a palindrome')
	False

	>>> is_palindrome('A man, a plan, a canal: Panama!!')
	True
	"""
# Your code goes here
#    precondition: string or int (i've made it so it can allow some special characters seen below)
   mylist = []
   for a in letters:
      if a != ' ' and a != ',' and a != ':' and a != '!' and a != '.':
         a = a.lower()
         mylist.append(a)

   if len(mylist) <= 1: #precondition. automatically a palindrome if length is 1 or 0
      return True

   if mylist[0] != mylist[-1]:
      return False

   del mylist[0]
   del mylist[-1]
   return is_palindrome("".join(mylist))


# Uncomment the next line to run the tests
doctest.testmod()
# print(is_palindrome('aba'))
