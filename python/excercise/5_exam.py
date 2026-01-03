#write a prgram to calculate GST tax amount from given bill amount and tax rate
bill_amount=0
tax_rate=0

bill_amount=input("Enter bill_amount=")
tax_rate=input("Enter tax_rate=")

bill_amount=float(bill_amount)
tax_rate=float(tax_rate)

gst=bill_amount*tax_rate/100

print("GST tax amount is",gst)