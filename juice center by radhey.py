from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
root=Tk()

root.geometry("800x600")
root.title("Radhey juice center")


class juice():
    def __init__(self,fruit_name,quantity):
        self.fruit_name=fruit_name
        self.quantity=quantity
        self.__cost=30
    
    def __calculate_cost(self):
        total_cost=self.quantity*self.__cost
        print("you need to pay : Rupees "+str(total_cost))
        if(self.fruit=="Apple"):
            calorie=52*self.quantity
        elif(self.fruit=="Mango"):
            calorie=60*self.quantity
        elif(self.fruit=="Orange"):
            calorie=47*self.quantity
            
        print("you are consuming "+str(calorie)+" for "+str(self.quantity)+" glasses of "+self.fruit_name+" juce")
            
    def get_cost(self):
        self.__calculate_cost()
        
def order_juce():
    fruit_name="Mango"
    quantity=3
    obj1=juice(fruit_name,quantity)
    obj1.get_cost()
    

        
root.mainloop()

