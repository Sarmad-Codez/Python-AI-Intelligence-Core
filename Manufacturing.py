# User se car ka manufacturing year poochna
car_year = int(input("Apni car ka model (year) enter karo: "))

# Year ke mutabiq status check karna
if car_year >= 2020:
    print("Zabardast! Yeh toh bilkul latest car hai.")
elif car_year >= 2006 and car_year <= 2012:
    print("Wah! Yeh toh legendary Reborn ka era hai.")
else:
    print("Old is gold! Classic model hai jani.")