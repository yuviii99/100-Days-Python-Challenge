import tkinter
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
time = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(time)
    canvas.itemconfig(canvas_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    tick_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        timer_label.config(text="WORK", fg=GREEN)
        count_down(work_sec)
    elif reps % 2 == 0:
        timer_label.config(text="SHORT BREAK", fg=PINK)
        count_down(short_break_sec)
    elif reps % 8 == 0:
        timer_label.config(text="LONG BREAK", fg=RED)
        count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global time
        time = window.after(1000, count_down, count - 1)
    else:
        timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        tick_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(height=224, width=210, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")

canvas.create_image(103, 112, image=tomato_img)
canvas_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.config(bg=YELLOW)
canvas.grid(row=1, column=1)

timer_label = tkinter.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "normal"), bg=YELLOW, highlightthickness=0)
timer_label.grid(row=0, column=1)

start_button = tkinter.Button(text="Start", highlightthickness=0, command=timer)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

tick_label = tkinter.Label(fg=GREEN, bg=YELLOW, highlightthickness=0)
tick_label.grid(row=3, column=1)

window.mainloop()
