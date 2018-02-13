# Defining the function
def decrypt_story():
    # Assigning story to class CipertextMessage
    ciphertext = CiphertextMessage(get_story_string())
    # a = shift
    # b = Decrypted Story
    (a, b) = ciphertext.decrypt_message()
    return (a, b)
