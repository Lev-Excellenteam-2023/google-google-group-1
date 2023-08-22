# group-1

## Project Description:

**Autocomplete Search Typing In Database Of Text Files.**

### Program Flow:
1. The user enters a string input into the CLI and presses the "Enter" key.
2. The five most relevant complete sentences are presented.
   Relevant sentences are those that contain the user's input.

### Additional Features:
1. Correction of one missing letter in the input (e.g., 'helo' to 'hello').
2. Correction of one wrong letter in the input (e.g., 'helko' to 'hello').

## Algorithms & Structures

### Structures:

The program is based on two trie-trees:
1. Sentences trie-tree (STT).
2. Words trie-tree (WTT).

The STT holds all the lines in the database.
The WTT holds all the words in the database.

### Algorithm:

1. Initializing the trie-trees.
2. Getting user's input.
3. Searching for matching sentences.
4. Printing the five most relevant results (highest-scored sentences).

## Detailed Code Flow

### Initializing:
1. Recursively search for text files in the directory and subdirectories.
2. Fill the STT.
3. Fill the WTT.

### Searching Input In The Tree:
1. Search for the first word of the input in the WTT.
2. The WTT terminal node contains references to the appearances of this word in the STT.
3. Create a list of sentences from the STT that match the rest of the user's input.
4. If there are five or more matches, print the first five results in alphabetic order.
5. If there are fewer than five results, search for close sentences (according to the exercise's instructions: one mistake, one letter missing, etc.).
6. Assign a score to every result.
7. Print the five sentences with the highest score.

### Scoring:
(scoring according to the exercise instructions).

## Examples

**Simple Example:**

Assume we have two sentences in our database:
1. "hello world"
2. "hello hello world"

The STT looks like this:


root --> "hello" --> "world"
				|
				|--> "hello" --> "world"
				
				
the WTTlooks like this:

root --> h --> e --> l --> l --> o
	|
	|--> w --> o --> r --> l --> d


Assume the user's input is 'hello'. 
The algorithm will find the word 'hello' in the WTT, and from it get the references to the STT. 
In this case, we get two references, and check the rest of the input against the sentences in the STT.
We have two matches, so the output will be:

1. "hello world"
2. "hello hello world"

