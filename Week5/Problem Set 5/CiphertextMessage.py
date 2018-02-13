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

        # Making a list of input text
        self.message_text = [word for word in self.message_text.split()]
        # Making a copy of above list
        message_text_copy = self.message_text[:]
        length = len(self.message_text)
        # Taking one letter from the list to get the value by which the entire text is shifted. What I thought here was that I should first calculate shift by using only one word and then apply that shift to whole paragraph
        self.message_text = self.message_text[length - 1][:]
        # Loop for finding shift
        for i in range(26):
            a = self.apply_shift(i)
            if a in self.valid_words:
                # Num is the shift value
                num = i
        # As the self.message_text retined only one word and lost others, I equated self.message_text to it's copy made earlier
        self.message_text = message_text_copy
        # List in which answers will be saved
        story = list()
        # Running loop for getting original message using the value of shift calculated earlier
        for i in range(len(self.message_text)):
            # giving one word at a time
            self.message_text = self.message_text[i]
            # getting actual word
            ans = self.apply_shift(num)
            # adding the word to list
            story.append(ans)
            # If this step is not done then the answer will have no spaces at all
            story.append(' ')
            # As the self.message_text retined only one word and lost others, I equated self.message_text to it's copy made earlier
            self.message_text = message_text_copy
        # We don't need space in the end of the list so this code deletes that space
        del story[-1]
        # Returning joint list of answer
        return (num, ''.join(story))
