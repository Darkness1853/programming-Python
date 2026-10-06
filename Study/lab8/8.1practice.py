import random
words = ["кот","кит","крокодил"]
secret = random.choice(words)
hidden = ["#"]*len(secret)
human = ["\n +---+\n     |\n     |\n     |\n   =====\n",
    "\n +---+\n 0   |\n     |\n     |\n   =====\n",
    "\n +---+\n 0   |\n |   |\n     |\n   =====\n",
    "\n +---+\n 0   |\n/|   |\n     |\n   =====\n",
    "\n +---+\n 0   |\n/|\\  |\n     |\n   =====\n",
    "\n +---+\n 0   |\n/|\\  |\n/    |\n   =====\n",
    "\n +---+\n 0   |\n/|\\  |\n/ \\  |\n   =====\n"]
errors=0
while errors<6 and "#" in hidden:
    print(" "*40)
    print(human[errors])
    print(hidden)
    c=input(">")
    if c in secret:
        for i in range(len(secret)):
            if secret[i]==c:
                hidden[i] = c
    else:
        errors +=1
print(human[errors])
print(*hidden)