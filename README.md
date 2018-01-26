## Annims.py
stands for Anniversaire Mail Service

It is a little handy python3 script you can add to your cronjobs if you are like me and you keep forgetting birthdays!

### What does it do?
Keeps track of the birthdays you add to the text file bdaylist.txt
when a birthday is in a certain time interval it will send you a friendly reminder email

### How to use
- git clone this
- add your GMail account to account_info.py
- enable "less secure Apps" for your GMail account 
- crontab -e 
    - Edit your crontab and add "annims.py" to be executed according to your liking
- edit the bdaylist.txt file
    - Add birthday dates either in DD-MM-YYYY or just DD-MM format
    - Use ":" as a delimiter between date and name

### When does it remind me?
As per default the time interval is set to 5 days in "settings.py"

Of course you could change this to 31 days and let the script be executed just once per month if monthly reminders are what you want.

#### License
GPL-3.0