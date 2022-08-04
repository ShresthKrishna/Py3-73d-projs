student_dict ={
    "students": ["Angela", "Angelee", "Angelina"],
    "score": [56, 66, 76]
}

for (value,key) in student_dict.items():
    print(key)

import pandas
student_data_frame = pandas.DataFrame(student_dict)

# Looping through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)
for (index,row) in student_data_frame.iterrows():
    print(row.students)
    if row.students == "Angela":
        print(row.score)
