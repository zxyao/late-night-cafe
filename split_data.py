import sys
import random

def splitdata(fname):
    with open(fname + '.txt', 'r') as f:
        lines = f.read().splitlines()
        lines.sort()
        random.seed(233)
        random.shuffle(lines)
        split1 = int(0.8 * len(lines))
        split2 = int(0.9 * len(lines))
        train = lines[:split1]
        val = lines[split1:split2]
        test = lines[split2:]
        with open(fname+'.train.txt', 'w') as f:
            for line in train:
                f.write(line + '\n')
        with open(fname+'.val.txt', 'w') as f:
            for line in val:
                f.write(line + '\n')
        with open(fname+'.test.txt', 'w') as f:
            for line in test:
                f.write(line + '\n')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Give me data file name!")
        sys.exit()
    splitdata(sys.argv[1])