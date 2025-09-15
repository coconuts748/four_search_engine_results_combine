import tkinter
from tkinter import ttk,messagebox
import sys
from 已完成.各搜索平台结果汇总.parts import search_encrypted_something
from 已完成.各搜索平台结果汇总.content import total_search_engine_running_frame

def searching_input():
    def input_searching():
        searching_input_root.destroy()
        def inner_input_searching():

            print('inner input searching running....')
            ensure_search_content_ = str(ensure_search_content.get()).strip()
            if messagebox.askyesno('提示',f'确认搜索?\n当前搜索内容为:\n{ensure_search_content_}'):
                input_searching_root.destroy()
                messagebox.showinfo('提示','请耐心等待....')
                ############################################################
                total_search_engine_running_frame(ensure_search_content_)
                ############################################################
                messagebox.showinfo('提示','搜索内容现已整理！')
                sys.exit()

        input_searching_root = tkinter.Tk()
        input_searching_root.title('搜索界面')
        input_searching_root.geometry('400x50')

        tkinter.Label(input_searching_root,text='搜索:').grid(row=1, column=0)

        ensure_search_content = tkinter.Entry(input_searching_root)
        ensure_search_content.insert(0,'删除此内容以进行输入搜索...')
        ensure_search_content.grid(row=1, column=1,columnspan=70)

        ensure_search_button = ttk.Button(input_searching_root,text='确认搜索',command=inner_input_searching)
        ensure_search_button.grid(row=2, column=0)

        input_searching_root.mainloop()

    def quit_searching_page():
        if messagebox.askyesno('提示','确认退出当前页面?'):
            searching_input_root.destroy()

    searching_input_root = tkinter.Tk()
    searching_input_root.title('搜索操作页面')
    searching_input_root.geometry('200x100')

    searching_input_button = ttk.Button(searching_input_root,text='进入搜索',command=input_searching)
    searching_input_button.pack()

    searching_input_button_1 = ttk.Button(searching_input_root,text='退出',command=quit_searching_page)
    searching_input_button_1.pack()
    searching_input_root.mainloop()

# searching_input()