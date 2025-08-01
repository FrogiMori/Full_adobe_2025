import tkinter as tk
import webbrowser

drive_link = "https://drive.google.com/drive/folders/1wbScxJR9f9fQaknLFi6Q3-2jyWg7jwPt"

def open_link():
    webbrowser.open(drive_link)

root = tk.Tk()
root.title("Mở Google Drive")
root.geometry("300x150")

label = tk.Label(root, text="Nhấn nút để mở thư mục Google Drive", wraplength=250)
label.pack(pady=20)

button = tk.Button(root, text="Mở Drive", command=open_link, bg="green", fg="white", padx=10, pady=5)
button.pack()

root.mainloop()
