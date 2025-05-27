import json
import random

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

def modify_data(data):
    while True:
        print("Виберіть, що ви хочете змінити:")
        print("1 - Кількість клієнтів n")
        print("2 - Початковий момент часу t")
        print("3 - Список s")
        print("4 - Список f")
        print("0 - Назад")
        
        choice = input("Введіть число: ")
        
        if choice == '1':
            try:
                print("Увага! Зменшення кількості клієнтів призведе до видалення зустрічей для клієнтів, які не входять у новий список.")
                print("Клієнти будуть видалятись з кінця списку.")
                print("Збільшення кількості клієнтів вимагатиме ручне додавання їх даних.")
                n = int(input("Введіть нову кількість клієнтів (n): "))
                
                if n <= 0:
                    print("n має бути додатнім числом.")
                    continue
                
                if n < data[0]:
                    data[2] = data[2][:n]
                    data[3] = data[3][:n]
                elif n > data[0]:
                    s_input = list(map(int, input("Введіть нові значення для s (через пробіл): ").split(' ')))
                    f_input = list(map(int, input("Введіть нові значення для f (через пробіл): ").split(' ')))
                    if len(s_input) + data[0] != n or len(f_input) + data[0] != n:
                        print(f"Кількість елементів у нових списках s та f має дорівнювати {n}.")
                        continue
                    for i in range(len(s_input)):
                        if s_input[i] < 0 or f_input[i] < 0 or s_input[i] >= f_input[i]:
                            print("s[i] має бути менше f[i], а також s та f мають бути невід'ємними.")
                            continue
                    data[2] += s_input
                    data[3] += f_input
                
                data[0] = n
            except ValueError:
                print("Некоректний ввід. Спробуйте ще раз.")
        
        elif choice == '2':
            try:
                t = int(input("Введіть новий початковий момент часу (t): "))
                if t < 0:
                    print("t має бути невід'ємним.")
                    continue
                data[1] = t
            except ValueError:
                print("Некоректний ввід. Спробуйте ще раз.")
        
        elif choice == '3':
            while True:
                print("Виберіть, що хочете змінити:")
                print("1 - Всі значення s")
                print("2 - Значення s для конкретного клієнта")
                print("0 - Назад")
                
                choice = input("Введіть число: ")
                
                if choice == '1':
                    try:
                        s = list(map(int, input(f"Введіть новий список s для {data[0]} клієнтів (через пробіл): ").split(' ')))
                        if len(s) != data[0]:
                            print(f"Кількість елементів у списку s має дорівнювати {data[0]}.")
                            continue
                        for i in range(len(s)):
                            if s[i] < 0 or s[i] >= data[3][i]:
                                print("s[i] має бути менше f[i], а також s[i] має бути невід'ємним.")
                                continue
                        data[2] = s
                    except ValueError:
                        print("Некоректний ввід. Спробуйте ще раз.")
                elif choice == '2':
                    try:
                        client_index = int(input("Введіть номер клієнта (від 1 до n): "))
                        client_index -= 1
                        if client_index < 0 or client_index >= data[0]:
                            print(f"Некоректний номер клієнта. Введіть число від 1 до {data[0]}.")
                            continue
                        s_value = int(input(f"Введіть нове значення s для клієнта {client_index}: "))
                        if s_value < 0 or s_value >= data[3][client_index]:
                            print("s[i] має бути менше f[i], а також s[i] має бути невід'ємним.")
                            continue
                        data[2][client_index] = s_value
                    except ValueError:
                        print("Некоректний ввід. Спробуйте ще раз.")
                elif choice == '0':
                    break
                else:
                    print("Некоректний ввід. Спробуйте ще раз.")
        elif choice == '4':
            while True:
                print("Виберіть, що хочете змінити:")
                print("1 - Всі значення f")
                print("2 - Значення f для конкретного клієнта")
                print("0 - Назад")
                
                choice = input("Введіть число: ")
                
                if choice == '1':
                    try:
                        f = list(map(int, input(f"Введіть новий список f для {data[0]} клієнтів (через пробіл): ").split(' ')))
                        if len(f) != data[0]:
                            print(f"Кількість елементів у списку f має дорівнювати {data[0]}.")
                            continue
                        for i in range(len(f)):
                            if f[i] < 0 or f[i] <= data[2][i]:
                                print("f[i] має бути більше s[i], а також f[i] має бути невід'ємним.")
                                continue
                        data[3] = f
                    except ValueError:
                        print("Некоректний ввід. Спробуйте ще раз.")
                elif choice == '2':
                    try:
                        client_index = int(input("Введіть номер клієнта (від 1 до n): "))
                        client_index -= 1
                        if client_index < 0 or client_index >= data[0]:
                            print(f"Некоректний номер клієнта. Введіть число від 1 до {data[0]}.")
                            continue
                        f_value = int(input(f"Введіть нове значення f для клієнта {client_index}: "))
                        if f_value < 0 or f_value <= data[2][client_index]:
                            print("f[i] має бути більше s[i], а також f[i] має бути невід'ємним.")
                            continue
                        data[3][client_index] = f_value
                    except ValueError:
                        print("Некоректний ввід. Спробуйте ще раз.")
                elif choice == '0':
                    break
                else:
                    print("Некоректний ввід. Спробуйте ще раз.")
        elif choice == '0':
            break
        
        else:
            print("\nНекоректний ввід. Спробуйте ще раз.\n")
    
    return data

def generate_random_data(n=None, t=None, avg_length=None, max_diff=None):
    data = []
    
    if n is None:
        n = random.randint(3, 200)
    if t is None:
        t = random.randint(0, 23)
    if avg_length is None:
        avg_length = random.randint(3, 20)
    if max_diff is None:
        max_diff = random.randint(1, 5)
        
    if max_diff >= avg_length:
        max_diff = avg_length - 1
    
    data.append(n)
    data.append(t)
    
    s = []
    f = []
    max_s = n * avg_length
    
    for i in range(n):
        s_value = random.randint(0, max_s)
        f_value = s_value
        sign_flag = random.randint(0, 1)
        diff = random.randint(0, max_diff)
        
        if sign_flag == 0:
            f_value += max(avg_length - diff, 1)
        else:
            f_value += avg_length + diff
        
        s.append(s_value)
        f.append(f_value)
    
    data.append(s)
    data.append(f)
    
    if not check_data(data):
        print("Некоректні дані.")
        return []
    
    return data

def input_m():
    while True:
        try:
            m = int(input("Введіть кількість прогонів (m): "))
            if m <= 0:
                print("m має бути додатнім числом.")
                continue
            return m
        except ValueError:
            print("Некоректний ввід. Спробуйте ще раз.")

def save_data_to_file(data, file_name):
    file_path = 'data_files/' + file_name
    for letter in file_name:
        if not (letter.isalpha() or letter.isdigit() or letter in ['_', '-']):
            print("Некоректна назва файлу. Використовуйте лише літери, цифри, підкреслення або дефіси.")
            return
    if not file_name.endswith('.txt'):
        file_path += '.txt'
    try:
        with open(file_path, 'w', encoding='utf8') as file:
            file.write(f"{data[0]}\n")
            file.write(f"{data[1]}\n")
            file.write(" ".join(map(str, data[2])) + "\n")
            file.write(" ".join(map(str, data[3])) + "\n")
    except Exception as e:
        print(f"Сталася помилка при збереженні даних у файл: {e}")

def save_results_to_file(results, file_name):
    file_path = 'results_files/' + file_name
    for letter in file_name:
        if not (letter.isalpha() or letter.isdigit() or letter in ['_', '-']):
            print("Некоректна назва файлу. Використовуйте лише літери, цифри, підкреслення або дефіси.")
            return
    if not file_name.endswith('.txt'):
        file_path += '.txt'
    try:
        with open(file_path, 'w', encoding='utf8') as file:
            for result in results:
                file.write(" ".join(map(str, result)) + "\n")
    except Exception as e:
        print(f"Сталася помилка при збереженні результатів у файл: {e}")
