import csv
import sys


def shortenList(file):
	file = open(file, encoding='utf-8')
	oldList = file.read().splitlines()
	newList = [x for x in oldList if "=" in x]
	newList = [x for x in newList if "end" not in x]

	return newList


def cutCountry(line):
	info = line.split("(")
	code = info[1]

	return(code[:3])


# deprecated
def cutPoliticalPower(line):
	info = line.split(" = ")
	number = info[1]
	if number[0].isdigit() or number[1].isdigit():
		return number
	else:
		number = number.split("(")
		number = number[1]
		number = number[:-1]

		return number


def cutDay(line):
	info = line.split(" = ")

	time = int(info[1]) - 706653

	if time % 2== 0:
		time = time - 1

	if time > 30:
		time = int(time / 30) + 1

	return time


def cutArmy(line):
	info = line.split(" = ")
	if info[1].isdigit():
		return info[1]
	else:
		newInfo = info[1].split("(")
		number = newInfo[1]
		number = number[:-1]

		return number


def cutEquip(line):
	info = line.split(" = ")
	if info[1][0].isdigit() or "-" in info[1] and info[1][1].isdigit():
		return info[1]
	else:
		newInfo = info[1].split("(")
		number = newInfo[1]
		number = number[:-1]

		return number


def cutMpw(line):
	info = line.split(" = ")
	if "(" in info[1]:
		newInfo = info[1].split("(")
		return newInfo[1][:-1]

	return info[1]


def breakDownList(inputList):
	dict = {
		"countryTag":"" ,
		"time": "", 
		"numArmies":"",
		"infantryEquipment":"",
		"ships":"",
		"manpower":"",
		"fuel":"",
		"tankLight":"",
		"tankMedium":"",
		"tankHeavy":"",
	}

	data = []

	for i in inputList:
		if i != "===================================":
			if "1ogt" in i:
				dict["countryTag"] = cutCountry(i)
			if "3numarmie" in i:
				dict["numArmies"] = cutArmy(i)
			if "4totdays" in i:
				dict["time"] = cutDay(i)
			if "5equipinf" in i:
				dict["infantryEquipment"] = cutEquip(i)
			if "6amtships" in i:
				dict["ships"] = cutArmy(i)
			if "7mpw" in i:
				dict["manpower"]= cutMpw(i)
			if "8fink" in i:
				dict["fuel"] = cutMpw(i)
			if "91numarmlight" in i:
				dict["tankLight"] = cutArmy(i)
			if "92numarmmedi" in i:
				dict["tankMedium"] = cutArmy(i) 
			if "93numarmheavy" in i:
				dict["tankMedium"] = cutArmy(i) 
			
		else:
			time = dict["time"]
			country = dict["countryTag"]
			numArmies = dict["numArmies"]
			infequip = dict["infantryEquipment"]
			ships = dict["ships"]
			mpw = dict["manpower"]
			fuel = dict["fuel"]
			tankLight = dict["tankLight"]
			tankMedium = dict["tankMedium"]
			tankHeavy = dict["tankHeavy"]
			row = country, time, numArmies, infequip, ships, mpw, fuel, tankLight, tankMedium, tankHeavy
			data.append(row)
	
	writeRow(data)


def writeRow(data):
	header = ["country", "time", "armies", "infantryEquipment", "ships", "manpower", "fuel", "lighTank", "mediumTank", "heavyTank"]

	with open("game_analyse.csv", "w", newline="", encoding='utf-8') as file:
		writer = csv .writer(file)

		writer.writerow(header)
		writer.writerows(data)
	

def checkFile(file):
	name = file[1].split(".")
	if name[1] == "log":
		return True
	else:
		return False


def main():
	file = sys.argv

	try:
		if checkFile(file):
			liste = shortenList(file[1])
			breakDownList(liste)
			print("Everything seemed to work!")
			input("Press a key to quit.")
	except:
		print("""	Something went wrong!
		Did you choose the right file?

		If so, please submit an error report on Steam:
			!!! ADD LINK !!!
		or over at GitHub:
			!!! ADD LINK !!!
		""")
		input("Press a key to quit.")


if __name__ == "__main__":
    main()