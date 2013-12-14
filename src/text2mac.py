#!/usr/bin/python3

__author__ = "Komarov Alexander"
__version__ = "1.0"
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


def convert(file,out_file,before="",after=""):
    macs=""
    try:
        with open(file,'r') as f:
            for line in f:
                macs+=before+':'.join([line[i:i+2] for i in range(0, len(line), 2)])[:-2]+after+'\n'
    except(FileNotFoundError):
        print("No such file or directory")

    with open(out_file,'w') as f:
        for line in macs:
            f.write(line)

if __name__ == '__main__':
    try:
        after=argv[3]
    except:
        after=""
    try:
        before=argv[4]
    except:
        before=""
    if len(argv)>2:
        convert(argv[1],argv[2],after,before)
    else:
        print("TEXT2MAC HELP\n"
              "-------------------------------------------------------------------------------------\n"
              "example command: text2mac file1.txt out_file.txt 'text_before_mac ' ' text_after_mac'\n"
              "-------------------------------------------------------------------------------------\n"
              "file1.txt:\n"
              "**********\n"
              "24A921418907\n"
              "24A92141891D\n"
              "24A9214189F4\n"
              "**********\n"
              "out_file1.txt:\n"
              "**********\n"
              "text_before_mac 24A921418907 text_after_mac\n"
              "text_before_mac 24A92141891D text_after_mac\n"
              "text_before_mac 24A9214189F4 text_after_mac\n"
              "**********\n")




