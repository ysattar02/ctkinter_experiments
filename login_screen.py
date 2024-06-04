import customtkinter
import requests 
import json 
import time

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.title("Login App")

def get_weather_info(zipcode):
    running = True
    while running:
        base_url = 'http://api.openweathermap.org/data/2.5/weather?q='
        api_key = '55592219da64379c5a1872dccb250590'
        city_name = ""
        complete_url = f'{base_url}{city_name},{zipcode}&appid={api_key}'
        print(complete_url)
        try:
            response = requests.get(complete_url)
            response.raise_for_status()
            w_data = response.json()
            temp = w_data['main']['temp']
            print(temp)
            running = False
            return temp
        except ConnectionError:
            print("Connection Failed")
            return None
            running = False
            

def login():
    user_name = entry_username.get()
    password = entry_password.get()
    if user_name == "user1" and password == "1234":
        message_label.configure(text = "Login Complete", text_color = "green")
        root.after(1000, weather_frame(user_name))
    else:
        message_label.configure(text = "Login Failed", text_color = "red")
    entry_username.delete(0, 'end')
    entry_password.delete(0, 'end')

def weather_frame(user_name):
    frame_two = customtkinter.CTkToplevel(root)
    frame_two.geometry("500x300")
    frame_two.title("Weather App")
    
    label = customtkinter.CTkLabel(master = frame_two, text = f"Welcome {user_name}")
    label.pack(pady = 12, padx = 10)
    
    entry_zipcode = customtkinter.CTkEntry(master = frame_two, placeholder_text = "Zipcode")
    entry_zipcode.pack(pady = 12, padx = 10)
    
    weather_label = customtkinter.CTkLabel(master = frame_two, text = "---")
    weather_label.pack(pady = 12, padx = 10)
    
    def get_weather_lambda():
        zipcode = entry_zipcode.get()
        temp = get_weather_info(zipcode)
        temp = round((temp - 273.15) * (9/5) + 32, 2)
        if temp is not None:
            weather_label.configure(text = f"Temp: {temp}C")
        else:
            weather_label.configure(text = "Failed")
        
    get_weather_button = customtkinter.CTkButton(master = frame_two, text = "Get Weather", command = get_weather_lambda)
    get_weather_button.pack(pady = 12, padx = 10)
    logout_button = customtkinter.CTkButton(master = frame_two, text = "Logout", command = frame_two.destroy)
    logout_button.pack(pady = 12, padx = 10)
    
frame_one = customtkinter.CTkFrame(master = root)
frame_one.pack(pady = 20, padx = 20, fill = "both", expand = True)

label = customtkinter.CTkLabel(master = frame_one, text = "Login Portal")
label.pack(pady = 12, padx = 10)

entry_username = customtkinter.CTkEntry(master = frame_one, placeholder_text = "Username")
entry_username.pack(pady = 12, padx = 10)
entry_password = customtkinter.CTkEntry(master = frame_one, placeholder_text = "Password")
entry_password.pack(pady = 12, padx = 10)

button = customtkinter.CTkButton(master = frame_one, text = "Login", command = login)
button.pack(pady = 12, padx = 10)

message_label = customtkinter.CTkLabel(master = frame_one, text = "")
message_label.pack(pady = 12, padx = 10)

root.mainloop()
    