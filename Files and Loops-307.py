## 1. Opening Files ##

a = open("test.txt", "r")
print(a)
f=open("crime_rates.csv","r")
print(f)

## 2. Reading In Files ##

f = open("crime_rates.csv", "r")
data=f.read()
print(data)

## 3. Splitting ##

# We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
print(split_list)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

# Code from previous cells
f = open('crime_rates.csv', 'r')
data = f.read()
rows=data.split("\n")
print(rows[0:6])

## 5. Practice - Loops ##

ten_rows = rows[0:10]
for ten_rows in rows[0:10] :
    print(ten_rows)
    

## 7. Practice - Splitting Elements in a List ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])

final_data =[]
for row in rows:
    split_data=row.split(",")
    final_data.append(split_data)
    print(final_data[0:5])

## 8. Accessing Elements in a List of Lists: The Manual Way ##

print(five_elements)
cities_list=[]
cities_list.append(five_elements[0][0])
cities_list.append(five_elements[1][0])
cities_list.append(five_elements[2][0])
cities_list.append(five_elements[3][0])
cities_list.append(five_elements[4][0])
print(cities_list)

## 9. Looping Through a List of Lists ##

crime_rates = []

for row in five_elements:
    # row is a list variable, not a string.
    crime_rate = row[1]
    # crime_rate is a string, the crime rate of the city.
    crime_rates.append(crime_rate)
    
cities_list = []
for row in final_data:
    rows=row[0]
    cities_list.append(rows)
    print(cities_list)

## 10. Challenge ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])
int_crime_rates = []
for row in rows:
    split_rates = row.split(",")
    int_data=int(split_rates[1])
    int_crime_rates.append(int_data)
    print(int_crime_rates)
    
    
    