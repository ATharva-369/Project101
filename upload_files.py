'''
This program copies all the files from the given folder diectory and upoads them to a dropbox directory specified by the user.
It uses inputs for both of the directories
It uses the os and dropbox module and a class has been used to create an object, so that the functions and properties
can be reused
'''
import dropbox
import os

#constructing a class
class upload_folders(object):
    #inializing a constructor that takes an access_token for parameter to ensure reusability 
    def __init__(self, access_token):
        self.access_token = access_token
#constructing a upload_folder function that takes source and destination for parameters 
    def upload_folder(self, source, destination):

        db = dropbox.Dropbox(self.access_token)
        #checking if the directory inputed exists
        if os.path.exists(source):
            for root, dirs, files in os.walk(source):

                for filename in files:
                    #constructing a local path of the file using the local directory and the file's name
                    local_path = os.path.join(root, filename)
                    #constructing a relative path using the local_path variable and the local directory 
                    rel_path = os.path.relpath(local_path, source)
                    #constructing the dropbox path using the destination specified and the rel_path
                    db_path = os.path.join(destination, rel_path)

                    # upload the file
                    with open(local_path, 'rb') as f:
                        db.files_upload(f.read(), db_path,
                                        mode=dropbox.files.WriteMode.overwrite)
                        print('all the files have been uploaded ;)')
                        print("---------------------------------")
        else:
            print("are you sure the folder's path  exists? -_-")
            print("------------------------------------------------")                


def main():
    at = '4YD-pMmUrAkAAAAAAAAAATRVew8jifZqtA4HXifLchYUVxb69excS7G8Yag-aA0W'
    t = upload_folders(at)
    s = input("enter the folder's path: ")
    print("------------------------------------------------")  
    d = input(
        'enter the folder you want to store the files (for example /Music) in: ')
    print("------------------------------------------------")  
    t.upload_folder(s, d)



# calling the main function
main()
