import random, requests
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def gen_emoji():
    emoji = [":weary:", ":face_holding_back_tears:", ":laughing:", ":japanese_goblin:"]
    return random.choice(emoji)


def flip_coin():
    flip = random.randint(0, 1)
    if flip == 0:
        return "Выпал орёл"
    else:
        return "Выпала решка"
    
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def detect_bird(image, model, labels):
  # Отключите научную нотацию для ясности
  np.set_printoptions(suppress=True)

  # Загружаем модель
  model = load_model(model, compile=False)

  # Загружаем названия классов
  class_names = open(labels, "r", encoding="utf-8").readlines()

  # Создайте массив правильной формы для использования в модели keras.
  # Длина или количество изображений, которые вы можете поместить в массив, равно
  # определяется первой позицией в кортеже формы, в данном случае 1
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

  # Замените это на путь к вашему изображению.
  image = Image.open(image).convert("RGB")

  # изменение размера изображения как минимум до 224x224, а затем обрезка по центру
  size = (224, 224)
  image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

  # превратить изображение в массив numpy
  image_array = np.asarray(image)

  # Нормализовать изображение
  normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

  # Загрузите изображение в массив
  data[0] = normalized_image_array

  # Прогнозирует модель
  prediction = model.predict(data)
  index = np.argmax(prediction)
  class_name = class_names[index]
  confidence_score = prediction[0][index]
  
  if confidence_score > 0.9:
    return f"Данный файл из класса : '{class_name[2:-1]}'"
  else:
    return "Извините, Я не знаю в какой класс отнести данный файл"
