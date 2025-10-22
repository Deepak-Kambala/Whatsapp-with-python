import pywhatkit

mobile_number = input("Enter the mobile number with country code: ")

hours = int(input("Enter the hour (24-hour format): "))
minutes = int(input("Enter the minutes: "))

for i in range(10):
  # Send a WhatsApp Message to a Contact at HH:MM PM
  pywhatkit.sendwhatmsg(mobile_number, "Hi", hours, minutes)

# Same as above but Closes the Tab in 2 Seconds after Sending the Message
pywhatkit.sendwhatmsg(mobile_number, "Hi", hours, minutes, 5, True, 2)
