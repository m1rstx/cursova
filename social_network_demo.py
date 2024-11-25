from login import CheckDBLog
from registration import RegDB
from post import PostDB
from title import *
from postlist import AllPost


class SN:
    def user_sign_in():
        user_log = CheckDBLog()
        user_log.check_user_exists()
        return user_log.is_authenticated, user_log.user_in_sn
    
    def user_sign_up():
        user_reg = RegDB()
        user_reg.save_to_db()

    def user_create_post(author):
        user_post = PostDB(author)
        user_post.save_to_db()
        user_post.introduce()

    def user_view_post():
        all_post = AllPost()
        all_post.watch_all_post()

sn_hndlers = SN

def sn_choice(): 
    print(welcome_to_sn)
    option = int(input("\n1 - sign in \n2 - sign up \n>>> "))
            
    if option == 1:
        is_autenticated, user_name = sn_hndlers.user_sign_in()
        if is_autenticated:
            print(succesfull)
            main_program(user_name)
        else:
            print("error")
    elif option == 2:
        sn_hndlers.user_sign_up()
        print(succesfull)
        sn_choice()
    else:
        print("incorrect value")
    
def main_program(user_name):
    while True:
        user_option = int(input("1 - create post \n2 - watch all post \n3 - exit \n>>> "))

        if user_option == 1:
            sn_hndlers.user_create_post(user_name)
        elif user_option == 2:
            sn_hndlers.user_view_post()
        else:
            print(goodbye)
            break


sn_choice()