from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    jeremy = Tk()
    # Hide the window using the window's .withdraw() method
    jeremy.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    meep = random.randint(0, 3)
    # 2. Print your variable to the console
    print(meep)
    # 3. Get the user to enter something that they think is awesome
    simpledialog.askstring(title=':D', prompt="name something you think is awesome")
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    if meep == 0:
        messagebox.showinfo(title='cool', message="That's very nice!")

    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    if meep == 1:
        messagebox.showinfo(title='ToT', message="Alright. You are brave, and you do you.")
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    if meep == 2:
        messagebox.showinfo(title='..Ok :l', message="Based on this response I say that YOU are boring as a rock.")
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
    if meep == 3:
        messagebox.showinfo(title='C:', message="That is sooo unprofessional and unethhicull.")
    # Run the window's .mainloop() method
    jeremy.mainloop()
