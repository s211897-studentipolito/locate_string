import os, sys
import magic


def evaluate_dir (dir, key, flag, printdir):
    listD = os.listdir (dir)
    os.chdir (dir)
    with magic.Magic () as m:
        for fileN in listD:
            typefile = m.id_filename (fileN)
            if 'directory' in typefile:
                evaluate_dir (fileN, key, flag,dir + '/')
            elif 'ASCII' in typefile:
                if evaluate_file (fileN, dir, key, flag):
                    print (printdir + dir + fileN)
            else:
                pass
    os.chdir ('../')


def evaluate_file (filename, directory, key, flag):
    with open (filename, 'r') as fp:
        line = fp.readline ()
        while line:
            if key in line or (flag == True and key.lower() in line.lower()):
                return True
            else:
                line = fp.readline ()
    return False



if __name__ == '__main__':
    lowercaseFlag = False
    args = sys.argv[1:]
    for entry in args:
        if entry == '-i':
            lowercaseFlag = True
            args.remove (entry)
        if entry == '-h':
            print ('usage: directory, strings')
            exit ()
    dir = args.pop (0)
    for sKey in args:
        evaluate_dir (dir, sKey, lowercaseFlag, '')
