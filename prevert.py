import re
import warnings
from collections import OrderedDict
re_attr_val=re.compile(r' (.+?)="(.*?)"')

class dataset:
    
    def __init__(self,path,xml=True):
        self.path=path
        self.file=open(path)
        if xml:
            line=self.file.readline()
            if not line.startswith('<corpus'):
                warnings.warn("Warning: your prevert might not have a XML header. Define the xml second parameter as False in the constructor if this is the case.")
    
    def __iter__(self):
        return self
    
    def __next__(self):
        doc_text=[]
        for line in self.file:
            doc_text.append(line)
            if line=='</doc>\n':
                return document(doc_text)
        raise StopIteration
    
class document:
    
    def __init__(self,lines):
        self.lines=lines
        self.idx=1
        self.meta=OrderedDict(re_attr_val.findall(self.lines[0]))
        self.metastr = self.lines[0]

    def __iter__(self):
        return self
    
    def __next__(self):
        p_text=[]
        for line in self.lines[self.idx:]:
            p_text.append(line)
            self.idx+=1
            if line=='</p>\n':
                    return paragraph(p_text)
        raise StopIteration

    def __str__(self):
        return ''.join([e for e in self.lines if e[0]!="<"])

    def to_prevert(self):
        lines = self.lines
        firstline = "<doc"
        for key, value in self.meta.items():
            firstline += f' {key}="{str(value)}"'
        firstline += ">\n"
        lines[0] = firstline
        return ''.join([e for e in lines])

class paragraph:

    def __init__(self,lines):
        self.lines=lines
        self.meta=OrderedDict(re_attr_val.findall(self.lines[0]))

    def __str__(self):
        return ''.join(self.lines[1:-1])
