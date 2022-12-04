#!/usr/bin/env python3

import os 
import sys 
from rich.tree import Tree 
import rich 
import argparse

class Default:
    Level: int = 0

class DirectoryTree:
    def __init__(self, dir: str = None, level: int = 0) -> None:
        assert dir is not None
        self.__dir = dir 
        self.__abspath = os.path.abspath(self.__dir)
        self.PrintTree(self.__abspath, level)


    def CreateTree(self, file: str =None, level: int = 0):

        assert file is not None 
        __current = file.split("/")[-1]
        Top = Tree(__current, highlight=True)
        for f in os.listdir(file):
            __full_path_name =  self.__new_path(file, f)
            

            if self.__TypeDir(__full_path_name): 
                if level == 0:
                    Top.add(self.__last_name(__full_path_name))
                else:    
                    sub = self.CreateTree(__full_path_name,  level=level-1)
                    Top.add(sub)
            elif self.__TypeFile(self.__last_name(__full_path_name)): 
                Top.add(f)
            else: 
                Top.add(f)
        return Top

    def __last_name(self, fullpath: str = None):
        assert fullpath is not None 
        return fullpath.split("/")[-1]
    
    def __new_path(self, path: str = None, dir: str = None ):
        assert path is not None
        assert dir is not None
        return os.path.join(path, dir)


    def __TypeFile(self, file: str = None):
        assert file is not None 
        if os.path.isfile(file):
            return True 
        return False 

    def __TypeDir(self, file: str = None):
        assert file is not None 
        if os.path.isdir(file):
            return True
        return False 

    def PrintTree(self, file: str = None, level: int = 0):
        assert file is not None 
        Top = self.CreateTree(file, level=level)
        
        rich.print(Top)

def main():
    args = argparse.ArgumentParser()
    args.add_argument('-d', default=".", help="")
    args.add_argument('--level', type=int, default=Default.Level, help="")
    params = args.parse_args()
    print(params.d)
    DirectoryTree(params.d, params.level)


if __name__ == "__main__":
    main()