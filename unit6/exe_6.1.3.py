from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import os


def photo():
    root = tk.Tk()
    root.title("unit 6")

    # Create a line above the question
    line_label = tk.Label(root, text="", pady=10)
    line_label.pack()

    label = tk.Label(root, text="What is my favorite movie?", font=("Varela Round", 16))
    label.pack()

    # Create a line above the button
    line_label = tk.Label(root, text="", pady=10)
    line_label.pack()

    button = tk.Button(root, text="Show Answer", command=show_answer, font=("Varela Round", 16), padx=10, pady=5)
    button.pack()
    root.geometry("400x300")  # Set the desired width and height for the window

    # Calculate the x and y coordinates for centering the window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - 952) // 2  # Adjust the value based on the desired width
    y = (screen_height - 600) // 2  # Adjust the value based on the desired height

    # Set the window geometry to center the window
    root.geometry(f"952x600+{x}+{y}")  # Set the desired width, height, and coordinates for the window
    root.mainloop()


def show_answer():
    current_dir = os.getcwd()
    image_path = os.path.join(current_dir, "shrek.jpg")
    answer_image = Image.open(image_path)
    render = ImageTk.PhotoImage(answer_image)
    label = tk.Label(image=render)
    label.image = render
    label.pack(side="bottom")


def main():
    photo()


if __name__ == '__main__':
    main()

