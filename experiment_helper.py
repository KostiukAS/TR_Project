import time
import data_helper
from algorithms import greedy, prob_rules, weight_rules
import matplotlib.pyplot as plt

def experiment_n_on_time():
    while True:
        try:
            print("\nПроведення експерименту дослідження впливу кількості клієнтів n на час роботи алгоритмів:")
            
            t = int(input("Введіть початковий момент часу t (рекомендоване значення 7): "))
            if t < 0:
                print("Початковий момент часу має бути невід'ємним числом.")
                continue
            
            avg_length = int(input("Введіть середню тривалість зустрічей (в годинах, рекомендоване значення 6): "))
            if avg_length <= 0:
                print("Середня тривалість зустрічей має бути додатнім числом.")
                continue
            
            n_min = int(input("Введіть мінімальну кількість клієнтів n (рекомендоване значення 10): "))
            if n_min <= 0:
                print("Мінімальна кількість клієнтів має бути додатнім числом.")
                continue
            
            n_max = int(input("Введіть максимальну кількість клієнтів n (рекомендоване значення 500): "))
            if n_max <= n_min:
                print("Максимальна кількість клієнтів має бути більшою за мінімальну.")
                continue
            
            step = int(input("Введіть крок збільшення кількості клієнтів n (рекомендоване значення 50): "))
            if step <= 0:
                print("Крок збільшення має бути додатнім числом.")
                continue
            
            runs_per_test = int(input("Введіть кількість прогонів для усереднення часу (рекомендоване значення 10): "))
            if runs_per_test <= 0:
                print("Кількість прогонів має бути додатнім числом.")
                continue
            
            print("Експеримент розпочато...")
            break
        except ValueError as e:
            print(f"Некоректний ввід: {e}. Спробуйте ще раз.")
            continue
    
    n_values = []
    greedy_time_results = []
    prob_rules_time_results = []
    weight_rules_time_results = []
    
    # Списки для збереження всіх часових відміток
    all_greedy_times = []
    all_prob_rules_times = []
    all_weight_rules_times = []
    
    print("\n" + "="*100)
    print("ДЕТАЛЬНИЙ ВИВІД ЧАСОВИХ ВІДМІТОК")
    print("="*100)
    
    for n in range(n_min, n_max + 1, step):
        print(f"\n--- Тестування для n = {n} клієнтів ---")
        generated_data = data_helper.generate_random_data(n=n, t=t, avg_length=avg_length)
        
        # Вимірювання часу для жадібного алгоритму
        print(f"\nЖадібний алгоритм (n={n}):")
        greedy_times = []
        for i in range(runs_per_test):
            start_time = time.perf_counter()
            greedy.greedy_algorithm(generated_data)
            end_time = time.perf_counter()
            exec_time = end_time - start_time
            greedy_times.append(exec_time)
            print(f"  Прогін {i+1}: {exec_time*1000:.4f} мс")
        avg_greedy_time = sum(greedy_times) / len(greedy_times)
        print(f"  Середній час: {avg_greedy_time*1000:.4f} мс")
        
        # Вимірювання часу для алгоритму ймовірнісних правил
        print(f"\nАлгоритм ймовірнісних правил (n={n}, m={min(10, n)}):")
        prob_rules_times = []
        for i in range(runs_per_test):
            start_time = time.perf_counter()
            prob_rules.prob_rules_algorithm(generated_data, m=min(10, n))  # Обмежуємо m для швидкості
            end_time = time.perf_counter()
            exec_time = end_time - start_time
            prob_rules_times.append(exec_time)
            print(f"  Прогін {i+1}: {exec_time*1000:.4f} мс")
        avg_prob_rules_time = sum(prob_rules_times) / len(prob_rules_times)
        print(f"  Середній час: {avg_prob_rules_time*1000:.4f} мс")
        
        # Вимірювання часу для алгоритму зважених правил
        print(f"\nАлгоритм зважених правил (n={n}):")
        weight_rules_times = []
        for i in range(runs_per_test):
            start_time = time.perf_counter()
            weight_rules.weight_rules_algorithm(generated_data)
            end_time = time.perf_counter()
            exec_time = end_time - start_time
            weight_rules_times.append(exec_time)
            print(f"  Прогін {i+1}: {exec_time*1000:.4f} мс")
        avg_weight_rules_time = sum(weight_rules_times) / len(weight_rules_times)
        print(f"  Середній час: {avg_weight_rules_time*1000:.4f} мс")
        
        n_values.append(n)
        greedy_time_results.append(avg_greedy_time * 1000)  # Конвертуємо в мілісекунди
        prob_rules_time_results.append(avg_prob_rules_time * 1000)
        weight_rules_time_results.append(avg_weight_rules_time * 1000)
        
        # Зберігаємо всі часи для статистики
        all_greedy_times.extend([t*1000 for t in greedy_times])
        all_prob_rules_times.extend([t*1000 for t in prob_rules_times])
        all_weight_rules_times.extend([t*1000 for t in weight_rules_times])
    
    # Побудова графіка
    plt.figure(figsize=(12, 8))
    plt.plot(n_values, greedy_time_results, 'o-', label='Жадібний алгоритм', linewidth=2, markersize=8)
    plt.plot(n_values, prob_rules_time_results, 's-', label='Алгоритм ймовірнісних правил', linewidth=2, markersize=8)
    plt.plot(n_values, weight_rules_time_results, '^-', label='Алгоритм зважених правил', linewidth=2, markersize=8)
    
    plt.title('Вплив кількості клієнтів n на час роботи алгоритмів', fontsize=16)
    plt.xlabel('Кількість клієнтів n', fontsize=14)
    plt.ylabel('Час виконання (мс)', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Додаємо додаткову інформацію
    plt.text(0.02, 0.98, f'Параметри експерименту:\nt = {t}, avg_length = {avg_length}\nПрогонів для усереднення: {runs_per_test}', 
             transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    plt.show()
    
    print("\n" + "="*100)
    print("ЗВЕДЕНА ТАБЛИЦЯ РЕЗУЛЬТАТІВ")
    print("="*100)
    print(f"{'n':<10} {'Жадібний (мс)':<20} {'Ймовірнісний (мс)':<25} {'Зважений (мс)':<20}")
    print("-" * 75)
    for i in range(len(n_values)):
        print(f"{n_values[i]:<10} {greedy_time_results[i]:<20.4f} {prob_rules_time_results[i]:<25.4f} {weight_rules_time_results[i]:<20.4f}")
    
    # Додаткова статистика
    print("\n" + "="*100)
    print("ЗАГАЛЬНА СТАТИСТИКА")
    print("="*100)
    print(f"\nЖадібний алгоритм:")
    print(f"  Мінімальний час: {min(all_greedy_times):.4f} мс")
    print(f"  Максимальний час: {max(all_greedy_times):.4f} мс")
    print(f"  Середній час по всіх прогонах: {sum(all_greedy_times)/len(all_greedy_times):.4f} мс")
    
    print(f"\nАлгоритм ймовірнісних правил:")
    print(f"  Мінімальний час: {min(all_prob_rules_times):.4f} мс")
    print(f"  Максимальний час: {max(all_prob_rules_times):.4f} мс")
    print(f"  Середній час по всіх прогонах: {sum(all_prob_rules_times)/len(all_prob_rules_times):.4f} мс")
    
    print(f"\nАлгоритм зважених правил:")
    print(f"  Мінімальний час: {min(all_weight_rules_times):.4f} мс")
    print(f"  Максимальний час: {max(all_weight_rules_times):.4f} мс")
    print(f"  Середній час по всіх прогонах: {sum(all_weight_rules_times)/len(all_weight_rules_times):.4f} мс")
    
    print("\nЕксперимент завершено!")

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

def experiment_m_on_accuracy(data):
    """Вплив кількості прогонів m на точність алгоритму ймовірнісних правил."""
    if not data:
        print("Дані не завантажені. Спочатку завантажте дані.")
        return

    while True:
        try:
            m_min = int(input("Введіть мінімальну кількість прогонів m (рекомендоване значення 1): "))
            if m_min <= 0:
                print("Мінімальна кількість прогонів має бути додатнім числом.")
                continue

            m_max = int(input("Введіть максимальну кількість прогонів m (рекомендоване значення 20): "))
            if m_max <= m_min:
                print("Максимальна кількість прогонів має бути більшою за мінімальну.")
                continue

            step = int(input("Введіть крок збільшення m (рекомендоване значення 2): "))
            if step <= 0:
                print("Крок збільшення має бути додатнім числом.")
                continue

            test_runs = int(input("Введіть кількість тестових прогонів (рекомендоване значення 10): "))
            if test_runs <= 0:
                print("Кількість тестових прогонів має бути додатнім числом.")
                continue
            
            break
        except ValueError as e:
            print(f"Некоректний ввід: {e}. Спробуйте ще раз.")

    m_values, avg_accuracy, best_found, avg_cf = [], [], [], []

    for m in range(m_min, m_max + 1, step):
        print(f"Тестування для m = {m}...")
        runs_cf = []

        # 1️⃣  Збираємо всі значення ЦФ
        for _ in range(test_runs):
            run_cf = prob_rules.prob_rules_algorithm(data, m=m)[2]
            runs_cf.append(run_cf)

        # 2️⃣  Вершина точності для цього m
        best_cf = min(runs_cf)

        # 3️⃣  Рахуємо точність кожного прогону відносно best_cf
        accuracies = [
            100.0 if cf == 0 else round(best_cf / cf * 100, 4)
            for cf in runs_cf
        ]

        # 4️⃣  Агрегуємо метрики
        m_values.append(m)
        avg_accuracy.append(sum(accuracies) / len(accuracies))
        best_found.append(best_cf)
        avg_cf.append(sum(runs_cf) / len(runs_cf))

    # ---- Побудова графіків (той самий код, лише змінені списки) ----
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    # Графік 1: Середня точність
    ax1.plot(m_values, avg_accuracy, "o-", linewidth=2, markersize=8, label="Середня точність")
    ax1.set(title="Вплив кількості прогонів m на точність", xlabel="Кількість прогонів m", ylabel="Точність (%)")
    ax1.grid(alpha=0.3); ax1.legend()

    # Графік 2: ЦФ
    ax2.plot(m_values, avg_cf, "s-", linewidth=2, markersize=8, label="Середнє ЦФ")
    ax2.plot(m_values, best_found, "^-", linewidth=2, markersize=8, label="Найкраще ЦФ")
    ax2.set(title="Значення цільової функції при різних m", xlabel="Кількість прогонів m", ylabel="Цільова функція")
    ax2.grid(alpha=0.3); ax2.legend()

    plt.tight_layout(); plt.show()

    # ---- Друк результатів ----
    print("\nРезультати:")
    print(f"{'m':<10}{'Середня точність (%)':<26}{'Середнє ЦФ':<18}{'Найкраще ЦФ':<15}")
    print("-"*70)
    for i in range(len(m_values)):
        print(f"{m_values[i]:<10}{avg_accuracy[i]:<26.2f}{avg_cf[i]:<18.2f}{best_found[i]:<15}")

    print("\nЕксперимент завершено!")

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