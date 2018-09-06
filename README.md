# API-Sprakbank

API-fulltekst NB

# coding: utf-8

# ## Fulltekstapiet - lager løsning med Flask rundt den her koden
# 
# Merk at det er problemer av en eller annen grunn med å eksekvere query(ft,...) i skopet til apply(...). Så det gjøres i selve skriptet.

# In[132]:
from flask import Flask, request, jsonify,Response
import ngram_api
from ngram_single_process import ngram_bok, ngram_avis, ngram_bok_tot, ngram_avis_tot, avisnavn
from wildcards import wildcard_hub
#import pandas as pd
import konk_api
from konk_api import query
from collections import Counter
import ipyparallel as ipp
import json
import sys
from navnegjenkjenning_production import ner
from random import shuffle
#from IPython.display import HTML


application = Flask(__name__)
print('initialisert')
#print('test: ngram_api.clients[22]["ft"]', ngram_api.clients[22]['ft'])





@application.route('/')
def hello_world():
    return 'Trendlinjer og konkordanser: /ngram?word=...., eller /konk?word=...&corpus=...&offset='



@application.route('/ner', methods=['POST'])
def named_entity():
    parameters = request.json
    text = parameters['text']
    dist = False
    if 'dist' in parameters:
        dist = parameters['dist']
    result =  ner(text, dist)
    return jsonify(result)


@application.route('/ngram')
def ngram_request():
    word = request.args.get('word')
    corpus = request.args.get('corpus')
    cond_word = request.args.get('cond')
    topic = request.args.get('topic')
    ddk = request.args.get('ddk')
    name = request.args.get('paper_name')
    month = request.args.get('month')
    yearfrom = request.args.get('yearfrom')
    yearto = request.args.get('yearto')
    total = request.args.get('total')
    # set defaults
    if total == None:
        total = False
    elif total == 'yes' or total == True:
        total = True
    else:
        total = False
        
    if name == None:
        name = '#'
    if yearto == None and yearfrom == None:
        period = '#'
    else:
        if yearto == None:
            period = yearfrom
        elif yearfrom == None:
            period == yearto
        else:
            period = (yearfrom, yearto)
    if month == None:
        month == '#'
    if ddk == None:
        ddk = "#"
    if cond_word == None:
        cond_word = "#"
    if topic == None:
        topic = "#"
    if corpus == None:
        corpus='bok'
    if total == False:
        if corpus == 'avis':
            result = ngram_avis(word, avisnavn=name, cond_word=cond_word, period=period, month=month)
        elif corpus == 'avisnavn':
            result = avisnavn(word)
        else:
            result = ngram_bok(word, cond_word=cond_word, period=period, topic=topic, ddk=ddk)
    else:
        if corpus == 'avis':
            result = ngram_avis_tot(avisnavn=name, cond_word=cond_word, period=period, month=month)
        else:
            result = ngram_bok_tot( cond_word=cond_word, period=period, topic=topic, ddk=ddk)
    
    return jsonify(result)


@application.route('/konk')
def konk_request():
    word = request.args.get('word')
    corpus = xstr(request.args.get('corpus'),'bok')
    author=xstr(request.args.get('author'))
    title=xstr(request.args.get('title'))
    subtitle=xstr(request.args.get('subtitle'))
    lang=xstr(request.args.get('lang'))
    ddk = xstr(request.args.get('ddk'))
    yearfrom = xstr(request.args.get('yearfrom'), 1820)
    yearto=xstr(request.args.get('yearto'), 2020)
    before = xstr(request.args.get('before'), 5)
    after = xstr(request.args.get('after'), 5)
    size = xstr(request.args.get('size'), 3)
    offset = xstr(request.args.get('offset'),0)
    result = konk(word, 
                corpus=corpus, 
                offset=int(offset)*int(size), 
                size=str(max(int(size), 4)), 
                before=str(min(int(before),12)),
                after=str(min(int(after),12)), 
                author=author,
                lang=lang, 
                title=title, 
                ddk=ddk,
                subtitle=subtitle,
                yearfrom=yearfrom, 
                yearto=yearto)
    return result


@application.route('/collocation')
def collocation_request():
    word = request.args.get('word')
    corpus = xstr(request.args.get('corpus'),'bok')
    author=xstr(request.args.get('author'))
    title=xstr(request.args.get('title'),'%')
    subtitle=xstr(request.args.get('subtitle'))
    lang=xstr(request.args.get('lang'))
    ddk = xstr(request.args.get('ddk'))
    yearfrom = xstr(request.args.get('yearfrom'), 1820)
    yearto=xstr(request.args.get('yearto'), 2020)
    limit = xstr(request.args.get('limit'), 100)
    before = xstr(request.args.get('before'), 5)
    after = xstr(request.args.get('after'), 5)
    result = collocation(word, 
                corpus=corpus, 
                before=str(min(int(before),52)),
                after=str(min(int(after),52)), 
                author=author,
                lang=lang, 
                title=title, 
                ddk=ddk,
                subtitle=subtitle,
                yearfrom=yearfrom, 
                yearto=yearto,
                limit=limit)
    return result


@application.route('/wildcards')
def wildcard_search():
    books = "/disk1/bokhylla/digibok/book_words.db"
    wildword = request.args.get('word')
    factor= int(xstr(request.args.get('factor'), 2))
    freq_lim = int(xstr(request.args.get('freq_lim'), 50))
    limit= int(xstr(request.args.get('limit'),50))
    res = wildcard_hub(wildword, factor=factor, freq_lim=freq_lim, limit=limit)
    return jsonify(dict(res))



@application.route('/count', methods=['GET'])
def count_request():
    #word = request.args.get('word')
    
    corpus = xstr(request.args.get('corpus'),'bok')
    author=xstr(request.args.get('author'))
    title=xstr(request.args.get('title'))
    subtitle=xstr(request.args.get('subtitle'))
    lang=xstr(request.args.get('lang'),'nob')
    yearfrom = xstr(request.args.get('yearfrom'), 1820)
    yearto=xstr(request.args.get('yearto'), 2020)
    ddk = xstr(request.args.get('ddk'))
    result = count(
                corpus=corpus, 
                author=author,
                lang=lang, 
                title=title, 
                subtitle=subtitle,
                ddk=ddk,
                yearfrom=yearfrom, 
                yearto=yearto)
    #print(corpus, yearfrom)
    return jsonify(result)




@application.route('/freq', methods=['POST'])
def freq():
    parameters = request.json
    words = parameters['words']
    urn = parameters['urn']
    urndb = "/disk1/bokhylla/urn2db.db"
    #Take a list of words and return the frequencies
    
    db = konk_api.query(urndb, "select dbfile from urn_db where urn =? ",(urn,))
    res = []
    q = ','.join(['?']*len(words))
    #print(q)
    sql = "select word, freq from unigram where urn = ? and word in ({q}) ".format(q=q)
    #print(sql)
    if db != []:
        res = konk_api.query(db[0][0], sql, (urn,) + tuple(words), size=0)
    return jsonify(res)


@application.route('/meta', methods=['GET'])
def meta():
    import re
    mods = "/disk1/bokhylla/digibok/urn-biblio-mods.db"
    urns = xstr(request.args.get('urn'),'')
    res = []
    for urn in re.findall("[0-9]+", urns):
        res += konk_api.query(mods, "select urn, author, year, title, publisher from biblio where urn = ?",(urn,), size=0)
    return jsonify(res)


@application.route('/graph', methods=['POST'])
def make_graph():
    import sqlite3
    import pandas as pd
    import json
    
    
    urn_db = '/disk1/bokhylla/urn2db.db'
    
    parameters = request.json
    urn = parameters['urn']
    wordbag = parameters['words']
    db = query(urn_db, "select dbfile from urn_db where urn = ? ",(urn,))[0][0]
    print(db)
    with sqlite3.connect(db) as con:
        cur = con.cursor()
        cur.execute("attach '' as wordbag")
        cur.execute('create table wordbag.words (word varchar)')
        for word in wordbag:
            cur.execute("insert into wordbag.words values ('{u}')".format(u=word))
        cur.execute("""
        select  c.para, c.word, count(*) 
        from ft as c 
            inner join wordbag.words as b on b.word = c.word 
        where c.urn = ?
        group by c.para, c.word
        """, (urn,))
        G = cur.fetchall()
        D = dict()
        for t in G:
            S = dict()
            for v in G:
                if t[0] == v[0]:
                    S[v[1]] = v[2]
            D[t[0]] = S
        G = pd.DataFrame(D).fillna(0)
        Gd = G.dot(G.transpose())
        J = json.loads(Gd.to_json())
        res = []
        for x in J:
            for y in J[x]:
                res.append((x,y,J[x][y]))
    return jsonify(res)


@application.route('/vekstdiagram', methods=['POST'])
def vekst_diagram():
    import sqlite3
    parameters = request.json
    urn = parameters['urn']
    window = 100
    if 'window' in parameters:
        window= parameters['window']
    pr = 100
    if 'pr' in parameters:
        pr = parameters['pr']
    if 'words' in parameters:
        words = parameters['words']
    else:
        words = ". , ! ? ; -".split()
        
    urndb = "/disk1/bokhylla/urn2db.db"
    #print(words)
    #parameters = request.json
    window = max(100, window)
    pr = max(pr, 100)
    db = konk_api.query(urndb, "select dbfile from urn_db where urn =? ",(urn,))
    if db != []:
        database = db[0][0]
        print(database)
        rowstart = konk_api.query(database, "select rowid from ft where urn = ? order by rowid limit 1",(urn,))
        rowend = konk_api.query(database, "select rowid from ft where urn = ? order by rowid desc limit 1",(urn,))
        if rowstart != [] and rowend !=[]:
            rowstart = rowstart[0][0]
            rowend = rowend[0][0]
            with sqlite3.connect(database) as con:
                cur = con.cursor()
                cur.execute("attach database '' as wordset")
                cur.execute("create table wordset.words (word varchar)")
                for w in words:
                    cur.execute("insert into wordset.words values (?)",(w,))
                count = []
                for row in range(rowstart, rowend, pr):
            
                    sql = """select count(b.word) from ft as a inner join wordset.words as b on b.word = a.word
                where a.urn = ? and a.rowid > ? and a.rowid <= ?"""
        #print(sql)
                    res = cur.execute(sql, (urn, row, row + window )).fetchall()
                    if res != []:
                        count.append(res[0][0])
    return jsonify(count)



@application.route('/urnfreq', methods=['GET'])
def urn():
    urndb = "/disk1/bokhylla/urn2db.db"
    parameters = request.json
    urn = parameters['urn']
    keys = parameters.keys()
    top = 20
    if 'top' in keys:
        top = parameters['top']
    cutoff=5
    if 'cutoff' in keys:
        cutoff = parameters['cutoff']
    res = []
    db = konk_api.query(urndb, "select dbfile from urn_db where urn =? ",(urn,))
    sql = """select word, freq from unigram 
    where urn = ? and freq > ? order by freq desc limit ?"""
    #print(sql)
    if db != []:
        res = konk_api.query(db[0][0], sql, (urn, cutoff, top), size=0)
    return jsonify(res)






@application.route('/avisfreq', methods=['GET'])
def fetchavis():
    urndb = "/disk1/bokhylla/alto_avis/urn_mods_avis.db"
    parameters = request.json
    keys = parameters.keys()
    navn = '%'
    if 'navn' in keys:
        navn = parameters['navn']
    yearfrom = 1800
    if 'yearfrom' in keys:
        yearfrom = parameters['yearfrom']
    yearto = '2018'
    if 'yearto' in keys:
        yearto = parameters['yearto']
    samplesize = 20
    if 'samplesize' in keys:
        samplesize= parameters['samplesize']
    top = 20
    if 'top' in keys:
        top = parameters['top']
    cutoff=5
    if 'cutoff' in keys:
        cutoff = parameters['cutoff']
    res = []
    db = konk_api.query(urndb, "select urn from avisdata where avisnavn like ? and year <= ? and year >= ? order by random() limit ?",(navn, yearto, yearfrom, samplesize), size=0)
    sql = """select word, freq from unigram where urn = ? and freq > ? order by freq desc"""
    #print(sql)
    aviser = []
    for x in db:
        avisfil = findavis(x[0])
        print(x[0], avisfil)
        aviser.append(konk_api.query(avisfil, sql, (x[0], cutoff), size=0))
    return jsonify(aviser)    




@application.route('/urn', methods=['GET'])
def urns():
    
    mods = "/disk1/bokhylla/digibok/urn-biblio-mods.db"
    
    params = request.json
    keys = params.keys()
    sql_condition = ""
    tuples = []
    if 'author' in keys:
        auth = params['author']
    else:
        auth = '%'
    select_statement = " distinct a.urn, a.author, a.title, a.year from biblio as a "
    sql_condition += " a.author like ? "
    tuples.append(auth)
    if 'gender' in keys:
        gender = params['gender']
        sql_condition += " a.gender like ? "
        tuples.append(gender)
    if 'year' in keys:
        year = params['year']
    else:
        year = 1800
    sql_condition += " and a.year >= ?"
    tuples.append(year)
    neste = 10
    if 'neste' in keys:
        neste = params['neste']
    if 'next' in keys:
        neste = params['next']
    sql_condition += " and a.year <= ?"
    tuples.append(int(year) + int(neste))
    if 'title' in keys:
        title = params['title']
        sql_condition += " and a.title like ? "
        tuples.append(title)
    if 'ddk' in keys:
        ddk = params['ddk']
        sql_condition += " and c.class like ? and c.authority = 'ddc' and a.urn = c.urn "
        select_statement += ", classifications as c"
        tuples.append(ddk)
    if 'subject' in keys:
        subject = params['subject']
        sql_condition += " and s.topic like ? and s.urn = a.urn "
        select_statement += ", subjects as s"
        tuples.append(subject)
    if 'lang' in keys:
        lang=params['lang']
        sql_condition += " and a.lang = ? "
        tuples.append(lang)
    if 'limit' in keys:
        try:
            limit = int(params['limit'])
            sql_condition += " order by random()  limit ?"
            tuples.append(limit)
        except:
            True
    else:
        sql_condition += "order by random() limit 10"
    sql =  "select {select} where {condition}".format(select=select_statement, condition = sql_condition)
    res = konk_api.query(mods, sql, tuple(tuples), size=0)
    return jsonify(res)
        
def findavis(num):
    x = int(num / 20000) 

    return "/disk1/bokhylla/alto_avis/alto_avis_{s}_{e}.db".format(s = x * 20000 + 1, e = (x + 1)*20000 )




@application.route('/urnkonk', methods=[ 'POST'])
def urn_konk_request():
    parameters = request.json
    word = parameters['word']
    corpus = parameters['corpus']
    before = parameters['before']
    after = parameters['after']
    size =parameters['size']
    offset = parameters['offset']
    urns = parameters['urns']
    result = konk_urn(word, 
                corpus=corpus, 
                offset=int(offset)*int(size), 
                size=str(max(int(size), 4)), 
                before=str(min(int(before),12)),
                after=str(min(int(after),12)),
                urns=urns)
    return result
    

