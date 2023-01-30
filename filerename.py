import os
import shutil

url = input('Enter Source: ')
items = 0
p_folder = ''

completed = 0

for i in url:
    if i == '\\':
        p_folder += '/'
        continue
    p_folder += i
p_folder += '/'

for count, foldername in enumerate(os.listdir(p_folder)):
    items += 1

for count, foldername in enumerate(os.listdir(p_folder)):

    folder = p_folder+foldername+'/'
    renamed = 'renamer'
    

    for count, filename in enumerate(os.listdir(folder)):
        index = len(filename)-1
        for i in filename[::-1]:
            if i == '.':
                break
            index -= 1
        
        dst = f'{str(count+1)}{filename[index:]}'
        src =f"{folder}/{filename}"
        dst = f'{renamed}/{dst}'
        os.rename(src,dst)

    completed += 1

    print(f'{completed}/{items}')
    print('File renamed successfully...')

    for count, filename in enumerate(os.listdir(renamed)):
        shutil.move(f'{renamed}/{filename}', f'{folder}/{filename}')

    print('File moved successfully')
    
