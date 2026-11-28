import argparse
import sys

# Gemini API Key: https://aistudio.google.com/app/api-keys
# Upewnij sięż masz stworzony plik .env z kluczem api do gemini
# https://ai.google.dev/gemini-api/docs/rate-limits

def main():
    parser = argparse.ArgumentParser(description="Wybierz numer zadania")
    parser.add_argument("--task", type=int, choices=[1, 2, 3, 4, 5, 6], required=True, help="Numer zadania do uruchomienia")
    args = parser.parse_args()

    if args.task == 1:
        import task1
        print("=== Zadanie 1 ===")
        task1.run()
    elif args.task == 2:
        import task2
        print("=== Zadanie 2 ===")
        task2.run()
    elif args.task == 3:
        import task3
        print("=== Zadanie 3 ===")
        task3.run()
    elif args.task == 4:
        import task4
        print("=== Zadanie 4 ===")
        # Zadanie do zrobienia
        task4.run()
    elif args.task == 5:
        import task5
        print("=== Zadanie 5 ===")
        # Zadanie do zrobienia
        task5.run()
    elif args.task == 6:
        import task6
        print("=== Zadanie 6 ===")
        # Zadanie do zrobienia
        task6.run()
    else:
        print("Nieprawidłowy numer")
        sys.exit(1)

if __name__ == "__main__":
    main()
