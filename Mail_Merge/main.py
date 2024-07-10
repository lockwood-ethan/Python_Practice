#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
with open("./Mail_Merge/Input/Names/invited_names.txt") as data:
    names = data.readlines()
    
with open("./Mail_Merge/Input/Letters/starting_letter.txt") as data:
    letter = data.read()
    
for name in names:
    name = name.strip()
    new_letter = letter.replace("[name]", name)
    with open("./Mail_Merge/Output/ReadyToSend/"f"letter_for_{name}.txt", "w") as data:
        data.write(new_letter)