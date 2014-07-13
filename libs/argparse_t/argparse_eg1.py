#encoding=utf-8
'''
Created on 2014-7-13

@author: jack
'''
import argparse

def cmd():
    print 'cmd'
    parser = argparse.ArgumentParser(description='Parse Arguments')
    
    parser.add_argument('-d',
                        '--store-dir',
                        dest='dirname',
                        action='store',
                        default='Default Value',
                        help='path to store files')
    args = parser.parse_args()
    print args
#     maybe . operation has been rewritten in argparse.Namespace
    print type(args)

if __name__=='__main__':
    cmd()