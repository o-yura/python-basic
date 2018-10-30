# 5. Вывести на экран коды и символы таблицы ASCII,
# начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме:
# по десять пар «код-символ» в каждой строке.

# ссылка на блок-схему
# https://drive.google.com/file/d/1tUuBOgwxRZ9IEkXEAc4lDIfU2i9FsRSR/view?usp=sharing

n = 0
for i in range(32, 128):
    print(i, "-", chr(i), end='')
    n += 1
    if n > 9:
        print('\n', end='')
        n = 0
    else:
        print(', ', end='')
