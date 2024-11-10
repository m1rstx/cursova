from login import *
from registration import *
from post import *
from comment import *

def user_sign_in():
    user_log = Check_DB_log()
    user_log.check_user_exists()

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

option = int(input(f"1 - sign in \n2 - sign up \n>>> "))

def sn_choice():
    if option == 1:
        user_sign_in()
    else:
        user_sign_up()
    
def main_program():
    print("200")