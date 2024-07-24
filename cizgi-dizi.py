import tkinter as tk
from tkinter import messagebox

# Çizgi dizi veri tabanı sistemi
cartoon_database = [
    {"name": "Adventure Time", "genre": "Adventure", "network": "Cartoon Network", "year": 2010, "target_age": "10+"},
    {"name": "The Amazing World of Gumball", "genre": "Comedy", "network": "Cartoon Network", "year": 2011, "target_age": "7-12"},
    {"name": "Regular Show", "genre": "Comedy", "network": "Cartoon Network", "year": 2010, "target_age": "12+"},
    {"name": "DuckTales", "genre": "Adventure", "network": "Disney", "year": 2017, "target_age": "7-12"},
    {"name": "Kim Possible", "genre": "Action", "network": "Disney", "year": 2002, "target_age": "10+"},
    #!eklemek istediğiniz çizgi diziler olursa buraya ekleye bilirsiniz
]

def get_cartoon_recommendations(user_preferences):
    recommended_cartoons = []
    for cartoon in cartoon_database:
        match = True
        for key, value in user_preferences.items():
            if value and cartoon.get(key) != value:
                match = False
                break
        if match:
            recommended_cartoons.append(cartoon)
    return recommended_cartoons

def show_recommendations():
    genre = genre_var.get()
    network = network_var.get()
    target_age = age_var.get()

    user_preferences = {
        "genre": genre if genre != "Seçin" else None,
        "network": network if network != "Seçin" else None,
        "target_age": target_age if target_age != "Seçin" else None
    }
    
    recommendations = get_cartoon_recommendations(user_preferences)

    if not recommendations:
        messagebox.showinfo("Sonuç", "Bu kriterlere uygun çizgi dizi bulunamadı.")
    else:
        result = "Tavsiyeler:\n"
        for cartoon in recommendations:
            result += f"- {cartoon['name']} ({cartoon['year']}) - {cartoon['genre']} - {cartoon['network']} - {cartoon['target_age']}\n"
        messagebox.showinfo("Sonuç", result)

# Tkinter penceresi oluşturma
root = tk.Tk()
root.title("Çizgi Dizi Tavsiye Sistemi")

# Tür seçenekleri
tk.Label(root, text="Tür:").grid(row=0, column=0)
genre_var = tk.StringVar(value="Seçin")
genre_options = ["Seçin", "Adventure", "Comedy", "Action"]
genre_menu = tk.OptionMenu(root, genre_var, *genre_options)
genre_menu.grid(row=0, column=1)

# Kanal seçenekleri
tk.Label(root, text="Kanal:").grid(row=1, column=0)
network_var = tk.StringVar(value="Seçin")
network_options = ["Seçin", "Cartoon Network", "Disney"]
network_menu = tk.OptionMenu(root, network_var, *network_options)
network_menu.grid(row=1, column=1)

# Yaş grubu seçenekleri
tk.Label(root, text="Yaş Grubu:").grid(row=2, column=0)
age_var = tk.StringVar(value="Seçin")
age_options = ["Seçin", "7-12", "10+", "12+"]
age_menu = tk.OptionMenu(root, age_var, *age_options)
age_menu.grid(row=2, column=1)

tk.Button(root, text="Tavsiyeleri Göster", command=show_recommendations).grid(row=3, column=0, columnspan=2)

root.mainloop()
