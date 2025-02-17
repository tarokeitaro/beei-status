import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

# Memuat variabel lingkungan dari file .env
load_dotenv(override=True)

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
remember = os.getenv('REMEMBER')
target_url = os.getenv('TARGET_URL')

# URL halaman login
login_url = 'https://beei.org/index.php/EEI/login/signIn'

# Membuat sesi
session = requests.Session()

# Melakukan login
response = session.post(login_url, data={'username': username, 'password': password, 'remember': remember})

# Memeriksa apakah login berhasil
if response.ok:
    # Mengakses halaman target setelah login berhasil
    response = session.get(target_url)
    
    # Parsing HTML dengan BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Mencari div dengan ID "status"
    status_div = soup.find('div', id='status')
    
    if status_div:
        # Mencari tabel di dalam div tersebut
        table = status_div.find('table', class_='data')
        
        if table:
            # Mencari semua baris dalam tabel
            rows = table.find_all('tr')
            
            # Iterasi melalui setiap baris dan mengekstrak label dan nilai
            for row in rows:
                label_cell = row.find('td', class_='label')
                value_cell = row.find('td', class_='value')
                
                # Memastikan bahwa kedua elemen ditemukan sebelum mengaksesnya
                if label_cell and value_cell:
                    label = label_cell.get_text(strip=True)
                    value = value_cell.get_text(strip=True)
                    print(f'{label}: {value}')
                else:
                    print('Salah satu elemen label atau value tidak ditemukan dalam baris ini.')
        else:
            print('Tabel tidak ditemukan dalam div status.')
    else:
        print('Div dengan ID "status" tidak ditemukan.')
else:
    print('Login gagal')