from tkinter import * #tkinterdaki her şeyi ekledik. Bazı özellikle kısayol olarak eklendi

window = Tk() #tkinter.Tk() yerine böyle kısaca yazdık üstteki tüm importları alarak.
window.title("Tkinter Python")
window.minsize(width=600,height=600)
window.config(padx=20,pady=20) #Görünümler arası boşluk bırakır

#label
my_label = Label(text="my label")
my_label.config(bg="black")
my_label.config(fg="white")
my_label.config(padx=10, pady=10)
my_label.pack()

#button
def button_clicked():
    print("button clicked")
    print(my_text.get("1.0",END))
    #"1.0",END --> 1 -> line , 0-> character , END -> Sonuna kadar git

my_button = Button(text="button", command=button_clicked)
my_button.config(padx=10, pady=10)
my_button.pack()

#entry --> singleline
my_entry = Entry(width=20)
my_entry.focus() #program açıldığında buradan başlar mouse
my_entry.pack()

#text --> multiline
my_text = Text(width=30,height=5)
#my_text.focus()
my_text.pack()

#scale
def scale_selected(value):
    print(value)
    # scale ile çağırdığımız için bu formatta yaptık .get ile hata veriyor.

my_scale = Scale(from_=0, to=50, command=scale_selected)
my_scale.pack()

#spinbox
def spinbox_selected():
    print(my_spinbox.get()) #Aynı buton gibi her tıkladığımda değerini getirebilirim.

my_spinbox = Spinbox(from_=0, to=50,command=spinbox_selected)
my_spinbox.pack()

#check button
def checkbutton_selected():
    print(check_state.get())

check_state = IntVar() #seçildiyse 1 seçilmediyse 0
my_checkbutton = Checkbutton(text="check",variable=check_state,command=checkbutton_selected)
my_checkbutton.pack()

#radio button

def radio_selected():
    print(radio_checked_state.get())

radio_checked_state = IntVar()
my_radio_button = Radiobutton(text="1. option", value=10, variable=radio_checked_state,command=radio_selected)
my_radio_button2 = Radiobutton(text="2. option", value=20, variable=radio_checked_state,command=radio_selected)
my_radio_button.pack()
my_radio_button2.pack()

#list box
def listbox_selected(event): #eventi yazmak zorundayız
    print(my_listbox.get(my_listbox.curselection())) #curseselection gerekli listbox için

my_listbox = Listbox()
name_list = ["Atil","ABC","KJF","SKDDfk","KJSFkida"]
for i in range(len(name_list)):
    my_listbox.insert(i,name_list[i])

my_listbox.bind('<<ListboxSelect>>',listbox_selected) #.bind ve bu format ile fonk çağırdık
my_listbox.pack()





window.mainloop()





