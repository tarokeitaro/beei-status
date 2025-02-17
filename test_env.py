import os
from dotenv import load_dotenv

# Memuat variabel lingkungan dari file .env
load_dotenv(override=True)

# Mengambil nilai dari variabel lingkungan
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
remember = os.getenv('REMEMBER')
target_url = os.getenv('TARGET_URL')

# Menampilkan nilai untuk verifikasi
print(f'Username: {username}')
print(f'Password: {password}')
print(f'Remember: {remember}')
print(f'Remember: {target_url}')