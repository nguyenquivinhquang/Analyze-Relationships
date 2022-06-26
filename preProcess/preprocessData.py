
class PreprocessData(object):

    def __init__():
        return

    @property
    def data(self):
        return self.dataframe

    def filter_in_range(self, lower, upper):
        self.dataframe = self.dataframe[self.dataframe["YEAR"].between(lower, upper)].reset_index()

        return
