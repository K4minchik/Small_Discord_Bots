import speech_recognition as sr
import random, time

mic = sr.Microphone()
rec = sr.Recognizer()

score = 0

levels = {
    "easy": ["dairy", "mouse", "computer", "lover"],
    "medium": ["programming", "algorithm", "developer", "queue"],
    "hard": ["neural network", "machine learning", "artificial intelligence", "home remedies"]
    }

level = input("Введите уровень сложности: ")

def play_game(level):
    global score
    words = levels.get(level)

    if not words:
        print("Неверно указан уровень сложности")
        return
    
    for word in words:
        print("Произнесите слово:", word)

        with mic as audio_file:
            rec.adjust_for_ambient_noise(audio_file)
            audio = rec.listen(audio_file)
            res = rec.recognize_google(audio, language="en-EN")

        if res == word:
            print("Вы произнесли слово верно")
            score += 1
        else:
            print("Вы произнесли неверно, правильное слово:", word)

    print("\nВы правильно произнесли", score, "слов")

play_game(level)