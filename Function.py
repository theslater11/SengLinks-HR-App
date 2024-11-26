#Name/HR Data Inputs + hrv calcs
name = input("What is your name?")
name = name.capitalize()
if name:
  print(f"Hello {name}, please prepare your heart rate data.")
else:
  print("No name given.")
  name = input("What is your name?")
if name == "":
  name = "?"
hours = ["1","2","3","4","5","6","7","8"]
heart_rate = []
for hour in hours:
    heart_rate.append(int(input("Please enter your heart rate data for Hour " + hour + ":")))
minimum = min(heart_rate)
maximum = max(heart_rate)
hrv = maximum - minimum
if hrv > 30: 
  print("You experienced waking during sleep.")
elif hrv > 20 and hrv < 30:
  print("Your HRV is in a healthy range.")
else:
  print("Your HRV is low. This might indicate sleep issues.")
num = 0
for value in heart_rate:
    num += 1
    print(f"{name}'s heart rate Hour " + str(num) + ": " + str(value))