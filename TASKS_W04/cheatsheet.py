
Children = 3
Hometown = "Klaukkala" \
#Lista
TownsInFinland = ["Lahti", "Helsinki", "Espoo", "Vantaa", "Klaukkala"]
RandomIformation = ["Liisa", 34, True, Children, Hometown]
print(TownsInFinland[0])
TownsInFinland.append("Tampere")
print(TownsInFinland)

NumOfTowns = len(TownsInFinland) #vastaus 6
print(TownsInFinland[NumOfTowns - 1])

Kunta = ["Asikkala", "Hollola", "Karvia", "Kempele"]
Towns = ["Lahti", "Helsinki", "Lappeenranta", "Tampere", "Oulu"]
KuntaAndTowns = [Kunta, Towns]
print(KuntaAndTowns[1][-2]) #vastaus Tampere #-2 koska listassa on 5 alkiota ja indeksi alkaa nollasta 
#Toinen lista  koska 1 tarkoitaa toista listaa
Towns.sort() #Järjestää aakkosjärjestykseen
print(Towns)
# Towns.reverse() #Kääntää järjestyksen toisin päin
# print(Towns)
# Towns.remove("Oulu") #Poistaa Oulun listasta
# print(Towns)
# Towns.clear() #Tyhjentää listan

Teacher = {
   'Name': 'Liisa',
    'Age': 34,
    'Hometown': 'Lahti',
}
print(Teacher['Name'])

Teacher['email']: 'liisa.liikainen@lab.fi' #Lisää uuden avain-arvo parin
print(Teacher)

for key in Teacher: #Käy läpi sanakirjan avaimet
    print(key, end=' ') #Tulostaa avaimet
    print(Teacher[key]) #Tulostaa arvot

Student = [
    {'Name': 'Matti', 'Age': 24, 'Hometown': 'Helsinki',}, 
    {'Name': 'Teppo','Age': 22,'Hometown': 'Espoo',},
    {'Name': 'Liisa', 'Age': 23, 'Hometown': 'Vantaa',}
    ] #Lista, jossa on kolme sanakirjaa
print(Student[0]['Name']) #Tulostaa Matti koska ensimäinen opiskelija on indeksi 0 ja nimi on avain 'Name'

Cities = {
    'Finland': ['Helsinki', 'Espoo', 'Vantaa', 'Tampere'],
    'Sweden': ['Stockholm', 'Gothenburg', 'Malmo'],
    'Norway': ['Oslo', 'Bergen', 'Trondheim']
} #Sanakirja, jossa on kolme avainta ja arvona lista Dictionary in a list
print(Cities['Sweden'][0]) #Tulostaa Stockholm koska Ruotsin lista on avain 'Sweden' ja indeksi 0 on ensimmäinen kaupunki

for Town in Towns : #Käy läpi listan
    print(f"The town of {Town}") #Tulostaa jokaisen kaupungin eteen The town of
print(f"All of the towns {Towns}") #Tulostaa koko listan jokaisen kaupungin jälkeen

for i in range(1,10): #Tulostaa luvut 1-9
    print(i)
for i in range(1,10):
    print(i, end=' ') #Tulostaa luvut 1-9 samalle riville
print() #Rivinvaihto
for i in range(1,10, 3):#Tulostaa luvut 1-9 kahden välein
    print(i, end=' ')

print()

Total = 0
for i in range(1,101): #Laskee luvut 1-100 yhteen
    Total += i  #Total = Total + i
    print(Total) #Tulostaa jokaisen vaiheen yhteenlaskusta
print(Total) #Tulostaa lopullisen summan

print()

for i in range(9):
    if i == 3: #Jos i on 3, hyppää yli
        continue
    print(i, end=' ') #Tulostaa luvut 0-8 paitsi 3

#For ja while ja niihin liityvät komennot continue ja break

continueLoop = True
while continueLoop == True: #Toistaa niin kauan kuin continueLoop on True
    if input("Do you want to continue? (y/n): ") == 'n': #Kysyy käyttäjältä haluaako jatkaa
        continueLoop = False #Jos käyttäjä vastaa n, asettaa continueLoopin Falseksi

while True: #Toistaa ikuisesti
    if input("Do you want to continue?: ") != 'yes': #Kysyy käyttäjältä haluaako jatkaa
        break #Jos käyttäjä vastaa n, lopettaa silmukan
    else:
        continue #Jos käyttäjä vastaa jotain muuta kuin yes, jatkaa silmukkaa
    