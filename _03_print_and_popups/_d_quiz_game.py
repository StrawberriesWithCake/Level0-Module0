from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    seed = Tk()
    # Hide the window using the window's .withdraw() method
    seed.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    s = 0
    # ASK A QUESTION AND CHECK THE ANSWER
    q1 = simpledialog.askstring(title='Are YOU smarter than a fifth grader?', prompt="What is the capitol of Argentina?")
    if q1 == "Buenos Aires":
        s +=1
    q2 = simpledialog.askstring(title='Are YOU smarter than a fifth grader?', prompt="What is the process which plants use to turn sunlight into energy.")
    if q2 == "Photosynthesis":
        s +=1

    q4 = simpledialog.askstring(title='Are YOU smarter than a fifth grader?', prompt="What is the square root of 625?")
    if q4 == "25" or "Twenty-Five" or "twenty-five":
        s +=1
    q5 = simpledialog.askstring(title='Are YOU smarter than a fifth grader?', prompt="How did Napoleon Bonaparte pass away?")
    if q5 == "Stomach Ulcer":
        s +=1
    #      // 2.  Ask the user a question 

    #      // 3.  Use an if statement to check if their answer is correct

    #      // 4.  if the user's answer was correct, add one to their score 
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    print(s)
    # Run the window's .mainloop() method
    seed.mainloop()
