#screenshot using python #nxtechs task 
import tkinter as tk
import pyautogui

screenshot_counter = 1  

def take_screenshot():
    global screenshot_counter
    screenshot = pyautogui.screenshot()
    file_path = f"C:/Users/Rama Krishna/Pictures/Screenshots/screenshot_{screenshot_counter}.png"
    screenshot.save(file_path)
    screenshot_counter += 1

def close_window():
    root.destroy()

root = tk.Tk()
root.title("Screenshot Tool")

screenshot_button = tk.Button(root, text="Take Screenshot", command=take_screenshot)
screenshot_button.pack(pady=10)

close_button = tk.Button(root, text="Close", command=close_window)
close_button.pack()

root.mainloop()

#lets see the output 
#thank you
