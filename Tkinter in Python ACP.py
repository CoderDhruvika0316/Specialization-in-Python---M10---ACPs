from tkinter import *

window = Tk()
window.title("My Personal Bio Form")
window.geometry("450x520")
window.config(bg = "lavender")

frame = Frame(window, bg = "#FFFFFF", padx = 20, pady = 20)
frame.grid(row = 0, column = 0, padx = 30, pady = 30)

title = Label(frame, text = "Personal Bio Form", font = ("Garamond", 18, "bold"), bg = "#C882DA", fg = "#000000", width = 25)
title.grid(row = 0, column = 0, columnspan = 2, pady = 10)

name = Label(frame, text = "Name", bg = "#FFFFFF", fg = "#000000", font = ("Garamond", 12))
name.grid(row = 1, column = 0, sticky = "w", pady = 5)

age = Label(frame, text = "Age", bg = "#FFFFFF", fg = "#000000", font = ("Garamond", 12))
age.grid(row = 2, column = 0, sticky = "w", pady = 5)

hobby = Label(frame, text = "Hobby", bg = "#FFFFFF", fg = "#000000", font = ("Garamond", 12))
hobby.grid(row = 3, column = 0, sticky = "w", pady = 5)

about = Label(frame, text="About Me:", bg="#FFFFFF", fg = "#000000", font=("Garamond", 11))
about.grid(row = 4, column = 0, sticky = "nw", pady = 5)

name_entry = Entry(frame, width = 30, bg = "#FFFFFF", fg = "#000000")
name_entry.grid(row = 1, column = 1, sticky = "w")

age_entry = Entry(frame, width = 30, bg = "#FFFFFF", fg = "#000000")
age_entry.grid(row = 2, column = 1, sticky = "w")

hobby_entry = Entry(frame, width = 30, bg = "#FFFFFF", fg = "#000000")
hobby_entry.grid(row = 3, column = 1, sticky = "w")

about_me = Text(frame, width = 23, height = 6, bg = "#FFFFFF", fg = "#000000")
about_me.grid(row = 4, column = 1, pady = 5)

def display():
    n = name_entry.get()
    a = age_entry.get()
    h = hobby_entry.get()
    am = about_me.get(1.0, END).strip()

    result.config(text = f"Hi {n}!\nYour age: {a}\nYour Hobby: {h}\nAbout you: {am}")

submit = Button(frame, text = "View My Personal Bio", command = display, bg = "#BD78D8", fg = "#000000")
submit.grid(row = 5, column = 0, columnspan = 2, pady = 15)

result = Label(window, text = "Your Bio will appear here.", bg = "#FFFFFF", fg = "#000000", wraplength = 300, justify = "left")
result.grid(row = 6, column = 0, columnspan = 2)

window.mainloop()