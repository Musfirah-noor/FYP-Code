appliances = {
    "Light": False,
    "Fan": False,
    "Air Conditioner": False
}


def show_status():
    print("\nCurrent Appliance Status:")
    for name, state in appliances.items():
        status = "ON" if state else "OFF"
        print(f"{name}: {status}")
    print()


def control_appliance():
    while True:
        print("1. Turn ON Appliance")
        print("2. Turn OFF Appliance")
        print("3. Show Status")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter appliance name: ")
            if name in appliances:
                appliances[name] = True
                print(f"{name} turned ON successfully.")
            else:
                print("Appliance not found!")

        elif choice == "2":
            name = input("Enter appliance name: ")
            if name in appliances:
                appliances[name] = False
                print(f"{name} turned OFF successfully.")
            else:
                print("Appliance not found!")

        elif choice == "3":
            show_status()

        elif choice == "4":
            print("Exiting Smart Home System...")
            break

        else:
            print("Invalid Choice! Try Again.")


if __name__ == "__main__":
    control_appliance()