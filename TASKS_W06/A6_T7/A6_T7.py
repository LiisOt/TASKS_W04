LOWER_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
UPPER_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DELIMITER = ';'

def read_file(pFilename):
    Content = ''
    Filehandle = open(pFilename, 'r')
    row = Filehandle.readline()
    while row != '':
        Content += row
        row = Filehandle.readline()
    Filehandle.close()
    return Content

def write_file():
    return None

def append_to_file():
    return None

def rot():
    newContent = ''
    return newContent

def getLocation(locationId):
    Locations = "unknown"
    if locationId == 0:
        Locations = "Home"
    elif locationId == 1:
        Locations = "Galba's Palace"
    elif locationId == 2:
        Locations = "Otho's Palace"
    elif locationId == 3:
        Locations = "Vitellius's Palace"
    elif locationId == 4:
        Locations = "Vespasian's Palace"
    return Locations


def main():
    print("Travel starting.")
    playerProgressFilename = 'player_progress.txt'
    progress = read_file(playerProgressFilename)
    LastProgress = progress.strip().split('\n')[-1].split(DELIMITER)
    CurrentLocationId = int(LastProgress[0])
    CurrentLocation = getLocation(CurrentLocationId)
    NextLocationId = int(LastProgress[1])
    nextLocation = getLocation(NextLocationId)
    passPhrase = LastProgress[2]
    print(f"Currenly at {CurrentLocation}.")
    print(f"Travelling to {nextLocation}.")
    print(f"...Arriving to the next location {nextLocation}.")
    print(f"Passing the guard at the entrance.")
    print("Travel ending.")
    return None

if __name__ == '__main__':
    main()