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
    q2 = simpledialog.askstring(title='Are YOU smarter than a fifth grader?', prompt="What organelle do plant cells have that animal cells do not?")
    if q2 == "Chloroplast" or "chloroplast":
        s +=1
    q3 = simpledialog.askstring(title='Are YOU smarter than a fifth grader?', prompt="When did the war of 1812 happen?")
    if q3 == "1812" or "Eighteen-Twelve" or "eighteen-twelve" or "eighteen twelve":
        s +=1
    q4 = simpledialog.askstring(title='Are YOU smarter than a fifth grader?', prompt="What is the square root of 625?")
    if q4 == "25" or "Twenty-Five" or "twenty-five":
        s +=1
    q5 = simpledialog.askstring(title='Are YOU smarter than a fifth grader?', prompt="What is the plural form of the noun 'goose'?")
    if q5 == "geese" or "Geese":
        s +=1
    q6 = simpledialog.askstring(title='Are YOU smarter than a fifth grader?', prompt="Name one of the top 5 most popular ice cream flavors")
    if q6 == "Vanilla" or "vanilla" or "chocolate" or "Chocolate" or "strawberry" or "Strawberry" or "Butter-Pecan" or "butter-pecan" or "butter pecan" or "Butter Pecan" or "Cookie Dough" or "cookie dough" or "cookie-dough" or "Cookie-dough":
        s +=1
    #      // 2.  Ask the user a question 

    #      // 3.  Use an if statement to check if their answer is correct

    #      // 4.  if the user's answer was correct, add one to their score 
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    print(s.__str__())
    # Run the window's .mainloop() method
    seed.mainloop()
