import sys


# 面向过程

'''
d = {}

d['-c'] = sys.argv[sys.argv.index('-c')+1]
d['-d'] = sys.argv[sys.argv.index('-d')+1]
d['-o'] = sys.argv[sys.argv.index('-o')+1]

print(d)
'''

# 面向对象 1


class Args1:
    '''
    处理命令行参数的类
    '''

    def __init__(self):
        self.d = {}
        self.parse_argv()

    def parse_argv(self):
        self.d['-c'] = sys.argv[sys.argv.index('-c')+1]
        self.d['-d'] = sys.argv[sys.argv.index('-d')+1]
        self.d['-o'] = sys.argv[sys.argv.index('-o')+1]


# 面向对象 2


class Args2:
    '''
    处理命令行参数的类
    '''

    def __init__(self):
        self.c = sys.argv[sys.argv.index('-c')+1]
        self.d = sys.argv[sys.argv.index('-d')+1]
        self.o = sys.argv[sys.argv.index('-o')+1]



if __name__ == '__main__':
    args = Args2()
    print(args.c)
    print(args.d)
    print(args.o)



