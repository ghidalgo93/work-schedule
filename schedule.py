# Gerardo Hidalgo-Cuellar
# Main scheduling application, import excell file
# 09/06/2020 https://github.com/ghidalgo93


# Import Libraries
from helperfunctions import monthToNumber
import pandas as pd
import calendar as cal
import sys

# Globals
scheduleFile = f"months/{sys.argv[1]}.csv"
monthYearList = sys.argv[1].split("-") 
year = int(monthYearList[1])
month = monthYearList[0]
monthNumber = monthToNumber(month)
numberOfDays = cal.monthrange(year, monthNumber)[1]

def main():
    data = pd.read_csv(scheduleFile)
    print(data)

main()

