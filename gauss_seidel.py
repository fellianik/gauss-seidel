'''
Nama  : Felliani Kurniawati
NPM   : 20081010085
Prodi : Informatika
MK    : Metode Numerik Kelas A
'''

print("=" * 75)
print(f"|{'I':>2} | {'x1':^20} | {'x2':^20} | {'x3':^20} |")
print("=" * 75)

akhir = [0.0, 0.0, 0.0];
terbaru = [99.0, 99.0, 99.0];
i = 0

while True:

  print(f"|{i:3} | {akhir[0]:<20} | {akhir[1]:<20} | {akhir[2]:<20} |")

  terbaru[0] = (7.85 + 0.1 * akhir[1] + 0.2 * akhir[2]) / 3
  terbaru[1] = (-190.3 - 0.1 * terbaru[0] + 0.3 * akhir[2]) / 7
  terbaru[2] = (71.4 - 0.3 * terbaru[0] + 0.2 * terbaru[1]) / -10

  if terbaru[0] == akhir[0] and terbaru[1] == akhir[1] and terbaru[2] == akhir[2]:
    print(f"|{(i + 1):3} | {terbaru[0]:<20} | {terbaru[1]:<20} | {terbaru[2]:<20} |")
    break

  akhir[0] = terbaru[0];
  akhir[1] = terbaru[1];
  akhir[2] = terbaru[2];

  i += 1

print("=" * 75)
print(f"{f'| Iterasi Terakhir: {i}':74}|")
print(f"{f'| Nilai X : {akhir}':74}|")
print("=" * 75)
