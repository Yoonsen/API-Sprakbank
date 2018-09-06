
# Wildcard API

```
def wildcard_search():
    books = "/disk1/bokhylla/digibok/book_words.db"
    wildword = request.args.get('word')
    factor= int(xstr(request.args.get('factor'), 2))
    freq_lim = int(xstr(request.args.get('freq_lim'), 50))
    limit= int(xstr(request.args.get('limit'),50))
    res = wildcard_hub(wildword, factor=factor, freq_lim=freq_lim, limit=limit)
    return jsonify(dict(res))
```
