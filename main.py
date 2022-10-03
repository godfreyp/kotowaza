import tkinter as tk
import kotowaza as kw
import random

cache = []
length = int(kw.returnLength())

def callsaying():
    if len(cache) == length:
        l2.config(text = "You're finished!")
    else:
        randnum = random.choice([i for i in range(1, length + 1) if i not in cache])
        cache.append(randnum)
        saying = kw.returnSaying(randnum)
        l2.config(text = saying)
        l3.config(text = str(length - len(cache)) + " remaining idioms/sayings.")

window = tk.Tk()
window.geometry("900x600")
window.config(bg="#F39C12")
window.resizable(width=True,height=True)
window.title('Random Kotowaza Generator')
 
 
l1 = tk.Label(text="Random Kotowaza Generator",font=("Arial",20),bg="Black",fg="White")
b1 = tk.Button(text="Click for your next idiom/saying",font=("Arial",15),bg="#A3E4D7",command=callsaying)
l2 = tk.Label(bg="#F39C12",font=("Arial",40),text="", wraplength=800)
l3 = tk.Label(bg="#F39C12",font=("Arial",40),text="", wraplength=800, justify="center")
 
l1.place(x=300,y=20)
b1.place(x=300,y=70)
l2.place(x=50,y=110)
l3.place(x=50,y=500)
 
window.mainloop()