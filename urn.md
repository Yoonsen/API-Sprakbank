# URN API

@application.route('/urn', methods=['GET'])

````
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
```

**Title**
----
  <_Additional information about your API call. Try to use verbs that match both request type (fetching vs modifying) and plurality (one vs multiple)._>

* **URL**

  <_The URL Structure (path only, no root url)_>

* **Method:**
  
  <_The request type_>

  `GET` | `POST` | `DELETE` | `PUT`
  
*  **URL Params**

   <_If URL params exist, specify them in accordance with name mentioned in URL section. Separate into optional and required. Document data constraints._> 

   **Required:**
 
   `id=[integer]`

   **Optional:**
 
   `photo_id=[alphanumeric]`

* **Data Params**

  <_If making a post request, what should the body payload look like? URL Params rules apply here too._>

* **Success Response:**
  
  <_What should the status code be on success and is there any returned data? This is useful when people need to to know what their callbacks should expect!_>

  * **Code:** 200 <br />
    **Content:** `{ id : 12 }`
 
* **Error Response:**

  <_Most endpoints will have many ways they can fail. From unauthorized access, to wrongful parameters etc. All of those should be liste d here. It might seem repetitive, but it helps prevent assumptions from being made where they should be._>

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "Log in" }`

  OR

  * **Code:** 422 UNPROCESSABLE ENTRY <br />
    **Content:** `{ error : "Email Invalid" }`

* **Sample Call:**

  <_Just a sample call to your endpoint in a runnable format ($.ajax call or a curl request) - this makes life easier and more predictable._> 

* **Notes:**

  <_This is where all uncertainties, commentary, discussion etc. can go. I recommend timestamping and identifying oneself when leaving comments here._> 
