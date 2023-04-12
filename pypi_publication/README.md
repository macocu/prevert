# Prevert iterator

To use the prevert parser, copy the file `prevert.py` in your directory.

## Use

```python
# import libraries
from prevert import dataset
import pandas as pd
```

If you are using the MaCoCu corpora in the XML format, the method dataset() needs only the path of the file as the argument:

```python
# Open the dataset with the prevert parser 
dset = dataset("/data/monolingual/mk.xml")
```


`dset` consists of docs where you can access the metadata by `doc.meta['attribute_name']`. Docs consist of paragraphs where you can access the metadata by `par.meta['attribute_name']`.

Basic use:
```python
for doc in dset: # iterating through documents of a dataset
    print(doc.meta) # all attributes
    print(eval(doc.meta['lang_distr'])[0][0]) # most prominent language in the document
    print(str(doc)) # whole document text
    for par in doc: # iterating through paragraphs of a document
        print(par.meta['id']) # specific attribute
        print(str(par)) # whole paragraph text
    print(doc.to_prevert()) # obtaining the original format
```
