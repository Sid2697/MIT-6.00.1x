import string

### DO NOT MODIFY THIS FUNCTION ###


def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###


def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


WORDLIST_FILENAME = 'words.txt'


class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        # pass  # delete this line and replace with your code here
        dict_cipher = dict()
        # Getting uppercase and lowercase letters
        a = string.ascii_lowercase
        b = string.ascii_uppercase
        # Getting list of uppercase and lowercase letters
        a = [letter for letter in a]
        b = [letter for letter in b]
        # Initializing lists
        lower_dict = dict()
        upper_dict = dict()
        i = shift
        # assigning lower case letters to shifted lower case in form of dictionary
        for letter in a:
            lower_dict[letter] = a[i]
            i += 1
            if i >= 26:
                i = 0
        # assigning upper case letters to shifted upper case in form of dictionary
        i = shift
        for letter in b:
            upper_dict[letter] = b[i]
            i += 1
            if i >= 26:
                i = 0
        # Method of merging two different dictionaries
        final_dict = {**upper_dict, **lower_dict}
        return final_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        a = list()
        # getting shifted dictionary from above function
        main_dict = self.build_shift_dict(shift)
        # converting word into list
        word = [letter for letter in self.message_text]
        # changing input string to encrpyted string
        for letter in word:
            # Check for letters other than uppercase and lowercase alphabets
            if letter not in main_dict:
                a.append(letter)
            else:
                a.append(main_dict[letter])
        # Joining charachtes in list to form string
        b = ''.join(a)
        return b


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less
        code is repeated
        '''
        # pass  # delete this line and replace with your code here
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        # pass  # delete this line and replace with your code here
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class

        Returns: a COPY of self.encrypting_dict
        '''
        # pass  # delete this line and replace with your code here
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        # pass  # delete this line and replace with your code here
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift (ie. self.encrypting_dict and
        message_text_encrypted).

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        # pass  # delete this line and replace with your code here
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # pass  # delete this line and replace with your code here
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # pass  # delete this line and replace with your code here
        # valid_words = load_words(WORDLIST_FILENAME)
        # Getting puncuation characters
        punch = string.punctuation
        # Making a list of input text
        self.message_text = [word for word in self.message_text.split()]
        # Making a copy of above list
        message_text_copy = self.message_text[:]
        length = len(self.message_text)
        # If the last letter contains '.' then it is not a valid word, so to escape puntation this block is being used
        for things in self.message_text[length - 1]:
            if things in punch:
                sid = 2
                break
            else:
                sid = 1
        # Taking one letter from the list to get the value by which the entire text is shifted. What I thought here was that I should first calculate shift by using only one word and then apply that shift to whole paragraph
        self.message_text = self.message_text[length - sid][:]
        # Loop for finding shift
        for i in range(26):
            a = self.apply_shift(i)
            if a in self.valid_words:
                # Num is the shift value
                number = i

        # As the self.message_text retined only one word and lost others, I equated self.message_text to it's copy made earlier
        self.message_text = message_text_copy
        # List in which answers will be saved
        story = list()
        # Running loop for getting original message using the value of shift calculated earlier
        for i in range(len(self.message_text)):
            # giving one word at a time
            self.message_text = self.message_text[i]
            # getting actual word
            ans = self.apply_shift(number)
            # adding the word to list
            story.append(ans)
            # If this step is not done then the answer will have no spaces at all
            story.append(' ')
            # As the self.message_text retined only one word and lost others, I equated self.message_text to it's copy made earlier
            self.message_text = message_text_copy
        # We don't need space in the end of the list so this code deletes that space
        del story[-1]
        # Returning joint list of answer
        return (number, ''.join(story))


def decrypt_story():
    ciphertext = CiphertextMessage(get_story_string())
    (a, b) = ciphertext.decrypt_message()
    return (a, b)

# Example test case (PlaintextMessage)
# plaintext = PlaintextMessage('hello', 2)
# print('Expected Output: jgnnq')
# print('Actual Output:', plaintext.get_message_text_encrypted())


# Example test case (CiphertextMessage)
# ciphertext = CiphertextMessage('jgnnq')
# print('Expected Output:', (24, 'hello'))
# print(ciphertext.decrypt_message())

# msg = Message('jgnnq jgnnq jgnnq jgnnq jgnnq')
# b = msg.get_valid_words()
# story = list()
# msg_list = [letter for letter in msg.get_message_text()]


ciphertext = CiphertextMessage(get_story_string())
print(ciphertext.decrypt_message())
# story1 = ciphertext.CiphertextMessage()

# print(decrypt_story())
