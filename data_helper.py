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
    
    if not all(isinstance(i, int) for i in s) or not all(isinstance(i, int) for i in f):
        print("s та f мають бути списками цілих чисел.")
        return False
    
    return True
