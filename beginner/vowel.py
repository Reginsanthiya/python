r = input("Input a letter of the alphabet: ")

if r in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % r)
elif r == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % r) 
