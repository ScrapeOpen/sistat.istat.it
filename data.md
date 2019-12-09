Data
================

This document describes the tables produced from scraping *comune*
variations from sistat.istat.it.

## Variables

  - `sistat_id`: a *comune* unique ID within the dataset
  - `?(*_)istat_cod`: reference to the *comune* ISTAT code.
  - `event_num`: the unique ID of an event within the dataset.
  - `event_type`: the type of event.

## Tables

### Comuni

This table contains one record for each *comune* describes in the
dataset.

  - file name: `open_csv_20190601_comuni.csv`
  - records: 10331
  - data example:

| sistat\_id | last\_name       | last\_istat\_cod |
| ---------: | :--------------- | ---------------: |
|       1412 | Tovo San Giacomo |             9062 |
|       2460 | Vercurago        |            97086 |
|       1162 | Ricaldone        |             6143 |
|      10967 | Morter/Morter    |            21858 |
|       8179 | Vajont           |            93052 |

### Comuni variations

This table contains one record for each variation associated with a
*comune*. A *comune* with no variation is not present in this table (I
think…).

  - file name: `open_csv_20190601_comuni_variations.csv`
  - records: 23075
  - data example:

| sistat\_id | event\_num | event\_type        | event\_date | event\_validity\_from |
| ---------: | ---------: | :----------------- | :---------- | :-------------------- |
|         17 |       2364 | creation           | 1946-11-22  | 1947-01-10            |
|      10237 |       3786 | extinction         | 1874-11-02  | NA                    |
|       7953 |        575 | change\_part\_of   | 2001-07-12  | 2006-01-01            |
|       4277 |       4578 | territory\_cession | 1870-05-01  | 1870-07-01            |
|      11051 |       2767 | change\_part\_of   | 1927-01-02  | 1927-01-12            |

  - event types:

| event\_type            |    n |
| :--------------------- | ---: |
| annexation             | 1907 |
| change\_code           |  321 |
| change\_name           | 2747 |
| change\_part\_of       | 5017 |
| creation               | 3578 |
| extinction             | 3384 |
| territory\_acquisition | 4003 |
| territory\_cession     | 2118 |

### Events

This table details the variation events and the scope of the variation
events described in the dataset.

  - file name: `open_csv_20190601_events.csv`
  - records: 8677
  - data example:

| event\_num | event\_act   | event\_date | event\_description                                                                                                                                      | event\_validity\_from | event\_validity\_to |
| ---------: | :----------- | :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------- | :------------------ |
|       5959 | L.R. N. 67   | 2013-11-22  | NUOVO COMUNE DI SCARPERIA E SAN PIERO COSTITUITO MEDIANTE FUSIONE DEI COMUNI DI SCARPERIA E SAN PIERO A SIEVE IN PROVINCIA DI FIRENZE                   | NA                    | 2014-01-01          |
|       4016 | R.D. N. 1384 | 1931-10-15  | NUOVO COMUNE DI VAL DI VIZZE/PFITSCHVIENE COSTITUITO CON I TERRITORI DEI SOPPRESSI COMUNI DI VIZZE/PFITSCH E PRATI/WIESEN IN PROVINCIA DI BOLZANO/BOZEN | 1927-01-12            | 1931-12-06          |
|       5164 | R.D. N. 840  | 1912-07-18  | NUOVA DENOMINAZIONE CAPPELLE SUL TAVO ASSUNTA DAL COMUNE DI CAPPELLE IN PROVINCIA DI TERAMO                                                             | 1912-08-24            | 1927-01-12          |

### Event: change code

This table details variations in the ISTAT code.

  - file name: `open_csv_20190601_event_change_code.csv`
  - records: 321
  - data example:

| sistat\_id | event\_num | event\_old\_istat\_cod | event\_new\_istat\_cod |
| ---------: | ---------: | ---------------------: | ---------------------: |
|       4143 |        300 |                  30160 |                  30116 |
|       8022 |        302 |                  92158 |                  92095 |
|       4075 |        300 |                  30092 |                  30064 |
|       4063 |        300 |                  30080 |                  30055 |
|       4105 |        300 |                  30122 |                  30087 |

### Event: change name

This table details variations in the name.

  - file name: `open_csv_20190601_event_change_name.csv`
  - records: 2747
  - data example:

| sistat\_id | event\_num | event\_new\_name       | event\_old\_name     |
| ---------: | ---------: | :--------------------- | :------------------- |
|      10857 |       3541 | Virle                  | Virle Treponti       |
|       2184 |       2664 | San Zenone             | San Zenone al Lambro |
|         64 |       2757 | Castagneto             | Castagneto Po        |
|       5555 |       5339 | Castello di Campagnano | Castel Campagnano    |
|       1280 |       2931 | Valtornenza            | Valtournanche        |

### Event: change part of

This table details variations in hierarchical relations (when a *comune*
change provice).

  - file name: `open_csv_20190601_event_change_part_of.csv`
  - records: 5017
  - data example:

| sistat\_id | event\_num | event\_new\_istat\_cod | event\_new\_province           | event\_old\_istat\_cod | event\_old\_province |
| ---------: | ---------: | ---------------------: | :----------------------------- | ---------------------: | :------------------- |
|       7114 |        310 |                 102018 | Vibo Valentia                  |                  79066 | Catanzaro            |
|        164 |       6029 |                   1164 | Città metropolitana di Torino  |                   1164 | \-                   |
|       3789 |       6029 |                  27005 | Città metropolitana di Venezia |                  27005 | \-                   |
|       5758 |       6029 |                  63049 | Città metropolitana di Napoli  |                  63049 | \-                   |
|       2162 |        615 |                 108037 | Monza e della Brianza          |                  15180 | \-                   |

### Event: event creation

This table details the creation event.

  - file name: `open_csv_20190601_event_creation.csv`
  - records: 4262
  - data example:

| sistat\_id | event\_num | event\_from\_name       | event\_from\_istat\_cod | event\_from\_area | event\_from\_population | event\_from\_extinction\_flag |
| ---------: | ---------: | :---------------------- | ----------------------: | :---------------- | :---------------------- | :---------------------------- |
|       4174 |       4294 | \-                      |                      NA | NON DOCUMENTATA   | NON DOCUMENTATA         |                               |
|       3434 |       3619 | \-                      |                      NA | NON DOCUMENTATA   | NON DOCUMENTATA         |                               |
|       7486 |       5693 | Sant’Agata di Militello |                   83084 | NON DOCUMENTATA   | NON DOCUMENTATA         | N                             |
|       8249 |        359 | Scandeluzza             |                    5102 | 599               | 250                     | S                             |
|       1115 |       2927 | Molino Alzano           |                    6813 | 274               | 891                     | S                             |

### Event: event extinction

This table details the extinction event.

  - file name: `open_csv_20190601_event_extinction.csv`
  - records: 3585
  - data example:

| sistat\_id | event\_num | event\_to\_name | event\_to\_istat\_cod | event\_to\_area | event\_to\_population | event\_to\_creation\_flag |
| ---------: | ---------: | :-------------- | --------------------: | :-------------- | :-------------------- | :------------------------ |
|       9869 |       2535 | Varallo         |                  2156 | NON DOCUMENTATA | NON DOCUMENTATA       | N                         |
|       6852 |       5505 | Chiaromonte     |                 76028 | NON DOCUMENTATA | NON DOCUMENTATA       | N                         |
|       3218 |       3910 | Condino         |                 22066 | NON DOCUMENTATA | NON DOCUMENTATA       | N                         |
|       2652 |       3372 | Valsaviore      |                 17906 | 8241            | 2265                  | S                         |
|      11408 |       4308 | Primano         |                701712 | NON DOCUMENTATA | NON DOCUMENTATA       | N                         |

### Event: territory acquisition

This table details the acquisition of territory.

  - file name: `open_csv_20190601_event_territory_acquisition.csv`
  - records: 5828
  - data example:

| sistat\_id | event\_num | event\_from\_name | event\_from\_istat\_cod | event\_from\_area | event\_from\_population | event\_from\_extinction\_flag |
| ---------: | ---------: | :---------------- | ----------------------: | :---------------- | :---------------------- | :---------------------------- |
|       5758 |       5322 | Pozzuoli          |                   63060 | NON DOCUMENTATA   | NON DOCUMENTATA         | N                             |
|       5755 |       5398 | Sorrento          |                   63080 | NON DOCUMENTATA   | NON DOCUMENTATA         |                               |
|      11465 |       5326 | Vitulazio         |                   63899 | 2272              | 3328                    | S                             |
|       4180 |       4301 | Corona            |                   31802 | NON DOCUMENTATA   | NON DOCUMENTATA         | S                             |
|       1444 |       4480 | Nervi             |                   10812 | NON DOCUMENTATA   | NON DOCUMENTATA         | S                             |

### Event: territory cession

This table details the cession of territory.

  - file name: `open_csv_20190601_event_territory_cession.csv`
  - records: 2368
  - data example:

| sistat\_id | event\_num | event\_to\_name | event\_to\_istat\_cod | event\_to\_area | event\_to\_population | event\_to\_creation\_flag |
| ---------: | ---------: | :-------------- | --------------------: | :-------------- | :-------------------- | :------------------------ |
|       1346 |       4479 | Soldano         |                  8058 | NON DOCUMENTATA | NON DOCUMENTATA       | S                         |
|       7881 |       5853 | Las Plassas     |                 92056 | NON DOCUMENTATA | NON DOCUMENTATA       | S                         |
|       6377 |       5207 | Buonanotte      |                 69009 | NON DOCUMENTATA | NON DOCUMENTATA       | S                         |
|       3390 |       4052 | Soraga          |                 22176 | NON DOCUMENTATA | NON DOCUMENTATA       | N                         |
|       7311 |       5617 | Custonaci       |                 81007 | 6961            | 4410                  | S                         |

## Data schema and integrity

#### `open_csv_20190601_comuni_variations.csv` – `open_csv_20190601_events.csv`

Every variation event contained in
`open_csv_20190601_comuni_variations.csv` is described in
`open_csv_20190601_events.csv`.

``` r
filename <- sprintf("open_csv_%s_comuni_variations.csv", version)
comuni_variations <- read.csv(filename)

filename <- sprintf("open_csv_%s_events.csv", version)
events <- read.csv(filename)

any(!!comuni_variations$event_num %in% events$event_num)
```

    ## [1] TRUE

Relationship: one-to-many on `event_num`.

#### `open_csv_20190601_comuni_variations.csv` – `open_csv_20190601_event_change_code.csv`

``` r
filename <- sprintf("open_csv_%s_event_change_code.csv", version)
event_change_code <- read.csv(filename)

nrow(merge(comuni_variations[comuni_variations$event_type == "change_code",],
           event_change_code, 
           by = c("sistat_id", "event_num"),
           all = FALSE)) ==
  sum(comuni_variations$event_type == "change_code")
```

    ## [1] TRUE

Relationship: one-to-one on `sistat_id`, `event_num`.

#### `open_csv_20190601_comuni_variations.csv` – `open_csv_20190601_event_change_name.csv`

``` r
filename <- sprintf("open_csv_%s_event_change_name.csv", version)
event_change_name <- read.csv(filename)

nrow(merge(comuni_variations[comuni_variations$event_type == "change_name",],
           event_change_name, 
           by = c("sistat_id", "event_num"),
           all = FALSE)) ==
  sum(comuni_variations$event_type == "change_name")
```

    ## [1] TRUE

Relationship: one-to-one on `sistat_id`, `event_num`.

#### `open_csv_20190601_comuni_variations.csv` – `open_csv_20190601_event_change_part_of.csv`

``` r
filename <- sprintf("open_csv_%s_event_change_part_of.csv", version)
event_change_part_of <- read.csv(filename)

nrow(merge(comuni_variations[comuni_variations$event_type == "change_part_of",],
           event_change_part_of, 
           by = c("sistat_id", "event_num"),
           all = FALSE)) ==
  sum(comuni_variations$event_type == "change_part_of")
```

    ## [1] TRUE

Relationship: one-to-one on `sistat_id`, `event_num`.

#### `open_csv_20190601_comuni_variations.csv` – `open_csv_20190601_event_creation.csv`

``` r
filename <- sprintf("open_csv_%s_event_creation.csv", version)
event_creation <- read.csv(filename)

nrow(merge(comuni_variations[comuni_variations$event_type == "creation",],
           event_creation[!duplicated(event_creation[,1:2]),], 
           by = c("sistat_id", "event_num"),
           all = FALSE)) ==
  sum(comuni_variations$event_type == "creation")
```

    ## [1] TRUE

Relationship: one-to-many on `sistat_id`, `event_num`.

#### `open_csv_20190601_comuni_variations.csv` – `open_csv_20190601_event_extinction.csv`

``` r
filename <- sprintf("open_csv_%s_event_extinction.csv", version)
event_extinction <- read.csv(filename)

nrow(merge(comuni_variations[comuni_variations$event_type == "extinction",],
           event_extinction[!duplicated(event_extinction[,1:2]),], 
           by = c("sistat_id", "event_num"),
           all = FALSE)) ==
  sum(comuni_variations$event_type == "extinction")
```

    ## [1] TRUE

Relationship: one-to-many on `sistat_id`, `event_num`.

#### `open_csv_20190601_comuni_variations.csv` – `open_csv_20190601_event_territory_acquisition.csv`

``` r
filename <- sprintf("open_csv_%s_event_territory_acquisition.csv", version)
event_territory_acquisition <- read.csv(filename)

nrow(merge(comuni_variations[
  comuni_variations$event_type == "territory_acquisition",],
           event_territory_acquisition[
             !duplicated(event_territory_acquisition[,1:2]),], 
           by = c("sistat_id", "event_num"),
           all = FALSE)) ==
  sum(comuni_variations$event_type == "territory_acquisition")
```

    ## [1] TRUE

Relationship: one-to-many on `sistat_id`, `event_num`.

#### `open_csv_20190601_comuni_variations.csv` – `open_csv_20190601_event_territory_cession.csv`

``` r
filename <- sprintf("open_csv_%s_event_territory_cession.csv", version)
event_territory_cession <- read.csv(filename)

nrow(merge(comuni_variations[
  comuni_variations$event_type == "territory_cession",],
           event_territory_cession[
             !duplicated(event_territory_cession[,1:2]),], 
           by = c("sistat_id", "event_num"),
           all = FALSE)) ==
  sum(comuni_variations$event_type == "territory_cession")
```

    ## [1] TRUE

Relationship: one-to-many on `sistat_id`, `event_num`.
