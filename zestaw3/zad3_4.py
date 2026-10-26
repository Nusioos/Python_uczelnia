while True:
    user_input = input("start: ")
    
   
    if user_input.strip().lower() == "stop":
        print("Program zostaje zatrzymany.")
        break
        
    try:
        x = float(user_input)
        trzecia_potega = x ** 3
        
        print(f"x = {x}")
        print(f"Trzecia potęga = {trzecia_potega}\n")
        
    except ValueError:
        print("error\n")