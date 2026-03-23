# Tacops-Scripting
Diff scripting questions

# Challenge 1: Who's Logged In?


Headquarters needs a quick roster of who logged in from the China office. The system log includes entries from all locations, but we only care about the workers in China.
Your task: extract only the names of workers who logged in from China, in the order they appear.

Example stdin: 

[Germany] Zara Chowdhury - 16:34  
Database synced  
[China] Nora Lui - 17:20  
[France] David Campbell - 10:11  
[Canada] Leila Howard - 04:35  
Backup completed  
[Brazil] Satoshi Turner - 09:34  
[Canada] Elijah Roberts - 18:58  
No activity  
[China] Nancy Zhang - 09:34  
[Japan] Xavier Evans - 19:38  
[Germany] Ananya Richardson - 12:10  
[France] Ethan Gupta - 04:47  
Error: connection lost  
[China] Chloe Lee - 20:20  

Example stdout:

Nora Lui  
Nancy Zhang  
Chloe Lee  

The flag should be the names found concatenated with no spaces.

Ex. tacops{NoraLuiNancyZhangChloeLee}

