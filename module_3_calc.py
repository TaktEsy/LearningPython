import tkinter as tk

# Окно программы
window = tk.Tk()
window.title('Калькулятор')
window.geometry("350x350")
window.resizable(width=False, height=False)

# Кнопки
button_add = tk.Button(window, text="+", width=2, height=2)
button_add.place(x=100, y=200)

button_sub = tk.Button(window, text="-", width=2, height=2)
button_sub.place(x=150, y=200)

button_mul = tk.Button(window, text="*", width=2, height=2)
button_mul.place(x=200, y=200)

button_div = tk.Button(window, text="/", width=2, height=2)
button_div.place(x=250, y=200)

# Поля ввода/вывода
num1_entry = tk.Entry(window, width=28)
num1_entry.place(x=100, y=75)

num2_entry = tk.Entry(window, width=28)
num2_entry.place(x=100, y=150)

answer = tk.Entry(window, width=28)
answer.place(x=100, y=300)

# Надписи
num1 = tk.Label(window, text="Число 1")
num1.place(x=100, y=50)
window.mainloop()
