import random
class BirthdayExperiment:
    def __init__(self, number_of_people, trials, seed=None):
        # Validate inputs
        self.number_of_people = number_of_people
        self.trials = trials
        self._probability = None  # to store the result
        self._rng = random.Random(seed) # dedicated random number generator


    @property
    def number_of_people(self):
        return self._number_of_people

    @number_of_people.setter
    def number_of_people(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("number_of_people must be a positive integer.")
        self._number_of_people = value

    @property
    def trials(self):
        return self._trials

    @trials.setter
    def trials(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("trials must be a positive integer.")
        self._trials = value

    @property
    def probability(self):
        return self._probability
    # probability is read-only, no setter
    # why probability is read-only?
    # Because it is computed by the experiment and should not be set directly.
    
    # helping methods
    def _generate_birthdays(self):
        # Generate a list of random birthdays for the group
        birthday = []
        for _ in range(self.number_of_people):
            # Random birthday between 1 and 365
            birthday.append(self._rng.randint(1, 365))
        return birthday
            
    def _has_duplicates(self, birthdays):
        # Check if there are any duplicate birthdays
        return len(birthdays) != len(set(birthdays))

    def run_experiment(self):
        # Run the experiment and calculate the probability
        duplicate_count = 0
        # Run the trials
        for _ in range(self.trials):
            # Generate birthdays for the group
            birthdays = self._generate_birthdays()
            # Check for duplicates
            if self._has_duplicates(birthdays):
                # If duplicates found, increment count
                duplicate_count += 1
                # Debugging output
        self._probability = duplicate_count / self.trials 
        # formula: probability = (number of trials with duplicates) / (total number of trials)
        return self._probability

    def __str__(self):
         probability_display = (
            f"{self._probability:.3f}" if self._probability is not None else "Not calculated yet"
        )
         return f"n = {self.number_of_people}, Estimated Probability = {probability_display}"
        
   


    


