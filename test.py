i=str(input())
while (i != '0'):
	if (i == "muffin" and muffins > 0):
		muffins -= 1
	elif (i == "cupcake" and cupcake > 0):
		cupcake -= 1
	else:
		print("Out of Stock")
print("muffins:", muffins, "cupcakes:",cupcakes)