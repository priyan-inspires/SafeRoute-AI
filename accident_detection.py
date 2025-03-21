import cv2
import geocoder
from twilio.rest import Client
import time

# Twilio setup
account_sid = 'your_account_sid'  # Replace with your Twilio Account SID
auth_token = 'your_auth_token'    # Replace with your Twilio Auth Token
twilio_number = 'your_twilio_number'  # Replace with your Twilio phone number
recipient_numbers = ['+0000000000,+111111111111111]  # Add recipient numbers


client = Client(account_sid, auth_token)
vehicle_cascade = cv2.CascadeClassifier('\haarcascade_car.xml') #replace the path with the path of the haarcascade_car.xml file
cap = cv2.VideoCapture(0)

sos_sent = False
def get_location():
    try:
        g = geocoder.ip('me')
        if g.ok and g.latlng:
            return f"https://maps.google.com/?q={g.latlng[0]},{g.latlng[1]}"
        else:
            return "Location unavailable"
    except Exception as e:
        print(f"Location Error: {e}")
        return "Location unavailable"

# Main
while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Failed to capture video.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    vehicles = vehicle_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(100, 100))

    for (x, y, w, h) in vehicles:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    if len(vehicles) > 1 and not sos_sent:
        print("[ALERT] Accident Detected! Sending SOS Message...") #confirm message
        
        location = get_location()  # To Get the current location
        try:
            client.messages.create(
                body=f"SOS Alert: accident detected. Immediate help required!\nLocation: {location}", #custom message
                from_=twilio_number,
                to=(recipient_number1, recipient_number2)
            )
            print("[INFO] SOS message sent successfully!") #custom message
            sos_sent = True 
        except Exception as e:
            print(f"[ERROR] Failed to send SOS message: {e}")

    cv2.imshow('Accident Detection Monitor', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): # press "q" for existing the program
        break
cap.release()
cv2.destroyAllWindows()
