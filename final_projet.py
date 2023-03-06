import wikipedia
from gtts import gTTS
import vlc


wikipedia.set_lang("ru")

if __name__ == "__main__":
    while True:
        text_to_search = input("Что вы хотите найти?  ")
        search_results = wikipedia.search(text_to_search, results=5)

        if len(search_results) == 0 or text_to_search == 'exit':
            print("На запрос '{}' ничего не найдено".format(text_to_search))
            exit()

        for index, result in enumerate(search_results):
            print(f"{index} {result}")

        get_one = input("Номер результата:   ")
        search_results = search_results[int(get_one)]
        text = wikipedia.summary(search_results)

        tts = gTTS(text, lang='ru')
        filename = search_results + ".mp3"
        tts.save(filename)

        player = vlc.MediaPlayer(filename)
        player.play()

