## 2. Sets ##

import csv
f=open("legislators.csv","r")
file=csv.reader(f)
files=list(file)
legislators=files[1:len(files)]
gender=[]
for row in legislators:
    rows=row[3]
    gender.append(rows)
gender=set(gender)
print(gender)

## 3. Exploring the Dataset ##

import csv
f=open("legislators.csv","r")
file=csv.reader(f)
files=list(file)
legislators=files[1:len(files)]
party=[]
for row in legislators:
    party.append(row[6])
party=set(party)
print(party)
print(legislators)
    
    

## 4. Missing Values ##

import csv
f=open("legislators.csv","r")
file=csv.reader(f)
files=list(file)
legislators=files[1:len(files)]
for row in legislators:
    if row[3] == "":
        row[3] = "M"

## 5. Parsing Birth Years ##

import csv
f=open("legislators.csv","r")
file=csv.reader(f)
files=list(file)
legislators=files[1:len(files)]
birth_years=[]
parts=[]
for row in legislators:
    rows=row[2]
    parts=rows.split('-')
    birth_years.append(parts[0])
    
    

## 6. Try/except Blocks ##

try:
    float("hello")
except Exception:
    print("Error converting to float.")

## 7. Exception Instances ##

try:
    int('')
except Exception as exc:
    print(type(exc))
    print(str(exc))

## 8. The Pass Keyword ##

converted_years = []
import csv
f=open("legislators.csv","r")
file=csv.reader(f)
files=list(file)
legislators=files[1:len(files)]
birth_years=[]
parts=[]
for row in legislators:
    rows=row[2]
    parts=rows.split('-')
    birth_years.append(parts[0])
for year in birth_years:
    try:
        year=int(year)
    except Exception:
        pass
    converted_years.append(year)
    
    

## 9. Convert Birth Years to Integers ##

for row in legislators:
    birthday = row[2]
    birth_year = birthday.split("-")[0]
    try:
        birth_year = int(birth_year)
    except Exception:
        birth_year = 0
    row.append(birth_year)

## 10. Fill in Years Without a Value ##

last_value=1
for row in legislators:
    if row[7]==0:
        row[7]=last_value
    last_value=row[7]
    