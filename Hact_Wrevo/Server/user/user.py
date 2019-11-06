__author__ = 'Kulimi'


def adduser(username, password):
    try:
        user_file = open('./player/' + username, 'r')
        user_file.close()
        return 1
    except:
        user_file = open('./player/' + username, 'w')
        user_write(password + '\n')
        user_file.close()
        user_file = open('./player_mail/' + username, 'w')
        user_file.close()
        return 0