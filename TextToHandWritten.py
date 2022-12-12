import pywhatkit

ques = input("Enter the Question: ")
ans = input("Enter your Answer: ")
# noinspection PyTypeChecker
pywhatkit.text_to_handwriting("Question: "+ques+"\n" + "Answer: " + ans, rgb=[0, 0, 255])


# text = input("Enter the text: ")
# # noinspection PyTypeChecker
# pywhatkit.text_to_handwriting(text, rgb=[0, 0, 255])


