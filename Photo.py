""" Photo class """
# The objective of that file is to create a Photo class.
# An instance of the Photo should have the properties listed below:
# An uid(not name), name, path, datetime.
# uid will be randomly generated, name, path will be original.
# datetime will be extracted from MODIFIED date and time data.


class Photo:
    def __init__(self, directory, name):
        self.directory = directory
        self.name = name
        self.datetime = None            # an instance of Photo will get datetime and uid
        self.uid = None                 # later (with method of Photo class). So they're 'None' for now.
        
    def __str__(self):
        s = 'uid:\t'
        if self.uid:
            s += str(self.uid) + ',\t'
        else:
            s += 'NO UID,\t'
        s += 'date/time:\t'
        if self.datetime:
            s += str(self.datetime) + ',\t'
        else:
            s += 'NO DATE/TIME,\t'
        s += 'directory:\t' + self.directory
        s += 'name:\t' + self.name
        return s
        
    def get_uid(self, uid):             
        """ get uid from the 'Library.generate_uid()' """
        self.uid = uid   
        
    def get_directory(self, directory):
        pass                             
        
# test phase

photo = Photo('directory/test', 'IMG_TEST.JPG')

print photo

photo.get_uid(1)

print photo

     
        
