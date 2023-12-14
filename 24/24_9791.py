s = open("24_9791.txt").readline()

wrong_letters = "GHIJKLMNOPQRSTUVWXYZ"

for letter in wrong_letters:
    s = s.replace(letter, "*")

s = s.split("*")
answer = max(s, key=len)
print(len(answer))
