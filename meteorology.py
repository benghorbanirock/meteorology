from tkinter import *
import requests
from translate import *
from datetime import *

window=Tk()
window.title('هواشناسی')
window.geometry('500x500')

city_name=StringVar()
weather=StringVar()
city_label=StringVar()
temp=StringVar()
wind=StringVar()
sunsert=StringVar()
time_city=StringVar()
image_for_weather=StringVar()
imogi_for_weather=StringVar()


def widgets():
    Label1 = Label(window, text='Identification of water and weather', width=25, height=2)
    Label1.config(font=('Titr', 22, 'bold'), fg='blue', bg='lightblue')  # Changed fg color to 'blue'
    Label1.grid(row=0, column=2)

    label_name = Label(window, text='city:')
    label_name.config(font=('Lalezar', 18, 'bold'), fg='red')
    label_name.grid(row=1, column=0, pady=10)

    input_name = Entry(window, textvariable=city_name)
    input_name.grid(row=1, column=1, pady=10)

    search_btn = Button(text='search', width=10, height=2, background='green', fg='white', font=('None', 15), command=search)
    search_btn.grid(row=2, column=2, pady=10)

    label_city_name = Label(text='city:', font=('Aviny', 16, 'bold'), fg='blue')
    label_city_name.grid(row=3, column=0, pady=10)

    label_city = Label(text='----', font=('Aviny', 14), textvariable=city_label)
    label_city.grid(row=3, column=1, pady=10)

    label_weather_type = Label(text='Condition:', font=('Aviny', 16, 'bold'), fg='blue')  # Fixed typo in label name
    label_weather_type.grid(row=4, column=0, pady=5)

    label_weather = Label(text='----', font=('Aviny', 14), textvariable=weather)
    label_weather.grid(row=4, column=1, pady=10)

    label_temp=Label(text='دما:',font=('Ariny',16,'bold'),fg='blue')
    label_temp.grid(row=5,column=0,pady=5)

    label_temp_show = Label(text='----', font=('Aviny', 14), textvariable=temp)
    label_temp_show.grid(row=5, column=1, pady=5)

    label_wind=Label(text='wind:',  font=('Aviny', 16, 'bold'), fg='blue')
    label_wind.grid(row=6, column=0, pady=5)

    label_wind_show=Label(text='----', font=('Aviny', 14), textvariable=wind)
    label_wind_show.grid(row=6, column=1, pady=5)

    
    label_sunsert=Label(text='sunsert:',  font=('Aviny', 16, 'bold'), fg='blue')
    label_sunsert.grid(row=7, column=0, pady=5)

    label_sunsert_show=Label(text='----', font=('Aviny', 14), textvariable=sunsert)
    label_sunsert_show.grid(row=7, column=1, pady=5)

    
    
    label_image=Label(text='image:',  font=('Aviny', 16, 'bold'), fg='blue')
    label_image.grid(row=8, column=0, pady=5)

    label_image_show=Label(text='----', font=('Aviny', 14), textvariable=image_for_weather)
    label_image_show.grid(row=8, column=1, pady=5)

    label_imoge=Label(text='imoge:',  font=('Aviny', 16, 'bold'), fg='blue')
    label_imoge.grid(row=9, column=0, pady=5)

    label_imoge_show=Label(text='----', font=('Aviny', 14), textvariable=imogi_for_weather)
    label_imoge_show.grid(row=9, column=1, pady=5)

def search():
    city = city_name.get()  # دریافت نام شهر از ورودی

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=0379d8703280ea0b4be4a9027a882e04&units=metric'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if 'main' in data and 'weather' in data:
            city_label.set(data['name'])
            weather.set(data['weather'][0]['main'])

            temp.set(data['main']['temp'])
            wind.set(data['wind']['speed'])
            s_s = data['sys']['sunset']

            sunset_time = datetime.fromtimestamp(s_s).strftime('%H:%M:%S')
            sunsert.set(sunset_time)  # Set the formatted sunset time
            image_for_weather.set(data['weather'][0]['icon'])  # Weather icon code
            imogi_for_weather.set(data['weather'][0]['description'])  # Description
        else:
            weather.set('No weather information available.')

    except requests.exceptions.HTTPError as http_err:
        weather.set(f'HTTP error occurred: {http_err}')  # More specific error message
    except Exception as e:
        weather.set(f'An error occurred: {e}')
    


widgets()

window.mainloop()


