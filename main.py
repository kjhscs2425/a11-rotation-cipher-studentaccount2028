import string

alphabet = string.ascii_lowercase
print(alphabet)

password = "hi potato zzz"
# eve wants to steal my password

# make my password secret
key = 4

def encrypt(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        old_position = alphabet.find(letter)
        if old_position == -1:
            ciphertext += " "
        else:
            new_position = old_position + key
            new_position = new_position % len(alphabet)
            new_letter = alphabet[new_position]
            ciphertext += new_letter
    return ciphertext

# print(encrypt(password, key))

# Your task:
# figure out what key I used to encrypt this message:
secret_message = "y qc q iushuj cuiiqwu oek mybb duluh wkuii"


def decrypt(secret_message, key):
    text = ""
    for letter in secret_message:
        old_position = alphabet.find(letter)
        if old_position == -1:
            text += " "
        else:
            new_position = old_position - key
            new_position = new_position % len(alphabet)
            new_letter = alphabet[new_position]
            text += new_letter
    return text
    # old_position = new_position - key
    # old_position = old_position * len(alphabet)
    # old_letter = alphabet[old_position]
    # decryptedtest = decryptedtext - old_letter

print(decrypt("y qc q iushuj cuiiqwu oek mybb duluh wkuii", key))

for i in range(50):
    print(decrypt("y qc q iushuj cuiiqwu oek mybb duluh wkuii", 16))

# # key = 1
# # for i in range(100000):
# #     cipherencrypt(password(key))
# #     if 
