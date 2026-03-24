import base64

valid_users = []
admin_ids = ""

with open("headquarter-log.txt", "r") as file:
    for line in file:
        # Only process lines that look like a UK log entry
        if line.startswith('[UK]'):
            try:
                # Split off location
                after_bracket = line.split('] ', 1)[1]  # "Lucas Rogers - 04:38 - QURNSU45MzcyODI="
                
                # Split into name, time, login_id
                name_part, time_part, login_id = map(str.strip, after_bracket.split(' - '))
                
                # Try to decode the Base64 login ID strictly
                decoded_id = base64.b64decode(login_id, validate=True).decode('utf-8', errors='ignore')
                
                # Only store the username if the decoded ID contains "ADMIN"
                if "ADMIN" in decoded_id:
                    valid_users.append(name_part)
                    decoded_id = decoded_id.replace("ADMIN", "")
                    decoded_id = str(decoded_id)
                    admin_ids += decoded_id
                    print(name_part, decoded_id)
            
            except (ValueError, IndexError):
                # Skip lines that fail splitting or Base64 decoding
                continue

# Build flag (concatenate usernames without spaces)
print("tacops{"+admin_ids+"}")
