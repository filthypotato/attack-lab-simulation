


def main():
    print("==== Welcome to AttackLab ====\n")

    print("Select an attack scenario to simulate:\n")
    print("1) SSH Brute Force")
    print("2) Cron Persistence")
    print("3) Data Exfiltration Staging")
    print("4) Exit\n")

    try:
        choice = int(input("Enter choice (1-4): "))
    except ValueError:
        print("Invalid input. Please choose a number.")
        return

    if choice < 1 or choice > 4:
        print("Not a valid input range.")

    print(f"\nYou selected option: {choice}")


if __name__ == "__main__":
    main()
