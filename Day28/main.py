
from tkinter import *

checkmark = "✔"
completed_pomodoros = 0
pause = False
pomodoro_running = True

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 25
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
current_timer = 0


def set_current_timer_ms(time: float):
    global current_timer
    current_timer = time * 60 * 1000

set_current_timer_ms(WORK_MIN) 

def get_current_time() -> str:
    total_minutes = float(f"{round(current_timer / 1000 / 60, 2)}")
    min = int(total_minutes)
    sec = round((total_minutes - min) * 60)
    if sec == 60:
        minutes += 1
        sec = 0
    
    return f"{min:02}:{sec:02}"

def set_timer_label(canvas: Canvas, item_id: int, val: str):
    canvas.itemconfig(item_id, text=get_current_time())

def update_timer(canvas: Canvas, timer_id: int):
    global current_timer
    global pause

    if pause: 
        window.after(1000, update_timer, canvas, timer_id)
        return
    
    current_timer -= 1000
    set_timer_label(canvas, timer_id, get_current_time())
    check_for_break()
    check_to_start_pomodoro()
    window.after(1000, update_timer, canvas, timer_id)

def start_next_pomodoro():
    global pomodoro_running
    global pause
    
    if pomodoro_running and pause:
        update_title("Pomodoro", GREEN)
        pause = False
        return

    if pomodoro_running and not pause:
        return
    
    set_current_timer_ms(WORK_MIN)
    pause = False
    pomodoro_running = True
    update_title("Pomodoro", GREEN)

def reset_pomodoros():
    global completed_pomodoros
    global pause

    completed_pomodoros = 0
    restart_completed_pomodoros()
    pause = True

def check_for_break():
    global pomodoro_running
    global current_timer

    if not pomodoro_running or current_timer > 0:
        return
    
    pomodoro_running = False
    
    raise_above_all()

    if current_timer <= 0: 
        pomodoro_completed()
        if completed_pomodoros % 4 == 0:
            set_current_timer_ms(LONG_BREAK_MIN)
            update_title("Break", RED)
        else:
            set_current_timer_ms(SHORT_BREAK_MIN)
            update_title("Break", PINK)

def check_to_start_pomodoro():
    global pomodoro_running
    global current_timer
    global pause
    
    if pomodoro_running or current_timer > 0:
        return
    
    update_title("Pomodoro", GREEN)
    set_current_timer_ms(WORK_MIN)
    update_title("Click on Start\n to begin the\n next pomodoro", GREEN)
    pause = True
    pomodoro_running = True 

def pomodoro_completed():
    global completed_pomodoros
    completed_pomodoros += 1
    update_completed_pomodoros()


def start_long_break():
    pass

def start_short_break():
    pass


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()


window.title("Pomodoro App")
window.config(padx=100, pady= 50, bg=YELLOW)

title = Label(text="Pomodoro", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 28, "bold"))
title.grid(column=1,row=0)

def update_title(val: str, color: str):
    title.config(text=val)
    title.config(fg=color)

canvas = Canvas(width=212, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Day28/tomato.png")
canvas.create_image(106, 112,image=tomato_img)
timer_id = canvas.create_text(106,130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
set_timer_label(canvas, timer_id, current_timer)

update_timer(canvas, timer_id)

canvas.grid(column=1,row=1)

start_button = Button(text="Start", bg=PINK, font=(FONT_NAME, 18))
start_button.grid(column=0, row=2)
start_button.config(command=start_next_pomodoro)

completed_pomodoros_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12))
completed_pomodoros_label.grid(column=1, row=3)

def update_completed_pomodoros():
    temp = completed_pomodoros_label.cget("text") + checkmark
    completed_pomodoros_label.config(text=temp)

def restart_completed_pomodoros():
    completed_pomodoros_label.config(text="")

def raise_above_all():
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)

reset_button = Button(text="Reset", bg=PINK, font=(FONT_NAME, 18))
reset_button.grid(column=2, row=2)
reset_button.config(command=reset_pomodoros)

window.mainloop()