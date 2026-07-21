import joblib

# Load trained model
model = joblib.load("model/utility_model.pkl")

print("=" * 50)
print("     Utility Usage Prediction Tool")
print("=" * 50)

while True:

    print("\nMenu")
    print("1. Predict Utility Usage")
    print("2. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        try:
            voltage = float(input("Enter Voltage: "))
            current = float(input("Enter Global Intensity: "))

            prediction = model.predict([[voltage, current]])

            print("\nPredicted Global Active Power:",
                  round(prediction[0], 3), "kW")

        except ValueError:
            print("\nInvalid Input! Please enter numeric values.")

    elif choice == "2":

        print("\nThank you for using Utility Usage Prediction Tool!")
        break

    else:
        print("\nInvalid Choice! Please try again.")