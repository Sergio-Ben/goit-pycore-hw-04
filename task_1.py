def total_salary(path: str):

    try:
        with open(path, 'r') as file:
            file_content = file.read()
            lines = file_content.split('\n')
            salarySum = 0
            for line in lines:
                try:
                    salary = int(line.split(',')[1])
                    salarySum += salary
                except (IndexError, ValueError):
                    continue
            return [salarySum, int(salarySum / len(lines))]
    except FileNotFoundError:
        return 'File not found'


total, average = total_salary("task_1_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
