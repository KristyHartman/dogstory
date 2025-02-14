def create_interactive_story():
    # Ask for the dog's name
    dog_name = input("What is the name of the runaway dog? ").strip()
    if not dog_name:
        dog_name = "Max"  # Default name if no input is provided

    print(f"\nOnce upon a time in a small town, there was a dog named {dog_name}. One day, {dog_name} ran away from home and had to find his way back.\n")
    
    print(f"{dog_name} first wandered through the dense forest.")
    choice1 = input("Should {dog_name} (a) follow the sound of running water or (b) follow the trail of footprints? Enter 'a' or 'b': ").strip().lower()
    
    if choice1 == 'a':
        print(f"\n{dog_name} followed the sound of running water and found a stream. There he met a wise old owl who guided him towards the busy city.\n")
    else:
        print(f"\n{dog_name} followed the trail of footprints and met a kind fox who pointed him towards the busy city.\n")
    
    print(f"In the city, {dog_name} faced many challenges.")
    choice2 = input("Should {dog_name} (a) hide in an alley or (b) ask for help from a passerby? Enter 'a' or 'b': ").strip().lower()
    
    if choice2 == 'a':
        print(f"\n{dog_name} hid in an alley but soon realized it was a dead-end. A stray cat noticed him and offered to help him find the way to the vast field.\n")
    else:
        print(f"\n{dog_name} asked for help from a passerby. A kind stranger gave {dog_name} directions to the vast field.\n")
    
    print(f"Finally, {dog_name} reached the vast field.")
    choice3 = input("Should {dog_name} (a) rest under a tree or (b) keep searching for his home? Enter 'a' or 'b': ").strip().lower()
    
    if choice3 == 'a':
        print(f"\n{dog_name} rested under a tree. After a nap, he awoke to find a familiar scent. He followed the scent and it led him back home.\n")
    else:
        print(f"\n{dog_name} kept searching and found a familiar scent. He followed the scent and it led him back home.\n")
    
    print(f"And so, after a long and adventurous journey, {dog_name} returned safely to his loving family. The end.")

# Start the interactive story
create_interactive_story()
