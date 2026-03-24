# Tacops-Scripting
Diff scripting questions

# Challenge 1: Who's Logged In?


Headquarters needs a quick roster of who logged in from the China office. The system log includes entries from all locations, but we only care about the workers in China.
Your task: extract only the names of workers who logged in from China, in the order they appear.

Example stdin: 

[Germany] Zara Chowdhury - 16:34  
Database synced  
[China] Jennifer Jacobs - 17:20  
[France] David Campbell - 10:11  
[Canada] Leila Howard - 04:35  
Backup completed  
[Brazil] Satoshi Turner - 09:34  
[Canada] Elijah Roberts - 18:58  
No activity  
[China] Mark Zhang - 09:34  
[Japan] Xavier Evans - 19:38  
[Germany] Ananya Richardson - 12:10  
[France] Ethan Gupta - 04:47  
Error: connection lost  
[China] Sarah Lee - 20:20  

Example Stdout:

Note: The flag should be the names found concatenated with no spaces.

Ex. tacops{JenniferJacobsMarkZhangSarahLee}

# Challenge 2: Who's Logged In Pt 2

So you completed the first task? We have a new job for you. We need a list of admin login IDs from the UK.

Each log entry contains a one-time login ID, but these IDs are encoded. When properly decoded, valid admin IDs will contain the string 'ADMIN' somewhere within them. Be aware that the logs include noise and invalid IDs, which should be ignored.
From the valid UK admin entries, extract the login IDs, remove the ADMIN portion, and concatenate the remaining values in the order they appear (top to bottom) to form the flag.

Here is a copy of the log file you will be working with. 

https://drive.google.com/uc?export=download&id=14OtTlChAGL6RpI8C7BOtfmrx8Mg5-pQK 

Best, 
Headquarters


