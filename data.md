Data
================

This document describes the tables produced from scraping *comune*
variations from sistat.istat.it.

## Tables

### Comuni

This table contains one record for each *comune* describes in the
dataset.

  - file name: `open_csv_20190601_comuni.csv`
  - records: 10331
  - data example:

| sistat\_id | last\_name                | last\_istat\_cod |
| ---------: | :------------------------ | ---------------: |
|      11558 | Figline e Incisa Valdarno |            48052 |
|      11483 | Lieto Colle               |            13891 |
|        612 | Re                        |           103060 |
|       1085 | Dernice                   |             6066 |
|        650 | Acceglio                  |             4001 |

### Comuni variations

This table contains one record for each variation associated with a
*comune*. A *comune* with no variation is not present in this table (I
think…).

  - file name: `open_csv_20190601_comuni_variations.csv`
  - records: 23075
  - data example:

| sistat\_id | event\_num | event\_type            | event\_date | event\_validity\_from |
| ---------: | ---------: | :--------------------- | :---------- | :-------------------- |
|       4026 |        300 | change\_code           | 1968-03-01  | 1968-04-06            |
|       5392 |       5092 | territory\_acquisition | 1935-03-07  | 1935-04-18            |
|       1909 |        367 | territory\_acquisition | 1999-07-07  | 1999-07-27            |
|       4276 |       4673 | territory\_acquisition | 1943-04-14  | 1943-05-29            |
|       5481 |       5128 | territory\_acquisition | 1948-04-21  | 1948-08-11            |

### Events

This table details the variation events and the scope of the variation
events described in the dataset.

  - file name: `open_csv_20190601_events.csv`
  - records: 8677
  - data example:

| event\_num | event\_act   | event\_date | event\_description                                                                                                                   | event\_validity\_from | event\_validity\_to |
| ---------: | :----------- | :---------- | :----------------------------------------------------------------------------------------------------------------------------------- | :-------------------- | :------------------ |
|       2997 | R.D. N. 2476 | 1927-12-11  | AGGREGATO AL COMUNE DI NAVE IL TERRITORIO DEL SOPPRESSO COMUNE DI CAINO IN PROVINCIA DI BRESCIA                                      | NA                    | 1928-01-22          |
|       3936 | R.D. N. 1172 | 1928-05-06  | AGGREGATI AL COMUNE DI VIGO RENDENA I TERRITORI DEI SOPPRESSI COMUNI DI DARÈ E PELUGO IN PROVINCIA DI TRENTO                         | 1928-06-27            | 1946-12-19          |
|       5875 | L.R. n. 10   | 1958-06-11  | NUOVO COMUNE DI TRINITA’ D’AGULTO E VIGNOLA COSTITUITO CON LE FRAZIONI OMONIME STACCATE DAL COMUNE DI AGGIUS IN PROVINCIA DI SASSARI | 1958-08-12            | 2006-01-01          |

### Event: change code

This table details variations in the ISTAT code.

  - file name: `open_csv_20190601_event_change_code.csv`
  - records: 321
  - data example:

| sistat\_id | event\_num | event\_old\_istat\_cod | event\_new\_istat\_cod |
| ---------: | ---------: | ---------------------: | ---------------------: |
|       7961 |        302 |                  92097 |                  92054 |
|       4078 |        300 |                  30095 |                  30067 |
|       6461 |        301 |                  70084 |                  70051 |
|       8018 |        302 |                  92154 |                  92091 |
|       6440 |        301 |                  70063 |                  70037 |

### Event: change name

This table details variations in the name.

  - file name: `open_csv_20190601_event_change_name.csv`
  - records: 2741
  - data example:

| sistat\_id | event\_num | event\_new\_name | event\_old\_name     |
| ---------: | ---------: | :--------------- | :------------------- |
|       3781 |       4173 | Vittorio         | Vittorio Veneto      |
|      11091 |       3875 | Scale/Schalders  | Scaleres/Schalders   |
|       7000 |       4999 | Roseto           | Rosito Capo Spulico  |
|       3930 |       3630 | Villafranca      | Villafranca Padovana |
|       5308 |       4987 | Camerata         | Camerata Nuova       |

### Event: change part of

This table details variations in hierarchical relations (when a *comune*
change provice).

  - file name: `open_csv_20190601_event_change_part_of.csv`
  - records: 4996
  - data example:

| sistat\_id | event\_num | event\_new\_istat\_cod | event\_new\_province | event\_old\_istat\_cod | event\_old\_province |
| ---------: | ---------: | ---------------------: | :------------------- | ---------------------: | :------------------- |
|       3395 |       4170 |                  22222 | Trento               |                 802876 | \-                   |
|       7854 |        624 |                  95088 | Oristano             |                  91092 | Nuoro                |
|       8021 |        575 |                 107022 | \-                   |                  92094 | \-                   |
|      11316 |       4303 |                  30947 | Udine                |                 801257 | \-                   |
|       6402 |        301 |                  94010 | Isernia              |                  70025 | Campobasso           |

### Event: event creation

This table details the creation event.

  - file name: `open_csv_20190601_event_creation.csv`
  - records: 4248
  - data example:

| sistat\_id | event\_num | event\_from\_name | event\_from\_istat\_cod | event\_from\_area | event\_from\_population | event\_from\_extinction\_flag |
| ---------: | ---------: | :---------------- | ----------------------: | :---------------- | :---------------------- | :---------------------------- |
|       7869 |       5815 | Oristano          |                   92080 | NON DOCUMENTATA   | NON DOCUMENTATA         | N                             |
|       3695 |       4252 | Montebelluna      |                   26046 | NON DOCUMENTATA   | NON DOCUMENTATA         | N                             |
|       8008 |       5867 | Milis             |                   92062 | NON DOCUMENTATA   | NON DOCUMENTATA         | N                             |
|       3781 |       4115 | Serravalle        |                   26807 | NON DOCUMENTATA   | NON DOCUMENTATA         | S                             |
|       1852 |       3022 | Verna             |                   13954 | NON DOCUMENTATA   | NON DOCUMENTATA         | S                             |

### Event: event extinction

This table details the extinction event.

  - file name: `open_csv_20190601_event_extinction.csv`
  - records: 3569
  - data example:

| sistat\_id | event\_num | event\_to\_name               | event\_to\_istat\_cod | event\_to\_area | event\_to\_population | event\_to\_creation\_flag |
| ---------: | ---------: | :---------------------------- | --------------------: | :-------------- | :-------------------- | :------------------------ |
|      11077 |       4008 | Chiusa/Klausen                |                 21022 | NON DOCUMENTATA | NON DOCUMENTATA       | N                         |
|       8201 |       5777 | Ghilarza                      |                 92045 | NON DOCUMENTATA | NON DOCUMENTATA       | N                         |
|       1654 |       3113 | Venegono                      |                 12899 | 577             | 3127                  | S                         |
|        198 |       2857 | Perosa Argentina              |                  1184 | NON DOCUMENTATA | NON DOCUMENTATA       | N                         |
|      10659 |       3639 | Corte de’ Cortesi con Cignone |                 19032 | NON DOCUMENTATA | NON DOCUMENTATA       | N                         |

### Event: territory acquisition

This table details the acquisition of territory.

  - file name: `open_csv_20190601_event_territory_acquisition.csv`
  - records: 5797
  - data example:

| sistat\_id | event\_num | event\_from\_name   | event\_from\_istat\_cod | event\_from\_area | event\_from\_population | event\_from\_extinction\_flag |
| ---------: | ---------: | :------------------ | ----------------------: | :---------------- | :---------------------- | :---------------------------- |
|       6671 |       5460 | Francavilla Fontana |                   75812 | 3458              | 6546                    | N                             |
|        431 |       2559 | Villa del Bosco     |                    2161 | NON DOCUMENTATA   | NON DOCUMENTATA         | S                             |
|       4026 |       5933 | Basiliano           |                   30009 | NON DOCUMENTATA   | NON DOCUMENTATA         | N                             |
|        452 |       2774 | Piane Sesia         |                    2824 | NON DOCUMENTATA   | NON DOCUMENTATA         | S                             |
|       1174 |       2507 | Gremiasco           |                    6083 | NON DOCUMENTATA   | NON DOCUMENTATA         | S                             |

### Event: territory acquisition

This table details the cession of territory.

  - file name: `open_csv_20190601_event_territory_cession.csv`
  - records: 2363
  - data example:

| sistat\_id | event\_num | event\_to\_name  | event\_to\_istat\_cod | event\_to\_area | event\_to\_population | event\_to\_creation\_flag |
| ---------: | ---------: | :--------------- | --------------------: | :-------------- | :-------------------- | :------------------------ |
|       7057 |       6051 | Petronà          |                 79095 | 23              | 82                    | N                         |
|        684 |       2498 | Gottasecca       |                  4098 | NON DOCUMENTATA | NON DOCUMENTATA       | N                         |
|       3112 |       4064 | Andriano/Andrian |                 21002 | NON DOCUMENTATA | NON DOCUMENTATA       | S                         |
|        107 |       2742 | Levone           |                  1133 | NON DOCUMENTATA | NON DOCUMENTATA       | N                         |
|       6124 |       5208 | Lucoli           |                 66052 | NON DOCUMENTATA | NON DOCUMENTATA       | S                         |
