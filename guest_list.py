#Ryan Walters Nov14 2020 -- A simple project that prints guest list invitations, and then adds and removes its items.
#Initial guest list and name variable
guest_list = ['david', 'mike', 'jimbo', "lewis"]
my_name = 'ryan walters'

#Initial invitations
#David
invitation1 = f"Greetings, {guest_list[0].title()}. I would like to cordially invite you to a specially prepared dinner at my apartment. Please let me know if you can make it. It would be great to see you again. Sincerely, {my_name.title()}"
#Mike
invitation2 = f"Greetings, {guest_list[1].title()}. I would like to cordially invite you to a specially prepared dinner at my apartment. Please let me know if you can make it. It would be great to see you again. Sincerely, {my_name.title()}"
#Jimbo
invitation3 = f"Greetings, {guest_list[2].title()}. I would like to cordially invite you to a specially prepared dinner at my apartment. Please let me know if you can make it. It would be great to see you again. Sincerely, {my_name.title()}"
#Lewis
invitation4 = f"Greetings, {guest_list[3].title()}. I would like to cordially invite you to a specially prepared dinner at my apartment. Please let me know if you can make it. It would be great to see you again. Sincerely, {my_name.title()}"

#Printing initial invitations
print(invitation1)
print(invitation2)
print(invitation3)
print(invitation4)

#Modifying
print(f"Oh dear, it seems that our friend {guest_list[2].title()} cannot attend the event this evening. We will have to invite someone else.")
guest_list[2] = 'bilbo'
invitation3 = f"Greetings, {guest_list[2].title()}. I would like to cordially invite you to a specially prepared dinner at my apartment. Please let me know if you can make it. It would be great to see you again. Sincerely, {my_name.title()}"
print(invitation3)

#Inserting and Appending new names
guest_list.insert(0, 'Colton')
guest_list.insert(2, 'Kyle')
guest_list.append('Brianna')

#Printing new set of invitations
#Colton
invitation1 = f"Greetings, {guest_list[0].title()}. I would like to cordially invite you to a specially prepared dinner at my apartment. Please let me know if you can make it. It would be great to see you again. Sincerely, {my_name.title()}"
print(invitation1)
#David
invitation2 = f"Greetings, {guest_list[1].title()}. I would like to cordially invite you to a specially prepared dinner at my apartment. Please let me know if you can make it. It would be great to see you again. Sincerely, {my_name.title()}"
print(invitation2)
#Kyle
invitation3 = f"Greetings, {guest_list[2].title()}. I would like to cordially invite you to a specially prepared dinner at my apartment. Please let me know if you can make it. It would be great to see you again. Sincerely, {my_name.title()}"
print(invitation3)
#Mike
invitation4 = f"Greetings, {guest_list[3].title()}. I would like to cordially invite you to a specially prepared dinner at my apartment. Please let me know if you can make it. It would be great to see you again. Sincerely, {my_name.title()}"
print(invitation4)
#Bilbo
invitation5 = f"Greetings, {guest_list[4].title()}. I would like to cordially invite you to a specially prepared dinner at my apartment. Please let me know if you can make it. It would be great to see you again. Sincerely, {my_name.title()}"
print(invitation5)
#Lewis
invitation6 = f"Greetings, {guest_list[5].title()}. I would like to cordially invite you to a specially prepared dinner at my apartment. Please let me know if you can make it. It would be great to see you again. Sincerely, {my_name.title()}"
print(invitation6)
#Brianna
invitation7 = f"Greetings, {guest_list[6].title()}. I would like to cordially invite you to a specially prepared dinner at my apartment. Please let me know if you can make it. It would be great to see you again. Sincerely, {my_name.title()}"
print(invitation7)

#Shrinking guest list
print(f"Unfortunately, it so happens that I can only invite two guests. I am a terrible planner, I know.")

uninvited_colton = guest_list.pop(0)
uninvited_mike = guest_list.pop(2)
uninvited_bilbo = guest_list.pop(2)
uninvited_david = guest_list.pop(0)
uninvited_kyle = guest_list.pop(0)
print(guest_list)

uninvited1 = f"My Dearest Apologies {uninvited_colton.title()}, it appears I can no longer accomodate you at this party. I will however be having another dinner this weekend to make it up to you."
uninvited2 = f"My Dearest Apologies {uninvited_mike.title()}, it appears I can no longer accomodate you at this party. I will however be having another dinner this weekend to make it up to you."
uninvited3 = f"My Dearest Apologies {uninvited_bilbo.title()}, it appears I can no longer accomodate you at this party. I will however be having another dinner this weekend to make it up to you."
uninvited4 = f"My Dearest Apologies {uninvited_david.title()}, it appears I can no longer accomodate you at this party. I will however be having another dinner this weekend to make it up to you."
uninvited5 = f"My Dearest Apologies {uninvited_kyle.title()}, it appears I can no longer accomodate you at this party. I will however be having another dinner this weekend to make it up to you."
print(uninvited1)
print(uninvited2)
print(uninvited3)
print(uninvited4)
print(uninvited5)

#Final invitations
final_invitation1 = f"Dear {guest_list[0].title()}, I had to make some changes to the guest list tonight, but wanted to let you know that you are still invited! See you tonight."
final_invitation2 = f"Dear {guest_list[1].title()}, I had to make some changes to the guest list tonight, but wanted to let you know that you are still invited! See you tonight."
print(final_invitation1)
print(final_invitation2)

#Final Deletions to empty list
del guest_list[0]
del guest_list[0]
print(guest_list)

#END OF PROGRAM
