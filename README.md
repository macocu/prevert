# prevert

Iterator for the prevert format

To use the `prevert` format iterator, install it via pypi with the following command line instruction:

`
$ pip install prevert
`

## Use

```
# import libraries
from prevert import dataset
# Open the dataset with the prevert parser 
dset=dataset("/data/monolingual/mk.xml")
```

The dataset can be iterated for documents where you can access the metadata by `doc.meta['attribute_name']`. Documents consist of paragraphs where you can access the metadata by `par.meta['attribute_name']`.

Basic use:

```
for doc in dset: # iterating through documents of a dataset
    print(doc.meta) # all attributes
    print(eval(doc.meta['lang_distr'])[0][0]) # most prominent language in the document
    print(str(doc)) # whole document text
    for par in doc: # iterating through paragraphs of a document
        print(par.meta['id']) # specific attribute
        print(str(par)) # whole paragraph text
    print(doc.to_prevert()) # obtaining the original format
```
