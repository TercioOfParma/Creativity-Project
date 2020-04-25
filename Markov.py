import random
import re

from collections import defaultdict
from sys import argv

class Mdict:
    def __init__(self):
        self.d = {}
    def __getitem__(self, key):
        if key in self.d:
            return self.d[key]
        else:
            raise KeyError(key)
    def add_key(self, prefix, suffix):
        if prefix in self.d:
            self.d[prefix].append(suffix)
        else:
            self.d[prefix] = [suffix]
    def get_suffix(self,prefix):
        l = self[prefix]
        return random.choice(l)

class Markov:
    def __init__(self, filename):
        """
        Building the dictionary
        """
        fp = open(filename)
        text = fp.read()
        #print(text)
        textList = text.split('\n')
        self.mcd = Mdict()
        oldnames = []
        self.chainlen = 1

        for l in textList:
            l = l.strip()
            oldnames.append(l)
            s = " " * self.chainlen + l
            for n in range(0, len(l)):
                self.mcd.add_key(s[n:n + self.chainlen], s[n + self.chainlen])
            self.mcd.add_key(s[len(l):len(l) + self.chainlen], "\n")

    def New(self):
        prefix = " " * self.chainlen
        name = ""
        suffix = ""
        while True:
            suffix = self.mcd.get_suffix(prefix)
            if suffix == "\n" or len(name) > 15:
                break
            else:
                name = name + suffix
                prefix = prefix[1:] + suffix
        name = re.sub(r'[^a-zA-Z]', '',name)
        return name.capitalize()