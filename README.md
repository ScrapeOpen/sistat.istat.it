# sistat.istat.it

Scraper for  The dataset is (not yet) stored on [Dataverse](https://doi.org/10.7910/DVN/ADKV8H). To cite:

```
@data{DVN/ADKV8H_2018,
author = {Bailo, Francesco},
publisher = {Harvard Dataverse},
title = {Historical Information System of Territorial Administrations | sistat.istat.it},
year = {2018},
doi = {10.7910/DVN/ADKV8H},
url = {https://doi.org/10.7910/DVN/ADKV8H}
}
```

# Source

[sistat.istat.it](http://http://sistat.istat.it/) is a web application curated by Italy's National Institute of Statistics (Istat). It provides information of official changes to territorial administrations. 

# Code

These three scripts must be run sequentially

*  `01_scrape_comune_variations.py` is used to scrape and store all the variations from "Ricerca Gerarchica - Comuni - Storia Comuni" [Link](https://sistat.istat.it/sistat/gestioneComuni.do). It creates this SQLite table:

```
    CREATE TABLE comune_variation (
    comuni_sistat_id INT,
    comune_last_name CHAR,
    comune_last_istat_cod CHAR,
    data_inizio_validita CHAR,
    data_fine_validita CHAR,
    tipo_variazione CHAR,
    tipo_variazione_script CHAR,
    tipo_documento CHAR,
    data_publicazione CHAR
	);
```

The field `tipo_variazione_script` contains the script requesting the variation page. 


*  `02_scrape_comune_variation_details.py` request, scrape and store each variation contained in the table populated with the previous script. It will return a database with multiple tables. 

* `03_read_and_write.R` write the `.csv`  from the tables contained in the database created in the previous steps.

Data is described [here](data.md).







