from prevert import dataset

def opening_works() -> bool:
    try:
        dataset("tests/example.prevert")
        return True
    except Exception as e:
        return e
    
    
def test_opening():
    assert opening_works() == True, "The example dataset cannot be opened"
    
def test_reading():
    dset = dataset("tests/example.prevert")
    dset_list = list(dset)
    assert (l := len(dset_list)) == 2, f"Dataset has unusual length: {l}"
    assert str(dset_list[0]).startswith('Pijača\nDostava\nNovo v Ponudbi\n€6,0\nBombeta,'), "The content of the first document is suspicious."
    