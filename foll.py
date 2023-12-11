from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# معلومات الحساب
username = "اسم_المستخدم"
password = "كلمة_المرور"

# رابط حساب المستخدم الذي ترغب في متابعته
target_profile = "https://twitter.com/target_user"

# إعداد متصفح Selenium
driver = webdriver.Chrome()

# فتح تويتر
driver.get("https://twitter.com")

# انتظر قليلاً لحين تحميل الصفحة
time.sleep(2)

# العثور على حقل اسم المستخدم وإدخال قيمته
username_field = driver.find_element_by_name("session[username_or_email]")
username_field.send_keys(username)

# العثور على حقل كلمة المرور وإدخال قيمته
password_field = driver.find_element_by_name("session[password]")
password_field.send_keys(password)

# النقر على زر تسجيل الدخول
password_field.send_keys(Keys.RETURN)

# انتظار لتحميل الصفحة بعد تسجيل الدخول
time.sleep(2)

# فتح ملف المستخدم الهدف
driver.get(target_profile)

# النقر على زر متابعة
follow_button = driver.find_element_by_xpath('//span[text()="Follow"]')
follow_button.click()

# انتظار لحين يتم إتمام العملية
time.sleep(5)

# إغلاق المتصفح
driver.quit()
