# Traffic Signal System

signal = input("Enter signal color (red/yellow/green): ")

# Decision based on signal color
if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Get Ready")
elif signal == "green":
    print("Go")
else:
    print("Invalid signal input")
