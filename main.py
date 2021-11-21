# Example Mail Merge
# Uses each name in "invited_names.txt"
# Replaces each [name] placeholder in "starting_letter.txt" with the actual name and creates a new file.
# New letter text files saved to folder "ReadyToSend".

PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt", mode="r") as starting_letter:
    letter_contents = starting_letter.read()

with open("./Input/Names/invited_names.txt", mode="r") as invited_names:
    invitees = invited_names.readlines()

for guest in invitees:
    stripped_guest = guest.strip()
    new_letter_text = letter_contents.replace(PLACEHOLDER, guest)
    with open(f"./Output/ReadyToSend/{stripped_guest}.txt", mode="w") as final_letter:
        final_letter.write(new_letter_text)
