import pygame
import random

def perbaharui_posisi_logo(koordinat_x, koordinat_y, kecepatan_x, kecepatan_y):
    koordinat_x = koordinat_x + kecepatan_x
    koordinat_y = koordinat_y + kecepatan_y
    return koordinat_x, koordinat_y

def perbaharui_arah_logo(kecepatan):
    kecepatan = kecepatan * -1
    return kecepatan

def perbaharui_warna_logo(logo, warna):
    lebar_logo, tinggi_logo = logo.get_size()
    for koordinat_x in range(lebar_logo):
        for koordinat_y in range(tinggi_logo):
            color = logo.get_at((koordinat_x, koordinat_y))
            logo.set_at((koordinat_x, koordinat_y), (warna[0], warna[1], warna[2], color.a))
    return logo

def deteksi_tabrakan(koordinat_x, koordinat_y, lebar_layar, tinggi_layar):
    if koordinat_x < 0 or koordinat_x > lebar_layar:
        return 0
    if koordinat_y < 0 or koordinat_y > tinggi_layar:
        return 1
    return -1

def dapatkan_warna_random():
    return (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))

lebar_layar = 900
tinggi_layar = 600

lebar_logo = 100
tinggi_logo = 60

warna_layar = (0, 0, 0)
warna_logo = (255, 255, 255)

koordinat_x = lebar_layar // 2
koordinat_y = tinggi_layar // 2

kecepatan_x = random.randint(2, 5) * random.choice([-1, 1])
kecepatan_y = random.randint(2, 5) * random.choice([-1, 1])

jumlah_tabrakan = 0

pygame.init()
pygame.display.set_caption("Bouncing DVD Logo")
layar = pygame.display.set_mode((lebar_layar, tinggi_layar))
teks = pygame.font.Font(None, 24)
waktu = pygame.time.Clock()
program_aktif = True

logo_dvd = pygame.image.load('logo_dvd.png')
logo_dvd = pygame.transform.scale(logo_dvd, (lebar_logo, tinggi_logo))
logo_dvd = logo_dvd.convert_alpha()
logo_dvd = perbaharui_warna_logo(logo_dvd.copy(), warna_logo)

while program_aktif:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_aktif = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if kecepatan_y > 0:
                    kecepatan_y = kecepatan_y * -1
            elif event.key == pygame.K_s:
                if kecepatan_y < 0:
                    kecepatan_y = kecepatan_y * -1
            elif event.key == pygame.K_a:
                if kecepatan_x > 0:
                    kecepatan_x = kecepatan_x * -1
            elif event.key == pygame.K_d:
                if kecepatan_x < 0:
                    kecepatan_x = kecepatan_x * -1
            elif event.key == pygame.K_SPACE:
                logo_dvd = perbaharui_warna_logo(logo_dvd.copy(), dapatkan_warna_random())
            elif event.key == pygame.K_q:
                kecepatan_x = (abs(kecepatan_x) + 1) * (1 if kecepatan_x > 0 else -1)
                kecepatan_y = (abs(kecepatan_y) + 1) * (1 if kecepatan_y > 0 else -1)
            elif event.key == pygame.K_e:
                kecepatan_x = max(0, abs(kecepatan_x) - 1) * (1 if kecepatan_x > 0 else -1)
                kecepatan_y = max(0, abs(kecepatan_y) - 1) * (1 if kecepatan_y > 0 else -1)
            elif event.key == pygame.K_r:
                kecepatan_x = 0
                kecepatan_y = 0

    layar.fill(warna_layar)

    koordinat_x, koordinat_y = perbaharui_posisi_logo(koordinat_x, koordinat_y, kecepatan_x, kecepatan_y)

    hasil_deteksi = deteksi_tabrakan(koordinat_x, koordinat_y, lebar_layar - lebar_logo, tinggi_layar - tinggi_logo)

    if hasil_deteksi != -1:
        warna_logo = dapatkan_warna_random()
        logo_dvd = perbaharui_warna_logo(logo_dvd.copy(), warna_logo)
        jumlah_tabrakan += 1
    if hasil_deteksi == 0:
        kecepatan_x = perbaharui_arah_logo(kecepatan_x)
    elif hasil_deteksi == 1:
        kecepatan_y = perbaharui_arah_logo(kecepatan_y)

    layar.blit(logo_dvd, (koordinat_x, koordinat_y))

    pygame.display.flip()

    waktu.tick(60)

pygame.quit()