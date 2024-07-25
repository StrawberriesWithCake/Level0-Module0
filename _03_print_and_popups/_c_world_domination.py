from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
# if __name__ == '__main__':

    # Make a new window variable, window = Tk()
tarp = Tk()
    # Hide the window using the window's .withdraw() method
tarp.withdraw()
    # 1. Ask the user if they know how to write code.
yes = simpledialog.askstring(title='Can you code? Take this POPUP quiz TODAY!', prompt="Can you write code fluently?")
if yes =="yes":
    messagebox.showinfo(title='ur kewl', message="RULE THE WORLD!!! ti is ur oisterr. P.S. no bad stuf tho")
    # 2. If they say "yes", tell them they will rule the world in a message box pop-up.
    # 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.
else:
    messagebox.showerror(title='Lame.', message="dude come on, dis was, like supposed to be ur finest momnet. Go take sum classs")

    # Run the window's .mainloop() method
