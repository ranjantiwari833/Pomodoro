from tkinter import *

#constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 1
flag = 0 #ignores the multiple start clicked once the timer is running once
reset = 1

#timer mechnism
def start_clicked():
    global flag, reps, reset
    reset = 0
    if flag ==0:
        if reps %2 == 1:
            title_label.config(text="Work",background=YELLOW,font=(FONT_NAME,45,"bold"),foreground=RED)
            count_down(WORK_MIN*60)
        elif reps%8 == 0:
            count_down(LONG_BREAK_MIN*60)
            title_label.config(text="Long Break",background=YELLOW,font=(FONT_NAME,45,"bold"),foreground=GREEN)
        elif reps %2 ==0:
            count_down(SHORT_BREAK_MIN*60)
            title_label.config(text="Short Break",background=YELLOW,font=(FONT_NAME,45,"bold"),foreground=GREEN)


def reset_clicked():
    global reps, flag, reset
    reps = 1
    flag = 0
    reset = 1
    title_label.config(text="Timer",background=YELLOW,font=(FONT_NAME,45,"bold"),foreground=GREEN)
    tick.config(text="",background=YELLOW,foreground=RED)
    canvas.itemconfig(timer_text,text="00:00")


#countdown mechnism
def count_down(time):
    global flag, reps, reset     
    minutes = time // 60
    seconds = time % 60
    if seconds <10:
        seconds = f"0{seconds}"
    
    if time > 0 and reset==0:
        canvas.itemconfig(timer_text,text="{}:{}".format(minutes,seconds))
        window.after(1000,count_down,time-1)
        flag = 1
        
        
    elif time ==0:
        canvas.itemconfig(timer_text,text="{}:{}".format(minutes,seconds))
        flag = 0
        if reps==8:
            reset_clicked()
        
        reps +=1
        if reps%2 == 0:
            ticker_number = int(reps/2) 
            tick.config(text=ticker_number*"✔")
        start_clicked()
    

#UI setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=40,background=YELLOW)

#Label
title_label = Label(text="Timer",background=YELLOW,font=(FONT_NAME,45,"bold"),foreground=GREEN)
title_label.grid(row=0,column=1)

#canvas
canvas = Canvas(width=600,height=600,background=YELLOW,highlightthickness=0)#last *args to remove canvas and background border
tomato = PhotoImage(file="tomato.png")
canvas.create_image(300,300,image=tomato)
timer_text = canvas.create_text(300,300,text="00:00",fill="white",font=(FONT_NAME,50,"bold"))
canvas.grid(row=1,column=1)

#buttons
start = Button(text="Start",command=start_clicked)
start.grid(row=2,column=0)

reset = Button(text="Reset",command=reset_clicked)
reset.grid(row=2,column=2)

#ticks
tick = Label(text="",background=YELLOW,foreground=RED)#✔
tick.grid(row=3,column=1)


window.mainloop()