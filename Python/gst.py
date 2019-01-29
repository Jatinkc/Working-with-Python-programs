net=input("Enter the Amount: ")
qty=input("Enter the Quantity: ")
amt= float(net)* float(qty)

cgst= (amt*9)/100
sgst= (amt*9)/100

print("Initial Amount: ₹",net)
print("Quantity: ",qty)
print("Total Base Amount: ₹",amt)
print("Service TAX: ₹",cgst)
print("State TAX:   "  ,sgst)

print("Final amount Payable: "+"₹",amt+cgst+sgst)



