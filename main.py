from food import Food
from drink import Drink

food1 = Food('Roti Lapis', 5, 330)
food2 = Food('Kue Coklat', 4, 450)
food3 = Food('Kue Sus', 2, 180)

foods = [food1, food2, food3]

drink1 = Drink('Kopi', 3, 180)
drink2 = Drink('Jus Jeruk', 2, 350)
drink3 = Drink('Espresso', 3, 30)

drinks = [drink1, drink2, drink3]

print('''Welcome to Python Cafe
      ''')

print('Makanan')
index = 0
for food in foods:
    print(str(index) + '. ' + food.info())
    index += 1

print('Minuman')
index = 0
for drink in drinks:
    print(str(index) + '. ' + drink.info())
    index += 1

print('--------------------')

#Menggunakan try dan while untuk mencegah input ilegal ke dalam pesanan

try:
    food_order = int(input('Masukkan kode makanan: '))
except(ValueError):
    print("Kode makanan tidak ada. Mohon ulangi kembali.")
    food_order = int(input('Masukkan kode makanan: '))
while(food_order<0) or (food_order>2):
     print("Kode makanan tidak ada. Mohon ulangi kembali")
     food_order = int(input('Masukkan kode makanan: '))
else:
    selected_food = foods[food_order]

    
try:
    drink_order = int(input('Masukkan kode minuman: '))
except(ValueError):
    print("Kode minuman tidak ada. Mohon ulangi kembali.")
    drink_order = int(input('Masukkan kode minuman: '))
while(drink_order<0) or (drink_order>2):
     print("Kode minuman tidak ada. Mohon ulangi kembali")
     drink_order = int(input('Masukkan kode minuman: '))
else:
    selected_drink = drinks[drink_order]

# Ambil input dari console dan tetapkan ke variable count
# Mencegah pemesanan berjumlah kurang dari atau sama dengan 0
try:
    count = int(input('Masukkan jumlah paket yang diinginkan (Diskon 10% untuk 3 atau lebih): '))
except(ValueError):
    print("Mohon hanya masukkan angka.")
    count = int(input('Masukkan jumlah paket yang diinginkan (Diskon 10% untuk 3 atau lebih): '))   
while(count<1):
    print("Pemesanan minimal adalah 1 paket")
    count = int(input('Masukkan jumlah paket yang diinginkan (Diskon 10% untuk 3 atau lebih): '))   
   

# Panggil method get_total_price dari selected_food dan selected_drink
result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

print('--------------------')

# Menunjukkan waktu transaksi
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print(dt_string)

# Cetak 'Total harga adalah $____'
print('Total harga adalah $' + str(result))

# Cetak 'Terima kasih sudah berbelanja.'
print('''
Terima kasih sudah berbelanja.
Selamat datang kembali.
''')

print('--------------------')

"""
Module: Menyimpan Transaksi ke File (History Transaksi)
"""

def writeHistory(date, total):
    text = date + "\n" + "Total harga adalah $" + str(total) + "\n\n"
    file = open('history.txt', 'at')
    file.write(text)

writeHistory(dt_string, result)
