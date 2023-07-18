# encrypted_decrypted_password_admin_system

encrypted password system for administration users.

-master password

-database with customer usernames and passwords

-encrypted key 

-modules: Fernet | OS 



future implementation ideas:
since it's too easy to reset the master password, when initially creating the master password,
I should set up a backup question/answer system. so I create my master password as 'masterpassword123' then after, 
I ask for future password resetting purposes, please type in a question and an answer that only you would know so question could be 'your first pet name' and 
answer could be 'skylar'. I could store the question and the answer in a txt file, then when needing to reset the master password, 
I would ask the question then if the input is 'skylar' then the master password txt file can be wiped so I can enter the new master password, 
if the answer to the question is wrong, then give 1 or 2 more tries and quit (or additionally, 
if there's a way to lock the system for 30 seconds for inputting too many wrong answers, then that would be another level of security)
