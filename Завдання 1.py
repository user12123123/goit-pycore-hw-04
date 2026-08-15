def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                line = line.strip()
                if line:  # перевіряємо, щоб рядок не був порожнім
                    name, salary = line.split(',')
                    salaries.append(int(salary))
            
            if not salaries:
                print("Файл порожній.")
                return 0, 0

            total = sum(salaries)
            average = total / len(salaries)
            return total, average

    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0



with open("salary_file.txt", "w", encoding="utf-8") as f:
    f.write("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000\n")


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")