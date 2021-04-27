# rpmcamera
- This repo is the backend of the project. The ultimate goal here is to find the rpm of rotating no matter the speed just using its video.

## Rules
- Gitflow methadolgies should be used religiosly
- files that shouldn't be commited must be added to .gitignore.
- for every new package used .yaml file should be recompiled and pushed in next develop-commit.
- Files having size < 10mb should be uploaded in this google drive folder.
    https://drive.google.com/drive/folders/18lvZoHgPh4tyXl4oM-Q5vRjilFS72VRF?usp=sharing
    - name of file uploaded should be noted in "res\uploaded res.txt" with discription of file.
    - while using the file add it to .gitignore so that it won't get commited while staging changes.

## Setting up project in your pc
- To create the exact environment. (if conda is installed properly on your pc) just type
``conda env create --file envname.yml``

## The Todo List
- To do list is given in issue section in github

## Folder-File discription
- res: This folder is for resources means files like images videos etc.