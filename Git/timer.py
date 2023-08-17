import tkinter as tk
import time

class TimeTableApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MY WORK TIMER")
        self.geometry("300x150")
        
        self.timer_running = False
        self.start_time = None
        self.total_time = 0
        
        self.time_label = tk.Label(self, font=("Helvetica", 50))
        self.time_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        self.start_button = tk.Button(self, text="Start", command=self.start_timer)
        self.start_button.grid(row=1, column=0, padx=10, pady=5)
        
        self.pause_button = tk.Button(self, text="Pause", command=self.pause_timer)
        self.pause_button.grid(row=1, column=1, padx=10, pady=5)
        self.pause_button.configure(state="disabled")
        
        self.reset_button = tk.Button(self, text="Reset", command=self.reset_timer)
        self.reset_button.grid(row=1, column=2, padx=10, pady=5)
        
        self.work_button = tk.Button(self, text="Work", command=self.record_work_time)
        self.work_button.grid(row=2, column=0, columnspan=3, padx=10, pady=5)
        self.work_button.configure(state="disabled")
        
        self.reminder_button = tk.Button(self, text="Set Reminder", command=self.set_reminder)
        self.reminder_button.grid(row=3, column=0, columnspan=3, padx=10, pady=5)
        
        self.mainloop()
        
    def start_timer(self):
        self.timer_running = True
        self.start_time = time.time()
        self.update_timer()
        self.start_button.configure(state="disabled")
        self.pause_button.configure(state="normal")
        self.work_button.configure(state="normal")
        
    def pause_timer(self):
        self.timer_running = False
        self.total_time += time.time() - self.start_time
        self.start_button.configure(state="normal")
        self.pause_button.configure(state="disabled")
        self.work_button.configure(state="disabled")
        
    def reset_timer(self):
        self.timer_running = False
        self.total_time = 0
        self.start_time = None
        self.time_label.configure(text="00:00:00")
        self.start_button.configure(state="normal")
        self.pause_button.configure(state="disabled")
        self.work_button.configure(state="disabled")
        
    def update_timer(self):
        if self.timer_running:
            elapsed_time = time.time() - self.start_time + self.total_time
            elapsed_hours = int(elapsed_time / 3600)
            elapsed_minutes = int((elapsed_time % 3600) / 60)
            elapsed_seconds = int(elapsed_time % 60)
            self.time_label.configure(text=f"{elapsed_hours:02}:{elapsed_minutes:02}:{elapsed_seconds:02}")
            self.after(1000, self.update_timer)
        
    def record_work_time(self):
        with open("work_time.txt", "a") as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}: {self.time_label.cget('text')}\n")
        
    def set_reminder(self):
        # Add code here to open a dialog to set a reminder
        pass

if __name__ == "__main__":
    app = TimeTableApp()
