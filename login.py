from tkinter import *
from tkinter import ttk
from tkinter import messagebox

player = 0

#假資料庫
Login = {'King':'123456', 'OOXX':'666', 'Sleep':'4125252'}
Name = []

#--------------------------圈圈叉叉系統----------------------------

def openNewWindow():
    def btn_click(btn):
        global player
        if btn['text'] == '':
            if player:
                btn['text'] = 'X'
                lab['text'] = f'當前玩家: {Name[0]} (O)'
                player = 0
            else:
                btn['text'] = 'O'
                lab['text'] = f'當前玩家: {Name[1]} (X)'
                player = 1
            btn['state'] = DISABLED
            check_win()

    def set_btn_disabled():
        btn00['state'] = DISABLED
        btn01['state'] = DISABLED
        btn02['state'] = DISABLED
        btn03['state'] = DISABLED
        btn04['state'] = DISABLED
        btn05['state'] = DISABLED
        btn06['state'] = DISABLED
        btn07['state'] = DISABLED
        btn08['state'] = DISABLED

    def check_win():
        if btn00['text'] == btn01['text'] == btn02['text'] and btn00['text'] != '':
            set_btn_disabled()
            messagebox.showinfo("Game Over", btn00['text'] + " wins")
        elif  btn03['text'] == btn04['text'] == btn05['text'] and btn03['text'] != '':
            set_btn_disabled()
            messagebox.showinfo("Game Over", btn03['text'] + " wins")
        elif  btn00['text'] == btn03['text'] == btn06['text'] and btn00['text'] != '':
            set_btn_disabled()
            messagebox.showinfo("Game Over", btn00['text'] + " wins")
        elif  btn06['text'] == btn07['text'] == btn08['text'] and btn06['text'] != '':
            set_btn_disabled()
            messagebox.showinfo("Game Over", btn06['text'] + " wins")
        elif  btn01['text'] == btn04['text'] == btn05['text'] and btn01['text'] != '':
            set_btn_disabled()
            messagebox.showinfo("Game Over", btn01['text'] + " wins")
        elif  btn02['text'] == btn05['text'] == btn08['text'] and btn02['text'] != '':
            set_btn_disabled()
            messagebox.showinfo("Game Over", btn02['text'] + " wins")
        elif  btn00['text'] == btn04['text'] == btn08['text'] and btn00['text'] != '':
            set_btn_disabled()
            messagebox.showinfo("Game Over", btn00['text'] + " wins")
        elif  btn02['text'] == btn04['text'] == btn06['text'] and btn02['text'] != '':
            set_btn_disabled()
            messagebox.showinfo("Game Over", btn02['text'] + " wins")
        elif (btn00['text'] != '' and
                btn01['text'] != '' and
                btn02['text'] != '' and
                btn03['text'] != '' and
                btn04['text'] != '' and
                btn05['text'] != '' and
                btn06['text'] != '' and
                btn07['text'] != '' and
                btn08['text'] != ''):
            set_btn_disabled()
            messagebox.showinfo("Game Over","沒輸沒贏")
    
    def again():
        openNewWindow()
        game.destroy()
    
    def LogOut():
        LogInWindow()
        game.destroy()
    
    game = Tk()
    game.title("Tic Tac Toe")
    game.geometry("300x300+200+100")
    game.grid_rowconfigure(0, weight=1)
    game.grid_rowconfigure(1, weight=1)
    game.grid_rowconfigure(2, weight=1)
    game.grid_rowconfigure(3, weight=1)
    game.grid_rowconfigure(4, weight=1)
    game.grid_columnconfigure(0, weight=1)
    game.grid_columnconfigure(1, weight=1)
    game.grid_columnconfigure(2, weight=1)
    
    lab = Label(game, text=f'當前玩家:{Name[0]} (O)', font=('Arial', 20))
    lab.grid(row=3, column=0, columnspan=20, sticky=NSEW)
    
    btn00 = Button(game, text='', font=('Arial', 20),
                    command=lambda: btn_click(btn00))
    btn00.grid(row=0, column=0, sticky=NSEW, pady=2, padx=2)
    
    btn01 = Button(game, text='', font=('Arial', 20),
                    command=lambda: btn_click(btn01))
    btn01.grid(row=0, column=1, sticky=NSEW, pady=2, padx=2)
    
    btn02 = Button(game, text='', font=('Arial', 20),
                    command=lambda: btn_click(btn02))
    btn02.grid(row=0, column=2, sticky=NSEW, pady=2, padx=2)
    
    btn03 = Button(game, text='', font=('Arial', 20),
                    command=lambda: btn_click(btn03))
    btn03.grid(row=1, column=0, sticky=NSEW, pady=2, padx=2)
    
    btn04 = Button(game, text='', font=('Arial', 20),
                    command=lambda: btn_click(btn04))
    btn04.grid(row=1, column=1, sticky=NSEW, pady=2, padx=2)
    
    btn05 = Button(game, text='', font=('Arial', 20),
                    command=lambda: btn_click(btn05))
    btn05.grid(row=1, column=2, sticky=NSEW, pady=2, padx=2)
    
    btn06 = Button(game, text='', font=('Arial', 20),
                    command=lambda: btn_click(btn06))
    btn06.grid(row=2, column=0, sticky=NSEW, pady=2, padx=2)
    
    btn07 = Button(game, text='', font=('Arial', 20),
                    command=lambda: btn_click(btn07))
    btn07.grid(row=2, column=1, sticky=NSEW, pady=2, padx=2)
    
    btn08 = Button(game, text='', font=('Arial', 20),
                    command=lambda: btn_click(btn08))
    btn08.grid(row=2, column=2, sticky=NSEW, pady=2, padx=2)
    
    Remake = Button(game, text='重製',
                    command=again)
    Remake.grid(row=4, column=1, sticky=NSEW)
    
    Logout = Button(game, text='登出',
                    command=LogOut)
    Logout.grid(row=4, column=0, sticky=NSEW)
    
#-----------------------------------------------------------------

#---------------------------註冊系統------------------------------
def SignIn_window():
    def INPUT():
        SignId = Sign_ID.get()
        Signpassword = Sign_password.get()
        Login.update({SignId: Signpassword})
        messagebox.showinfo("創建完成", "已新增帳號 !")
        signin.destroy()
    
    signin = Tk()
    signin.title("Sign in")
    signin.geometry("500x200+500+100")
    #排版
    signin.rowconfigure(0, weight=1)
    signin.rowconfigure(1, weight=1)
    signin.rowconfigure(2, weight=1)
    signin.rowconfigure(3, weight=1)
    signin.rowconfigure(4, weight=1)
    signin.rowconfigure(5, weight=1)
    signin.rowconfigure(6, weight=1)
    signin.columnconfigure(0, weight=1)
    signin.columnconfigure(1, weight=1)
    signin.columnconfigure(2, weight=1)

    Sign_labl = Label(signin, text="圈圈叉叉競賽註冊系統", 
                    background='#ccddff',
                    font=("Arial", 20, "bold"))
    Sign_labl.grid(row=0, column=1)
    
    Sign_labl2 = Label(signin, text='帳號名稱',
                    font=("Arial", 10, "bold"))
    Sign_labl2.grid(row=1, column=1)
    
    Sign_ID = Entry(signin, width=20)
    Sign_ID.grid(row=2, column=1)
    
    Sign_labl3 = Label(signin, text='密碼',
                    font=("Arial", 10, "bold"))
    Sign_labl3.grid(row=3, column=1)
    
    Sign_password = Entry(signin, width=20, show='*')
    Sign_password.grid(row=4, column=1)
    
    OkBtn = Button(signin, text='註冊', command=INPUT)
    OkBtn.grid(row=5, column=1)

#---------------------------登入系統------------------------------
def LogInWindow():
    def check():
        id = ID.get()
        key = password.get()
        
        if id in Login:
            if Login[id] == key:
                messagebox.showinfo("登入成功", "水喔")
                NAME()
                root.destroy()
            else:
                messagebox.showerror("登入失敗", "連自己密碼都不知道嗎?")
        else:
            messagebox.showerror("查無此號", "沒帳號快去創一個")
    root = Tk()
    root.title("Login")
    root.geometry("500x200+500+100")
    #排版
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.rowconfigure(5, weight=1)
    root.rowconfigure(6, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    
    labl = Label(root, text="圈圈叉叉競賽登入系統", 
                    background='#ccddff',
                    font=("Arial", 20, "bold"))
    labl.grid(row=0, column=1)
    
    labl2 = Label(root, text='登入',
                    font=("Arial", 10, "bold"))
    labl2.grid(row=1, column=1)
    
    ID = Entry(root, width=20)
    ID.grid(row=2, column=1)
    
    labl3 = Label(root, text='密碼',
                    font=("Arial", 10, "bold"))
    labl3.grid(row=3, column=1)
    
    password = Entry(root, width=20, show='*')
    password.grid(row=4, column=1)
    
    EnterBtn = Button(root, text='登入', command=check)
    EnterBtn.grid(row=5, column=1)
    
    SignInBtn = Button(root, text='註冊', command=SignIn_window)
    SignInBtn.grid(row=5, column=2)
#-------------------------------------------------------------------------

#---------------------------玩家名稱-----------------------------------
def NAME():
    def StartGame():
        n1 = ID.get()
        n2 = ID2.get()
        Name.append(n1)
        Name.append(n2)
        openNewWindow()
        name.destroy()
    
    name = Tk()
    name.title("Name")
    name.geometry("500x200+500+100")
    #排版
    name.rowconfigure(0, weight=1)
    name.rowconfigure(1, weight=1)
    name.rowconfigure(2, weight=1)
    name.rowconfigure(3, weight=1)
    name.rowconfigure(4, weight=1)
    name.rowconfigure(5, weight=1)
    name.rowconfigure(6, weight=1)
    name.columnconfigure(0, weight=1)
    name.columnconfigure(1, weight=1)
    name.columnconfigure(2, weight=1)
    
    labl = Label(name, text="建立玩家名稱", 
                    background='#ccddff',
                    font=("Arial", 20, "bold"))
    labl.grid(row=0, column=1)
    
    labl2 = Label(name, text='玩家一',
                    font=("Arial", 10, "bold"))
    labl2.grid(row=1, column=1)
    
    ID = Entry(name, width=20)
    ID.grid(row=2, column=1)
    
    labl3 = Label(name, text='玩家二',
                    font=("Arial", 10, "bold"))
    labl3.grid(row=3, column=1)
    
    ID2 = Entry(name, width=20)
    ID2.grid(row=4, column=1)
    
    EnterBtn = Button(name, text='開始遊戲', command=StartGame)
    EnterBtn.grid(row=5, column=1)

#------------------------初始介面-----------------------------------------
def L():
    LogInWindow()
    start.destroy()

if __name__ == "__main__":
    start = Tk()
    start.title("Start")
    start.geometry("300x100+500+100")
    
    startBtn = Button(start, text='點擊開始', font=("Arial", 20, "bold"), command=L)
    startBtn.pack()
    
    start.mainloop()