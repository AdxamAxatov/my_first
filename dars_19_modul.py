
# def user_info():
#     dct = {
#         'average age': 40_000,
#         'old age': 0,
#         'adult age': 60_000,
        
#     }
#     new = ''
#     response = ''
#     overall = 0
#     lst = []
#     canceled = []
#     print('we are here selling tickets for the concert.'.upper())
#     while True:
#         user = int(input('Enter your age to idetify the price for you: '))
#         lst.append(user)
#         if user <= 7 or user >= 60:
#             overall += dct['old age']
#             print('the ticket is free')
#         elif user > 7 and user <= 18:
#             overall += dct['average age']
#             print('the ticket is 40.000 sum')
#         else:
#             user > 18 and user < 60
#             overall += dct['adult age']
#             print('the ticket is 60.000 sum')
        
#         new = input('do you want to buy the ticket? (yes/no): ').lower()
#         if new == 'no':
#             canceled.append(user)
#             overall -= dct['adult age'] or dct['average age'] or dct['old age']
#             print('if you change your mind, come back to buy some tickets \n Have a good time.')
#             print(f'\nYou bought tickets for ages: {lst}\nthe canceled one is for {canceled} ages \nThe overall cost is: {overall}')
#             break
#         else:
#             print('you bought the ticket.')
#             response = input('do you want to buy more ticket? (yes/no): ').lower()
#             if response == 'no' and new == 'no':
#                 break
#         print(f'\nYou bought tickets for ages: {lst} \nThe overall cost is: {overall}')























