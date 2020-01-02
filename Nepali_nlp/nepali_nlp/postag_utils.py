class PostagUtils:
    """
    This class will help us to preprocess  encode text and POS TAG
    """

    def __init__(self, max_length):
        self.max_length = max_length
        pass

    def padding_sequence(self,sequence):
        """This function make pad the sequence with fix length
            
                Arguments:
                     {list} -- list of tokenized sequence 
                Returns:
                    list --  list of padded sequences
                """
        true_length = len(sequence)
        temp_sequence = sequence
        for idx in range(true_length,self.max_length):
            temp_sequence.append('<PAD>')
        return temp_sequence 