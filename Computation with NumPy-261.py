## 2. Array Comparisons ##

years_1984 = (world_alcohol[:,0] == "1984")
countries_canada = (world_alcohol[:,2] == "Canada")

## 3. Selecting Elements ##

country_is_algeria=(world_alcohol[:,2] == "Algeria")
country_algeria=(world_alcohol[country_is_algeria,:])

## 4. Comparisons with Multiple Conditions ##

is_algeria_and_1986=(world_alcohol[:,0] == "1986") & (world_alcohol[:,2] == "Algeria")
rows_with_algeria_and_1986=world_alcohol[is_algeria_and_1986,:]

## 5. Replacing Values ##

first_column=world_alcohol[:,0] == "1986"
world_alcohol[first_column,0]=2014
fourth_column=world_alcohol[:,3] == "Wine"
world_alcohol[fourth_column,3] = "Grog"


## 6. Replacing Empty Strings ##

is_value_empty=world_alcohol[:,4] == ""
world_alcohol[is_value_empty,4]=0

## 7. Converting Data Types ##

alcohol_consumption=world_alcohol[:,4]
alcohol_consumption=alcohol_consumption.astype(float)

## 8. Computing with NumPy ##

total_alcohol=alcohol_consumption.sum()
average_alcohol=alcohol_consumption.mean()

## 9. Total Annual Alcohol Consumption ##

is_canada_1986=(world_alcohol[:,0]=="1986")&(world_alcohol[:,2]=="Canada")
canada_1986=world_alcohol[is_canada_1986,:]
is_empty=(canada_1986[:,4]=="")
canada_1986[is_empty,4]=0
canada_alcohol=canada_1986[:,4]
canada_1986=canada_alcohol.astype(float)
total_canadian_drinking=canada_1986.sum()
  

## 10. Calculating Consumption for Each Country ##

totals = {}
countries=world_alcohol[:,2]
is_year=(world_alcohol[:,0]=="1989")
year=world_alcohol[is_year,:]
for country in countries:
    is_country=(year[:,2]==country)
    country_consumption=year[is_country,:]
    country_consumption=country_consumption[:,4]
    is_empty=(country_consumption=="")
    country_consumption[is_empty]=0
    country_consumption=country_consumption.astype(float)
    country_sum=country_consumption.sum()
    totals[country]=country_sum
print(totals)
        
            



## 11. Finding the Country that Drinks the Most ##

highest_value = 0
highest_key = None
for key,value in totals.items():
    if value > highest_value:
        highest_value=value
        highest_key=key
        