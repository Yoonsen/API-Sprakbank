# Concordance

@application.route('/konk')

```
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
````

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
