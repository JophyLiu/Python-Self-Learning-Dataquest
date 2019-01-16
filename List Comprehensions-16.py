## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]
for i,ship in enumerate(ships):
  
    print(ship)

    print(cars[i])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]
for i,thing in enumerate(things):
    thing.append(trees[i])

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]
apple_prices_doubled=[2*price for price in apple_prices]
apple_prices_lowered=[price-100 for price in apple_prices]


## 5. Counting Female Names ##

name_counts={}
for row in legislators:
    if row[3] == "F":
        if row[7] >1940:
            if row[1] in name_counts:
                name_counts[row[1]]=name_counts[row[1]]+1
            else:
                name_counts[row[1]]=1
                


## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks=[]
checks = [x is not None and x > 30 for x in values]


## 8. Highest Female Name Count ##

max_value=None 
for keys in name_counts:
    count=name_counts[keys]
    if max_value is None or count > max_value:
        max_value=count
        
    

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}
for key,value in plant_types.items():
    print(key)
    print(value)
    

## 10. Finding the Most Common Female Names ##

top_female_names = []
for key,value in name_counts.items():
    if value == 2:
        top_female_names.append(key)

## 11. Finding the Most Common Male Names ##

top_male_names = []
male_name_counts={}
for row in legislators:
    if row[3] == "M":
        if row[7] > 1940:
            if row[1] in male_name_counts:
                male_name_counts[row[1]]=male_name_counts[row[1]]+1
            else:
                male_name_counts[row[1]]=1

highest_male_count=None
for key,values in male_name_counts.items():
    if highest_male_count is None or values > highest_male_count:
        highest_male_count=values
for key,values in male_name_counts.items():
    if values == highest_male_count:
        top_male_names.append(key)
    
    
            