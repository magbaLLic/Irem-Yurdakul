def toplama(x, y):
    return x + y

def cıkarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    return x / y


print("İşlem Seçiniz.")
print("1. Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")

while True:
   
    secim = input("Lütfen işlemlerden birini seçiniz. (1/2/3/4): ")

    
    if secim in ('1', '2', '3', '4'):
        num1 = int(input("Lütfen ilk sayıyı giriniz: "))
        num2 = int(input("Lütfen ikinci sayıyı giriniz: "))

        if secim == '1':
            print(num1, "+", num2, "=", toplama(num1, num2))

        elif secim == '2':
            print(num1, "-", num2, "=", cıkarma(num1, num2))

        elif secim == '3':
            print(num1, "*", num2, "=", carpma(num1, num2))

        elif secim == '4':
            print(num1, "/", num2, "=", bolme(num1, num2))
        break
    else:
        print("Geçersiz Giriş")
