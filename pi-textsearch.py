import os
from itertools import product

# File paths
encodings_file_path = "D:\\encodings.txt"
pi_file_path = "D:\\pi-billion.txt"

def get_base_encoding(text):
    return [(ord(char) - ord('a')) if char.isalpha() else None for char in text.lower()]

def generate_encodings(base_encoding):
    shift_ranges = [range(num, 100, 26) if num is not None else [None] for num in base_encoding]
    
    encodings = []
    for shifted_values in product(*shift_ranges):
        encoding = "".join(f"{num:02d}" if num is not None else " " for num in shifted_values)
        encodings.append(encoding)
    
    return encodings

def save_encodings(encodings, file_path):
    if os.path.exists(file_path):
        os.remove(file_path)  # Delete the file if it already exists
    
    with open(file_path, "w") as file:
        for encoding in encodings:
            file.write(encoding + "\n")

def generate_and_save_encodings():
    text = "text"  # Change this to your desired text input
    base_encoding = get_base_encoding(text)
    encodings = generate_encodings(base_encoding)
    save_encodings(encodings, encodings_file_path)
    print(f"Encodings saved to {encodings_file_path}")

def search_in_pi():
    # Load encodings
    with open(encodings_file_path, "r") as f:
        encodings = set(f.read().splitlines())
    
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

def main():
    generate_and_save_encodings()
    search_in_pi()

if __name__ == "__main__":
    main()
