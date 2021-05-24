subtotal = float(input("Enter the subtotal: "))
rate = float(input("Enter the gratuity rate: "))

gratuity = subtotal * rate / 100
total = subtotal + gratuity

print("The gratuity is", int(gratuity * 100) / 100,
      "and the total is", int(total * 100) / 100)
