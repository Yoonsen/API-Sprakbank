def get_freq(urn, top=50, cutoff=3):
    r = requests.get("https://api.nb.no/ngram/urnfreq", json={'urn':urn, 'top':top, 'cutoff':cutoff})
    return Counter(dict(r.json()))

def get_papers(top=5, cutoff=5, navn='%', yearfrom=1800, yearto=2020, samplesize=10):
    r = requests.get("https://api.nb.no/ngram/avisfreq", json={'navn':navn, 'top':top, 'cutoff':cutoff,
                                                              'yearfrom':yearfrom, 'yearto':yearto,'samplesize':samplesize})
    return r.json()

def collocation(word, yearfrom=2010, yearto=2018, corpus='avis'):
    data =  requests.get("https://api.nb.no/ngram/collocation", params={'word':word,'corpus':corpus, 'yearfrom':yearfrom, 'yearto':yearto}).json()
    return pd.DataFrame.from_dict(data['freq'], orient='index')

def get_urn(urns):
    r = requests.get('https://api.nb.no/ngram/urn', json=urns)
    return r.json()

def vekstdiagram(urn, params=dict()):
    import requests
    import pandas as pd
    
    # if urn is the value of get_urn() it is a list 
    # otherwise it just passes
    if type(urn) is list:
        urn = urn[0]
    
    para = params
    para['urn']= urn
    r = requests.post('https://api.nb.no/ngram/vekstdiagram', json = para)
    return pd.DataFrame(r.json())


