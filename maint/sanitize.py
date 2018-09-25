import csv

FIELDS= ['field','digital','home_meetup','meetup_guest','call_center','palrig',
         'election_day']

# name,email,phone,hood,address,edu_foundations,field,digital,home_meetup,meetup_guest,call_center,palrig,election_day,notes,whatever,state

c = csv.DictReader(open("db6.csv"))

for row in c:
    for f in FIELDS:
        v = row[f]
        if len(v) > 1:
            name = row['name']
            print(f"{name}: {f} = {v}")


