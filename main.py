import os.path

def read_file(fname):
    file = open(fname)
    for line in file:
        words = len(line.split())
        print(line,f"слів:{words} ,символів:{len(line)}")
    file.close()

if __name__ == '__main__':
    read_file(os.path.join('/Users/mac/Desktop/zalikk', 'text.txt'))