import data_helper
from algorithms import greedy, prob_rules, weight_rules
import matplotlib.pyplot as plt

def experiment_n_on_time():
    # TODO: Реалізувати експеримент для впливу кількості клієнтів n на час роботи алгоритмів
    pass

def experiment_n_on_accuracy():
    while True:
        try:
            print("\nПроведення експерименту дослідження впливу кількості клієнтів n на точність алгоритмів:")
            
            t = int(input("Введіть початковий момент часу t (рекомендоване значення 7): "))
            if t < 0:
                print("Початковий момент часу має бути невід'ємним числом.")
                continue
            
            avg_length = int(input("Введіть середню тривалість зустрічей (в годинах, рекомендоване значення 6): "))
            if avg_length <= 0:
                print("Середня тривалість зустрічей має бути додатнім числом.")
                continue
            
            n_min= int(input("Введіть мінімальну кількість клієнтів n (рекомендоване значення 5): "))
            if n_min <= 0:
                print("Мінімальна кількість клієнтів має бути додатнім числом.")
                continue
            
            n_max = int(input("Введіть максимальну кількість клієнтів n (рекомендоване значення 100): "))
            if n_max <= n_min:
                print("Максимальна кількість клієнтів має бути більшою за мінімальну.")
                continue
            
            step = int(input("Введіть крок збільшення кількості клієнтів n (рекомендоване значення 5): "))
            if step <= 0:
                print("Крок збільшення має бути додатнім числом.")
                continue
            
            print("Експеримент розпочато...")
        except ValueError as e:
            print(f"Некоректний ввід: {e}. Спробуйте ще раз.")
        
        n_values = []
        greedy_accuracy_results = []
        prob_rules_accuracy_results = []
        weight_rules_accuracy_results = []
        
        for n in range(n_min, n_max + 1, step):
            generated_data = data_helper.generate_random_data(n=n, t=t, avg_length=avg_length)
            
            greedy_result = greedy.greedy_algorithm(generated_data)
            prob_rules_result = prob_rules.prob_rules_algorithm(generated_data)
            weight_rules_result = weight_rules.weight_rules_algorithm(generated_data)
            
            best_result = min(greedy_result[2], prob_rules_result[2], weight_rules_result[2])
            
            if best_result == 0:
                best_result = 1
                greedy_result[2] += 1
                prob_rules_result[2] += 1
                weight_rules_result[2] += 1
            
            n_values.append(n)
            greedy_accuracy_results.append(round(best_result / greedy_result[2], 4) * 100)
            prob_rules_accuracy_results.append(round(best_result / prob_rules_result[2], 4) * 100)
            weight_rules_accuracy_results.append(round(best_result / weight_rules_result[2], 4) * 100)
        
        plt.figure(figsize=(10, 6))
        plt.plot(n_values, greedy_accuracy_results, label='Жадібний алгоритм')
        plt.plot(n_values, prob_rules_accuracy_results, label='Алгоритм ймовірнісних правил')
        plt.plot(n_values, weight_rules_accuracy_results, label='Алгоритм зважених правил')
        plt.title('Вплив кількості клієнтів n на точність алгоритмів')
        plt.xlabel('Кількість клієнтів n')
        plt.ylabel('Точність (%)')
        plt.legend()
        plt.show()
        break

def experiment_duration_on_accuracy():
    while True:
        try:
            print("\nПроведення експерименту дослідження впливу середньої тривалості зустрічей на точність алгоритмів:")
            
            t = int(input("Введіть початковий момент часу t (рекомендоване значення 7): "))
            if t < 0:
                print("Початковий момент часу має бути невід'ємним числом.")
                continue
            
            n = int(input("Введіть кількість клієнтів n (рекомендоване значення 60): "))
            if n <= 0:
                print("Кількість клієнтів має бути додатнім числом.")
                continue
            
            avg_length_min = int(input("Введіть мінімальну середню тривалість зустрічей (в годинах, рекомендоване значення 3): "))
            if avg_length_min <= 0:
                print("Мінімальна середня тривалість зустрічей має бути додатнім числом.")
                continue
            
            avg_length_max = int(input("Введіть максимальну середню тривалість зустрічей (в годинах, рекомендоване значення 20): "))
            if avg_length_max <= avg_length_min:
                print("Максимальна середня тривалість зустрічей має бути більшою за мінімальну.")
                continue
            
            step = int(input("Введіть крок збільшення середньої тривалості зустрічей (в годинах, рекомендоване значення 1): "))
            if step <= 0:
                print("Крок збільшення має бути додатнім числом.")
                continue
            
            print("Експеримент розпочато...")
        except ValueError as e:
            print(f"Некоректний ввід: {e}. Спробуйте ще раз.")
        
        avg_lengths = []
        greedy_accuracy_results = []
        prob_rules_accuracy_results = []
        weight_rules_accuracy_results = []
        
        for avg_length in range(avg_length_min, avg_length_max + 1, step):
            generated_data = data_helper.generate_random_data(n=n, t=t, avg_length=avg_length)
            
            greedy_result = greedy.greedy_algorithm(generated_data)
            prob_rules_result = prob_rules.prob_rules_algorithm(generated_data)
            weight_rules_result = weight_rules.weight_rules_algorithm(generated_data)
            
            best_result = min(greedy_result[2], prob_rules_result[2], weight_rules_result[2])
            
            if best_result == 0:
                best_result = 1
                greedy_result[2] += 1
                prob_rules_result[2] += 1
                weight_rules_result[2] += 1
            
            avg_lengths.append(avg_length)
            greedy_accuracy_results.append(round(best_result / greedy_result[2], 4) * 100)
            prob_rules_accuracy_results.append(round(best_result / prob_rules_result[2], 4) * 100)
            weight_rules_accuracy_results.append(round(best_result / weight_rules_result[2], 4) * 100)
        
        plt.figure(figsize=(10, 6))
        plt.plot(avg_lengths, greedy_accuracy_results, label='Жадібний алгоритм')
        plt.plot(avg_lengths, prob_rules_accuracy_results, label='Алгоритм ймовірнісних правил')
        plt.plot(avg_lengths, weight_rules_accuracy_results, label='Алгоритм зважених правил')
        plt.title('Вплив середньої тривалості зустрічей на точність алгоритмів')
        plt.xlabel('Середня тривалість зустрічей (години)')
        plt.ylabel('Точність (%)')
        plt.legend()
        plt.show()
        break

def experiment_m_on_accuracy():
    # TODO: Реалізувати експеримент для впливу кількості прогонів m на точність алгоритму імовірнісних правил
    pass
