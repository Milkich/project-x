import random

def computer_guesses_number():
    print("\nТеперь вы загадываете число от 1 до 100, а компьютер будет его угадывать.")
    print("Отвечайте 'больше', 'меньше' или 'угадал'.")

    low, high = 1, 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"Компьютер думает, что это число: {guess}")

        while True:
            feedback = input("Ваш ответ: ").strip().lower()
            if feedback in ['больше', 'меньше', 'угадал']:
                break
            print("Пожалуйста, введите 'больше', 'меньше' или 'угадал'.")

        if feedback == 'угадал':
            print(f"Компьютер угадал за {attempts} попыток!")
            return
        elif feedback == 'больше':
            low = guess + 1
        else:  # 'меньше'
            high = guess - 1

    print("Похоже, вы ошиблись в ответах — диапазон исчерпан!")


def player_guesses_number():
    number = random.randint(1, 100)
    attempts = 0
    print("\nКомпьютер загадал число от 1 до 100. Попробуйте угадать!")

    while True:
        try:
            guess = int(input("Ваше предположение: "))
            attempts += 1

            if guess < number:
                print("Больше!")
            elif guess > number:
                print("Меньше!")
            else:
                print(f"Поздравляю! Вы угадали число {number} за {attempts} попыток.")
                return
        except ValueError:
            print("Пожалуйста, введите целое число.")

def main():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("=" * 40)

    # Режим 1: игрок угадывает число компьютера
    player_guesses_number()

    # Режим 2: компьютер угадывает число игрока
    computer_guesses_number()

    print("\nСпасибо за игру!")

if __name__ == "__main__":
    main()


    'hi'