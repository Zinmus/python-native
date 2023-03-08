import sys

print("Give a sentence to check.")
sentence = input()

def format_sentence(sentence):
    sentence = sentence.replace(" ","")
    sentence = sentence.lower()
    if sentence.isalpha():
        return sentence
    else:
        print("This sentence has something that is not a letter. End of application")
        sys.exit()
    
def is_palindrome(sentence):
    sentence = format_sentence(sentence)
    for i in range(len(sentence)):
        if sentence[i] != sentence[len(sentence)-i-1]:
            return False
    return True

if is_palindrome(sentence):
    print("This sentence is a palindrome.")
else:
    print("This sentence is not a palindrome.")
