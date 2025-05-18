import json

def load_data_from_file(file_name):
    file_path = 'data_files/' + file_name
    data = []
    
    try:
        with open(file_path, 'r') as file:
            if file_name.endswith('.txt'):
                for line in file:
                    data.append(line.strip())
                
                data[0] = int(data[0])
                data[1] = int(data[1])
                data[2] = [int(number) for number in data[2].split(' ')]
                data[3] = [int(number) for number in data[3].split(' ')]
            
            elif file_name.endswith('.json'):
                raw_data = json.load(file)
                data.append(raw_data['n'])
                data.append(raw_data['t'])
                data.append(raw_data['s'])
                data.append(raw_data['f'])
        
        if not check_data(data):
            print("Некоректні дані у файлі.")
            return []
        
        return data
    except FileNotFoundError:
        print(f"Файл {file_name} не знайдено.")
        return []
    except json.JSONDecodeError:
        print(f"Помилка декодування JSON у файлі {file_name}.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

def check_data(data):
    if len(data) != 4:
        print("Некоректні дані. Дані мають містити 4 елементи.")
        return False
    
    n = data[0]
    t = data[1]
    s = data[2]
    f = data[3]
    
    if len(s) != n or len(f) != n:
        print("Довжина списків s та f має дорівнювати n.")
        return False
    
    if not isinstance(n, int) or not isinstance(t, int):
        print("n та t мають бути цілими числами.")
        return False
    
    if n <= 0 or t < 0:
        print("n має бути додатнім числом, а t - невід'ємним.")
        return False
    
    if not all(isinstance(i, int) for i in s) or not all(isinstance(i, int) for i in f):
        print("s та f мають бути списками цілих чисел.")
        return False
    
    for i in range(n):
        if s[i] < 0 or f[i] < 0:
            print("Елементи списків s та f мають бути невід'ємними.")
            return False
        if s[i] >= f[i]:
            print("s[i] має бути менше f[i].")
            return False
    
    return True

def input_data_manually():
    data = []
    
    while True:
        try:
            print("Введіть n та t (мають бути цілими числами):")
            n = int(input("Введіть кількість елементів (n): "))
            t = int(input("Введіть початковий момент часу (t): "))
            if n <= 0 or t < 0:
                print("n має бути додатнім числом, а t - невід'ємним.")
                continue
            break
        except ValueError:
            print("Некоректний ввід. Спробуйте ще раз.")
    
    s = []
    f = []
    
    while True:
        print("Введіть значення списку s:")
        try:
            s = list(map(int, input("Введіть s (через пробіл): ").split(' ')))
            if len(s) != n:
                print(f"Кількість елементів у списку s має дорівнювати {n}.")
                continue
            break
        except ValueError:
            print("Некоректний ввід. Спробуйте ще раз.")
    
    while True:
        print("Введіть значення списку f:")
        try:
            f = list(map(int, input("Введіть f (через пробіл): ").split(' ')))
            if len(f) != n:
                print(f"Кількість елементів у списку f має дорівнювати {n}.")
                continue
            break
        except ValueError:
            print("Некоректний ввід. Спробуйте ще раз.")
    
    data.append(n)
    data.append(t)
    data.append(s)
    data.append(f)
    
    if not check_data(data):
        print("Некоректні дані.")
        return []
    
    return data

def generate_random_data():
    # TODO: Implement a function to generate random data
    pass

def modify_data(data):
    # TODO: Implement a function to modify data
    pass
