from datetime import datetime, timedelta

def get_date_before(date, n):
    # Convert the date string to a datetime object
    date_obj = datetime.strptime(date, '%y-%m-%d')
    
    # Calculate the date n days before the given date
    before_date = date_obj - timedelta(days=n)
    
    # Convert the result back to a string representation
    before_date_str = before_date.strftime('%y-%m-%d')
    
    return before_date_str

#example
date = '16-12-10'
n = 11
result = get_date_before(date, n)
print(result)
