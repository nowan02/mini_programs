* 26 key table
* a - z lowercase
* The last letter of a word -> into the table
* Word is maximum 10 letters long
* Table statuses; tombstone, occupied, never used
* Table starts with never used
* Searching:
    - Given a word, take it's last character
    - Search the corresponding slot
    - If it's there, found it
    - If tombstone or never used, it doesn't exist
    - Search until word is found, or until it's certain it doesn't exist
* Insertion:
    - First perform a search if the key exists, if it does, do nothing
    - If the corresponding slot is never used or tombstone, insert there
    - If occupied, try the next slot, until an empty one is found
* Deletion:
    - Search for the given value, if found change the slot to tombstone
* Commands:
    - AWord -> Add word
    - DWord -> Remove word
    - Ignore invalid inputs
    - When inputs are processed, print the table with space as separator