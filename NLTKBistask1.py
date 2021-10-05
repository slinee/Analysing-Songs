from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

fdistsave = ["a"]*5     # A list where fdist message will be saved
count = 0   # a variable to count how many times for loop has looped
unique_means = [0, 0, 0, 0, 0]
word_means = [0, 0, 0, 0, 0]

artists = ["Kanye.txt", "Justin.txt", "Eminem.txt", "Dua.txt", "Drake.txt"]
for artistinput in artists:     # For loop which will read the lyrics
    with open(artistinput, 'r', encoding="utf8") as file:
        Lyrics = file.read().rstrip('\n')

    tokenized_word = word_tokenize(Lyrics)
    fdist = FreqDist(tokenized_word)
    print("\n__________________________________________________\n")
    print(tokenized_word, "\n")
    fdistsave[count] = fdist    # save fdist messageS
    splitted = str(fdist).split()
    unique_means[count] = int(splitted[2])   # The number of unique words
    word_means[count] = int(splitted[5])
    count += 1
count = 0   # reset the value of the count variable so we can use it again
for i in fdistsave:
    print(artists[count], ": \n", i, "\n")     # prints the name of the artist
    count += 1
# input the dataset to plot the graph
labels = ['Kanye West', 'Justin Bieber', 'Eminem', 'Dua Lipa', 'Drake']
unique_means
word_means
unique_std = [300, 300, 300, 300, 300]
word_std = [1000, 1000, 1000, 1000, 1000]
width = 0.7    # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(labels, unique_means, width, yerr=unique_std, label='# of unique words')
ax.bar(labels, word_means, width, yerr=word_std, bottom=unique_means,
       label='# of words')

ax.set_ylabel('Number of words')
ax.set_title('Number of unique words compared to the number of words in songs')
ax.legend()

plt.show()
# Show graphic
plt.show()
input('Press ENTER to exit')
