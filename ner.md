#Named Entity Recognition API

@application.route('/ner', methods=['POST'])

```
def named_entity():
    parameters = request.json
    text = parameters['text']
    dist = False
    if 'dist' in parameters:
        dist = parameters['dist']
    result =  ner(text, dist)
    return jsonify(result)
```
