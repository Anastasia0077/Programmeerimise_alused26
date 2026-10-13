#siia kirjutame mis moodulid tahame importida ja hiljem kasutame
import math
print("Tere tulemast!") #kommentaar
print("Esimene programm, mis on kirjutatud Pythonis.") #sep=" ", end="/n" vaikimisi väärtus kasutatakse
# #muutujad
# kursus=2 #int
# print("Ma opin",1,".kursusel") #sep=" ", end="/n"
# print("Ma opin",kursus,".kursusel",sep="***",end=". ")
# kursus=int(input("Aga sina?")) #str->int
# print("Tore! Sa opid",kursus,".kursusel. Aga jargmisel aastal",kursus+1,"kursusel")
# nimi = input("Mis on sinu nimi? ")
# print("Tere,", nimi)
# print(nimi, "Opib ",kursus,". kursusel")

a = input("Esimene arv: ")
b = input("Teine arv: ")
print(a + b)

a = int(input("Esimene arv: "))
b = int(input("Teine arv: "))
print(a + b)
#Põhioperatsioonid: + - * / // % ** punkt 1.5
# astendamine	**	2 ** 3	8
# korrutamine	*	4 * 5	20
# jagamine	/	7 / 2	3.5
# jagamise täisarvuline osa	//	7 // 2	3
# jagamisjääk	%	7 % 2	1
# liitmine	+	10 + 3	13
# lahutamine	-	9 - 4	5

a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a ** b)

a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a * b)

a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a / b)

a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a // b)

a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a % b)

a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a + b)

a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a - b)

a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
print(a,"+",b,"=",a + b) #liitmine
print(a,"-",b,"=",a - b) #lahutamine
print(a,"*",b,"=",a * b) #korrutamine
print(a,"/",b,"=",a / b) #jagamine
print(a,"//",b,"=",a // b) #jagamise täisarvuline osa
print(a,"%",b,"=",a % b) #jagamisjääk
print(a,"**",b,"=",a ** b) #astendamine

#f-sõne kasutamine 
# nimi = "Mari"
# punktid = 87
# print(f"{nimi} sai {punktid} punkti.")
# hind = 19.9
# kogus = 3
# print(f"Kokku: {hind * kogus:.2f} eurot") #ühe kümnendkohaga

# #stringide ühendamine ja korrutamine 
# print("Tere" + " " + "päevast")
# print("-" * 20)
# vanus = 17
# print("Vanus: " + str(vanus))

#math mooduli kasutamine
print("Pii väärtus:", math.pi)
print("√16 =", math.sqrt(16))
print("sin(π/2) =", math.sin(math.pi / 2))
print("sin(30°) =", round(math.sin(math.radians(30)), 2))
print("5! =", math.factorial(5))