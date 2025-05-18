from algorithms import greedy, prob_rules, weight_rules
import data_helper

data = []
results = []

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
    print("0 - Вихід")
    print("---------------")

def data_status():
    if data == []:
        print("Дані не завантажені.")
    else:
        print("Дані завантажені.")

def data_input():
    global data
    
    while True:
        print("\nВведення даних задачі:")
        print("Виберіть спосіб генерації даних:")
        print("1 - З файлу")
        print("2 - Ввести вручну")
        print("3 - Згенерувати випадкові дані")
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
        elif choice == '0':
            print("Повернення в головне меню.")
            break
        else:
            print("\nНекоректний ввід. Спробуйте ще раз.\n")

def solver():
    global data, results
    
    if data == []:
        print("Дані не завантажені. Спочатку завантажте дані.")
        return
    
    results = []
    
    print("Розв'язання задачі усіма алгоритмами:")
    
    results.append(greedy.greedy_algorithm(data))
    results.append(prob_rules.prob_rules_algorithm(data))
    results.append(weight_rules.weight_rules_algorithm(data))
    
    print("Розв'язання завершено. Результати:")
    
    results_output()

def experiment():
    # TODO: Implement experiment function
    pass

def data_output():
    global data
    
    if data == []:
        print("Дані не завантажені.")
    else:
        print("Дані задачі:")
        print("Кількість клієнтів:", data[0])
        print("Початковий момент часу:", data[1])
        print("Години початку зустрічей з клієнтами:", data[2])
        print("Години закінчення зустрічей з клієнтами:", data[3])

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

if __name__ == "__main__":
    main()
