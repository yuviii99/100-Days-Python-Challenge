import requests
from twilio.rest import Client

api_key = "YOUR_API_KEY"
account_sid = "TWILIO ACCOUNT SID"
auth_token = "TWILIO ACCOUNT AUTH_TOKEN"

parameters = {
    "lat": float("YOUR LATITUDE"),
    "lon": float("YOUR LONGITUDE"),
    "appid": api_key,
    "exclude": "current, minutely, daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
hourly_data = data["hourly"][0:12]
will_rain = False

for hour_data in hourly_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if True:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Bring an Umbrella",
        from_="TWILIO_PHONE_NUMBER",
        to="YOUR_VERIFIED_PHONE_NUMBER"
    )

print(message.sid)
