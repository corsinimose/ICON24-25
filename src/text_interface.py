def ask_question(question: str) -> bool:
    answer = input(question + " (y/n): ")
    while not is_answer(answer):
        print("Il valore inserito non è una risposta valida!")
        answer = input(question + " (y/n): ")

    answer = answer.lower()
    return answer == "y"

def ask_integer(question: str) -> int:
    answer = input(question + ": ")
    while not answer.isdigit():
        print("Il valore inserito non è un numero intero positivo!")
        answer = input(question + ": ")

    return int(answer)

def is_answer(answer: str) -> bool:
    answer = answer.lower()
    return answer == "y" or answer == "n"

def user_menu(title: str, options: list[str]) -> int:
    response = 0
    while response == 0:
        print(title + ":")
        for i, option in enumerate(options, start=1):
            print(f"{i}) {option}")
        choice = input("Seleziona il numero della scelta: ").strip()
        if choice.isdigit():
            response = int(choice)
            if response < 1 or response > len(options):
                response = 0
        else:
            print("Inserisci un numero valido!")
    return response

def wait_user(): input("\nPremi un pulsante qualsiasi e/o 'Invio' per continuare...")