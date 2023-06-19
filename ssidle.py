import base64
import gzip
import os

#takes an input representing a saved game from Unnamed Space Idle and allows you to decrypt it / change values within the resulting json 
#and then re-encrypt it to load back into the game.  The file must not be saved as a text format, use a hex editor or some other mechanism
#to ensure the non-ascii values are preserved or it will not load

def base64_to_json(base64_string):

    decoded_bytes = base64.b64decode(base64_string)

    try:
        decompressed_bytes = gzip.decompress(decoded_bytes)

        output_file_path = os.path.join(os.path.dirname(__file__), "decompressed.txt")
        with open(output_file_path, "wb") as file:
            file.write(decompressed_bytes)
        print("Decrypted data saved to:", output_file_path)
    except OSError:
        print("The input string is not gzip-encoded.")


def compress_and_encode(file_path):
    try:

        with open(file_path, "rb") as file:
            data = file.read()

        compressed_data = gzip.compress(data)

        encoded_data = base64.b64encode(compressed_data)

        save_file_path = os.path.join(os.path.dirname(__file__), "save.txt")
        with open(save_file_path, "wb") as save_file:
            save_file.write(encoded_data)

        print("Output encrypted data to save.txt.")
    except OSError:
        print("Error occurred while compressing and encoding the file.")

# Path to the decompressed file
decompressed_file_path = os.path.join(os.path.dirname(__file__), "decompressed.txt")


#Paste save string here, too lazy to pull it in from a separate file since the save file names are constantly changing
base64_string = "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"

#flip these two functions depending on your goal

#use this to decrypt to a "Not quite json" format
# base64_to_json(base64_string) #input

#use this to re-encode to the proper save-file format
compress_and_encode(decompressed_file_path) #output


