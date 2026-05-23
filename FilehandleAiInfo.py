# Hey there! This little script is designed to gather some basic information about people.
# It'll ask for their name, age, and address, and keep doing so until you type 'quit'.
# All the info will be saved in a file called 'another.txt' for you.

def collect_and_save_info():
    """
    Gathers person's information (name, age, address) repeatedly
    until the user types 'quit'. Saves the information to 'another.txt'.
    Ensures age is stored as an integer.
    """
    
    all_people_info = [] # To store all collected info.
    
    print("✨ ---------------------------Welcome to the Super Info Collector! ✨ ---------------------------")
    print("Let's gather some details. I'll ask for a name, age, and address for each person.\n")
    print("If you want to stop at any point, just type 'quit' when I ask for any piece of info.\n\n")

    while True:
        current_person_details = {}

        # --- Name Input ---
        # Making the first question a bit more engaging.
        name_prompt = "Alright, let's start with a name! Who are we noting down today? (or type 'quit' to finish): "
        name = input(name_prompt)
        if name.lower() == 'quit':
            print("Okay, looks like you're all done entering names. Wrapping up!")
            break 

        current_person_details['name'] = name # Store the name right away.

        # --- Age Input with Validation ---
        while True: # Loop for age until valid input or 'quit'.
            age_input = input(f"Great! And how many years young is {name}? (enter a number, or type 'quit'): ")
            if age_input.lower() == 'quit':
                print("Got it, quitting as requested.")
                # We need to break out of the outer loop (person entry) as well.
                # A flag can help, or just break outer loop directly if we structure it so.
                # For simplicity here, we'll set a flag that the outer loop can check,
                # or better, just break the outer loop from here if we're quitting entirely.
                # Let's make the quit from age apply to the whole entry process.
                name = "quit_initiated_from_age" # Signal to outer loop to break
                break # Exit age loop

            try:
                age = int(age_input) # Try converting to an integer.
                if age < 0:
                    print("Hmm, age can't be negative. Please enter a valid age.")
                else:
                    current_person_details['age'] = age
                    break # Valid age entered, exit age loop.
            except ValueError:
                # This means the input wasn't a number.
                print("Whoops! That doesn't look like a valid number for age. Please try again or type 'quit'.")
        
        if name == "quit_initiated_from_age": # Check if quit was triggered from age input
            break # Exit the main person entry loop

        # --- Address Input ---
        address = input(f"Perfect! Lastly, what's {name}'s address? (or type 'quit'): ")
        if address.lower() == 'quit':
            print("Okay, stopping here before saving address.")
            break 

        current_person_details['address'] = address
        
        all_people_info.append(current_person_details)
        print(f"Thanks! I've noted down the details for {name}.\n")

    # --- Loop has finished ---

    if not all_people_info:
        print("No information was entered, so 'another.txt' will not be modified.")
        return

    try:
        with open('another.txt', 'a') as file: # 'a' for append mode
            print("\nSaving the collected information to 'another.txt'...")
            for person_info in all_people_info:
                file.write("--- Person Details ---\n")
                file.write(f"Name: {person_info['name']}\n")
                # Age will now be an integer, but writing to file converts it to string implicitly.
                file.write(f"Age: {person_info['age']}\n") 
                file.write(f"Address: {person_info['address']}\n")
                file.write("\n")
            print("All done! The information has been saved.")
    except IOError:
        print("Oops! Something went wrong while trying to write to 'another.txt'.")
        print("Please check if you have permission to write to this location.")

if __name__ == "__main__":
    collect_and_save_info()
    print("\nThanks for using the Info Collector! Have a fantastic day! 😊")
