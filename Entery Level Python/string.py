longword="Meachine leraning python artificali ntelligence data science c++ basic Neural network0"
word=longword.split()
#print(len(word))
longest_word= 0
for i in range(1, len(word)):
    if len(word[longest_word]) < len(word[i]):
        longest_word = i;
#print(word[longest_word])



longnum="Meachine learning python artifical intelligence data science c++ basic Neural network0"
words=longnum.split()
count = 0
print(len(words))
for i in range(1, len(words)):
    if len(words[count]) < len(words[i]):
        print(len(words[count]))
        print(words[count])
        count = i
print(words[count])
