setwd("/Users/francesco/public_git/ScrapeOpen/sistat.istat.it/")

sistat_dat <- 
  read.csv('open_csv_20190601_comuni.csv')

load("/Users/francesco/Desktop/projects/historical_geographic_entity_database/reboot/01_place_table/01_place_table.RData")

require(stringr)

sistat_dat$wikidata_id <-
  str_extract(place_table$wikidata_id[match(sistat_dat$sistat_id, 
                                place_table$sistat_id)], "Q[0-9]+")

sistat_dat$lon <-
  place_table$lon[match(sistat_dat$sistat_id, 
                        place_table$sistat_id)]

sistat_dat$lat <-
  place_table$lat[match(sistat_dat$sistat_id, 
                        place_table$sistat_id)]

write.csv(sistat_dat, 
          "open_csv_20190601_comuni_wikidata_linked.csv", row.names = FALSE)

