"""
Created on TUE AUG 4 16:49:00 2020

@description Change picture name for Android and IOS together
@author Richard
"""
#%%
import os
import shutil

def getName(tag=""):
    if(tag != "" and tag != "1x"):
        tag = "@" + tag
    if tag == "1x":
        tag = ""
        
    MODEL_NAME = {
        # f"example{tag}.png": f"example_new{tag}.png",
    }
    
    return MODEL_NAME

def getAndroidPath():
    return [
        "Android/drawable-mdpi",
        "Android/drawable-hdpi",
        "Android/drawable-xhdpi",
        "Android/drawable-xxhdpi",
        "Android/drawable-xxxhdpi",
    ]

def getIOSPath():
    return [
        "1x",
        "2x",
        "3x",
    ]

#%%
root_dir = os.path.dirname(os.path.abspath("__file__"))
img_dir = os.path.join(root_dir,"change_Android_IOS_pic_name/img")
output_dir = os.path.join(root_dir,"change_Android_IOS_pic_name/output")

# For integration of ios picture in the same folder
new_1x_dir = os.path.join(output_dir,"iOS","1x")

#%%

def changeName(dir="",dir_n="",tag=""):
    if dir != "" and dir_n != "":
        for ori,new in getName(tag).items():
            file = os.path.join(dir,ori)
            file_new = os.path.join(dir_n,new)
            
            if(os.path.exists(file)):
                if not os.path.isdir(dir_n):
                    # If it does NOT exist folder, it will be created
                    os.makedirs(dir_n)
                
                os.rename(file,file_new)
                
                # For integration of ios picture in the same folder
                if tag == "2x" or tag == "3x":
                    file_1x_new = os.path.join(new_1x_dir,new)
                    shutil.copyfile(file_new,file_1x_new)
                    
                print("Rename successfully")
            else:
                print("File does NOT exist");


#%%
files_dir = os.path.join(img_dir,getAndroidPath()[0])
print(os.listdir(files_dir))

#%%
for single_path in getAndroidPath():
    files_dir = os.path.join(img_dir,single_path)
    new_files_dir = os.path.join(output_dir,single_path)
    changeName(files_dir,new_files_dir)

for single_path in getIOSPath():
    files_dir = os.path.join(img_dir,"iOS",single_path)
    new_files_dir = os.path.join(output_dir,"iOS",single_path)
    changeName(files_dir,new_files_dir,single_path)

print("Finish!")
#%%
