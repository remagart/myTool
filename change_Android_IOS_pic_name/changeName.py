"""
Created on TUE AUG 4 16:49:00 2020

@description Change picture name for Android and IOS together
@author Richard
"""
#%%
import os

def getName(tag=""):
    if(tag != ""):
        tag = "@" + tag
        
    MODEL_NAME = {
        # f"example{tag}.png": f"example_new{tag}.png",
        f"aa{tag}.png": f"aaa{tag}.png",
        f"bb{tag}.png": f"bbb{tag}.png",
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

files_dir = os.path.join(img_dir,getAndroidPath()[4])
new_files_dir = os.path.join(output_dir,getAndroidPath()[4])

print(files_dir)


print(files_dir)

print(os.listdir(files_dir))

#%%

print(getName())
for ori,new in getName().items():
    file = os.path.join(files_dir,ori)
    file_new = os.path.join(new_files_dir,new)
    
    if(os.path.exists(file)):
        if not os.path.isdir(new_files_dir):
            os.mkdir(new_files_dir)
            
        os.rename(file,file_new)
        print("Rename successfully")
    else:
        print("File does NOT exist");


#%%

# %%
