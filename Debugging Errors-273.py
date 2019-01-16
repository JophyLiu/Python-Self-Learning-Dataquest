## 2. Syntax Errors ##

def first_elts (input_list):
    elts = []
    for each in input_list:
        elts.append(each)
    return elts

animals = [["dog","cat","rabbit"],["turtle","snake"],["sloth","penguin","bird"]]
first_animal = first_elts(animals)
print(first_animal)

## 4. TypeError and ValueError ##

forty_two = 42
forty_two + 42

float(2.22)

## 5. IndexError and AttributeError ##

lives = [1,2,3]
first_life=lives[0]

f = open("story.txt")
story=f.read()
story=story.split('\n')
print(first_life,story)

## 6. Traceback ##

def summary_statistics(input_lst):
    num_japan_films = feature_counter(input_lst,6,"Japan",True)
    num_color_films = feature_counter(input_lst,2,"Color",True)
    num_films_in_english = feature_counter(input_lst,5,"English",True)
    summary_dict = {"japan_films" : num_japan_films, "color_films" : num_color_films, "films_in_english" : num_films_in_english}
    return summary_dict

def feature_counter(input_list,index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_list = input_list[1:len(input_list)]
    for each in input_list:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt

summary = summary_statistics(movie_data)
print(summary)