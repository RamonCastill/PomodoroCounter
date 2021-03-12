from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    timer_title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(canvas_text, text="00:00")
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60



    if reps % 2 != 0:
        count_down(work_sec)
        timer_title.config(text="Work", fg=GREEN)
    if reps % 2 == 0:
        count_down(short_break_sec)
        timer_title.config(text="Break", fg=PINK)
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_title.config(text="Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        check_label.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Label
timer_title = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_title.grid(row=0, column=1)

button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(row=2, column=2)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

window.mainloop()
