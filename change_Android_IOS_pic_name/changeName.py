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
        "drawable-mdpi",
        "drawable-hdpi",
        "drawable-xhdpi",
        "drawable-xxhdpi",
        "drawable-xxxhdpi",
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


#%%

def changeName(dir="",dir_n="",tag=""):
    if dir != "" and dir_n != "":
        for ori,new in getName(tag).items():
            file = os.path.join(dir,ori)
            file_new = os.path.join(dir_n,new)
            
            if(os.path.exists(file)):
                if not os.path.isdir(dir_n):
                    os.mkdir(dir_n)
                
                shutil.copyfile(file,file_new)
                print("Rename successfully")
            else:
                print("File does NOT exist");


#%%
files_dir = os.path.join(img_dir,getAndroidPath()[0])
print(os.listdir(files_dir))

# %%
for single_path in getAndroidPath():
    files_dir = os.path.join(img_dir,single_path)
    new_files_dir = os.path.join(output_dir,single_path)
    changeName(files_dir,new_files_dir)

for single_path in getIOSPath():
    files_dir = os.path.join(img_dir,single_path)
    new_files_dir = os.path.join(output_dir,single_path)
    changeName(files_dir,new_files_dir,single_path)

print("Finish!")
#%%
