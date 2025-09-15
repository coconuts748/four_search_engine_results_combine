import tkinter as tk
from tkinter import ttk,messagebox
from 已完成.各搜索平台结果汇总.parts import search_encrypted_something
from 已完成.各搜索平台结果汇总.input import searching_input
import json
import time
import sys

class DATABASE:
    def __init__(self):
        self.user__data = {}
        default_messages = {
            search_encrypted_something('name'):search_encrypted_something('code')
        }
        try:
            with (open('data_base.json', 'wb') as f):
                f.write(json.dumps(default_messages).encode('utf-8'))

        except Exception as e:
            print(f"初始化账户信息失败..{e}")

    def add_user_data(self,account,password):
        if account is None or len(account) == 0:
            return
        elif password is None or len(password) == 0:
            return
        else:
            deal_account = search_encrypted_something(account)
            deal_password = search_encrypted_something(password)
            self.user__data[deal_account] = deal_password

            # print(self.user__data)
            # print(type(self.user__data))
            try:
                with open('data_base.json', 'ab') as f:
                    f.write(json.dumps(self.user__data).encode('utf-8'))
                    # print(self.user__data)

            except Exception as e:
                print(f'添加失败,reason:{e}')

    def del_user_data(self,account_name):
        if account_name is None or len(account_name) == 0:
            return
        else:
            try:
                deal_account_name = search_encrypted_something(account_name)
                del self.user__data[deal_account_name]

            except Exception as e:
                print(f'账户不存在,reason:{e}')

u_s_e_r_data = DATABASE()
u_s_e_r_data.add_user_data('name1','code1')

now = time.asctime(time.localtime(time.time()))

def the_first_ui():
    def go_to_login():
        the_first_ui_root.destroy()
        print('go to login running ....')
        def inner_go_to_login_quit():
            if messagebox.askyesno('提示','确认退出?'):
                go_to_login_root.destroy()
        def inner_go_to_login():
            login_name = str(login_name_1.get()).strip()
            login_password = str(login_password_1.get()).strip()
            if len(login_name) == 0 or len(login_password) == 0:
                messagebox.showwarning('错误','输入无效!')
                sys.exit()
            else:
                try:
                    login_name__ = search_encrypted_something(login_name)
                    login_password__ = search_encrypted_something(login_password)
                    if u_s_e_r_data.user__data[login_name__] == login_password__:
                        messagebox.showinfo('登陆成功',f'欢迎:用户{login_name}')
                        go_to_login_root.destroy()
                        ###########search_content_here###
                        searching_input()  #####search_content_here###
                        ###########search_content_here###

                    else:
                        messagebox.showwarning('提示','账号或密码错误!')
                except Exception as e:
                    print(f'引用类错误:{e}')

        go_to_login_root = tk.Tk()
        go_to_login_root.title('登录界面')
        go_to_login_root.geometry('400x200')

        tk.Label(go_to_login_root, text='用户名:').grid(row=1,column=0)
        login_name_1 = tk.Entry(go_to_login_root)
        login_name_1.insert(0,'删除此内容以输入....')
        login_name_1.grid(row=1,column=1,columnspan=5)

        tk.Label(go_to_login_root,text='密码:').grid(row=2,column=0)
        login_password_1 = tk.Entry(go_to_login_root, show='*')
        login_password_1.grid(row=2,column=1,columnspan=5)

        go_to_login_button = ttk.Button(go_to_login_root,text='确认登录',command=inner_go_to_login)
        go_to_login_button.grid(row = 1,column=7)

        go_to_login_button_1 = ttk.Button(go_to_login_root,text='退出',command=inner_go_to_login_quit)
        go_to_login_button_1.grid(row = 2,column=7)

        go_to_login_root.mainloop()

    def go_to_register():
        the_first_ui_root.destroy()
        def inner_go_to_register_quit():
            if messagebox.askyesno('提示','是否退出当前界面?'):
                go_to_register_root.destroy()

        def inner_go_to_register():
            print()
            register_name = str(register_name_1.get()).strip()
            register_code = str(register_code_1.get()).strip()
            if len(register_name) == 0 or len(register_code) == 0:
                messagebox.showwarning('错误', '输入无效!')
                sys.exit()
            else:
                if messagebox.askyesno('提示',
                                       f'确认注册?当前注册的账号信息为:\n账号:{register_name}\n密码:{register_code}'):
                    try:
                        register_name__ = search_encrypted_something(register_name)
                        register_code__ = search_encrypted_something(register_code)
                        u_s_e_r_data.user__data[register_name__] = register_code__
                        messagebox.showinfo('提示', '账号注册完成,现可进行登录...')
                        go_to_login()
                        return u_s_e_r_data.user__data[register_name__]

                    except Exception as e:
                        print(f'添加账号失败:{e}')
        go_to_register_root = tk.Tk()
        go_to_register_root.title('注册界面')
        go_to_register_root.geometry('400x200')

        tk.Label(go_to_register_root,text='注册账号:').grid(row=1,column=0)
        register_name_1 = tk.Entry(go_to_register_root)
        register_name_1.grid(row=1,column=1,columnspan=5)

        tk.Label(go_to_register_root,text='注册密码:').grid(row=2,column=0)
        register_code_1 = tk.Entry(go_to_register_root)
        register_code_1.grid(row=2,column=1,columnspan=5)

        go_to_register_button = ttk.Button(go_to_register_root,text='确认注册',command=inner_go_to_register)
        go_to_register_button.grid(row = 1,column=7)

        go_to_register_button_1 = ttk.Button(go_to_register_root,text='退出',command=inner_go_to_register_quit)
        go_to_register_button_1.grid(row = 2,column=7)
        go_to_register_root.mainloop()

    def quit_page():
        if messagebox.askyesno('提示','是否退出当前界面?'):
            sys.exit()

    def go_for_help():
        messagebox.showinfo('提示','111111111')

    the_first_ui_root = tk.Tk()
    the_first_ui_root.title('首界面 当前时间为:{}'.format(now))

    the_first_ui_button = ttk.Button(the_first_ui_root,text='去登录',command=go_to_login)
    the_first_ui_button.pack()

    the_first_ui_button_1 = ttk.Button(the_first_ui_root,text='去注册',command=go_to_register)
    the_first_ui_button_1.pack()

    the_first_ui_button_2 = ttk.Button(the_first_ui_root,text='帮助',command=go_for_help)
    the_first_ui_button_2.pack()

    the_first_ui_button_3 =ttk.Button(the_first_ui_root,text='退出',command=quit_page)
    the_first_ui_button_3.pack()

    the_first_ui_root.mainloop()

# the_first_ui()