import os
import shutil
src = 'D:/Users/Ian/Percussion Data/Timpani/LeiChen_MoCap/S4'
dest = 'D:/Users/Ian/Thesis/S4'

srcfiles = os.listdir(src)

for filename in srcfiles:

    if filename.endswith('.tsv'):
        full_file_name = os.path.join(src, filename)
        shutil.copy(full_file_name, dest)
