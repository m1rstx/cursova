from login import Check_DB_log
from registration import Reg_DB
from post import Post_DB
from comment import Comment_DB
from postlist import watch_all_post

def user_sign_in():
    user_log = Check_DB_log()
    user_log.check_user_exists()
    return user_log.is_authenticated
    
def user_sign_up():
    user_reg = Reg_DB()
    user_reg.save_to_db()

def user_create_post():
    user_post = Post_DB()
    user_post.save_to_db()
    user_post.introduce()

def user_create_comment():
    user_comment = Comment_DB()
    user_comment.save_to_db()
    user_comment.introduce()

def user_view_post():
    watch_all_post()



def sn_choice(): 
    option = int(input("\n1 - sign in \n2 - sign up \n>>> "))

    if option == 1:
        is_autenticated = user_sign_in()
        if is_autenticated:
            print("\nwelcome to SN!")
            main_program()
        else:
            print("error")
    elif option == 2:
        user_sign_up()
        print("\nsuccesfull registration!")
        main_program()
    else:
        print("incorrect value")
    
def main_program():
    while True:
        user_option = int(input("\n1 - create post \n2 - watch all post \n3 - exit \n>>> "))

        if user_option == 1:
            user_create_post()
        elif user_option == 2:
            user_view_post()
        else:
            print("goodbye!")
            break




sn_choice()