print("here with we are going to calucate the bmi of the person ")

print("formula == kg / m2 ** m = height to meter into square ")

x= float(input("enter your weight in kgs's = "))

y= float(input("enter your height in in feet : "))

z = float(input("enter the balence height in cm "))

def height(i,z):

i2 = i * 0.30
z2 = z * 0.01
return (y2+z2)*2

bmi = x / height(i,z)

bmi= round((bmi),2)

if bmi > 18 and bmi < 25:
print("bmi", bmi ,"you are healthy")
elif bmi < 18 :
print("bmi", bmi , "your are underweighted ")
else :
bmi > 25
print("bmi", bmi , "you are over weighted ")

print("all the best ")