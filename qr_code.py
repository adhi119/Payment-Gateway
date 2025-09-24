#importing the qrcode module
import qrcode

#enter the upid
upi_id=input("enter upi Id:")

#https://url?upid&name&amount&massage
phonepay_url=f'url://pay?pa={upi_id}'
paytm_url=f'{upi_id}'
google_pay_url=f'{upi_id}'

#generatinng the qrcode using the urls
phonepay_qr=qrcode.make(phonepay_url)
paytm_qr=qrcode.make(paytm_url)
google_pay_qr=qrcode.make(google_pay_url)

#save this qrcode in img format
phonepay_qr.save('phone_pay.png')
paytm_qr.save('paytm.png')
google_pay_qr.save('google_pay_qr.png')

#showing the qrcode of each payment with significant upid
phonepay_qr.show()
#paytm_qr.show()
#google_pay_qr.show()
