from BirthdayExperiment import BirthdayExperiment
def main():
    group_sizes = [5, 10, 20, 23, 35, 52]
    trials = 1000  # number of simulations for each group size

    for n in group_sizes:
        try:
            print(f"\n--- Group Size: {n}, Trials: {trials} ---")

            # Run with true randomness
            random_exp = BirthdayExperiment(n, trials)  
            random_exp.run_experiment()
            print("Random run:", random_exp)

            # Run with fixed seed
            seeded_exp = BirthdayExperiment(n, trials, seed=42)  
            seeded_exp.run_experiment()
            print("Seeded run:", seeded_exp)

        except ValueError as e:
            print(f"Error with group size {n}: {e}")
            # Catches cases like negative or zero group size

if __name__ == "__main__":
    main()
