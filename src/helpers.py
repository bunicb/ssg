import os
import shutil

def copy_static_files(src, dst):
    # empty the public folder if it exists
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)

    contents = os.listdir(src)
    for file in contents:
        src_file = os.path.join(src, file)
        dst_file = os.path.join(dst, file)
        print(f"Copying {src_file} to {dst_file}")
        if os.path.isfile(src_file):
            shutil.copy2(src_file, dst_file)
        elif os.path.isdir(src_file):
            copy_static_files(src_file, dst_file)
