import tkinter

#window
window = tkinter.Tk() #Ekranımızı Oluşturduk
window.title("Python Tkinter")
window.minsize(width=450,height=300) #Window ilk çıkan ekranda minimum size ayarlama

def click_button():
    user_input =  my_entry.get()
    print(user_input)

#label
my_label = tkinter.Label(text="This is a label", font=('Arial', 30, "bold"))
#my_label.config(bg="white", fg="black") #Label özelliklerini istersek değiştirebiliriz.
#my_label.pack(side='left') #Labelımızın ekrandaki yerini belirlemek.
#my_label.place(x=0,y=0) #Labelımızın spesifik konumu
my_label.grid(row=0,column=0) #Bizim için sanal row ve columnlar oluşturuyor.


#button
my_button = tkinter.Button(text="This is a Button",command=click_button)
#my_button.pack(side="left")
#my_button.place(x=225-63,y=150-14)

#my_button.update() #Butonumuzun height ve width değerleri için kullanmak gerekli.
#print(my_button.winfo_height())
#print(my_button.winfo_width())

my_button.grid(row=1,column=1)

#entry
my_entry = tkinter.Entry(width=20,)
#my_entry.pack(side="bottom")
#my_entry.place(x=220,y=220)
my_entry.grid(row=0,column=2)

window.mainloop()