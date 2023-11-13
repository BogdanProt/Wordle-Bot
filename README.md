# Wordle-Bot

Tool that finds the best solutions to solve Wordle (with least attempts) using Shannon's entropy, a concept from information theory, to strategically select words that provide the maximum information gain with the fewest attempts.

## How it works

The bot begins by accessing a curated list of Romanian words stored in ```cuvinte_wordle.txt```. From this lexicon, a random word is chosen as the initial puzzle-solving challenge. The crux of the algorithm lies in the calculation of entropies for each candidate word. This entails assessing the uncertainty associated with each word, with the goal of selecting the one that imparts the highest information content in terms of bits.

Once entropies are computed, a filtering process is initiated, narrowing down the list of potential solutions based on the obtained information. The selection of words is then relayed to the main code, the graphical user interface (```wordle_gui.py```), developed using Python's tkinter library.

It's worth noting that the optimal word to initiate each Wordle game, as determined by the algorithm, is **TAREI**, which yiels ~6.41 bits of information. 


![image](https://github.com/BogdanProt/Wordle-Bot/assets/92607347/cdb9b8e3-5411-4d64-8e97-1cd62566751b)




## References

For a deeper understanding of the theoretical foundations and the application of information theory in solving Wordle puzzles: [Solving Wordle using Information Theory](https://www.youtube.com/watch?v=v68zYyaEmEA)
