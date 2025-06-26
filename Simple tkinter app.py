import tkinter as tk

root = tk.Tk()
root.title("Simple tkinter App")
root.geometry("200x100")

def say_hello():
    print("hello World!")
    print("Good Bye")

hello_button = tk.Button(root, text="Click Me", command=say_hello)
hello_button.pack(pady=20)

root.mainloop()
