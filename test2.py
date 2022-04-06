#Benyir  J. Pacheco

count = 0


with open('win95coolest.txt') as text:
    for lines in text:
        count += 1
        wordCount = len(lines.split())
        avgLength = 0
        if wordCount != 0:
            total = 0
            wordSplit = lines.split()
            for word in wordSplit:
                total += len(word)
            avgLength = total / wordCount
        print(count, wordCount, avgLength, lines)
