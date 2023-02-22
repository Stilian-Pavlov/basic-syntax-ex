command = input()
counter = 0
upper_list = ["CODING", "CAT", "DOG", "MOVIE"]
lower_list = "coding", "cat", "dog", "movie"
while command != "END":
    if counter>5:
        print("You need extra sleep")
        break
    if command in upper_list:
        counter += 2
    elif command in lower_list:
        counter += 1
    elif command == "END":
        break
    command = input()
if counter <=5:
    print(counter)