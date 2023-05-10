

from chat_api_level import chat_me

print('bot --->  hellow , how about today')
count = 0

while True:


    count = count + 1
    if count == 3:
        print('------- spacial question -------')
        print('by the way how about your filing...')
        count =0

    else:
        user_text = input('user  <-- ')
        print('bot --->  ', chat_me(user_text))
