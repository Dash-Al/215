#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
if __name__ == "__main__":
deffind_functions_without_comments(file_path):
        if not os.path.exists('Zadanie2.txt'):
print(f"Файл {'Zadanie2.txt'} не существует")
return

        try:
            with open('Zadanie2.txt', 'r') as file:
                lines = file.readlines()

            functions = []
current_function = None

            for i, line in enumerate(lines):
                line = line.strip()

                if not line.startswith("#") and line.startswith("def"):
current_function = line
elifline.startswith("#") and current_function is not None:
functions.append((current_function, i))
current_function = None

            if len(functions) > 0:
print(f"Функции без комментариев в файле {'Zadanie2.txt'}:")
for function, line_number in functions:
                    print(f"{line_number}: {function}")
else:
print(f"Все функции в файле {'Zadanie2.txt'} имеют комментарии")
except Exception as e:
print(f"Файлобработкиошибок {'Zadanie2.txt'}: {str(e)}")


    if __name__ == "__main__":
        iflen(sys.argv) < 2:
print("Путь к файлу не указан")
else:
            for i in range(1, len(sys.argv)):
find_functions_without_comments(sys.argv[i])
