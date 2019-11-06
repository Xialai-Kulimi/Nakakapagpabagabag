import math

while True:
    command = input()
    head = command.split(' ')[0]
    if head == 'add':
        if len(command.split(' ')) > 3:
            print('Too many aruments')
            continue
        else:
            try:
                user_file = open('./player/' + command.split(' ')[1], 'r')
                user_file.close()
                print('User have exist!')
            except:
                user_file = open('./player/' + command.split(' ')[1], 'w')
                user_file.write(command.split(' ')[2] + '\n'
                                'Mail_progress: 0\n')
                user_file.close()
                user_file = open('./player_mail/' + command.split(' ')[1], 'w')
                user_file.close()
                print('add suscced')