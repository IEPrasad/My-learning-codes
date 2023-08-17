import tkinter as tk
from datetime import datetime


class Timer:
    def __init__(self, master):
        self.master = master
        master.title("Time Tracker")

        # Create a label for the current time
        self.time_label = tk.Label(master, font=("Garamond Bold", 22))
        self.time_label.pack(pady=20)

        # Create a label for the work log
        self.work_label = tk.Label(master, text="TODAY MY WORKS!", font=("Sans Bold", 22))
        self.work_label.pack()

        # Create a text widget for the work log
        self.work_text = tk.Text(master, height=25, width=34)
        self.work_text.pack()

        # Create a start/stop button
        self.start_stop_button = tk.Button(master, text="Start", font=("Sans Bold", 15), command=self.start_stop)
        self.start_stop_button.pack(pady=20)

        # Create a reset button
        self.reset_button = tk.Button(master, text="Reset", font=("Sans Bold", 15), command=self.reset)
        self.reset_button.pack()

        # Initialize the timer
        self.timer_running = False
        self.start_time = None
        self.elapsed_time = 0
        self.update_time()

    def update_time(self):
        """Update the current time label."""
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_label.configure(text=current_time)
        if self.timer_running:
            self.elapsed_time += 1
        self.master.after(1000, self.update_time)

    def start_stop(self):
        """Start or stop the timer."""
        if  self.timer_running:
            self.timer_running = False
            self.start_stop_button.configure(text="START NOW")
            self.log_work()
        else:
            self.timer_running = True
            self.start_stop_button.configure(text="STOP")
            self.start_time = datetime.now()
            self.elapsed_time = 0

    def reset(self):
        """Reset the timer and work log."""
        self.timer_running = False
        self.start_stop_button.configure(text="START")
        self.start_time = None
        self.elapsed_time = 0
        self.work_text.delete("1.0", "END")

    def log_work(self):
        """Log the work time to the text widget."""
        if self.start_time is not None:
            work_time = self.elapsed_time
            start_time_str = self.start_time.strftime('%Y-%m-%d (%H:%M:%S')
            end_time_str = datetime.now().strftime('%H:%M:%S)')
            work_title = "Work Title : "  # Replace this with the actual work title
            work = f"\n{start_time_str} - {end_time_str}\n{work_title}\nWorked Time: {work_time // 60} min {work_time % 60} sec\n"
            self.work_text.insert("end", work)

            # Tag the work title in blue and the worked time in red
            self.work_text.tag_add("work_title", f"{self.work_text.index('end-2l')}--1c", "end-1c")
            self.work_text.tag_add("worked_time", "end-3l", "end-1c")
            self.work_text.tag_config("work_title", foreground="black")
            self.work_text.tag_config("worked_time", foreground="darkblue")


root = tk.Tk()
timer = Timer(root)
root.mainloop()
