import pickle

class PosUtils:
    def __init__(self):
         """This class helps preprocess pos tag before feeding into the model"""
         pass


    def load_dataset(self,path):
        """ yari yari yara"""
        dbfile = open(path, 'rb')
        df = pickle.load(dbfile)
        return data_df


#-----------------------TEST CASE------------------------
utils = PosUtils()
data = utils.load_dataset('../local_dataset/processed_tag')
