"""
 This is the checkbday.py module which will check if any of the listed
 Birthdays in bdaylist.txt
 is in the near future
"""
import datetime as dt
import settings as st

def check_simple(bday):
    today = dt.date.today()
    bday_dt = dt.datetime.strptime(bday, '%d-%m').date()
    bday_dt = bday_dt.replace(year=today.year)
    delta = bday_dt - today 
    if delta.days > 0 and delta.days <= st.interval:
        return True
    else:
        return False

def check_full_date(bday):
    today = dt.date.today()
    bday_dt = dt.datetime.strptime(bday, '%d-%m-%Y').date()
    bday_dt = bday_dt.replace(year=today.year)
    delta = bday_dt - today 
    if delta.days > 0 and delta.days <= st.interval:
        return True
    else:
        return False
    
    

def parse_list():
    birthdaystring = ""
    with open(st.file_location) as f:
        bdaylist = f.readlines()

    for b in bdaylist:
        if not b.startswith("#"):
            b_split = [x.strip() for x in b.split(":")]
            # Full year given:
            if b_split[0].count("-") == 2:
                if check_full_date(b_split[0]):
                    birthdaystring += "{}'s birthday is {} \r\n".format(b_split[1], b_split[0])
            # Only day and month:
            elif b_split[0].count("-") == 1:
                if check_simple(b_split[0]):
                    birthdaystring += "{}'s birthday is {} \r\n".format(b_split[1], b_split[0])

    f.close()
    return birthdaystring



