import random


def guess_the_number():
    number = random.randint(1, 100)
    user_attempts = 0
    ai_attempts = 0
    max_attempts = 10

    ai_low = 1  # Lower bound for AI
    ai_high = 100  # Upper bound for AI

    print("Welcome to Guess the Number!")
    print(f"You and the AI will take turns guessing the number between 1 and 100.")
    print(f"Each has {max_attempts} total attempts to guess the correct number.")

    while user_attempts < max_attempts and ai_attempts < max_attempts:
        # User's turn
        print("\nYour turn:")
        try:
            user_guess = int(input("Enter your guess (1-100): "))
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 100.")
            continue
        user_attempts += 1

        if user_guess < number:
            print("Too low!")
        elif user_guess > number:
            print("Too high!")
        else:
            print(f"\n Congratulations! You guessed the number in {user_attempts} attempts. You win!")
            return

        # AI's turn
        print("\nAI's turn:")
        # Replace random guess with alpha_beta_guess
        ai_guess = alpha_beta_guess(ai_low, ai_high, depth=5, alpha=-float('inf'), beta=float('inf'), maximizing=True) # type: ignore
        if ai_guess is None:
            ai_guess = random.randint(ai_low, ai_high)  # Fallback to random if alpha_beta_guess returns None
        ai_attempts += 1
        print(f"AI guessed: {ai_guess}")

        if ai_guess < number:
            print("AI's guess is too low!")
            ai_low = ai_guess + 1  # AI adjusts its lower bound
        elif ai_guess > number:
            print("AI's guess is too high!")
            ai_high = ai_guess - 1  # AI adjusts its upper bound
        else:
            print(f"\n AI guessed the number in {ai_attempts} attempts. AI wins!")
            return

    print("\nNeither you nor the AI guessed the number within 10 attempts. Game over!")
