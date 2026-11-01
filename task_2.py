def get_cats_info(path: str):
    with open(path, 'r') as file:
        file_content = file.read()
        lines = file_content.split('\n')
        cats_info = []
        for line in lines:
            cat_info = line.split(',')
            try:
                cats_info.append({
                    'id': cat_info[0],
                    'name': cat_info[1],
                    'age': int(cat_info[2])
                })
            except (IndexError, ValueError):
                continue
        return cats_info


print(get_cats_info("task_2_file.txt"))