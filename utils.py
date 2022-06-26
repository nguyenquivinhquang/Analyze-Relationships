import os
class WriteFile(object):

    def __init__(self, save_path, filename, isFirstTime):
        self.save_path = os.path.join(save_path, filename + '.txt')
        if isFirstTime == True:
            f = open(self.save_path, 'w')
            f.close()

        return

    def update(self, infor):
        f = open(self.save_path, 'a')
        f.write(str(infor) + '\n')
        f.close()
        return