#!/usr/bin/python3

__author__ = "Komarov Alexander"
__version__ = "1.1.2"
__license__ = "GPL"
__email__ = "ignusius@gmail.com"


"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from sys import argv
joinnum=3
join=""
chars=""
def convert(file,out_file,before="",after=""):
    macs=""
    try:
        with open(file,'r') as f:
            for line in f:
                if chars=="lower":
                    macs+=before+join.join([line[i:i+joinnum] for i in range(0, len(line), joinnum)]).lower()[:-2]+after+'\n'
                if chars=="upper":
                    macs+=before+join.join([line[i:i+joinnum] for i in range(0, len(line), joinnum)]).upper()[:-2]+after+'\n'
    except(FileNotFoundError):
        print("No such file or directory")

    with open(out_file,'w') as f:
        for line in macs:
            f.write(line)
def help():
    print("TEXT2MAC HELP\n"
              "--------------------------------------\n"
              "example command: text2mac file1.txt\n"
              "--------------------------------------\n"
              "file1.txt:\n"
              "**********\n"
              "24A921418907\n"
              "24A92141891D\n"
              "24A9214189F4\n"
              "**********\n"
              "out_file1.txt:\n"
              "**********\n"
              "24:A9:21:41:89:07\n"
              "24:A9:21:41:89:1D\n"
              "24:A9:21:41:89:F4\n"
              "**********\n"
              "Options:\n"
              "text2mac f1.txt f2.txt [upper,lower] [2,3],[:,.] 'text ' ' text'\n"
              "example: text2mac f1.txt f2.txt  lower 3 . 'text1 ' ' text2'\n"
              "*********\n"
              "f2.txt\n"
              "text1 24a.921.418.907 text2\n"
              "text1 24a.921.418.91d text2\n"
              "text1 24a.921.418.9f4 text2\n")

if __name__ == '__main__':
    try:
        after=argv[6]
    except:
        after=""
    try:
        before=argv[7]
    except:
        before=""

    try:
        chars=argv[3]
    except:
        chars="lower"

    try:
        joinnum=int(argv[4])
    except:
        joinnum=2
    try:
        join=argv[5]
    except:
        join=":"

    if len(argv)>2:
        convert(argv[1],argv[2],after,before)
    else:
        help()




