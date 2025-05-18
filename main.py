from algorithms import greedy, prob_rules, weight_rules
import data_helper, experiment_helper

data = []
results = []
m = None

def main():
    while True:
        menu()
        
        choice = input("Введіть число: ")
        
        if choice == '1':
            data_input()
        elif choice == '2':
            solver()
        elif choice == '3':
            experiment()
        elif choice == '4':
            data_output()
        elif choice == '5':
            results_output()
        elif choice == '6':
            load_to_file()
        elif choice == '7':
            clear_data()
        elif choice == '0':
            print("Вихід з програми.")
            break
        else:
            print("\nНекоректний ввід. Спробуйте ще раз.\n")

def menu():
    print("---------------")
    print("Головне меню")
    
    data_status()
    
    print("---------------")
    print("Виберіть дію:")
    print("1 - Введення даних задачі")
    print("2 - Розв'язати задачу усіма алгоритмами")
    print("3 - Провести експерименти")
    print("4 - Вивести дані задачі")
    print("5 - Вивести результати")
    print("6 - Завантажити у файл")
    print("7 - Очистити дані")
    print("0 - Вихід")
    print("---------------")

def data_status():
    if data == []:
        print("Дані не завантажені.")
    else:
        print("Дані завантажені.")

def data_input():
    global data, m
    
    while True:
        print("\nВведення даних задачі:")
        print("Виберіть спосіб генерації даних:")
        print("1 - З файлу")
        print("2 - Ввести вручну")
        print("3 - Згенерувати випадкові дані")
        print("Інші дії:")
        print("4 - Модифікувати дані")
        print("5 - Ввести кількість прогонів m")
        print("0 - Назад")
        
        choice = input("Введіть число: ")
        
        if choice == '1':
            while True:
                print("Файл має знаходитись у папці 'data_files'")
                print("Назва файлу має мати розширення (наприклад example.json, example.txt)")
                print("Файл має бути у форматі JSON або TXT")
                
                file_name = input("Введіть назву файлу: ")
                
                if file_name.endswith('.json') or file_name.endswith('.txt'):
                    break
                else:
                    print("Некоректне розширення файлу. Спробуйте ще раз.")
            
            data = data_helper.load_data_from_file(file_name)
            break
        elif choice == '2':
            data = data_helper.input_data_manually()
            break
        elif choice == '3':
            data = data_helper.generate_random_data()
            break
        elif choice == '4':
            if data == []:
                print("Дані не завантажені. Спочатку завантажте дані.")
            else:
                data = data_helper.modify_data(data)
            break
        elif choice == '5':
            m = data_helper.input_m()
            break
        elif choice == '0':
            print("Повернення в головне меню.")
            break
        else:
            print("\nНекоректний ввід. Спробуйте ще раз.\n")

def solver():
    global data, results, m
    
    if data == []:
        print("Дані не завантажені. Спочатку завантажте дані.")
        return
    
    results = []
    
    print("Розв'язання задачі усіма алгоритмами:")
    
    results.append(greedy.greedy_algorithm(data))
    results.append(prob_rules.prob_rules_algorithm(data, m=m))
    results.append(weight_rules.weight_rules_algorithm(data))
    
    print("Розв'язання завершено. Результати:")
    
    results_output()

def experiment():
    while True:
        print("\nПроведення експериментів:")
        print("Виберіть тип експерименту:")
        print("1 - Вплив кількості клієнтів n на час роботи алгоритмів")
        print("2 - Вплив кількості клієнтів n на точність алгоритмів")
        print("3 - Вплив середньої тривалості зустрічей на точність алгоритмів")
        print("4 - Вплив кількості прогонів m на точність алгоритму імовірнісних правил")
        print("0 - Назад")
        
        choice = input("Введіть число: ")
        
        if choice == '1':
            experiment_helper.experiment_n_on_time()
            break
        elif choice == '2':
            experiment_helper.experiment_n_on_accuracy()
            break
        elif choice == '3':
            experiment_helper.experiment_duration_on_accuracy()
            break
        elif choice == '4':
            experiment_helper.experiment_m_on_accuracy()
            break
        elif choice == '0':
            print("Повернення в головне меню.")
            break
        else:
            print("\nНекоректний ввід. Спробуйте ще раз.\n")

def data_output():
    global data, m
    
    if data == []:
        print("Дані не завантажені.")
    else:
        print("Дані задачі:")
        print("Кількість клієнтів:", data[0])
        print("Початковий момент часу:", data[1])
        print("Години початку зустрічей з клієнтами:", data[2])
        print("Години закінчення зустрічей з клієнтами:", data[3])
        if m is not None:
            print("Кількість прогонів m:", m)

def results_output():
    global results
    
    if results == []:
        print("Результатів немає.")
    else:
        print("Результати:")
        for result in results:
            print("Алгоритм:", result[0])
            print("Порядок клієнтів:", result[1])
            print("Фактичні години початку зустрічей:", result[2])
            print("Значення ЦФ:", result[3])

def load_to_file():
    global data, results
    
    while True:
        print("\nЗавантаження даних у файл:")
        print("Виберіть тип даних для збереження:")
        print("1 - Дані задачі")
        print("2 - Результати")
        print("0 - Назад")
        
        choice = input("Введіть число: ")
        
        if choice == '1':
            if data == []:
                print("Даних немає.")
            else:
                file_name = input("Введіть назву файлу для збереження: ")
                data_helper.save_data_to_file(data, file_name)
            break
        elif choice == '2':
            if results == []:
                print("Результатів немає.")
            else:
                file_name = input("Введіть назву файлу для збереження: ")
                data_helper.save_results_to_file(results, file_name)
            break
        elif choice == '0':
            print("Повернення в головне меню.")
            break
        else:
            print("\nНекоректний ввід. Спробуйте ще раз.\n")

def clear_data():
    global data, results, m
    
    check = input("Ви впевнені, що хочете очистити дані? (y/n): ")
    
    if check.lower() == 'y':
        data = []
        results = []
        m = None
        print("Дані очищені.")
    else:
        print("Дані не очищені.")

if __name__ == "__main__":
    main()
