# importing the qrcode module
import qrcode
import os

# Function to generate and save a QR code
def generate_and_save_qr(url, filename):
    qr_image=qrcode.make(url)
    qr_image.save(filename)
    qr_image.show()

def main():
    upi_id=input("Enter upiid:").strip()
    
    if not upi_id:
        return 'None'
    
    
    upi_url=f"upi://pay?pa={upi_id}"
    result=f"{upi_id}_upi_qr.png"
    generate_and_save_qr(upi_url, result)

if __name__ == "__main__":
    main()

   