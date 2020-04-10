import subprocess
import re
import sys

def get_disk_space(filename): 
  with open(filename, 'w+') as f:
    df = subprocess.run('df', stdout=f, stderr=subprocess.DEVNULL)
def get_file_max_disk_usage(fname):
    get_disk_space(fname)
    filesystem=[]
    with open(fname) as f:
        for i in f:
            p1= re.compile('^.*100%.*$')
            if p1.match(i):
                Filesystem, Size, Used, Avail, Use, Mountedno =i.split()
                filesystem.append(Filesystem)
        return filesystem


def main():
    a=get_file_max_disk_usage(sys.argv[1])
    print(a)
if __name__ == "__main__":
    main()
