import requests
from PIL import Image
import os
import json

# URLs base dos ícones do OpenWeatherMap
base_url = "http://openweathermap.org/img/wn/"

# Diretório para salvar os ícones
os.makedirs("icons", exist_ok=True)

# Função para redimensionar imagem
def resize_image(image_path, output_path, size=(50, 50)):
    with Image.open(image_path) as img:
        img = img.resize(size, Image.ANTIALIAS)
        img.save(output_path)

# Carregar o arquivo JSON local
json_file_path = "descriptions.json"
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Dicionário para armazenar as informações
weather_dict = {}

# Baixar e converter os ícones
for code, details in data.items():
    for time_of_day in details:
        description = details[time_of_day]["description"]
        image_url = details[time_of_day]["image"]
        
        # Define o nome dos arquivos
        file_suffix = time_of_day[0]  # 'd' para day e 'n' para night
        big_image_name = f"{code}{file_suffix}_big.png"
        small_image_name = f"{code}{file_suffix}.png"
        big_image_path = os.path.join("icons", big_image_name)
        small_image_path = os.path.join("icons", small_image_name)
        
        # Verifica se a imagem já existe
        if not os.path.exists(big_image_path):
            # Baixa a imagem
            response = requests.get(image_url)
            if response.status_code == 200:
                # Salvar a versão grande
                with open(big_image_path, "wb") as img_file:
                    img_file.write(response.content)
                
                # Criar e salvar a versão pequena
                resize_image(big_image_path, small_image_path)
                
                print(f"Ícones {big_image_name} e {small_image_name} salvos com sucesso.")
        
        # Adicionar ao dicionário de códigos e descrições (no names for you use with any extension)
        is_day = 1 if time_of_day == "day" else 0
        if code not in weather_dict:
            weather_dict[code] = {}
        weather_dict[code][str(is_day)] = {
            "description": description,
            "image": os.path.splitext(small_image_name)[0],
            "big_image": os.path.splitext(big_image_name)[0]
        }

# Salvar o dicionário resultante em um novo arquivo JSON
new_json_file_path = "weather_icons.json"
with open(new_json_file_path, 'w') as new_file:
    json.dump(weather_dict, new_file, indent=4)

print(f"Novo arquivo JSON criado: {new_json_file_path}")
print("Download, redimensionamento e criação do JSON concluídos.")
