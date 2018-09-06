# Newspaper Frequence API

@application.route('/avisfreq', methods=['GET'])

```
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
