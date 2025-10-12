input_str= "teeter"
# first non repeted char
for char in input_str:
    if input_str.count(char)==1:
        print("char is ",char)
        break