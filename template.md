---


---

<h1 id="norkorr-–-norwegian-correspondences-and-linked-open-data">NorKorr – Norwegian Correspondences and Linked Open Data</h1>
<h2 id="about-the-project">About the Project</h2>
<p>The National Library of Norway has a substantial amount of private historical correspondences in its holdings, many of which are edited and published, either in printed editions or digitally. In addition, institutions of cultural heritage, like the Munch Museum, as well as Norwegian universities, like the University of Oslo and the Arctic University of Tromsø prepare digital editions of letters and correspondences of key figures of Norwegian public and academic life. Yet, these correspondences lead a solitary existence – hidden in editions of single authors. As a dialogical genre, their full potential lies in the connection of those sending and receiving letters, postcards, and telegrams – at a specific time and from and to a specific place. Because the collections of correspondences are distributed geographically and institutionally, there rarely exist links between them, thus making research on the correspondence networks that existed in Norway, the Nordic Countries - and beyond, to Europe and the rest of the world - impossible.</p>
<p>The project <strong>Norwegian Correspondences</strong> (NorKorr) aims to link these individual correspondences not only to each other but to historical correspondences in Europe and beyond by use of the <a href="https://correspsearch.net/index.xql">CorrespSearch web service</a>. CorrespSearch is a web service that aggregates specific metadata from editions of correspondences. These data can be searched via the CorrespSearch website or queried via an open API. Norwegian correspondences will thus become visible as part of the greater European network of letters and allow for a macroscopic view on the correspondence networks that existed throughout the centuries.</p>
<h2 id="aims">Aims</h2>
<p>The aim of the NorKorr project is to aggregate and provide correspondence metadata from Norwegian editions of correspondences from different projects, institutions and collections in a format that can be ingested by CorrespSearch. The final products are a large set of metadata for Norwegian correspondences under a Creative Commons licence in the CMIF (<a href="https://github.com/TEI-Correspondence-SIG/CMIF">Correspondence Metadata Interchange Format</a>) standard and an open workflow for (semi-)automatically creating and delivering CMIF-compliant correspondence metadata from future editions prepared by or hosted by the National Library of Norway (and other institutions) to the CorrespSearch web service.</p>
<h2 id="participants">Participants</h2>
<h3 id="national-library">National Library</h3>
<p>Ellen Wiger</p>
<p>Mette Witting</p>
<p>Annika Rockenberger</p>
<h3 id="other-norwegian-institutions">Other Norwegian Institutions</h3>
<p>Hilde Bøe (Munch Museum)</p>
<p>Philipp Conzett (Arctic University of Tromsø, University Library)</p>
<h2 id="implementation">Implementation</h2>
<h3 id="step-1-examination-of-materials">Step 1: Examination of Materials</h3>
<p>The project participants meet IRL at the National Library in Oslo for a one-day workshop (aka hackathon) in September 2018.</p>
<h4 id="schedule-for-the-kick-off-workshop">Schedule for the kick-off workshop</h4>

<table>
<thead>
<tr>
<th>Time</th>
<th>Topic</th>
</tr>
</thead>
<tbody>
<tr>
<td>10.00 – 10.45</td>
<td>Introduction to NorKorr</td>
</tr>
<tr>
<td>10.45 – 11.00</td>
<td>Break</td>
</tr>
<tr>
<td>11.30 – 13.00</td>
<td>Create an overview of correspondence editions in our collections</td>
</tr>
<tr>
<td>13.00 – 14.00</td>
<td>Lunch</td>
</tr>
<tr>
<td>14.30 – 15.45</td>
<td>Write a report on what we have collected, assign tasks for further work and decide on further steps</td>
</tr>
<tr>
<td>15.45 – 16.00</td>
<td>Wrapping up + coffee</td>
</tr>
</tbody>
</table><h3 id="examination-of-materials">Examination of Materials</h3>
<p>We will take a close look at our materials (digital editions of Norwegian correspondences), with regards to:</p>
<ul>
<li>Technical aspects
<ul>
<li>file format</li>
<li>TEI P5</li>
<li>TEI P4</li>
<li>Other XML</li>
<li>Non-XML</li>
<li>Plain text</li>
<li>Image (scan)</li>
</ul>
</li>
<li>metadata format and coverage
<ul>
<li>authority data for person &amp; place names, ISO standard for dates</li>
<li><a href="http://viaf.org/">http://viaf.org/</a> (NB is member</li>
<li><a href="https://en.wikipedia.org/wiki/Virtual_International_Authority_File">https://en.wikipedia.org/wiki/Virtual_International_Authority_File</a></li>
<li><a href="https://www.geonames.org/">https://www.geonames.org/</a></li>
<li><a href="https://www.iso.org/iso-8601-date-and-time-format.html">https://www.iso.org/iso-8601-date-and-time-format.html</a></li>
<li>licences (aka copyright, other limitations)</li>
<li>…</li>
</ul>
</li>
<li>Content
<ul>
<li>persons (who)</li>
<li>periods</li>
<li>scope (part, whole, selection etc.)</li>
</ul>
</li>
<li>Time and Budget</li>
</ul>
<h4 id="materials-to-depart-from">Materials to depart from</h4>
<ul>
<li><a href="https://www.nb.no/forskning/nb-kilder/">NB-kilder</a></li>
<li><a href="http://ibsen.uio.no/brev.xhtml">Ibsen skrifter</a></li>
<li><a href="https://www.emunch.no/english.xhtml">Munch tekster</a></li>
<li><a href="https://www.dokpro.uio.no/qvigstad/ombrev.html">Qvigstad brev</a> (started as a project of EDD/UiO <a href="http://www.dokpro.uio.no/qvigstad/">http://www.dokpro.uio.no/qvigstad/</a>, now at UiT/NB)</li>
<li><a href="http://www.bokselskap.no/">Bokselskap.no</a></li>
</ul>
<p>Goal of the workshop is to come up with (1) an overview of digital editions of correspondences that are good candidates for CorrespSearch and (2) identify the work tasks needed to transform (select, format) the metadata to conform to the CorrespSearch CMIF standard (3) assign tasks to the participants and (4) agree on delivery dates for the work packages.</p>
<p>A brief but precise description of (1) will be done, including a list of authors (see Appendix 1), time periods and content of the correspondences to show the potential for future research on this corpus.</p>
<h3 id="step-2-norkorr-to-correspsearch">Step 2: NorKorr to CorrespSearch</h3>
<p>The participants prepare a conference paper and a research article about the workflow (material, data formats, distributed hosting, transformations etc.) for NorKor as an example of preparing large distributed heterogeneous metadata sets for ingestion into CorrespSearch. They explore the potential of such an endeavour and discuss advantages (and challenges) of using decentralized infrastructure and third-party solutions with regards to Norwegian cultural heritage institution’s scrope and policies. The workflow is supposed to serve as a basis for further editions of Norwegian correspondences and should stand as an example of re-use of digital data (and especially metadata) provided by large institutions of cultural heritage and research, especially in the Nordic countries.</p>
<p>The paper could be presented at the TEI2019 International Conference in Graz/Austria in September 2019. Alternatively (or additionally), the paper could be given at one of the DH conferences (DHN2019 in early March, DHd2019 in late March, DH2019 in July) or at conferences for edition philology (NNE2019 in September or AG-Edition in February 2020) or Historical Network Research (HNR2019 tba).</p>
<p>The article should be an edited and polished version of the paper and published soon after delivering the paper (aim: 2020, open access journal, international).</p>
<h3 id="step-3-norkor-at-nb---the-catalogue-data-from-the-private-archives-and-automatic-correspondence-metadata-extraction-from-bokhylla.no">Step 3: NorKor at NB - The Catalogue Data from the Private Archives and Automatic Correspondence Metadata Extraction from <a href="http://Bokhylla.no">Bokhylla.no</a></h3>
<p>This part of the project is tentative. It shall show the potential of the physical and digital collections of the National Library of Norway, especially in regards to exploiting digital humanities methods in metadata and text mining.</p>
<h4 id="correspondence-material-in-the-private-archives">Correspondence Material in the Private Archives</h4>
<!-- Via nb.no/nbsok using the search phrase &#8220;brev -indulgens&#8221; yields 14.824 letters in the holdings of the Private Archives that have been digitized. These should be combed through to select all that are not correspondences or letters. Of the remaining, the letters have to be matched with DSEs in NB-kilder and Bokselskap.no as well as the digitized scholarly editions of letters in bokhylla.no. They can be used as facsimile or alternative presentations where copyright of scholarly editions prevents external access. The metadata of these letters could be extracted and matched with the CIMF standard. -->
<h4 id="hvem-til-hvem">Hvem-til-hvem</h4>
<!-- As of XXXX, metadata for correspondences in the holdings of the Private Archive are stored in HANSKE (Manuscript Catalogue, [https://www.nb.no/hanske/](https://www.nb.no/hanske/) ) which in the course of being phased out and replaced by ZZ.. Some of the correspondence metadata in the archive have previously been extracted for searching for correspondence partners and dates. There&#8217;s a website providing access to a tool (BETA version) where users can type in person names or years and get a list of results from which they can navigate onwards: [https://www.nb.no/hanske/brev/](https://www.nb.no/hanske/brev/) . The service has been developed by Torstein Tjelta (NB). -->
<p>Tasks:</p>
<ul>
<li>Take a look at the catalogue data and materials and sketch a workflow for making them compatible with the CMIF-Standard used by CorrespSearch</li>
<li>Take a look at database behind “Hvem skrev til hvem” and decide if and how to extract data and transform to CMIF-Standard</li>
<li>How is correspondence metadata stored today and in the future and how can it be easily fed into CorrespSearch, granted this is wanted by NB</li>
</ul>
<h4 id="bokhylla.no"><a href="http://Bokhylla.no">Bokhylla.no</a></h4>
<p>The digitisation efforts of the NB provide an enormous amount of textual data. Included in this are Norwegian scholarly editions of correspondences that formerly were printed and now have been digitized in full text (OCR). In order to complete the NorKorr metadata set, first a selection of scholarly editions of Norwegian correspondences has to be made. Then, from the text of the editions, correspondence metadata has to be (semi-)automatically extracted, stored, and transformed into a CMIF compliant format to be ingested into CorrespSearch.</p>
<p>This is an endeavour of considerable complexity and size and requires expert knowledge in information retrieval from plain text. At this stage, it should be seen as an experiment in retrieving specific textual data from a large collection of text without too much manual interference. The results of this experiment could be presented as a paper or article in the future and the workflow and code could be published for re-use on other full-text collections that contain flat encoded texts (aka plain text).</p>
<p>A list of URNs of digitized scholarly editions of correspondences and letters will be created (by AR) and the raw OCR files will be extracted from <a href="http://bokhylla.no">bokhylla.no</a> by LJ. The corpus will then be divided into materials that are in the public domain and such that are still under copyright protection. For the letters still under copyright protection, no full-text can be shown outside of the NB, however, amount of words, word lists and topic models can be extracted that should allow for ‘distant reading’ of these letters.</p>
<h4 id="aims-1">Aims</h4>
<p>The aims for the two subprojects in Step 3 are:</p>
<ul>
<li>meaningful re-use of a tool/service developed by NB (HANSKE / Hvem skrev til hvem)</li>
<li>accessibility of correspondence metadata that hasn’t been edited yet (or won’t ever be)</li>
<li>targeted retrieval of specific data (correspondence metadata from digitized scholarly editions) from <a href="http://bokhylla.no">bokhylla.no</a> showing the potential of the digital collection even though it is flat encoded</li>
<li>large scale show case for “distant reading the network of Norwegian correspondence”</li>
<li></li>
</ul>
<h2 id="bibliography">Bibliography</h2>
<h3 id="links">Links</h3>
<p><a href="https://www.nb.no/hanske/brev/">https://www.nb.no/hanske/brev/</a></p>
<p><a href="https://www.nb.no/hanske/">https://www.nb.no/hanske/</a></p>
<p><a href="http://historicalnetworkresearch.org/">http://historicalnetworkresearch.org/</a></p>
<p><a href="https://journal.tei-c.org/index.php/journal/index">https://journal.tei-c.org/index.php/journal/index</a></p>
<p><a href="https://correspsearch.net/index.xql?l=en">https://correspsearch.net/index.xql?l=en</a></p>
<p><a href="https://correspsearch.net/index.xql?id=participate">https://correspsearch.net/index.xql?id=participate</a></p>
<p><a href="http://dh2016.adho.org/abstracts/121">http://dh2016.adho.org/abstracts/121</a></p>
<p><a href="http://correspsearch-test.nodegoat.net/viewer.p/4/136/scenario/1/geo/fullscreen">http://correspsearch-test.nodegoat.net/viewer.p/4/136/scenario/1/geo/fullscreen</a></p>
<p><a href="http://www.tei-c.org/activities/sig/correspondence/">http://www.tei-c.org/activities/sig/correspondence/</a></p>
<p><a href="https://github.com/TEI-Correspondence-SIG">https://github.com/TEI-Correspondence-SIG</a></p>
<p><a href="http://www.dokpro.uio.no/">http://www.dokpro.uio.no/</a></p>
<p><a href="http://www.nnedit.org/index.html">http://www.nnedit.org/index.html</a></p>
<p><a href="http://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-correspDesc.html">http://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-correspDesc.html</a></p>
<p><a href="http://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD44CD">http://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html#HD44CD</a></p>
<h3 id="articles">Articles</h3>
<p>Dumont, Stefan. “CorrespSearch – Connecting Scholarly Editions of Letters.” Journal of the Text Encoding Initiative, no. 10 (December 7, 2016). <a href="https://doi.org/10.4000/jtei.1742">https://doi.org/10.4000/jtei.1742</a>.</p>
<p>Neuber, Frederike. “CorrespSearch.” Variants. The Journal of the European Society for Textual Scholarship, no. 12–13 (December 31, 2016): 284–85.</p>
<p>Dumont, S. (2016). correspSearch - A Web Service to Connect Diverse Scholarly Editions of Letters. In Digital Humanities 2016: Conference Abstracts. Jagiellonian University &amp; Pedagogical University, Kraków, pp. 175-178.</p>
<h2 id="appendix-1">Appendix 1</h2>
<h3 id="digital-editions-of-letters-in-nb-kilder">Digital Editions of Letters in NB-kilder</h3>
<p>Status: 1/8-2018</p>

<table>
<thead>
<tr>
<th>FRA</th>
<th>TIL</th>
<th>ÅR</th>
<th>PUBLISERT</th>
</tr>
</thead>
<tbody>
<tr>
<td>Collett, Camilla</td>
<td>Bjørnson, Bjørnstjerne</td>
<td>1867</td>
<td>NB kilder 2:2/2015</td>
</tr>
<tr>
<td>Collett, Camilla</td>
<td>Collett, Johan Christian</td>
<td>1849</td>
<td>NB kilder 2:4/2018</td>
</tr>
<tr>
<td>Collett, Camilla</td>
<td>Collett, Peter Jonas</td>
<td>1841-1851</td>
<td>NB kilder 2:4/2018</td>
</tr>
<tr>
<td>Collett, Camilla</td>
<td>Didriks, Emilie</td>
<td>1841-1842</td>
<td>NB kilder 2:4/2018</td>
</tr>
<tr>
<td>Collett, Camilla</td>
<td>Herre, Johanne Caroline</td>
<td>1830</td>
<td>NB kilder 2:4/2018</td>
</tr>
<tr>
<td>Collett, Camilla</td>
<td>Herre, Marie Emilie</td>
<td>1830</td>
<td>NB kilder 2:4/2018</td>
</tr>
<tr>
<td>Collett, Camilla</td>
<td>Ibsen, Henrik</td>
<td>1872-1889</td>
<td>NB kilder 2:1/2014</td>
</tr>
<tr>
<td>Collett, Camilla</td>
<td>Ibsen, Susanna</td>
<td>1872-1894</td>
<td>NB kilder 2:1/2014</td>
</tr>
<tr>
<td>Collett, Camilla</td>
<td>Lie, Jonas</td>
<td>1863-1884</td>
<td>NB kilder 2:3/2016</td>
</tr>
<tr>
<td>Collett, Camilla</td>
<td>Petersen, Emma</td>
<td>1839</td>
<td>NB kilder 2:4/2018</td>
</tr>
<tr>
<td>Collett, Camilla</td>
<td>Wergeland, Amalie Sofie</td>
<td>1839</td>
<td>NB kilder 2:4/2018</td>
</tr>
<tr>
<td>Collett, Camilla</td>
<td>Wergeland, Laura Augusta</td>
<td>1846</td>
<td>NB kilder 2:4/2018</td>
</tr>
<tr>
<td>Collett, Camilla</td>
<td>Wergeland, Nicolai</td>
<td>1841-1844</td>
<td>NB kilder 2:4/2018</td>
</tr>
<tr>
<td>Collett, Camilla</td>
<td>Wergeland, Oscar</td>
<td>1844</td>
<td>NB kilder 2:4/2018</td>
</tr>
</tbody>
</table><h3 id="planned-digital-editions-of-letters-in-nb-kilder">Planned Digital Editions of Letters in NB-kilder</h3>
<p>· Correspondence between Kitty Kielland and Arne Garborg, shall be published in 2018</p>
<p>· Letters from Sumatra (Jacob Iversen et al.), shall be published in 2018</p>
<p>· Letters by Just Qvigstad, shall be published in 2019</p>
<p>· Correspondence between Kitty Kielland and Eilif Peterssen, shall be published in 2019(?)</p>
<h3 id="digital-editions-of-letters-in-nslbokselskap.no">Digital Editions of Letters in NSL/bokselskap.no</h3>
<p>Status: 1/8-2018</p>

<table>
<thead>
<tr>
<th>FRA</th>
<th>TIL</th>
<th>ÅR</th>
<th>PUBLISERT</th>
</tr>
</thead>
<tbody>
<tr>
<td>Bjørnson, Bjørnstjerne</td>
<td>Div. danske mottakere (ca 400 brev)</td>
<td>1854-1874</td>
<td>NSL/bokselskap.no 2010</td>
</tr>
<tr>
<td>Brandes, Georg</td>
<td>Thoresen, Magdalene</td>
<td>1865-1899</td>
<td>NSL/bokselskap.no 2015</td>
</tr>
<tr>
<td>Ibsen, Henrik</td>
<td>Bjørnson, Bjørnstjerne</td>
<td>1864-1898</td>
<td>HIS/bokselskap.no 2014</td>
</tr>
<tr>
<td>Ibsen, Henrik</td>
<td>Collett, Camilla</td>
<td>1877-1893</td>
<td>HIS/bokselskap.no 2013</td>
</tr>
<tr>
<td>Ibsen, Henrik</td>
<td>Lie, Jonas</td>
<td>1879-1900</td>
<td>HIS/bokselskap.no 2012</td>
</tr>
<tr>
<td>Kielland, Alexander L.</td>
<td>Div. mottakere (ca 1800 brev)</td>
<td>1869-1906</td>
<td>NSL/bokselskap.no 2010</td>
</tr>
<tr>
<td>Obstfelder, Sigbjørn</td>
<td>Div. mottakere (ca 200 brev)</td>
<td>1884-1900</td>
<td>NSL/bokselskap.no 2016</td>
</tr>
<tr>
<td>Skram, Amalie</td>
<td>Skram, Erik</td>
<td>1882-1902</td>
<td>NSL/bokselskap.no 2016</td>
</tr>
<tr>
<td>Skram, Erik</td>
<td>Skram, Amalie</td>
<td>1882-1902</td>
<td>NSL/bokselskap.no 2016</td>
</tr>
<tr>
<td>Thoresen, Magdalene</td>
<td>Brandes, Georg</td>
<td>1865-1899</td>
<td>NSL/bokselskap.no 2015</td>
</tr>
<tr>
<td>Wergeland, Henrik</td>
<td>Bekkevold, Amalie</td>
<td>1838-1845</td>
<td>NSL/bokselskap.no 2011</td>
</tr>
</tbody>
</table><h2 id="appendix-2">Appendix 2</h2>
<h3 id="zotero-group-library">Zotero Group Library</h3>
<p>For scholarly editions of letters and correspondences in the hold of NB. Link to <a href="https://www.zotero.org/groups/2214573/norkorr">Group Library</a>.</p>
<h3 id="urns">URNs</h3>
<p>tba</p>
<h3 id="selection-criteria">Selection Criteria</h3>
<ul>
<li>
<p>has to be letters as part of an actual correspondence (no fictional letters, no religious sermons in the form of letters, no ‘letters to the editor’, no Briefromane)</p>
</li>
<li>
<p>has to be a scholarly edition - although, in the broadest, most inclusive sense</p>
</li>
</ul>
<p>Q: What to do with so called “utvandrerbrev”? There’s a couple of editions with letters from/to Norwegian emigrants (to the US and other places); could be of interest? Perhaps as a subcorpus; I assume that getting authority data for the senders/receivers is difficult in this case.</p>
<p>Q: Should the corpus be limited to “important” people? Pragmatically speaking, limiting the correspondences to “important” people like writers, politicians, cultural and academic elite, nobility could be the easiest way to create a corpus where authority data is available. Letters and correspondences of other people is interesting from a different perspective (local history, cultural history, genealogy etc.) but presumably harder to back with authority data and larger correspondences (aka ‘letters of a lifetime’).</p>

