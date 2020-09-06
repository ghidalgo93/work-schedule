# Gerardo Hidalgo-Cuellar
# Main scheduling application, import excell file
# 09/06/2020 https://github.com/ghidalgo93


# Globals
schedule = '../September'
# Import Libraries
import csv


def main():
    with open(schedule,newline='') as csvfile:
        scheduleReader = csv.reader(csvfile)
        for row in scheduleReader:
            print(row)



main()

