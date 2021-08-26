#!/usr/bin/python3
import os
import re

class CSSParser():
    
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        if self.file_path is None:
            return False
        
        file_content = None
        with open(self.file_path, "r") as file:
            file_content = file.read()
        if file_content is None:
            return False

        # cleanup
        file_content = self.__remove_comments(file_content)
        file_content = self.__remove_newline(file_content)
        
        # parsing
        self.__parse(file_content)
        return self.selectors

    def __remove_comments(self, s):
        s = re.sub(re.compile("/\*.*?\*/", re.DOTALL), "" , s) 
        s = re.sub(re.compile("//.*?\n"), "" , s)
        return s
    
    def __remove_newline(self, s):
        s = re.sub(re.compile("\n"), "" , s)
        return s

    def __remove_spaces(self, s):
        s = re.sub(re.compile(" "), "" , s)
        return s

    def __clean_key(self, s):
        return s.lstrip().rstrip()

    def __parse(self, s):
        self.selectors = {}
        split_medias_query = s.split("@media")
        if len(split_medias_query) == 1:
            self.__parse_in_media_query(split_medias_query[0])
        else:
            for medias_query in split_medias_query:
                in_media_query = None
                if "screen and" in medias_query:
                    in_media_query = medias_query.split("{")[0].split("max-width: ")[1].split(")")[0]
                    medias_query = "}".join("{".join(medias_query.split("{")[1:]).split("}")[:-1])
                self.__parse_in_media_query(medias_query, in_media_query)

    def __parse_in_media_query(self, s, media_query=None):
        split_lefts = s.split("}")

        for split_left in split_lefts:
            split_rights = split_left.split("{")
            if len(split_rights) != 2:
                continue
            keys_selector = self.__clean_key(split_rights[0]).split(",")
            
            split_commas = split_rights[1].split(";")
            for split_comma in split_commas:
                split_styles = split_comma.split(":")
                if len(split_styles) != 2:
                    continue
                for key_selector in keys_selector:
                    key_selector = self.__clean_key(key_selector)
                    if media_query is not None:
                        key_selector = "{}__{}".format(key_selector, media_query)
                    if self.selectors.get(key_selector) is None:
                        self.selectors[key_selector] = {}
                    self.selectors[key_selector][self.__clean_key(split_styles[0])] = self.__remove_spaces(split_styles[1])