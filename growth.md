# Growth Chart API

@application.route('/vekstdiagram', methods=['POST'])

```
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
