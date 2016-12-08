# olog-project

Repository for everything related to the olog-project.

---
### Repository Map

- The file `news_scraped_text.txt` contains the extracted data. 
- `nyt_text_scrape.py` and `toi_scrape_text.py` are python scripts for scraping the links.
- `links_extracted.txt` contains links extracted after filtering for `transport-related` articles on NYT, TOI, and Hindu news websites. These links were accessed and scraping was perfomed.
- `olog.sql`: This is the exported `sql` from [EASIK](https://github.com/CategoricalData/easik). Import this file in a local mysql instance to get the database.
- `noun_extractor.py`: This is a script to extract nouns from text using Stanford's Part-Of-Speech Tagger ([POS Tagger](http://nlp.stanford.edu/software/tagger.shtml))  
