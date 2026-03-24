import sys

for line in sys.stdin.read().splitlines():
    if line.startswith('[China]'):
        # Remove location
        after_bracket = line.split('] ', 1)[1]
        # Remove time, keep only worker name
        worker_name = after_bracket.split(' - ', 1)[0]
        worker_name = worker_name.replace(" ","")
            print(worker_name)
            names += worker_name
            
print("tacops{"+names+"}")
