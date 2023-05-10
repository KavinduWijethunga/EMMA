import re

import random



##########################################################################################################################
def check_dipp(user_input):

    R_EATING = "I don't like eating anything because I'm a bot obviously!"
    R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"


    def unknown():
        response = ["Could you please re-phrase that? ",
                    "...",
                    "I am sorry to hear that.",
                    "Have you had trouble sleeping?"][
            random.randrange(4)]
        return response



    def message_probability(user_message, recognised_words, single_response=False, required_words=[]):


        message_certainty = 0
        has_required_words = True

        # Counts how many words are present in each predefined message
        for word in user_message:
            if word in recognised_words:
                message_certainty += 1

        # Calculates the percent of recognised words in a user message
        percentage = float(message_certainty) / float(len(recognised_words))

        # Checks that the required words are in the string
        for word in required_words:
            if word not in user_message:
                has_required_words = False
                break

        # Must either have the required words, or be a single response

        if has_required_words or single_response:

            #print(int(percentage * 100))

            return int(percentage * 100)
        else:
            return 0


    def check_all_messages(message):
        highest_prob_list = {}


        # Simplifies response creation / adds it to the dict
        def response(bot_response, list_of_words, single_response=False, required_words=[]):


            nonlocal highest_prob_list
            highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words )


        response('I think i can help you', ['no', 'not', 'never', 'dont', 'not now'], single_response=True)
        response('your are not good', ['no', 'not', 'never', 'dont', 'not now'], single_response=True)
        response('nice to hear', ['yes', 'yea', 'yes i do', 'exsacly', 'orfanly'], single_response=True )


        # Longer responses
        # response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
        # response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])



        best_match = max(highest_prob_list, key=highest_prob_list.get)
        # print(highest_prob_list)
        #print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')


        annoy_mantal_state = False

        if best_match == 'your are not good':
            annoy_mantal_state = True

        if best_match == 'nice to hear':
            annoy_mantal_state = False


        return unknown() if highest_prob_list[best_match] < 1 else best_match , annoy_mantal_state


    # Used to get the response

    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    #print('response - ',split_message)
    response,ms = check_all_messages(split_message)

    return response , ms

##########################################################################################################################





# # Testing the response system
# while True:
#     print('Bot: how about you ... ')
#     human_response = input('You: ')
#     res , ms = check_sad(human_response)
#     print('respose - ',res ,'  -  ', 'mental_state - ', ms)
