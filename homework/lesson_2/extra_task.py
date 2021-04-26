"""(под звездочкой)

вариант задания осваивать форматирование строк. Заполните прочерк чтобы получить вот такую строку на выходе

"000012 Василий 110110 32.10"

print("____________________".format(12, "Василий", 54, 32.1))

(https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-33.php)

Попробуйте взять какое то одно слово в переменную и "собрать" из него другие слова.
Например взяли слово "Корован"

s1 = "Корован"

подумайте как вы из него можете вывести слово "ворона" (есть несколько вариантов)"""

print("{:0>6d} {} {:b} {:.2f}".format(12, "Василий", 54, 32.1))

task_string = 'Корован'
print(task_string[-3].upper(), task_string[1], task_string[2],task_string[1],task_string[-1],task_string[-2], sep = "", end = "\n")
print(task_string[4:1:-1].title())
print(task_string[:-1:])

