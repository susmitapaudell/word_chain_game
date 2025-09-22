from dictionary import collection

import random

def play():
    used_words = [ ]
    user_word = input("You: ").lower()

    while True:

        used_words.append(user_word)
        first_letter_for_bot = user_word[-1]
        
        chk = [w for w in collection if w[0] == first_letter_for_bot and w not in used_words]
        
        bot_word = random.choice(chk)
        
        if (bot_word == None):
            print('bot cant find any word, bot lost')
            exit()

        print('Bot: ', bot_word)

        used_words.append(bot_word)

        if (bot_word[0] != first_letter_for_bot):
            print("word not matched, bot lost!!!")
            exit()
        
        user_word = input("You: ").lower()
        if(user_word[0] != bot_word[-1]):
            print('word not matched, user lost!!!!')
            exit()

        elif (user_word in used_words):
            print('word repeated by the user, user lost!!!')
            exit()
        
play()   

        
