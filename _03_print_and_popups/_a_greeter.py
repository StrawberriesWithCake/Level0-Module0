from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block 
if __name__ == '__main__':
    
    # Make a new window variable, window = Tk()
    pop = Tk()
    # Hide the window using the window's .withdraw() method
    pop.withdraw()
    # Ask the user for their name and save it to a variable
    # name = simpledialog.askstring(title='Greeter', prompt="What is your name?")
    simpledialog.askstring(title='Back by unpopular demand...ME!', prompt="Hi there! I'm the weird virus you are not currently aware of in your computer. What's your name?")
    # Show a message box with your message using the .showinfo() method
    messagebox.showinfo(title='Meh.', message="It could be better.")

    # Print your message to the console using the print() function
    print("I'm joking. But I mean, I feel real sorry for you. Come on, who names their kid that? Might as well name them Burkle.")
    # Show an error message using messagebox.showerror()
    messagebox.showerror()
    # Run the window's .mainloop() method
    pop.mainloop()
pass
