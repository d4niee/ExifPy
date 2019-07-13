
'''
-------------------------------------------------------

ExifPy is a python script to read the metadatas
in jpg, jpeg, png,.. img files

@author: Daniel Lambrecht (d4nny251)
@version 0.1
required python version: 3 or higher 

-------------------------------------------------------
'''


try:
    from PIL import Image
    from PIL.ExifTags import TAGS
except ImportError as e:
    print("\033[1;31;40m[X]Missing modules... please install them with")
    print("\npip install -r requirements")
import os 



#banner function to draw the banner
def banner():
    print("\n\n\033[1;33;40m          _  __           ")
    print("\033[1;33;40m  _____ _(_)/ _|\033[1;32;40m_ __ _  _ ")
    print("\033[1;33;40m / -_) \ / |  _\033[1;32;40m| '_ \ || |   \033[1;33;40mdeveloper: \033[1;32;40m@d4nny251")
    print("\033[1;33;40m \___/_\_\_|_| \033[1;32;40m| .__/\_, |   \033[1;33;40mversion  : \033[1;32;40m0.1")
    print("\033[1;33;40m               \033[1;32;40m|_|   |__/    \033[1;33;40mgithub   : \033[1;32;40mhttps://github.com/d4nny251/exifpy")

#function to save the exif datas into a output file 
def save_to_file(tag, value, img, md, out):
    i = 1
    if not os.path.exists("files"):
        os.mkdir("files")
    try:
        with open("files/"+out, 'w') as f:
            for (tag ,value) in md.items():
                if i == 1:
                    f.write("METADATA of Image <"+img+">\n\n")
                f.write(str(tag) + ":\t" +\
                        str(value) + "\n")
                i = i + 1
            print("\33[1;32;40m[*] file was successfully created in file/"+out+"\033[1;37;40m")
    except:
        print("\033[1;31;40m[?] can't write in file (file was not created)...")



def get_meta_datas(imgpath):
    try:
        metadata = {}
        img = Image.open(imgpath)
        print("\n\033[1;32;40m[\033[1;37;40m*\033[1;32;40m] \033[1;33;40mgetting meta data...\033[1;37;40m")
        info = img._getexif()
        if info:
            print("\033[1;32;40m[*] meta data was found!\033[1;37;40m\n\n")
            print("-----------------------\n")
            for (tag, value) in info.items():
                tagname = TAGS.get(tag, tag)
                metadata[tagname] = value
                print(tagname, value)
            print("\n----------------------- \n")
            out = input("\033[1;32;40m[\033[1;37;40m*\033[1;32;40m]\033[1;33;40m output file (leave empty if none):\033[1;37;40m ")
            save_to_file(tagname, value, imgpath, metadata, out)

        else:
            print("\033[1;31;40m[X] meta data not found...")
        
    except:
        print("\033[1;31;40m[X] error: can't open the file '"+imgpath+"'")


if __name__ == "__main__":

    banner()
    img = input("\n\n\n\033[1;32;40m[\033[1;37;40m*\033[1;32;40m]\033[1;33;40m Image path:\033[1;37;40m ")
    get_meta_datas(img)
