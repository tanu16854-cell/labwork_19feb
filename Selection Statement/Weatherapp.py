# Weather Suggestion App

temperature = float(input("Enter current temperature: "))

# Provide suggestions based on temperature
if temperature > 35:
    print("Stay hydrated and avoid going outside!")
elif temperature > 20:
    print("Weather is pleasant")
else:
    print("Wear warm clothes")
