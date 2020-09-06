# Import Libraries
import datetime




# Function to turn a month name into a number
# Input: month name as string
# Return: month as number / 12
def  monthToNumber(month):
    long_month_name = month
    datetime_object = datetime.datetime.strptime(long_month_name, "%B")
    month_number = datetime_object.month
    
    return(month_number)
    
