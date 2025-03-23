import tkinter as tk

#Function that counts factorial sums by users input in upper(first) text box
def factorials(N):
    faktor = 1
    skait = 0
    
    for x in range(1, N + 1):
        faktor *= x
        skait += faktor
    return skait

#Function that gets it, man
def get_input():
    INPUT = int(Input_window.get("1.0", "end-1c"))
    return INPUT
    
#Function that inserts answer in output window
def insert_input():
    Output_window.insert(tk.END, factorials(get_input()))



#Creates main window
root = tk.Tk()
#Winows name
root.title("Adding Factorials")
#Sets windows resolution
root.geometry("250x170")


#Label for Input window
Input_l = tk.Label(root, text = "Ievadiet skaitli")

#makes interactible text input in main window
Input_window = tk.Text(root, height = 1, width = 20, bg = "beige")

#Makes button for factorial sum function excecution
Excecute = tk.Button(root, activebackground = "blue", text = "Izreķināt",
                     height = 1, width = 15, command = lambda:insert_input())

#Second interactible window, but only for answer output
Output_window = tk.Text(root, height = 3, width = 20, bg = "light cyan")

#Makes text box visible in the windows
Input_l.pack()
Input_window.pack()
Excecute.pack()
Output_window.pack()

# Thing that is launching window, making my window interactible and shit
tk.mainloop()