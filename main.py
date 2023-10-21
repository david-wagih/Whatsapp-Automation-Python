import pywhatkit
import time
import pyautogui
import csv


# Function to send WhatsApp message
def send_whatsapp_message(phone_number, message):
    pywhatkit.sendwhatmsg_instantly(phone_number, message, 5)
    time.sleep(5)

    pyautogui.click()

    # Simulate typing the message
    pyautogui.press("enter")

    # Wait for a few seconds to ensure that the WhatsApp window is open
    time.sleep(5)


# Function to close WhatsApp tab
def close_whatsapp_tab():
    pyautogui.hotkey("command", "w")
    time.sleep(2)  # Wait for the tab to close


# Rest of the static message
rest_of_the_message = """\n برجاء تحميل تطبيق مدرسة الشمامسة لتستطيع معرفة مواعيد وأماكن كورساتك من خلال هذا اللينك\n Android version: \n https://play.google.com/store/apps/details?id=com.shamamsa.shamamsa_app2 \n Apple version: \n https://apps.apple.com/eg/app/athanasius-deacons/id6444948964   \n App Gallery Version:  \n  https://appgallery.huawei.com/app/C109401311  \n يمكن التواصل مع المدرسة ومعرفة الأخبار 
من خلال:  \n -رقم الواتساب 01558898731   \n -صفحة المدرسة على الفيسبوك \n -Whatsapp Channel: https://whatsapp.com/channel/0029Va439pf77qVLp72kjg1N"""

# Read data from CSV file
csv_file_path = "YY.csv"  # Replace with your actual CSV file path
with open(csv_file_path, mode="r") as file:
    csv_reader = csv.reader(file)

    # Skip header if there is one
    header = next(csv_reader, None)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Assuming the phone number is in the first column and the message is in the second column
        phone_number = "+20" + row[2]
        user_name = row[3]
        user_password = row[4]
        custom_message = f"مرحبًا بك {user_name} في مدرسة الشمامسة\nكلمة المرور: {user_password}\nثم إنشاء كلمة مرور جديدة\nنبدأ الحصص الجمعة 27 أكتوبر ٢٠٢٣\n{rest_of_the_message}"

        print(f"Sending message to {user_name} at {phone_number}:")
        print(custom_message)

        # Send WhatsApp message
        send_whatsapp_message(phone_number, custom_message)

        # Close WhatsApp tab after sending
        close_whatsapp_tab()
