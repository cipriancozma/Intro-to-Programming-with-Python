def clean_line(line):
    for char in '-,.':
        line = line.replace(char, " ")
    line = line.lower()
    return line.split() 

word_count = {}
def poezie(fisier):
    with open(fisier) as file:
        for linie in file:
            cuvinte = clean_line(linie)

            for cuvant in cuvinte:
                if len(cuvant) > 1:
                    word_count[cuvant] = word_count.get(cuvant, 0) + 1

poezie('./plumb.txt')
sorted_dict = { word: word_count[word] for word in sorted(word_count)}
for word, count in sorted_dict.items():
    print(f"{word}: {count}")
print(f"Total: {len(sorted_dict)} cuvinte unice")









poezie('./plumb.txt')