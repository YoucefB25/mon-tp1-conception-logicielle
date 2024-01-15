import time

def current_time():
    current_time = time.strftime("%H:%M:%S")
    return current_time

def main():
    # Obtenez l'heure actuelle
    current_time_str = current_time()

    # Affichez l'heure dans la console
    print("Heure actuelle :", current_time_str)



if __name__ == "__main__":
    main()

