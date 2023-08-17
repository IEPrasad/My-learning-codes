import datetime
import time
import pygame
import tkinter as tk
from tkinter import simpledialog

# Initialize pygame
pygame.init()

# Define the time frames
time_frames = ["4:00 AM - 5:00 AM", "5:15 AM - 6:00 AM", "6:30 AM - 7:30 AM", "8:00 AM - 9:00 AM", "11:00 PM"]

# Define the tasks for each time frame
tasks = ["Wake up", "Work 1", "Work 2", "Work 3", "Sleep"]

# Define the alarm times for each time frame
alarm_times = ["4:00 AM", "5:15 AM", "6:30 AM", "8:00 AM", "11:00 PM"]

# Load the alarm sound file
pygame.mixer.music.load("alarm.mp3")

# Define a function to set the tasks and alarm times
def set_tasks():
    global tasks, alarm_times
    # Open a Tkinter window to get input from the user
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Set Tasks")
    
    # Create text boxes for each time frame
    text_boxes = []
    for i in range(len(time_frames)):
        tk.Label(root, text=time_frames[i]).grid(row=i, column=0)
        text_box = tk.Entry(root)
        text_box.insert(0, tasks[i])
        text_box.grid(row=i, column=1)
        text_boxes.append(text_box)
    
    # Create a button to save the input and close the window
    def save_input():
        global tasks, alarm_times
        tasks = [text_box.get() for text_box in text_boxes]
        alarm_times = []  # Clear the alarm_times list
        
        # Set the alarm times based on the user input
        for i in range(len(time_frames)):
            # Get the user input for the alarm time
            alarm_time_str = tk.simpledialog.askstring(title="Set Alarm Time", prompt=f"Set alarm time for {time_frames[i]} (HH:MM AM/PM): ")
            # Convert the user input to a datetime object
            alarm_time = datetime.datetime.strptime(alarm_time_str, "%I:%M %p")
            # Convert the datetime object back to a string in the format used in the rest of the program
            alarm_time_str = alarm_time.strftime("%I:%M %p")
            # Append the alarm time string to the alarm_times list
            alarm_times.append(alarm_time_str)
        
        root.destroy()
    tk.Button(root, text="Save", command=save_input).grid(row=len(time_frames), column=1)
    
    root.mainloop()

# Define a function to play the alarm sound
def play_alarm():
    pygame.mixer.music.play()
    time.sleep(5)  # wait for 5 seconds before stopping the alarm
    pygame.mixer.music.stop()  # stop the alarm sound

# Define a function to check for upcoming tasks and set alarms
def set_alarms():
    # Loop through each time frame and display the task and set an alarm
    for i in range(len(time_frames)):
        print("Time frame: ", time_frames[i])
        print("Task: ", tasks[i])
    
        # Set the alarm time
        alarm_time = datetime.datetime.strptime(alarm_times[i], "%I:%M %p")
    
        # Wait until the alarm time is reached and play an alarm sound
        while True:
            now = datetime.datetime.now().strftime("%I:%M %p")
            if now == alarm_times[i]:
                 play_alarm()
                 break
        
            time.sleep(1)  # check the current time every 1 second

# Define a function to display upcoming tasks
def display_tasks():
    # TODO: display upcoming tasks in the user interface
    pass

# Create a Tkinter window for the app
root = tk.Tk()
root.geometry("400x400")
root.title("Alarm and Schedule App")

# Create buttons to set tasks and display upcoming tasks
tk.Button(root, text="Set Tasks", command=set_tasks).pack()
tk.Button(root, text="Display Tasks", command=display_tasks).pack()

root.mainloop()
