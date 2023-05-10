

from chat_api_level import chat_me
from mental_state_detector import check_dipp
import random

# print('bot --->  hellow , how about today')
# count = 0

# while True:
#
#
#     human_text = input('You: ')
#
#     count = count + 1
#     if count == 3:
#         # print('------- spacial question -------')
#         print('by the way how about your filing...')
#         count =0
#
#         #print('Bot: how about you ... ')
#         #human_response = input('You: ')
#         human_response = human_text
#
#
#         res, ms = check_dipp(human_response)
#         print('respose - ', res, '  -  ', 'mental_state - ', ms)
#
#     else:
#         #user_text = input('user  <-- ')
#         user_text = human_text
#         print('bot --->  ', chat_me(user_text))



count = 0
ans_lock = False
finish_ans_in_a_ssion = False


report_lbl = ['stress','sleep_issu','prb 3','prob 4']
report = [False,False,False,False]
quiz_number = 0

def chat_engin(human_text):


    global count,ans_lock,report,quiz_number,finish_ans_in_a_ssion

    if ans_lock == False:
        #user_text = input('user  <-- ')
        user_text = human_text
        bot_text = chat_me(user_text)
        #print('bot --->  ', chat_me(user_text))

        if finish_ans_in_a_ssion == False:
            count = count + 1
        else:
            count = 0


    if count == 3 and finish_ans_in_a_ssion == False:


        if ans_lock == False:

            quiz_arr = [0,1,2,3]
            ar_max = len(quiz_arr)


            re_derect_ans_list = [

                'by the way how you feel today tired or relax ?',
                'ok i have a question how about you today stress or not',
                'by the way how about your filing...3',
                'by the way how about your filing...4',
            ]

            re_derect_ans = re_derect_ans_list[ quiz_arr[quiz_number]]
            bot_text = bot_text+'\n'+re_derect_ans

            ans_lock = True

        elif ans_lock == True:

            res, ms = check_dipp(human_text)
            bot_text = res

            if ms == True:

                report[quiz_number] = True

            #print(quiz_number)
            if quiz_number == 3:

                finish_ans_in_a_ssion = True


            quiz_number = quiz_number + 1

            #print(report)
            ans_lock = False
            count = 0

    return bot_text ,report



# while True:
#
#     inp = input('user  <-- ')
#     re_bot = chat_engin(inp)
#     print('bot --->  ', re_bot)

