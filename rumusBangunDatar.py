# Modul untuk menghitung luas bangun ruang

def persegi (a1):
    hasil = a1 ** 2
    print('luas persegi adalah = ', hasil)
    
def persegiPanjang (a1, a2):
    hasil = a1 * a2 
    print('luas persegi panjang adalah = ', hasil)
    
def segitiga (a, t):
    hasil = (a * t) / 2
    print('luas segitiga adalah = ', hasil)
    
def jajargenjang (a, t):
    hasil = a * t
    print('luas jajargenjang adalah = ', hasil)
    
def belahKetupat (d1):
    hasil = 1/2 * (d1 ** 2)
    print('luas belah ketupat adalah = ', hasil)
    
def layang2 (d1, d2):
    hasil = 1/2 * d1 * d2
    print('luas layang-layang adalah = ', hasil)
    
def lingkaran (r):
    hasil = 3.14 * (r ** 2)
    print('luas lingkaran adalah = ', hasil)
    
def trapesium (a, b, t):
    hasil = 1/2 * (a + b) *t
    print('luas trapesium adalah = ', hasil)