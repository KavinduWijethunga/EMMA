

from chat_api_level import chat_me

print('bot --->  hellow , how about today')

while True:

    user_text = input('user  <-- ')
    print('bot --->  ',chat_me(user_text))