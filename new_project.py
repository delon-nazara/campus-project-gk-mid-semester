import pygame
import random
import math

# Fungsi untuk menggambar objek
def gambar_bentuk_objek(layar, warna, koordinat_x, koordinat_y, radius, sisi):
    sudut_awal = -math.pi / 2
    titik_objek = []
    
    # Menghitung posisi titik-titik objek
    for i in range(sisi):
        x = koordinat_x + radius * math.cos(sudut_awal + i * 2 * math.pi / sisi)
        y = koordinat_y + radius * math.sin(sudut_awal + i * 2 * math.pi / sisi)
        titik_objek.append((x, y))

    # Gambar objek pada layar
    pygame.draw.polygon(layar, warna, titik_objek)  

    # Menghitung ukuran objek
    min_x = min(titik_objek, key=lambda t: t[0])[0]
    max_x = max(titik_objek, key=lambda t: t[0])[0]
    min_y = min(titik_objek, key=lambda t: t[1])[1]
    max_y = max(titik_objek, key=lambda t: t[1])[1]

    lebar_objek = max_x - min_x 
    tinggi_objek = max_y - min_y 

    return (lebar_objek, tinggi_objek)

# Fungsi untuk memperbaharui posisi objek
def perbaharui_posisi_objek(koordinat_x, koordinat_y, kecepatan_x, kecepatan_y):
    koordinat_x = koordinat_x + kecepatan_x
    koordinat_y = koordinat_y + kecepatan_y
    return koordinat_x, koordinat_y

# Fungsi untuk memperbaharui arah objek
def perbaharui_arah_objek(kecepatan):
    kecepatan = kecepatan * -1
    return kecepatan

# Fungsi untuk mendeteksi tabrakan objek dengan layar
def deteksi_tabrakan_layar(koordinat_x, koordinat_y, lebar_layar, tinggi_layar):

    # arti kode tabrakan
    # 0 = tidak ada tabrakan
    # 1 = tabrakan terjadi di bagian kiri atas layar
    # 2 = tabrakan terjadi di bagian atas layar
    # 3 = tabrakan terjadi di bagian kanan atas layar
    # 4 = tabrakan terjadi di bagian kanan layar
    # 5 = tabrakan terjadi di bagian kanan bawah layar
    # 6 = tabrakan terjadi di bagian bawah layar
    # 7 = tabrakan terjadi di bagian kiri bawah layar
    # 8 = tabrakan terjadi di bagian kiri layar

    # Menentukan kode tabrakan berdasarkan posisi tabrakan objek dengan layar
    kode_tabrakan = 0
    if koordinat_x < 0:
        kode_tabrakan = 8  
        if koordinat_y < 0:
            kode_tabrakan = 1  
        elif koordinat_y > tinggi_layar:
            kode_tabrakan = 7 
    elif koordinat_x > lebar_layar:
        kode_tabrakan = 4  
        if koordinat_y < 0:
            kode_tabrakan = 3  
        elif koordinat_y > tinggi_layar:
            kode_tabrakan = 5  
    elif koordinat_y < 0:
        kode_tabrakan = 2  
    elif koordinat_y > tinggi_layar:
        kode_tabrakan = 6  

    return kode_tabrakan

# Fungsi untuk mendapatkan warna acak
def dapatkan_warna_acak():
    return (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

# Fungsi untuk menampilkan informasi pada layar
def tampilkan_informasi(layar, teks, koordinat_x, koordinat_y, kecepatan_x, kecepatan_y, warna, tabrakan, sisi):
    # Menyusun informasi untuk ditampilkan
    teks_sisi      = f"Jumlah Sisi Objek:  {sisi}"
    teks_tabrakan  = f"Jumlah Tabrakan Layar:  {tabrakan}"
    teks_kecepatan = f"Kecepatan Objek (X, Y):  ({kecepatan_x}, {kecepatan_y})"
    teks_koordinat = f"Koordinat Objek (X, Y):  ({koordinat_x}, {koordinat_y})"
    teks_warna     = f"Warna Objek (R, G, B):  {warna}"
    
    # Render teks untuk ditampilkan
    teks1 = teks.render(teks_sisi, True, (255, 255, 255))
    teks2 = teks.render(teks_tabrakan, True, (255, 255, 255))
    teks3 = teks.render(teks_kecepatan, True, (255, 255, 255))
    teks4 = teks.render(teks_koordinat, True, (255, 255, 255))
    teks5 = teks.render(teks_warna, True, (255, 255, 255))
    
    # Menampilkan teks pada layar
    layar.blit(teks1, (20, 20))
    layar.blit(teks2, (20, 50))
    layar.blit(teks3, (20, 80))
    layar.blit(teks4, (20, 110))
    layar.blit(teks5, (20, 140))

# Inisialisasi layar
lebar_layar = 900
tinggi_layar = 600

# Inisialisasi objek
lebar_objek = 150
tinggi_objek = 150
radius_objek = 75
jumlah_sisi_objek = 3

# Inisialisasi warna layar dan objek
warna_layar = (0, 0, 0)
warna_objek = (255, 255, 255)

# Inisialisasi koordinat awal objek
koordinat_x = lebar_layar // 2 - radius_objek
koordinat_y = tinggi_layar // 2 - radius_objek

# Inisialisasi kecepatan awal objek
kecepatan_x = random.randint(2, 5) * random.choice([-1, 1])
kecepatan_y = random.randint(2, 5) * random.choice([-1, 1])

# Inisialisasi status tabrakan dan jumlah tabrakan
kode_tabrakan = 0
jumlah_tabrakan = 0

# Inisialisasi status program
program_dijeda = False
informasi_ditampilkan = False

# Inisialisasi library pygame
pygame.init()
pygame.display.set_caption("Proyek Grafika Komputer")

# Inisialisasi layar, teks, dan waktu
layar = pygame.display.set_mode((lebar_layar, tinggi_layar))
teks = pygame.font.Font(None, 30)
waktu = pygame.time.Clock()
program_aktif = True

# Looping selama program aktif
while program_aktif:

    # Memeriksa inputan dari pengguna
    for event in pygame.event.get():

        # Pengguna menekan tombol keluar
        if event.type == pygame.QUIT:
            program_aktif = False

        # Pengguna menekan salah satu tombol
        if event.type == pygame.KEYDOWN:

            # Mengubah arah objek
            if event.key == pygame.K_w and kecepatan_y > 0:
                kecepatan_y *= -1
            elif event.key == pygame.K_s and kecepatan_y < 0:
                kecepatan_y *= -1
            elif event.key == pygame.K_a and kecepatan_x > 0:
                kecepatan_x *= -1
            elif event.key == pygame.K_d and kecepatan_x < 0:
                kecepatan_x *= -1

            # Menjeda program
            elif event.key == pygame.K_p:
                program_dijeda = not program_dijeda

            # Menampilkan informasi
            elif event.key == pygame.K_i:
                informasi_ditampilkan = not informasi_ditampilkan

            # Mengganti warna objek
            elif event.key == pygame.K_c:
                warna_objek = dapatkan_warna_acak()

            # Mereset koordinat objek
            elif event.key == pygame.K_m:
                koordinat_x = lebar_layar // 2 - lebar_objek // 2
                koordinat_y = tinggi_layar // 2 - tinggi_objek // 2

            # Mereset kecepatan objek
            elif event.key == pygame.K_r:
                kecepatan_x = 0
                kecepatan_y = 0

            # Mengubah jumlah sisi objek
            elif event.key == pygame.K_MINUS and jumlah_sisi_objek > 3:
                jumlah_sisi_objek -= 1
            elif event.key == pygame.K_EQUALS:
                jumlah_sisi_objek += 1

            # Mengatur kecepatan objek (sumbu x dan y bersamaan)
            elif event.key == pygame.K_q:
                kecepatan_x = (abs(kecepatan_x) + 1) * (1 if kecepatan_x > 0 else -1)
                kecepatan_y = (abs(kecepatan_y) + 1) * (1 if kecepatan_y > 0 else -1)
            elif event.key == pygame.K_e:
                kecepatan_x = max(0, abs(kecepatan_x) - 1) * (1 if kecepatan_x > 0 else -1)
                kecepatan_y = max(0, abs(kecepatan_y) - 1) * (1 if kecepatan_y > 0 else -1)

            # Mengatur kecepatan objek (hanya sumbu x)
            elif event.key == pygame.K_1:
                kecepatan_x = (abs(kecepatan_x) + 1) * (1 if kecepatan_x > 0 else -1)
            elif event.key == pygame.K_2:
                kecepatan_x = max(0, abs(kecepatan_x) - 1) * (1 if kecepatan_x > 0 else -1)

            # Mengatur kecepatan objek (hanya sumbu y)
            elif event.key == pygame.K_9:
                kecepatan_y = (abs(kecepatan_y) + 1) * (1 if kecepatan_y > 0 else -1)
            elif event.key == pygame.K_0:
                kecepatan_y = max(0, abs(kecepatan_y) - 1) * (1 if kecepatan_y > 0 else -1)

    # Jika program tidak dijeda
    if not program_dijeda:

        # Menetapkan warna layar
        layar.fill(warna_layar)  

        # Memperbaharui posisi objek
        koordinat_x, koordinat_y = perbaharui_posisi_objek(koordinat_x, koordinat_y, kecepatan_x, kecepatan_y)

        # Mendeteksi tabrakan objek dengan layar
        hasil_deteksi = deteksi_tabrakan_layar(koordinat_x, koordinat_y, lebar_layar - lebar_objek, tinggi_layar - tinggi_objek)

        # Jika tabrakan sekarang berbeda dengan tabrakan sebelumnya
        if hasil_deteksi != kode_tabrakan:
            kode_tabrakan = hasil_deteksi

            # Jika tabrakan terdeteksi
            if kode_tabrakan != 0:

                # Perbaharui jumlah tabrakan
                jumlah_tabrakan += 1

                # Tambah sisi objek setiap 5x tabrakan
                # if (jumlah_tabrakan % 5 == 0):  
                jumlah_sisi_objek += 1
                
                # Ganti warna objek
                warna_objek = dapatkan_warna_acak()  

                # Ubah arah objek jika terjadi tabrakan
                if kode_tabrakan == 2 or kode_tabrakan == 6:
                    kecepatan_y = perbaharui_arah_objek(kecepatan_y)
                elif kode_tabrakan == 4 or kode_tabrakan == 8:
                    kecepatan_x = perbaharui_arah_objek(kecepatan_x)
                else:
                    kecepatan_x = perbaharui_arah_objek(kecepatan_x)
                    kecepatan_y = perbaharui_arah_objek(kecepatan_y)

        # Gambar objek dengan jumlah sisi yang sesuai
        lebar_objek, tinggi_objek = gambar_bentuk_objek(layar, warna_objek, koordinat_x + radius_objek, koordinat_y + radius_objek, radius_objek, jumlah_sisi_objek)

        # Tampilkan informasi objek
        if informasi_ditampilkan:
            tampilkan_informasi(layar, teks, koordinat_x, koordinat_y, kecepatan_x, kecepatan_y, warna_objek, jumlah_tabrakan, jumlah_sisi_objek)
        
        # Update tampilan layar
        pygame.display.flip()  

        # Batasi frame rate ke 60 FPS
        waktu.tick(60) 

# Menutup pygame setelah program selesai
pygame.quit()  