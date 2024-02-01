#!/usr/bin/python3
import pyperclip
import argparse


HELP = """
#----------------------------------------------------------------------------------------------------#
#                                                                                                    #
#                                            HELLO WORLD                                             #
#                                                                                                    #
#----------------------------------------------------------------------------------------------------#

 |<-------------------------------------------length----------------------------------------------->|

- comment_block    上記のサンプルの"全体"を指す
- comment          上記のサンプルにおける"HELLO WOLD"の部分を指す
- fill_char        上記のサンプルにおける"-"の部分をさす
- comment_out_char 上記のサンプルにおける"#"の部分をさす
- length           lengthはcomment_out_charを含まない長さ
"""

def gen_comment_block(comment):
    comment_block_lines = [
        args.fill_char * args.length,
        " " * args.length * len(args.fill_char),
        comment.center(args.length * len(args.fill_char)),
        " " * args.length * len(args.fill_char),
        args.fill_char * args.length,
    ]

    comment_block_lines = map(lambda x: args.comment_out_char + x + args.comment_out_char,comment_block_lines)
    comment_block = "\n".join(comment_block_lines)
    return comment_block

def main():
    if args.comment == None:
        comment = input("comment > ")
    else:
        comment = args.comment
    

    if args.go_upper:
        comment = comment.upper()

    separator = gen_comment_block(comment)

    print(separator)

    if args.copy_to_clipboard:
        pyperclip.copy(separator)


# TODO: スペースや改行が崩れてしまう
# parser = argparse.ArgumentParser(description=HELP)
parser = argparse.ArgumentParser()
parser.add_argument("--comment")
parser.add_argument("-co","--comment-out-char",default="#")
parser.add_argument("-f","--fill-char",default="-")
parser.add_argument("-u","--go-upper",action="store_true")
parser.add_argument("-c","--copy-to-clipboard",action="store_true")
parser.add_argument("-l","--length",type=int,default=100)
args = parser.parse_args()
main()
