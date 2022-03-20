import tkinter
import tkinter.messagebox

class Pizza:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('400x150')
        self.main_window.configure(bg= 'red')
        self.name_frame = tkinter.Frame(self.main_window)
        self.toppings_frame = tkinter.Frame(self.main_window)
        self.crust_frame = tkinter.Frame(self.main_window)
        self.buttons_frame = tkinter.Frame(self.main_window)
        self.message_frame = tkinter.Frame(self.main_window)

## input box can be used to record the name of the person placing the order

        self.name_label = tkinter.Label(self.name_frame, text = 'Enter a name for the order: ')
        self.name_entry = tkinter.Entry(self.name_frame, width = 30)
        self.name_label.pack(side = 'left')
        self.name_entry.pack(side = 'left')

## check boxes for toppings (each with different cost)

        self.cheese_var = tkinter.IntVar()
        self.peppers_var = tkinter.IntVar()
        self.mushroom_var = tkinter.IntVar()
        self.tomato_var = tkinter.IntVar()
        self.sausage_var = tkinter.IntVar()
        self.pineapple_var = tkinter.IntVar()

        self.cheese_var.set(0)
        self.peppers_var.set(0)
        self.mushroom_var.set(0)
        self.tomato_var.set(0)
        self.sausage_var.set(0)
        self.pineapple_var.set(0)

        self.cheese =tkinter.Checkbutton(self.toppings_frame, text = "Cheese",variable = self.cheese_var)
        self.pepper =tkinter.Checkbutton(self.toppings_frame, text = "Peppers",variable = self.peppers_var)
        self.mushroom =tkinter.Checkbutton(self.toppings_frame, text = "Mushroom",variable = self.mushroom_var)
        self.tomato =tkinter.Checkbutton(self.toppings_frame, text = "Tomato",variable = self.tomato_var)
        self.sausage =tkinter.Checkbutton(self.toppings_frame, text = "Sausage",variable = self.sausage_var)
        self.pineapple =tkinter.Checkbutton(self.toppings_frame, text = "Pineapple",variable = self.pineapple_var)


        self.cheese.pack()
        self.pepper.pack()
        self.mushroom.pack()
        self.tomato.pack()
        self.sausage.pack()
        self.pineapple.pack()

## radio buttons for the type of crust selected (each with a different cost)
        self.crust_radio = tkinter.IntVar()
        
        self.thin_crust = tkinter.Radiobutton(self.crust_frame, text = "Thin Crsut", variable= self.crust_radio, value = 10)
        self.standard_crust =  tkinter.Radiobutton(self.crust_frame, text = "Standard Crsut", variable= self.crust_radio, value = 5)
        self.thick_crust =  tkinter.Radiobutton(self.crust_frame, text = "Thick Crsut", variable= self.crust_radio, value = 15)
        self.cheese_crust =  tkinter.Radiobutton(self.crust_frame, text = "Cheesy Crsut", variable= self.crust_radio, value = 20)

        self.thin_crust.pack()
        self.standard_crust.pack()
        self.thick_crust.pack()
        self.cheese_crust.pack()

## buttons for calculation and quit

        self.calculte_button = tkinter.Button(self.buttons_frame, text = 'Calculate Price', bg='white', fg = 'black', command = self.calculate)
        self.quit_button= tkinter.Button(self.buttons_frame, text = "Quit", bg='white', fg = 'black', command = self.main_window.destroy)

        self.calculte_button.pack(side = 'left')
        self.quit_button.pack(side = 'right')

## message box to display the total cost of the pizza along with the name of the person placing the order


## packing frames 
        self.name_frame.pack('top')
        self.toppings_frame.pack('top')
        self.crust_frame.pack('top')
        self.buttons_frame.pack('top')
        self.message_frame.pack('top')




        tkinter.mainloop()
## message box to display the total cost of the pizza along with the name of the person placing the order
## def any methods 

    def calculate(self):
        tkinter.messagebox.showinfo('Name for order'+ self.name_entry.get())


## create instance of case 
my_GUI = Pizza()