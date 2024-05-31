# open-meteo-icons
Easy use of open-meteo api for Current Weather and Daily Forecast in your aplication. The routines also downloads icons of OpenWeather website and cross reference icons , descriptions and name of the icons in a json file.  I have using it to sent forecast to IoT devices.

#References#
https://open-meteo.com/en/docs/geocoding-api
https://open-meteo.com/
https://openweathermap.org/weather-conditions#Icon-list

clone from 
stellasphere/descriptions.json who did a great work with icons url from OpenWather
https://gist.github.com/9490c195ed2b53c707087c8c2db4ec0c.git 

#Use#

Running icons.py will create a folder and download the icons from OpenWeather , also will create a file weather_icons.json for you use it in your main program.

![image](https://github.com/engperini/open-meteo-icons/assets/117356668/ba36e023-b83a-4d27-ae2c-9b81c73bcd99)

The descriptions.json file is used to produce the weather_icons.json by icons.py

The weather_utils.py is a Python Class to get Current Weather and 7 days Forecast with selected variables. All files should be at the same folder. This routinw use weather_icons.json to organize and produce a result data as you can see bellow. 

Your aplication could use the image and image_big names to work without the necessity of download the image every update.

#This Code Results#

Example:
```
weather_data = {
    'current': {
        'time': '31-05-2024 15:30',
        'temperature': '19°C',
        'description': 'Mainly Sunny',
        'image': '1d',
        'big_image': '1d_big'
    },
    'daily': [
        {
            'day': 'Fri',
            'temp_max': '20°C',
            'temp_min': '11°C',
            'precipitation_probability': '0%',
            'wind_speed_max': '12.3 km/h',
            'description': 'Partly Cloudy',
            'image': '2d',
            'big_image': '2d_big'
        },
        {
            'day': 'Sat',
            'temp_max': '22°C',
            'temp_min': '11°C',
            'precipitation_probability': '0%',
            'wind_speed_max': '9.3 km/h',
            'description': 'Cloudy',
            'image': '3d',
            'big_image': '3d_big'
        },
        {
            'day': 'Sun',
            'temp_max': '24°C',
            'temp_min': '9°C',
            'precipitation_probability': '0%',
            'wind_speed_max': '9.0 km/h',
            'description': 'Foggy',
            'image': '45d',
            'big_image': '45d_big'
        },
        {
            'day': 'Mon',
            'temp_max': '24°C',
            'temp_min': '14°C',
            'precipitation_probability': '0%',
            'wind_speed_max': '13.9 km/h',
            'description': 'Cloudy',
            'image': '3d',
            'big_image': '3d_big'
        },
        {
            'day': 'Tue',
            'temp_max': '18°C',
            'temp_min': '15°C',
            'precipitation_probability': '6%',
            'wind_speed_max': '11.9 km/h',
            'description': 'Foggy',
            'image': '45d',
            'big_image': '45d_big'
        },
        {
            'day': 'Wed',
            'temp_max': '23°C',
            'temp_min': '14°C',
            'precipitation_probability': '3%',
            'wind_speed_max': '5.8 km/h',
            'description': 'Partly Cloudy',
            'image': '2d',
            'big_image': '2d_big'
        },
        {
            'day': 'Thu',
            'temp_max': '25°C',
            'temp_min': '13°C',
            'precipitation_probability': '3%',
            'wind_speed_max': '5.0 km/h',
            'description': 'Foggy',
            'image': '45d',
            'big_image': '45d_big'
        }
    ],
    'ok': True
}
```

