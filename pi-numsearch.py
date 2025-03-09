import os

# File paths
pi_file_path = "D:\\pi-billion.txt"
encodings_file_path = "D:\\encodings.txt"

# Load encodings
with open(encodings_file_path, "r") as f:
    encodings = set(f.read().splitlines())

# Function to search for matches in Pi
def search_in_pi():
    buffer_size = 10**7  # Read in chunks of 10 million characters
    match_found = False
    position = 0

    with open(pi_file_path, "r") as f:
        # Remove '3.' from the beginning
        f.seek(2)  

        while True:
            chunk = f.read(buffer_size)
            if not chunk:
                break  # End of file

            for encoding in encodings:
                if encoding in chunk:
                    print(f"Match found: {encoding} at approximate position {position + chunk.find(encoding)}")
                    match_found = True

            position += len(chunk)

    if not match_found:
        print("No matches found.")

# Run search
search_in_pi()
