#Name - Nadir Shaikh
#UIN - 251P)86
print("Nadir Shaikh")
print("251P086")

import tkinter as tk

def btnHandler():
     try:
        value = float(inputValue.get())
        choice = option.get()
        if choice == "Celsius to Fahrenheit":
            result = (value *9/5)+32
            output.config(text="Result: " + str(result) + "°F")

        elif choice == "Rupees to Dollars":
            result = value / 94
            output.config(text="Result: $" + str(round(result,2)))
        elif choice == "Inches to Feet":
            result = value / 32
            output.config(text="Result: " + str (result) + "ft")

     except:
         output.config(text="Enter valid number!")


root = tk.Tk()
root.title("Unit Converter App")
root.geometry("700x500")

tk.Label(root,text = "Enter Value").pack()
inputValue = tk.Entry(root)
inputValue.pack()
option = tk.StringVar()
option.set("Celsius to Fahrenheit")
menu = tk.OptionMenu(root,option,
                     "Celsius to Fahrenheit",
                     "Rupees to Dollars",
                     "Inches to Feet")
menu.pack(pady=10)
tk.Button(root, text ="Convert", command=btnHandler).pack(pady=10)
output = tk.Label(root, text="Result will appear here")
output.pack(pady=10)
root.mainloop()