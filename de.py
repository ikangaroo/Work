#!/usr/bin/env python
# -*- coding:utf-8 -*-

import argparse,glob

def defineArguments():
    parse = argparse.ArgumentParser(description="Use this tool to generate obfuscation program")
    parse.add_argument("-m","--mode",required=True,choices=["generate"],default="generate",help="The mode of operation")
    parse.add_argument("-s","--sourcedir",required=False,default=".",help="The path to the directory contaning the unobfuscated source code files")
    parse.add_argument("-t","--tigressdir",default=".",help="The path to the directory of tigress")
    parse.add_argument("-f","--obfuscationfunction",default="main",help="The name of the function to obfuscate")
    return parse

def main():
    try:
        argumentparser = defineArguments()
        arguments = argumentparser.parse_args()
        print("#################\nLet's do it\n#################")

        if argumentparser.mode == "generate":
            sourcesFiles = sorted(glob.glob("%s/*.c" % arguments.sourcedir))
        if len(sourcesFiles) < 1:
            print("There is no files in \"%s\" " % arguments.sourcedir)
            return

        #生成混淆程序



if __name__ == "__main__":
    main()
