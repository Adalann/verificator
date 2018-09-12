#!/usr/bin/env python3

import getopt
import hashlib
import os
import platform
import re
import shutil
import sys


def digDirectory(path):
    fileList = []
    try:
        for item in os.scandir(path):
            if item.is_file() and item.name != "index":
                fileList.append(item)
            elif item.name != "index":
                fileList += digDirectory(item)
        return fileList
    except OSError as e:
        print("OS error : {}".format(e))


def hashFile(filePath):
    hasher = hashlib.sha256()
    with open(filePath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)

    return hasher.hexdigest()


def getHashes(fileList):
    hashData = {}
    for file in fileList:
        fileHash = hashFile(file.path)
        hashData[file.name] = fileHash

    return hashData


def handleRemoteRepo(url, repoName):
    urlRegex = re.compile(r'^https://github.com/([\w\.@\:/\-~]+).git$')

    if urlRegex.match(url):
        print('Repo found, cloning...')
        clonedRepoPath = os.getcwd() + '/' + repoName
        os.system('git clone -q {} {}'.format(url, clonedRepoPath))
        remoteRepoHashData = getHashes(digDirectory(clonedRepoPath))
        print('Deleting generated files for downloaded repo...')
        shutil.rmtree(clonedRepoPath)
        return remoteRepoHashData
    else:
        print('This is not a GitHub repo url')
        sys.exit(-1)


def handleLocalRepo(path, repoName):
    if os.path.exists(path):
        localRepoHashData = getHashes(digDirectory(path))
        return localRepoHashData
    else:
        print('The path {} does not refer to an existing file or directory'.format(path))
        sys.exit(-1)
 

def displayList(aList):
    print('[')
    for element in aList:
        print("  {}".format(element))
    print(']')


def main(url, path):
    if url == None:
        url = input("URL to GitHub repo (https://github.com/user/repo-name.git) : ")
    repoName = url.replace('https://github.com/', '').replace('.git', '').split('/')[1]
    remoteRepoHash = handleRemoteRepo(url, repoName)

    if path == None:
        path = input('Path to the local repo : ')
    if path.endswith('/'):
        path = path[:len(path) - 2]
    localRepoHash = handleLocalRepo(path, repoName)
    edited = False
    modifiedFiles = []

    for file, fileHash in remoteRepoHash.items():
        if localRepoHash[file] != fileHash:
            edited = True
            modifiedFiles.append(file)
    if edited:
        print("Your local repo has been modified, please consider re-clone the repo to work with a fresh and safe copy.")
        print("Here is the list of the modified files :")
        displayList(modifiedFiles)
        sys.exit(1)
    else:
        print("Your local repo hasn't been modified, go to work !")
        sys.exit()


def usage():
    print(
        """
        Usage : verificator.py [OPTIONS]

        OPTIONS :
            You can specify the following options:
            -u, --url  : the GitHub repo's url (https://github.com/user/repo-name.git)
            -p, --path : the path to the local directory to test

        Use the -h, --help flag to see this help
        """
    )


if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hu:p:", ["help", "url", "path"])
        url = None
        path = None
        for opt, arg in opts:
            if opt in ("-u", "--url"):
                url = arg
            elif opt in ("-p", "--path"):
                path = arg
            else:
                usage()
                sys.exit(2)

        main(url, path)
        
    except getopt.GetoptError:          
        usage()                         
        sys.exit(2)
