import requests
from datetime import datetime

APP_ID = "d404bc0d"
API_KEY = "b339ecdfd13975897109c493a301c739"
EXERS_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_POST_ENDPOINT = "https://api.sheety.co/86f008a0b37c80ff68b03f75ac5f340c/myWorkouts/workouts"

exercise_done = input("What exercise have you completed?")

nutritionix_params = {
   "gender":"female",
    "weight_kg": 53,
    "height_cm": 165,
    "age": 19,
    "query": f"{exercise_done}"
}

headers = {
    "x-app-id":"d404bc0d",
    "x-app-key":"b339ecdfd13975897109c493a301c739",
}


response = requests.post(url=EXERS_ENDPOINT,json=nutritionix_params, headers=headers)
response= response.json()
#print(response)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in response["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_POST_ENDPOINT, json=sheet_inputs)

    print(sheet_response.text)

