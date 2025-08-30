**Python Simple Programs: Birthday Paradox & Word Counter**

**Description:**
This repository contains two Python programs demonstrating probability simulations and basic text analysis:

  1. **Birthday Paradox**: Estimates the probability of shared birthdays in a group using Monte Carlo simulations. Includes an option for reproducible results with a fixed random seed.  
  2. **Word Counter / White Spaces**: Counts the frequency of words in a given sentence, supporting input validation, dictionary-based counting, and clean, readable output.
Both programs are object-oriented and demonstrate basic Python programming principles.

## Features
- **Birthday Paradox**
  - Input the number of people and number of trials.
  - Optionally use a fixed seed for reproducible results.
  - Calculates estimated probability of at least two people sharing a birthday.
## Working
   - Generate random birthdays for each person in the group.
   - Check if any birthdays are repeated.
   - Repeat the experiment multiple times and calculate the fraction of trials with duplicates.
   - Display the estimated probability.
  
- **Word Counter**
  - Validate sentence input (non-empty string).
  - Split sentence into words and count occurrences.
  - Read-only property for the original sentence.
  - Efficient dictionary-based word frequency calculation.
  - User-friendly string representation of results.
## Working
  - Take the input text.
  - Split the text into individual words.
  - Count how many times each word appears.
  - Display the results in a user-friendly format.
