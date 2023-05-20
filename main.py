import requests

dictionary = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
lettersnottohave = []

response = requests.get(dictionary)

array = response.content.decode("utf-8").splitlines()
filterarray = []
for i in range(len(array)):
    word = array[i].lower()
    if len(word) != 5:
        continue
    else:
        flag = False
        for letter in lettersnottohave:
            if letter in word:
                flag = True
                break
        if not flag:
            filterarray.append(word) 

print(filterarray)