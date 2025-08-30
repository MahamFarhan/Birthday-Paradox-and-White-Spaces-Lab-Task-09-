class WordCounter:
    def __init__(self, sentence: str):
        # Validation
        if not isinstance(sentence, str):
            raise TypeError("Input must be a string.")
        if sentence.strip() == "":
            raise ValueError("Sentence cannot be empty.")
        # checkes if the input is empty or only white spaces.
        #This validates input: only strings are allowed.
        #If input is wrong, it raises an exception (TypeError) and stops the program.
        
        self._sentence = sentence
        self._counts = None  # will store the word frequncy later

    @property
    def sentence(self):
        # Read-only property for sentence
        return self._sentence
    # using encapsulation to protect the sentence attribute and internal state.

    @property
    def counts(self):
        # using abstraction because user only sees the result but cannot modify it directly.
        # allows us to read word frequencies like an attribute.
        # if counts is not calculated yet, it calls repetitions() to compute it.
        if self._counts is None:
            self.repetitions()
        return self._counts

    def make_list(self):
        # Convert sentence into list of words
        return self._sentence.split()
    # splits the sentence into a list of words

    def repetitions(self):
        # Efficiently count word occurrences using a dictionary
        words = self.make_list()
        # gets the list of words from the sentence
        word_count = {} # dictionary to store word counts
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
            # for each word, it increments its count in the dictionary
        self._counts = word_count
        return word_count

    def __str__(self):
        # Readable string representation of word counts
        if self._counts is None:
            return #No counts available. Run repetitions() first.
        
        result = ["Word counts:"]
        for word, count in self._counts.items():
            result.append(f"{word} = {count}")
        return "\n".join(result)