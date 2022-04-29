import requests
import time

GENDER = "YOUR_GENDER"
WEIGHT_KG = "YOUR_WEIGHT"
HEIGHT_CM = "YOUR_HEIGHT"
AGE = "YOUR_AGE"
NUTRITIONIX_API_KEY = "YOUR_APP_KEY"
NUTRITIONIX_APP_ID = "YOUR_APP_ID"

nutritionix_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "YOUR_SHEET_ENDPOINT"

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-remote-user-id": "0"  # Development Mode
}
sheet_header = {
    "Authorization": "Bearer YOUR_BEARER_TOKEN"
}
current_date = time.strftime("%d/%m/%Y")
current_time = time.strftime("%H:%M:%S")
workout = input("What did you do today: ")
exercise_params = {
    "query": workout,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=nutritionix_exercise_endpoint, json=exercise_params, headers=headers)

for exercise in response.json()["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=sheet_header)
    print(sheety_response.text)
