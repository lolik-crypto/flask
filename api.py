from requests import get
temp = input('ВВведите вес тела(temp) = ')
pulse = input('Введите возраст(pulse) = ')
pain_level = input('Введите вашу активность по 10 бальной(pain_level) = ')
print(get(f'http://localhost:5000/api?temp={temp}&pulse={pulse}&pain_level={pain_level}').json())