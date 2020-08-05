#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.


import zipfile, os

def backupToZip(folder):
    # Back up the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder)  # make sure folder is absolute

    # Figure out the filename this should use based on
    # what files already exist
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # Add the current folder to the ZIP file.
        backupZip.write(os.path.basename(foldername))

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue        # don't back up the ZIP files
            backupZip.write(os.path.join(os.path.basename(foldername), filename))
        backupZip.close()
        print('Done')


backupToZip('folderToZip')
#backupToZip(r'C:\Users\Bamboozle\PycharmProjects\learning_material\Chapter 10\backupToZip\folderToZip')

