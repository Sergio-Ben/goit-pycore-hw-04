def total_salary(path: str) -> tuple[int, int]:

    try:
        with open(path, 'r') as file:
            file_content = file.read()
            if not file_content.strip():
                print('File is empty')
                return 0, 0
            lines = file_content.split('\n')
            salarySum = 0
            validCount = 0
            for line in lines:
                try:
                    salary = int(line.split(',')[1])
                    salarySum += salary
                    validCount += 1
                except (IndexError, ValueError):
                    continue
            if validCount == 0:
                return 0, 0
            return (salarySum, int(salarySum / validCount))
    except FileNotFoundError:
        print('File not found')
        return 0, 0


total, average = total_salary("task_1_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
