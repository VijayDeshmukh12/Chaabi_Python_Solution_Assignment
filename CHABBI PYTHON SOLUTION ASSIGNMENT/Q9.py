from datetime import datetime, timedelta

def check_date_difference(from_date, to_date, difference):
    # Convert the date strings to datetime objects
    from_date_obj = datetime.strptime(from_date, '%y-%m-%d')
    to_date_obj = datetime.strptime(to_date, '%y-%m-%d')
    
    # Calculate the difference between the dates
    date_diff = to_date_obj - from_date_obj
    
    # Convert the difference to days
    num_days = abs(date_diff.days)
    
    # Check if the difference is less than the specified number of days
    if num_days < difference:
        return True
    else:
        return False

# Example usage
from_date = '16-12-10'
to_date = '16-12-20'
difference = 11

result = check_date_difference(from_date, to_date, difference)
print(result)

