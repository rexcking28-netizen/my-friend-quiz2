import tkinter as tk
from tkinter import messagebox

questions = [
    "Wanna make a trip with me? 🌍✈️",
    "Will you always be my son? 🤗",
    "can you allow me to sex with your girlfriend or mom ? 💦 ",
    " you can fuck your mom when you are havasi" 
]

final_response = "You're the best! Love you tons! 💖"

class MyFuckingFriendApp:
    def __init__(self, root):
        self.root = root
        self.root.title("myfuckingfriend123.com")
        self.root.geometry("420x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f8ff")

        self.title_label = tk.Label(
            root,
            text="Hey my son! 💖",
            font=("Segoe UI", 20, "bold"),
            bg="#f0f8ff",
            fg="#333"
        )
        self.title_label.pack(pady=10)

        self.message_label = tk.Label(
            root,
            text="I just want to tell you something...\n\n"
                 "I love you a lot 💕\n\n"
                 "You're the best son I could ever ask for!",
            font=("Segoe UI", 12),
            bg="#f0f8ff",
            fg="#444",
            justify="center"
        )
        self.message_label.pack(pady=10)

        self.question_label = tk.Label(
            root,
            text=questions[0],
            font=("Segoe UI", 14, "bold"),
            bg="#f0f8ff",
            fg="#000"
        )
        self.question_label.pack(pady=20)

        # Buttons frame
        self.buttons_frame = tk.Frame(root, bg="#f0f8ff")
        self.buttons_frame.pack(pady=10)

        self.yes_button = tk.Button(
            self.buttons_frame,
            text="Yes 😄",
            font=("Segoe UI", 12),
            bg="#4CAF50",
            fg="white",
            width=20,
            command=self.yes_clicked
        )
        self.yes_button.grid(row=0, column=0, padx=10, pady=5)

        self.no_button = tk.Button(
            self.buttons_frame,
            text="No 🙁",
            font=("Segoe UI", 12),
            bg="#d3d3d3",
            fg="#999",
            width=20,
            state="disabled"
        )
        self.no_button.grid(row=1, column=0, padx=10, pady=5)

        self.fuckoff_button = tk.Button(
            self.buttons_frame,
            text="F*** Off 😤",
            font=("Segoe UI", 12),
            bg="#d3d3d3",
            fg="#999",
            width=20,
            state="disabled"
        )
        self.fuckoff_button.grid(row=2, column=0, padx=10, pady=5)

        self.current_question = 0

    def yes_clicked(self):
        if self.current_question < len(questions) - 1:
            self.current_question += 1
            self.question_label.config(text=questions[self.current_question])
        else:
            messagebox.showinfo("Love ❤️", final_response)
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = MyFuckingFriendApp(root)
    root.mainloop()
import tkinter as tk
from tkinter import messagebox

questions = [
    "Wanna make a trip with me? 🌍✈️",
    "Will you always be my son? 🤗",
    "can you allow me to sex with your girlfriend or mom ? 💦 ",
    " you can fuck your mom when you are havasi" 
]

final_response = "You're the best! Love you tons! 💖"

class MyFuckingFriendApp:
    def __init__(self, root):
        self.root = root
        self.root.title("myfuckingfriend123.com")
        self.root.geometry("420x420")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f8ff")

        self.title_label = tk.Label(
            root,
            text="Hey my son! 💖",
            font=("Segoe UI", 20, "bold"),
            bg="#f0f8ff",
            fg="#333"
        )
        self.title_label.pack(pady=10)

        self.message_label = tk.Label(
            root,
            text="I just want to tell you something...\n\n"
                 "I love you a lot 💕\n\n"
                 "You're the best son I could ever ask for!",
            font=("Segoe UI", 12),
            bg="#f0f8ff",
            fg="#444",
            justify="center"
        )
        self.message_label.pack(pady=10)

        self.question_label = tk.Label(
            root,
            text=questions[0],
            font=("Segoe UI", 14, "bold"),
            bg="#f0f8ff",
            fg="#000"
        )
        self.question_label.pack(pady=20)

        # Buttons frame
        self.buttons_frame = tk.Frame(root, bg="#f0f8ff")
        self.buttons_frame.pack(pady=10)

        self.yes_button = tk.Button(
            self.buttons_frame,
            text="Yes 😄",
            font=("Segoe UI", 12),
            bg="#4CAF50",
            fg="white",
            width=20,
            command=self.yes_clicked
        )
        self.yes_button.grid(row=0, column=0, padx=10, pady=5)

        self.no_button = tk.Button(
            self.buttons_frame,
            text="No 🙁",
            font=("Segoe UI", 12),
            bg="#d3d3d3",
            fg="#999",
            width=20,
            state="disabled"
        )
        self.no_button.grid(row=1, column=0, padx=10, pady=5)

        self.fuckoff_button = tk.Button(
            self.buttons_frame,
            text="F*** Off 😤",
            font=("Segoe UI", 12),
            bg="#d3d3d3",
            fg="#999",
            width=20,
            state="disabled"
        )
        self.fuckoff_button.grid(row=2, column=0, padx=10, pady=5)

        self.current_question = 0

    def yes_clicked(self):
        if self.current_question < len(questions) - 1:
            self.current_question += 1
            self.question_label.config(text=questions[self.current_question])
        else:
            messagebox.showinfo("Love ❤️", final_response)
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = MyFuckingFriendApp(root)
    root.mainloop()
