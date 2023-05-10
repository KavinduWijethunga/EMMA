
from mental_state_detector import check_sad



# Testing the response system
while True:
    print('Bot: how about you ... ')
    human_response = input('You: ')
    res , ms = check_sad(human_response)
    print('respose - ',res ,'  -  ', 'mental_state - ', ms)















