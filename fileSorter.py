import os
import shutil

directoryInput = input("Enter the directory you want to be sorted (remove any quotes): ")
directoryFiles = os.listdir(directoryInput)

pdfFolder = os.path.join(directoryInput, 'PDFs')
if not os.path.exists(pdfFolder):
    os.mkdir(pdfFolder)
    print("Created PDFs folder directory.")

txtFolder = os.path.join(directoryInput, 'TXTs')
if not os.path.exists(txtFolder):
    os.mkdir(txtFolder)
    print("Created TXTs folder directory.")

exeFolder = os.path.join(directoryInput, 'EXEs')
if not os.path.exists(exeFolder):
    os.mkdir(exeFolder)
    print("Created EXEs folder directory.")

imageList = ['.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg']
imageFolder = os.path.join(directoryInput, 'Images')
if not os.path.exists(imageFolder):
    os.mkdir(imageFolder)
    print("Created Images folder directory.")

vidList = ['.mp4']
vidFolder = os.path.join(directoryInput, 'Videos')
if not os.path.exists(imageFolder):
    os.mkdir(imageFolder)
    print("Created Images folder directory.")

docList = ['.docx', '.html', '.xml']
docFolder = os.path.join(directoryInput, 'Docs')
if not os.path.exists(docFolder):
    os.mkdir(docFolder)
    print("Created Docs folder directory.")

for file in directoryFiles:
    if file.endswith('.pdf'):
        pdfSource = os.path.join(directoryInput, file)
        pdfDestination = os.path.join(pdfFolder, file)
        pdfFileMove = shutil.move(pdfSource, pdfDestination)
        print("Moved " + file + ' to ' + pdfDestination)
    elif file.lower().endswith(tuple(imageList)):
        imageSource = os.path.join(directoryInput, file)
        imageDestination = os.path.join(imageFolder, file)
        imageFileMove = shutil.move(imageSource, imageDestination)
        print("Moved " + file + ' to ' + imageDestination)
    elif file.lower().endswith(tuple(docList)):
        docSource = os.path.join(directoryInput, file)
        docDestination = os.path.join(docFolder, file)
        docFileMove = shutil.move(docSource, docDestination)
        print("Moved " + file + ' to ' + docDestination)
    elif file.lower().endswith(tuple(vidList)):
        vidSource = os.path.join(directoryInput, file)
        vidDestination = os.path.join(vidFolder, file)
        vidFileMove = shutil.move(vidSource, vidDestination)
        print("Moved " + file + ' to ' + vidDestination)
    elif file.endswith('.txt'):
        txtSource = os.path.join(directoryInput, file)
        txtDestination = os.path.join(txtFolder, file)
        txtFileMove = shutil.move(txtSource, txtDestination)
        print("Moved " + file + ' to ' + txtDestination)
    elif file.endswith('.exe'):
        exeSource = os.path.join(directoryInput, file)
        exeDestination = os.path.join(txtFolder, file)
        exeFileMove = shutil.move(exeSource, exeDestination)
        print("Moved " + file + ' to ' + exeDestination)
    else:
        print("No files were detected to sort!")
