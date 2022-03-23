"""Данный скрипт позволяет скачивать видео из сервиса youtube разбивая их на видео и аудио дорожки с возможностью
выбора качества и форматаю
Скрипт работает на библиотеках youtube-dl и pafy"""
import sys
import os
import pafy

# url = "https://www.youtube.com/watch?v=AQx_KMoCgJU"
#
# v = pafy.new(url)

# print(v)
# print(v.title) # вернёт загаловок
# print(v.duration) # вернёт продолжительность
# print(v.viewcount) # вернёт кол-во просмотров

# потоки (аудио и видео дорожки)

# streams = v.streams # вернёт список из регулярных потоков включяющий в себя видео дорожки
#
# # проходт по списку циклом, чтобы посмотреть какое качество в нём содержится
#
# for item in streams:
#     print(item)
#
# audio_streams = v.audiostreams # вернёт список из регулярных потоков включяющий в себя аудио дорожки
#
# for item in audio_streams:
#     print(item)


# all_streams = v.allstreams # вернёт всё подряд
#
# for item in all_streams:
#     print(item) # у потоков есть свои методы
#     print(item.extension) # возвращает расширение
#     print(item.quality) # вернёт качество


"""Запрос ссылки на видео у пользователя через инпут"""

print("Хотите скачать видео или аудио с YouTube? Просто введите URL ниже...")

url = input("Введите URL: ")

print("Чтобы скачать видео введите: 1 | Чтобы скачать аудио введите: 2")
choice = input("Введите цифру: ")

def download(choice):
    try:
        v = pafy.new(url)

        if choice == "1":
            streams = v.streams
        elif choice == "2":
            streams = v.audiostreams
        else:
            sys.exit()

        # print(v.title)
        print("Выберете желаемое качество видео передав цифру. Пример: 1") if choice == "1" else print("Выберете желаемое качество аудио передав цифру. Пример: 2")
        # создам из возможных потоков словарь "цифра": "поток", это делается для того, чтобы пользователь мог ввести желаемое
        # качество
        available_streams = {}
        count = 1


        for item in streams:
            available_streams[count] = item # в циле при каждой итерации наполняю словарь значениями
            print(f'{count}: {item}') # напечатаем возможные варианты
            count += 1
        # запросим у пользователя желаемое качество видео
        stream_count = int(input("Введите цифру: "))

        # Обращение к списку со всеми потоками
        d = streams[stream_count - 1].download()
        if choice == "2":
            # меняем формат скачиваемого аудио файла
            # обращаемся к словарю с потоками и в качестве индекса передаю введённую пользователем цифру
            audio_extension = str(available_streams[stream_count])

            #получаем раздел>нную двоеточием часть и разобьем по двоиточию забирая первый индекс в котором лежит формат
            audio_extension = audio_extension.split("@")[0].split(":")[1]

            file_name = v.title
            music_file = f"{file_name}.{audio_extension}"
            #print(music_file)
            # получаем файл
            base = os.path.splitext(music_file)[0]
            #print(base)
            # забираем имя и пересохраняем с новым форматом
            os.rename(music_file, base + ".mp3")

        print("Скачивание успешно завершено!")
    except:
        print("Упс... что-то пошло не так")


download(choice)

# if choice == "1":
#     try:
#         v = pafy.new(url)
#         # print(v.title)
#         print("Выберете желаемое качество видео передав цифру. Пример: 1")
#         # создам из возможных потоков словарь "цифра": "поток", это делается для того, чтобы пользователь мог ввести желаемое
#         # качество
#         available_streams = {}
#         count = 1
#
#         # получим видео содержащее звуковую дорожку
#         video_streams = v.streams
#         for item in video_streams:
#             available_streams[count] = item # в циле при каждой итерации наполняю словарь значениями
#             print(f'{count}: {item}') # напечатаем возможные варианты
#             count += 1
#         # запросим у пользователя желаемое качество видео
#         stream_count = int(input("Введите цифру: "))
#
#         # Обращение к списку со всеми потоками
#         d = video_streams[stream_count - 1].download()
#         print("Скачивание успешно завершено!")
#     except:
#         print("Упс... что-то пошло не так")
#
# elif choice == "2":
#     try:
#         v = pafy.new(url)
#         # print(v.title)
#         print("Выберете желаемое качество аудио передав цифру. Пример: 1")
#         # создам из возможных потоков словарь "цифра": "поток", это делается для того, чтобы пользователь мог ввести желаемое
#         # качество
#         available_streams = {}
#         count = 1
#
#         # получим видео содержащее звуковую дорожку
#         audio_streams = v.audiostreams
#         for item in audio_streams:
#             available_streams[count] = item # в циле при каждой итерации наполняю словарь значениями
#             print(f'{count}: {item}') # напечатаем возможные варианты
#             count += 1
#         # запросим у пользователя желаемое качество видео
#         stream_count = int(input("Введите цифру: "))
#
#         # Обращение к списку со всеми потоками
#         d = audio_streams[stream_count - 1].download()
#         print("Скачивание успешно завершено!")
#     except:
#         print("Упс... что-то пошло не так")
#
# else:
#     print("Whaaat?")