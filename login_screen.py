import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    user_name = entry_one.get()
    password = entry_two.get()
    if user_name == "user1" and password == "1234":
        message_label.configure(text = "Login Complete", text_color = "green")
    else:
        message_label.configure(text = "Login Failed", text_color = "red")
    
frame_one = customtkinter.CTkFrame(master = root)
frame_one.pack(pady = 20, padx = 20, fill = "both", expand = True)

label = customtkinter.CTkLabel(master = frame_one, text = "Login Portal")
label.pack(pady = 12, padx = 10)

entry_one = customtkinter.CTkEntry(master = frame_one, placeholder_text = "Username")
entry_one.pack(pady = 12, padx = 10)
entry_two = customtkinter.CTkEntry(master = frame_one, placeholder_text = "Password")
entry_two.pack(pady = 12, padx = 10)

button = customtkinter.CTkButton(master = frame_one, text = "Login", command = login)
button.pack(pady = 12, padx = 10)

message_label = customtkinter.CTkLabel(master = frame_one, text = "")
message_label.pack(pady = 12, padx = 10)

root.mainloop()
    