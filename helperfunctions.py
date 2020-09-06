# Import Libraries
import datetime





def  monthToNumber(month):
    long_month_name = month
    datetime_object = datetime.datetime.strptime(long_month_name, "%B")
    month_number = datetime_object.month
    
    return(month_number)
    
