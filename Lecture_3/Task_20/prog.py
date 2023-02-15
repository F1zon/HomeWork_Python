simvols_en = "AEIOULNSTRDGBCMPFHVWYKJXQZ"
simvols_en = simvols_en.lower()

simvols_rus = "АВЕИНОРСТДКЛМПУБГЁЬЯЙЫЖЗХЦЧШЭЮФЩЪ"
simvols_rus = simvols_rus.lower()

word = input("Введите слово: ")

check = bool(set(simvols_rus).intersection(set(word.lower()))) # Проверка на русские или английские символы
word = word.lower()
point = 0

if check:
    for i in range(len(word)):
        for j in range(len(simvols_rus)):
            if word[i] == simvols_rus[j]:
                if (j < 9):
                    point += 1
                elif (j > 8 and j < 15):
                    point += 2
                elif (j > 14 and j < 20):
                    point += 3
                elif (j > 19 and j < 22):
                    point += 4
                elif (j > 21 and j < 27):
                    point += 5
                elif (j > 26 and j < 30):
                    point += 8
                elif (j > 29 and j < 33):
                    point += 10
else:
    for i in range(len(word)):
        for j in range(len(simvols_en)):
            if word[i] == simvols_en[j]:
                if (j < 10):
                    point += 1
                elif (j > 9 and j < 12):
                    point += 2
                elif (j > 11 and j < 16):
                    point += 3
                elif (j > 15 and j < 21):
                    point += 4
                elif (j > 20 and j < 22):
                    point += 5
                elif (j > 21 and j < 24):
                    point += 8
                elif (j > 23 and j < 26):
                    point += 10

print(point)
