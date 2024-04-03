import os 
import shutil

from_dir = "/Users/gautammahesh/Downloads/C102_assets-main"
to_dir = "/Users/gautammahesh/Downloads/images"
list_of_files = os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name, ext = os.path.splitext(file_name)
    #print(name)
   # print(ext)
    if ext==" ":
        continue
    if ext in ['.gif', '.png', '.jpeg', '.jpg', '.jfif']:
        pathone = from_dir+'/'+file_name
        pathtwo = to_dir+'/'+"image_files"
        paththree = to_dir+'/'+"image_files"+'/'+file_name
        #print("pathone", pathone)
        #print("paththree", paththree)
        if os.path.exists(pathtwo):
            print("moving"+file_name+"...")
            shutil.move(pathone, paththree)
        else: 
            os.makedirs(pathtwo)
            print('moving'+file_name+"...")
            shutil.move(pathone,paththree)