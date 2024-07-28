
import tkinter as tk
from tkinter import ttk, PhotoImage, scrolledtext
import random
import string
import pyautogui

def generar_func():
    tam = tam_variable.get()
    caja_contra.delete('1.0', tk.END)
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    chars = lower + upper + num + symbols
    temp = random.sample(chars, tam)
    generated_password = "".join(temp)
    
    caja_contra.insert(tk.END, generated_password)
   
    ventana.clipboard_clear() 
    ventana.clipboard_append(generated_password)
    
    pyautogui.alert(text="Generated password copied to clipboard.", title="Password generator")

ventana = tk.Tk()
ventana.title("Password Generator")

# Set window size and prevent resizing
ventana.geometry("400x300")
ventana.resizable(width=False, height=False)

# Load window icon if available
try:
    logo = PhotoImage(file="icons/icono.png")
    ventana.iconphoto(False, logo)
except tk.TclError:
    pass  # Handle error if icon file is missing or not found

# Entry for password length
tam_variable = tk.IntVar()
tam_entry = ttk.Entry(ventana, textvariable=tam_variable, justify="center")
tam_entry.place(relx=0.3, rely=0.1)

# Button to generate password
generar_button = ttk.Button(ventana, text='Generate Password', command=generar_func)
generar_button.place(relx=0.35, rely=0.25)

# ScrolledText widget to display generated password
caja_contra = scrolledtext.ScrolledText(ventana, width=40, height=10)
caja_contra.place(relx=0.2, rely=0.4)

if __name__ == "__main__":
    ventana.mainloop()
