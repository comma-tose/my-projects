# This program brute forces all ten billion Windows 95 keys to see if they are valid.
# Made in a few hours at school.
# Does not work in the slightest

invalid_keys = 0
valid_keys = 0
#found_keys = [] # Removed for memory optimizations

for i in range(000, 999):
    print(f"Attempting block {i+1}/1000") # Optional, allows for tracking the progress of the script without using as much memory.
    for j in range(0000000, 9999999):
        k1 = str(i)
        while not len(k1) == 3:
            k1 = f"0{k1}"
        k2 = str(j)
        while not len(k2) == 7:
            k2 = f"0{k2}"
        if int(k1) == 333 or int(k1) == 444 or int(k1) == 555 or int(k1) == 666 or int(k1) == 777 or int(k1) == 888 or int(k1) == 999:
            invalid_keys = invalid_keys + 1
            #print(f"Key {k1}-{k2} invalid.") # Removed for memory optimizations
        else:
            if (int(k2[0]) + int(k2[1]) + int(k2[2]) + int(k2[3]) + int(k2[4]) + int(k2[5]) + int(k2[6]))%7 == 0 and not "9" in str(k2):
                #print(f"Key {k1}-{k2} valid.") # Removed for memory optimizations
                valid_keys = valid_keys + 1
                #found_keys.append(f"{k1}-{k2}") # Removed for memory optimizations
            else:
                invalid_keys = invalid_keys + 1
                #print(f"Key {k1}-{k2} invalid.") # Removed for memory optimizations

print(f"{invalid_keys} invalid keys found.")
print(f"{valid_keys} valid keys found.")
print(f"{invalid_keys + valid_keys} keys attempted.")
#print("Loading keys...") # Removed for memory optimizations
#for k in range(len(found_keys)): # Removed for memory optimizations
    #print(found_keys[k]) # Removed for memory optimizations