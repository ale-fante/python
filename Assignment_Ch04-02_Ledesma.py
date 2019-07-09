numToConvert = int(input("Enter a year between 1000 to 3000: " + "\n"))

def main():

    thousands = getThousandsPlace()
    hundreds = getHundredsPlace()
    tens = getTensPlace()
    ones = getOnesPlace()

    returnRomanThousandsPlace(thousands)
    returnRomanHundredsPlace(hundreds)
    returnRomanTensPlace(tens)
    returnRomanOnesPlace(ones)

def getThousandsPlace():
    numList = list(str(numToConvert))
    thousands = int(numList[0])
    return thousands

def getHundredsPlace():
    numList = list(str(numToConvert))
    hundreds = int(numList[1])
    return hundreds

def getTensPlace():
  numList = list(str(numToConvert))
  tens = int(numList[2])
  return tens

def getOnesPlace():
  numList = list(str(numToConvert))
  ones = int(numList[3])
  return ones

def returnRomanThousandsPlace(thousands):
  '''Accepts a thousands place int as an argument and returns the roman numerals for the thousand place.'''
  thousandsDict = {1:'M', 2:'MM', 3:'MMM'} 
  return thousandsDict.get(thousands)

def returnRomanHundredsPlace(hundreds):
  '''Accepts a hundreds place integer number as an argument and returns the roman numerals for the hundreds place.'''
  hundredsDict = {0:'', 1:'C', 2:'CC', 3:'CCC', 4:'CD', 5:'D', 6:'DC', 7:'DCC', 8:'DCCC', 9:'CM'}
  return hundredsDict.get(hundreds)

def returnRomanTensPlace(tens):
  '''Accepts a tens place integer number as an argument and returns the roman numerals for the tens place.'''
  tensDict = {0:'', 1:'X', 2:'XX', 3:'XXX', 4:'XL', 5:'L', 6:'LX', 7:'LXX', 8:'LXXX', 9:'XC'}
  return tensDict.get(tens)

def returnRomanOnesPlace(ones):
  '''Accepts a ones place integer number as an argument and returns the roman numerals for the ones place.'''
  onesDict = {0:'', 1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}
  return onesDict.get(ones)

def allNums():
  thousands = getThousandsPlace()
  hundreds = getHundredsPlace()
  tens = getTensPlace()
  ones = getOnesPlace()

  th = returnRomanThousandsPlace(thousands)
  hu = returnRomanHundredsPlace(hundreds)
  te = returnRomanTensPlace(tens)
  on = returnRomanOnesPlace(ones)

  return th, hu, te, on

# Expected output for 1984: MCMLXXXIV
romanNumerals = allNums()
thousands, hundreds, tens, ones = romanNumerals
print("Your number in roman numerals is: " + thousands + hundreds + tens + ones)

