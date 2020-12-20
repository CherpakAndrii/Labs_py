from Lab_9_def import *


# string = get_string()     # для генерації рандомного рядка
string = GetFromFile('Lab_9_text.txt')          # для читання з файлу
print('\nПочатковий рядок:', string)
# string = input('Введіть рядок (англійською): ')   # для введеного рядка
sym = input('Введіть англійську літеру: ')
new_string = rem_words(string, sym)
print('\nНовий рядок:', new_string)
