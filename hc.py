from bs4 import BeautifulSoup
import os
import subprocess

# Use npm bin to get the path to globally installed packages
npm_bin_path = subprocess.run(['npm', 'bin', '-g'], capture_output=True, text=True).stdout.strip()
purgecss_path = os.path.join(npm_bin_path, 'purgecss.cmd' if os.name == 'nt' else 'purgecss')

# اسم ملف CSS الذي تريد تنظيفه
css_file = 'king_main.css'

# اسم ملف HTML الذي يحتوي على العناصر التي قد تستخدمها صفحتك
html_file = 'index.html'

# اسم الملف الذي سيحتوي على الكود بعد التنظيف
purged_css_file = 'main.css'

# استخدام PurgeCSS لحذف الأكواد غير المستخدمة
subprocess.run([purgecss_path, '--css', css_file, '--content', html_file, '--output', purged_css_file])

# قراءة الملف الناتج بعد تنظيفه
with open(purged_css_file, 'r', encoding='utf-8') as f:
    purged_css_code = f.read()

# تحويل الملف إلى SCSS بتغيير الامتداد فقط
purged_scss_code = purged_css_code.replace('.css {', '.scss {').replace('.css,', '.scss,')

# حفظ الملف النهائي
with open('main.scss', 'w', encoding='utf-8') as f:
    f.write(purged_scss_code)

print("تم تنظيف الأكواد وتحويل الملف بنجاح.")
