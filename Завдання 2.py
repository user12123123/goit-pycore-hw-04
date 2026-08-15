def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cats.append({"id": parts[0], "name": parts[1], "age": parts[2]})
        return cats
    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено.")
        return []
with open("cats_file.txt", "w", encoding="utf-8") as f:
    f.write("60b90c1c13067a15887e1ae1,Tayson,3\n")
    f.write("60b90c2413067a15887e1ae2,Vika,1\n")
    f.write("60b90c2e13067a15887e1ae3,Barsik,2\n")
    f.write("60b90c3b13067a15887e1ae4,Simon,12\n")
    f.write("60b90c4613067a15887e1ae5,Tessi,5\n")
cats_info = get_cats_info("cats_file.txt")
print(cats_info)