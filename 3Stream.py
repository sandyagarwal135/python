import sys
# print(open("C:/Sandeep/Python/File/hosts").read())

def readfile():
    try:
        file_name="C:/Sandeep/Python/File/hosts"
        with file_name as abc:
            for line in abc:
                print(line)
    except:
        print("could not open file {0}",format(file_name))
        sys.exit(1)

if __name__ == '__main__':
    readfile()


