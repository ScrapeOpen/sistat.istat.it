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

| sistat\_id | last\_name          | last\_istat\_cod |
| ---------: | :------------------ | ---------------: |
|       7579 | Aidone              |            86002 |
|       7026 | Santa Sofia d’Epiro |            78133 |
|        711 | Ceresole Alba       |             4062 |
|      10242 | Centemero           |            13852 |
|       3755 | Resana              |            26066 |

### Comuni variations

This table contains one record for each variation associated with a
*comune*. A *comune* with no variation is not present in this table (I
think…).

  - file name: `open_csv_20190601_comuni_variations.csv`
  - records: 23075
  - data example:

| sistat\_id | event\_num | event\_type            | event\_date | event\_validity\_from |
| ---------: | ---------: | :--------------------- | :---------- | :-------------------- |
|       3874 |       3619 | creation               | 1866-11-04  | 1866-11-20            |
|       7943 |       5847 | creation               | 1946-02-22  | 1946-04-13            |
|      11387 |       4346 | territory\_acquisition | 1928-03-15  | 1928-05-02            |
|       3332 |       3461 | creation               | 1920-09-26  | 1920-10-16            |
|       1214 |       2948 | change\_name           | 1939-07-22  | 1939-10-21            |

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

| event\_num | event\_act   | event\_date | event\_description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | event\_validity\_from | event\_validity\_to |
| ---------: | :----------- | :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------- | :------------------ |
|       4516 | R.D. N. 386  | 1933-03-23  | NUOVO COMUNE DI BORGIO VEREZZI COSTITUITO CON I TERRITORI DEI SOPPRESSI COMUNI DI BORGIO E VEREZZI IN PROVINCIA DI SAVONA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 1927-01-12            | 1933-05-24          |
|        101 | L.R. N. 13   | 1968-06-15  | AGGREGATI AL COMUNE DI TRENTO I TERRITORI DEI SOPPRESSI COMUNI DI BASELGA DI VEZZANO E VIGOLO BASELGA IN PROVINCIA DI TRENTO                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 1947-01-15            | 1968-07-03          |
|       3320 | LEGGE N. 113 | 1950-03-13  | RICOSTITUITI I COMUNI DI BULGAROGRASSO E VENIANO A SEGUITO DEL DISTACCO DEI TERRITORI DAL COMUNE DI APPIANO GENTILE; RICOSTITUITI I COMUNI DI CARUGO E DI AROSIO (PRIVO DELLA FRAZIONE BIGONCINO GIA’ CEDUTA AL COMUNE DI INVERIGO NEL 1929) A SEGUITO DEL DISTACCO DEI TERRITORI DAL SOPPRESSO COMUNE DI CARUGO AROSIO; RICOSTITUITI I COMUNI DI BARNI E MAGREGLIO A SEGUITO DEL DISTACCO DEI TERRITORI DAL COMUNE DI CIVENNA; RICOSTITUITO IL COMUNE DI BENE LARIO A SEGUITO DEL DISTACCO DEL TERRITORIO DAL COMUNE DI GRANDOLA ED UNITI; RICOSTITUITO IL COMUNE DI NOVEDRATE A SEGUITO DEL DISTACCO DEL TERRITORIO DAL SOPPRESSO COMUNE DI CARIMATE; RICOSTITUITI I COMUNI DI COLONNO, OSSUCCIO E SALA COMACINA A SEGUITO DEL DISTACCO DEI TERRITORI DAL SOPPRESSO COMUNE DI ISOLA COMACINA; RICOSTITUITI I COMUNI DI LIVO E VERCANA A SEGUITO DEL DISTACCO DEI TERRITORI DAL COMUNE DI DOMASO; RICOSTITUITO IL COMUNE DI LOCATE VARESINO A SEGUITO DEL DISTACCO DEL TERRITORIO DAL COMUNE DI SEPRIO; RICOSTITUITO IL COMUNE DI SAN NAZZARO VAL CAVARGNA A SEGUITO DEL DISTACCO DEL TERRITORIO DAL COMUNE DI SAN BARTOLOMEO VAL CAVARGNA; RICOSTITUITO IL COMUNE DI DORIO A SEGUITO DEL DISTACCO DEL TERRITORIO DAL COMUNE DI DERVIO, TUTTI IN PROVINCIA DI COMO | 1950-04-05            | NA                  |

### Event: change code

This table details variations in the ISTAT code.

  - file name: `open_csv_20190601_event_change_code.csv`
  - records: 321
  - data example:

| sistat\_id | event\_num | event\_old\_istat\_cod | event\_new\_istat\_cod |
| ---------: | ---------: | ---------------------: | ---------------------: |
|       4052 |        300 |                  30069 |                  30045 |
|       7892 |        302 |                  92028 |                  92011 |
|       4070 |        300 |                  30087 |                  30061 |
|       4038 |        300 |                  30055 |                  30036 |
|       4028 |        300 |                  30045 |                  30029 |

### Event: change name

This table details variations in the name.

  - file name: `open_csv_20190601_event_change_name.csv`
  - records: 2747
  - data example:

| sistat\_id | event\_num | event\_old\_name | event\_new\_name     |
| ---------: | ---------: | :--------------- | :------------------- |
|       5308 |       4987 | Camerata         | Camerata Nuova       |
|       9513 |       5015 | Civitella        | Civitella Licinio    |
|       4016 |       4100 | Cavazzo          | Cavazzo Carnico      |
|        405 |       2650 | Palazzolo        | Palazzolo Vercellese |
|       6146 |       2681 | Pettorano        | Pettorano sul Gizio  |

### Event: change part of

This table details variations in hierarchical relations (when a *comune*
change provice).

  - file name: `open_csv_20190601_event_change_part_of.csv`
  - records: 5017
  - data example:

| sistat\_id | event\_num | event\_new\_istat\_cod | event\_new\_province                   | event\_old\_istat\_cod | event\_old\_province |
| ---------: | ---------: | ---------------------: | :------------------------------------- | ---------------------: | :------------------- |
|       5265 |       2767 |                  57044 | Rieti                                  |                  58905 | \-                   |
|      10969 |       4170 |                  22675 | Trento                                 |                 802851 | \-                   |
|       7258 |       6030 |                  80051 | Città metropolitana di Reggio Calabria |                  80051 | \-                   |
|       7849 |        624 |                  95087 | Oristano                               |                  91087 | Nuoro                |
|      10966 |       4170 |                  22406 | Trento                                 |                 802211 | \-                   |

### Event: event creation

This table details the creation event.

  - file name: `open_csv_20190601_event_creation.csv`
  - records: 4262
  - data example:

| sistat\_id | event\_num | event\_from\_name | event\_from\_istat\_cod | event\_from\_area | event\_from\_population | event\_from\_extinction\_flag |
| ---------: | ---------: | :---------------- | ----------------------: | :---------------- | :---------------------- | :---------------------------- |
|      11647 |       6048 | Saletto           |                   28074 | 1079              | 2869                    | S                             |
|      11476 |       2934 | Rhêmes Notre Dame |                    7055 | NON DOCUMENTATA   | NON DOCUMENTATA         | S                             |
|       1701 |       3158 | Capiago           |                   13832 | NON DOCUMENTATA   | NON DOCUMENTATA         | S                             |
|       5052 |       4771 | Campagnatico      |                   53002 | 19271             | 4775                    | N                             |
|         79 |       2412 | Cuorgnè           |                    1098 | 403               | 298                     | N                             |

### Event: event extinction

This table details the extinction event.

  - file name: `open_csv_20190601_event_extinction.csv`
  - records: 3585
  - data example:

| sistat\_id | event\_num | event\_to\_name  | event\_to\_istat\_cod | event\_to\_area | event\_to\_population | event\_to\_creation\_flag |
| ---------: | ---------: | :--------------- | --------------------: | :-------------- | :-------------------- | :------------------------ |
|      11472 |       3341 | Stazzona         |                 13218 | 746             | 665                   | S                         |
|       4538 |       5956 | Poggio Torriana  |                 99028 | 1176            | 1096                  | S                         |
|       3396 |       5993 | Porte di Rendena |                 22244 | 3496            | 760                   | S                         |
|       8016 |       5787 | Lunamatrona      |                 92057 | NON DOCUMENTATA | NON DOCUMENTATA       | N                         |
|       9482 |       5345 | Napoli           |                 63049 | NON DOCUMENTATA | NON DOCUMENTATA       | N                         |

### Event: territory acquisition

This table details the acquisition of territory.

  - file name: `open_csv_20190601_event_territory_acquisition.csv`
  - records: 5828
  - data example:

| sistat\_id | event\_num | event\_from\_name    | event\_from\_istat\_cod | event\_from\_area | event\_from\_population | event\_from\_extinction\_flag |
| ---------: | ---------: | :------------------- | ----------------------: | :---------------- | :---------------------- | :---------------------------- |
|      10066 |       3679 | Dergano              |                   15869 | NON DOCUMENTATA   | NON DOCUMENTATA         | S                             |
|      11603 |       6000 | Farra d’Alpago       |                   25020 | 4121              | 3037                    | S                             |
|       2564 |       3137 | Presegno             |                   17879 | NON DOCUMENTATA   | NON DOCUMENTATA         | S                             |
|       8031 |       5800 | Siamanna             |                   95809 | NON DOCUMENTATA   | NON DOCUMENTATA         | S                             |
|       4509 |       4635 | Civitella di Romagna |                   40009 | NON DOCUMENTATA   | NON DOCUMENTATA         | N                             |

### Event: territory cession

This table details the cession of territory.

  - file name: `open_csv_20190601_event_territory_cession.csv`
  - records: 2368
  - data example:

| sistat\_id | event\_num | event\_to\_name         | event\_to\_istat\_cod | event\_to\_area | event\_to\_population | event\_to\_creation\_flag |
| ---------: | ---------: | :---------------------- | --------------------: | :-------------- | :-------------------- | :------------------------ |
|       4113 |        601 | Coseano                 |                 30031 | 2               |                       | N                         |
|       2728 |       3855 | Borgarello              |                 18015 | NON DOCUMENTATA | NON DOCUMENTATA       | N                         |
|       7890 |       5758 | Selargius               |                 92116 | NON DOCUMENTATA | NON DOCUMENTATA       | S                         |
|        328 |         57 | Camandona               |                  2023 | NON DOCUMENTATA | 12                    | N                         |
|       7704 |        190 | Sant’Antonio di Gallura |                 90085 | 7200            | 1492                  | S                         |

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
