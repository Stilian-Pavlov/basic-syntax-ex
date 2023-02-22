
first_string=input()
second_string=input()
temp_string=""
final_string=""
index=0

while index < len(first_string):
    temp_string+=second_string[index]
    final_string=temp_string+first_string[index+1:]
    if first_string[index]!=second_string[index]:
        print(final_string)
    index+=1


