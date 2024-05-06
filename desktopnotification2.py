import customtkinter
import schedule
import time
from win10toast import ToastNotifier

toaster = ToastNotifier()

def notification(message):
    toaster.show_toast("Notification", message, duration=10)

def schedule_notification():
    message = entry1.get()
    day = entry2.get()
    time_str = entry3.get()

    if day.lower() == "monday":
        schedule.every().monday.at(time_str).do(notification, message)
    elif day.lower() == "sunday":
        schedule.every().sunday.at(time_str).do(notification, message)
    

    print(f"Notification set for {day} at {time_str}.")

def check_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

def login():
    schedule_notification()
    print("Notificaiton will appear at the time you set.")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("700x650")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Set a Notificaiton")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter the Notification")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter day")
entry2.pack(pady=12, padx=10)

entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter time(HH:MM)")
entry3.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Set", command=login)
button.pack(pady=12, padx=10)


import threading
threading.Thread(target=check_schedule).start()

root.mainloop()
