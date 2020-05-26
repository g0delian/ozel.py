import random
import re

poems = open("erbain.txt", "r", encoding='utf-8').read()
rx = r"\.([a-zA-Z])"
result = re.sub(rx, ".\n", poems)
word_bag = result.split()

index = 1
chain = {}
count = 100

for word in word_bag[index:]:
    key = word_bag[index - 1]
    if key in chain:
        chain[key].append(word)
    else:
        chain[key] = [word] # create a list
    index += 1

word1 = random.choice(list(chain.keys())) #random first word
message = word1.capitalize()

while len(message.split(' ')) < count:
    word2 = random.choice(chain[word1])
    word1 = word2
    message += ' ' + word2

with open("poem.txt", "w", encoding='utf-8') as file:
    file.write(message)
output = open('poem.txt', 'r', encoding='utf-8')
print(output.read())