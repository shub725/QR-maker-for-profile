import qrcode

n = int(input("How many profiles do you want to create QR codes for? "))

for i in range(n):
    url = input(f"Enter URL for profile {i+1}: ")
    name = input("Enter name for this QR file: ")
    
    qr = qrcode.make(url)
    qr.save(f"{name}.png")
    
    print(f"QR code saved as {name}.png")

print("All QR codes generated!")