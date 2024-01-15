import tkinter as tk
from PIL import ImageTk

root=tk.Tk()

def f1_submit():
    # Hide the current page
    current_page.pack_forget()

    # Show the new page
    page2.pack()

def add():

    page2.pack_forget()

    page3.pack()
    date=date_txt.get()
    name=name_txt.get()
    amount=amount_txt.get()
    split=split_txt.get()
    notes=note_txt.get()
    share=int(amount)//int(split)

    p1=tk.Label(page3, text=f"Date:{date} \nPayee Name: {name}\nTotal Amount Spent: {amount}\nNo of shares: {split}\nNotes: {notes}\n\nPER HEAD SHARE: {share}", font="Arial 15", bg="GREY", fg="black")
    p1.pack(pady=1)
    
      
#title
root.title("Expense Tracker")
root.geometry("500x600")
root.configure(background="black")

#frame 
f1=tk.Frame(root,width=500,height=530, bg="black")


#logo and page1
logo=ImageTk.PhotoImage(file="D:\\Personal\\Coderscave Intern\\ExpensesTracking\\logoo.png")
logo_wid=tk. Label(f1, image=logo)
logo_wid.pack()


#page2
page2=tk.Frame(root, bg="black")
title1=tk.Label(page2, text="EXPENSE TRACKER", font="Arial 20", bg="black", fg="White")
title1.pack(pady=50)

#details
date=tk.Label(page2, text="DATE", bg="black", fg="White", font="Arial 12")
date.pack(pady=1)
date_txt=tk.Entry(page2)
date_txt.pack(pady=1)

name=tk.Label(page2, text="PERSON PAID", bg="black", fg="White", font="Arial 12")
name.pack(pady=10)
name_txt=tk.Entry(page2)
name_txt.pack(pady=1)

amount=tk.Label(page2, text="AMOUNT SPENT", bg="black", fg="White", font="Arial 12")
amount.pack(pady=10)
amount_txt=tk.Entry(page2)
amount_txt.pack(pady=1)

spilt=tk.Label(page2, text="SPLIT", bg="black", fg="White", font="Arial 12")
spilt.pack(pady=10)
split_txt=tk.Entry(page2)
split_txt.pack(pady=1)

note=tk.Label(page2, text="NOTES", bg="black", fg="White", font="Arial 12")
note.pack(pady=10)
note_txt=tk.Entry(page2)
note_txt.pack(pady=1)

#page3
page3=tk.Frame(root, width=300, height=300, bg="black")
title2=tk.Label(page3, text="EXPENSE TRACKER", font="Arial 25", bg="black", fg="White")
title2.pack(pady=50)


current_page = f1
current_page.pack()


# Button to switch to the new page
Open_but=tk.Button(f1, text="OPEN APP", command=f1_submit, bg="green")
Open_but.pack(pady=10)


#buttonss
add_button=tk.Button(page2, text="Add item", command=add, bg="green")
add_button.pack(pady=5, padx=1)
#clear_but=tk.Button(page2, text="Clear")
#clear_but.pack()
page2.pack()


root.mainloop()