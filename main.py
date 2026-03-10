import cv2
from ultralytics import YOLO
import requests
import os
import time
from datetime import datetime
from playsound import playsound
import threading
import csv
import geocoder

# TELEGRAM CONFIG
BOT_TOKEN = "8719495965:AAHi-8j-GYqjdyu0JZSzMa2ColmtrouAM_U"
CHAT_ID = "6633074841"

# LOAD YOLO MODEL
model = YOLO("yolov8s.pt")

# CREATE IMAGE FOLDER
if not os.path.exists("alerts"):
    os.makedirs("alerts")

# CAMERA
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

# ALERT COOLDOWN
last_alert_time = 0
cooldown = 5

# FRAME SKIP
frame_skip = 3
frame_count = 0


# ===============================
# GET LOCATION
# ===============================
def get_location():
    try:
        g = geocoder.ip('me')
        lat = g.latlng[0]
        lon = g.latlng[1]
        link = f"https://maps.google.com/?q={lat},{lon}"
        return lat, lon, link
    except:
        return 0,0,"Location unavailable"


# ===============================
# TELEGRAM ALERT FUNCTION
# ===============================
def send_telegram(message, image_path):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    try:

        with open(image_path, "rb") as img:

            response = requests.post(
                url,
                data={
                    "chat_id": CHAT_ID,
                    "caption": message
                },
                files={"photo": img},
                timeout=10
            )

        print("Telegram response:", response.status_code)

    except Exception as e:

        print("Telegram error:", e)


# ===============================
# SAVE ALERT DATA
# ===============================
def save_alert(time_now, lat, lon, image):

    file_exists = os.path.isfile("alerts.csv")

    with open("alerts.csv","a",newline="") as f:

        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["Time","Latitude","Longitude","Image"])

        writer.writerow([time_now,lat,lon,image])


# ===============================
# PLAY ALARM
# ===============================
def play_alarm():

    threading.Thread(
        target=playsound,
        args=("alarm.wav",),
        daemon=True
    ).start()


print("AI Surveillance Started...")


# ===============================
# MAIN LOOP
# ===============================
while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame_count += 1

    if frame_count % frame_skip != 0:

        cv2.imshow("AI Surveillance",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        continue


    frame = cv2.resize(frame,(640,480))

    results = model(frame, imgsz=320)

    for r in results:

        boxes = r.boxes

        for box in boxes:

            cls = int(box.cls[0])
            conf = float(box.conf[0])
            label = model.names[cls]

            print("Detected:",label,"Confidence:",conf)

            current_time = time.time()

            if label in ["knife","gun","fight"] and conf > 0.4 and (current_time-last_alert_time>cooldown):

                last_alert_time = current_time

                print("⚠ Threat Detected!")

                x1,y1,x2,y2 = map(int,box.xyxy[0])

                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)

                cv2.putText(frame,label,(x1,y1-10),
                cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

                # TIME
                time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

                image_path = f"alerts/alert_{file_time}.jpg"

                cv2.imwrite(image_path,frame)

                print("Image saved:",image_path)

                lat,lon,link = get_location()

                message = f"""
🚨 AI SURVEILLANCE ALERT 🚨

Threat: {label}

Time: {time_now}

Location:
{link}
"""

                # SEND TELEGRAM
                threading.Thread(
                    target=send_telegram,
                    args=(message,image_path),
                    daemon=True
                ).start()

                # SAVE CSV
                save_alert(time_now,lat,lon,image_path)

                # ALARM
                play_alarm()

                time.sleep(2)


    cv2.imshow("AI Surveillance",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()