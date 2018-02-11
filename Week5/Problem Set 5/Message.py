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
        # pass  # delete this line and replace with your code here
        # Defining list for storing word in form of list

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
        a = list()
        # getting shifted dictionary from above function
        main_dict = build_shift_dict(self, shift)
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
