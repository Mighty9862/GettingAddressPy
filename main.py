import customtkinter
import tkinter
from geopy.geocoders import Nominatim #Подключаем библиотеку

customtkinter.set_appearance_mode("light")



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('Координаты адреса')
        self.geometry('600x600')

        customtkinter.CTkLabel(self, text='Введите адрес: ').place(x=70, y=410)
        self.entry_count = customtkinter.CTkEntry(self, width=300)
        self.entry_count.place(x=190, y=410)


        self.btn_clear = customtkinter.CTkButton(self, text='Очистить', command=self.clear)
        self.btn_clear.place(x=350, y=520)

        self.btn_generate = customtkinter.CTkButton(self, text='Найти', command=self.generate)
        self.btn_generate.place(x=150, y=520)

        self.text_field = customtkinter.CTkTextbox(self, width=560, height=300)
        self.text_field.place(x=20, y=30)




    def generate(self):
        # Geocoding code
        self.geolocator = Nominatim(user_agent="Tester")
        self.address = self.entry_count.get()
        self.location = self.geolocator.geocode(self.address)
        if self.location:
            self.text_field.insert(tkinter.END, str(self.location) + '\n')
            self.text_field.insert(tkinter.END, str(self.location.latitude) + ', ' + str(self.location.longitude) + '\n')
            self.text_field.insert(tkinter.END, "-" * 80 + '\n')
        else:
            self.text_field.insert(tkinter.END, "Адрес не найден\n")
            self.text_field.insert(tkinter.END, "-" * 80 + '\n')

    def clear(self):
        self.text_field.delete(0.0, tkinter.END)

        
    
    def clear(self):
        self.text_field.delete(0.0, tkinter.END)
    


app = App()
app.mainloop()