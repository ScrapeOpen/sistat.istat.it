source('https://raw.githubusercontent.com/fraba/R_cheatsheet/master/database.R')

# 20190601

db1 <- 
  "/Users/francesco/public_git/ScrapeOpen/sistat.istat.it/01_sistat_comune_variations_20190601.sqlite"
db2 <- 
  "/Users/francesco/public_git/ScrapeOpen/sistat.istat.it/02_sistat_comune_variation_details_20190601.sqlite"
db3 <- 
  "/Users/francesco/public_git/ScrapeOpen/sistat.istat.it/02_sistat_comune_variation_details_20180331.sqlite"

comune_variation <- sqliteGetTable(db1, "comune_variation")

open_csv_20190601_comuni <- 
  unique(comune_variation[,c('comuni_sistat_id','comune_last_name','comune_last_istat_cod')])
colnames(open_csv_20190601_comuni) <- c('sistat_id', 'last_name', 'last_istat_cod')
open_csv_20190601_comuni <- open_csv_20190601_comuni[order(open_csv_20190601_comuni$last_name),]

open_csv_20190601_comuni_variations <- unique(event_scope[,c(1:3,5,7)])
open_csv_20190601_comuni_variations$event_date <- 
  as.Date(open_csv_20190601_comuni_variations$event_date, "%d/%m/%Y")  
open_csv_20190601_comuni_variations$event_validity_from <- 
  as.Date(open_csv_20190601_comuni_variations$event_validity_from, "%d/%m/%Y")  

open_csv_20190601_events <- sqliteGetTable(db2, "event_scope")

open_csv_20190601_events$event_date <- 
  as.Date(open_csv_20190601_events$event_date, "%d/%m/%Y")
open_csv_20190601_events$event_validity_from <- 
  as.Date(open_csv_20190601_events$event_validity_from, "%d/%m/%Y")
open_csv_20190601_events$event_validity_to <- 
  as.Date(open_csv_20190601_events$event_validity_to, "%d/%m/%Y")

open_csv_20190601_event_change_code <- 
  unique(sqliteGetTable(db2, "event_change_code"))
open_csv_20190601_event_change_name <- 
  unique(sqliteGetTable(db2, "event_change_name"))
open_csv_20190601_event_change_part_of <- 
  unique(sqliteGetTable(db2, "event_change_part_of"))
open_csv_20190601_event_creation <- 
  unique(sqliteGetTable(db2, "event_creation"))
open_csv_20190601_event_extinction <- 
  unique(sqliteGetTable(db2, "event_extinction"))
open_csv_20190601_event_territory_acquisition <- 
  unique(sqliteGetTable(db2, "event_territory_acquisition"))
open_csv_20190601_event_territory_cession <- 
  unique(sqliteGetTable(db2, "event_territory_cession"))

# Integration for missing records
library(dplyr)
open_csv_20180331_event_change_name <- 
  unique(sqliteGetTable(db3, "event_change_name"))
res <-
  setdiff(open_csv_20180331_event_change_name, 
        open_csv_20190601_event_change_name)
open_csv_20190601_event_change_name <-
  rbind(open_csv_20190601_event_change_name,
        res)

open_csv_20180331_event_change_part_of <- 
  unique(sqliteGetTable(db3, "event_change_part_of"))
res <-
  setdiff(open_csv_20180331_event_change_part_of, 
          open_csv_20190601_event_change_part_of)
## Differences in same events
intersect(res[,1:2],
          open_csv_20190601_event_change_part_of[,1:2])
res <- res[-(which(res$sistat_id == 3168 &
                     res$event_num == 4170)),]
res <- res[-(which(res$sistat_id == 11077 &
                     res$event_num == 4170)),]
open_csv_20190601_event_change_part_of <- 
  open_csv_20190601_event_change_part_of[
    -which(open_csv_20190601_event_change_part_of$sistat_id == 213 &
             open_csv_20190601_event_change_part_of$event_num == 6029),]
open_csv_20190601_event_change_part_of <-
  rbind(open_csv_20190601_event_change_part_of,
        res)

open_csv_20180331_event_creation <- 
  unique(sqliteGetTable(db3, "event_creation"))
res <-
  setdiff(open_csv_20180331_event_creation, 
          open_csv_20190601_event_creation)
intersect(res[,1:2],
          open_csv_20190601_event_creation[,1:2])
res <- res[-(which(res$sistat_id == 7838 &
                     res$event_num == 5886)),]
open_csv_20190601_event_creation <-
  rbind(open_csv_20190601_event_creation,
        res)

open_csv_20180331_event_extinction <- 
  unique(sqliteGetTable(db3, "event_extinction"))
res <-
  setdiff(open_csv_20180331_event_extinction, 
          open_csv_20190601_event_extinction)
intersect(res[,1:2],
          open_csv_20190601_event_extinction[,1:2])
open_csv_20190601_event_extinction <- 
  open_csv_20190601_event_extinction[
    -which(open_csv_20190601_event_extinction$sistat_id == 10873 &
             open_csv_20190601_event_extinction$event_num == 4193),]
open_csv_20190601_event_extinction <- 
  open_csv_20190601_event_extinction[
    -which(open_csv_20190601_event_extinction$sistat_id == 10336 &
             open_csv_20190601_event_extinction$event_num == 3799),]
open_csv_20190601_event_extinction <-
  rbind(open_csv_20190601_event_extinction,
        res)

open_csv_20180331_event_territory_acquisition <- 
  unique(sqliteGetTable(db3, "event_territory_acquisition"))
res <-
  setdiff(open_csv_20180331_event_territory_acquisition, 
          open_csv_20190601_event_territory_acquisition)
intersect(res[,1:2],
          open_csv_20190601_event_territory_acquisition[,1:2])
open_csv_20190601_event_territory_acquisition <- 
  open_csv_20190601_event_territory_acquisition[
    -which(open_csv_20190601_event_territory_acquisition$sistat_id == 2701 &
             open_csv_20190601_event_territory_acquisition$event_num == 3777),]
res <- res[-(which(res$sistat_id == 7838 &
                     res$event_num == 5886)),]
res <- res[-(which(res$sistat_id == 2844 &
                     res$event_num == 177)),] # This is somehow unclear
open_csv_20190601_event_territory_acquisition <-
  rbind(open_csv_20190601_event_territory_acquisition,
        res)

open_csv_20180331_event_territory_cession <- 
  unique(sqliteGetTable(db3, "event_territory_cession"))
res <-
  setdiff(open_csv_20180331_event_territory_cession, 
          open_csv_20190601_event_territory_cession)
intersect(res[,1:2],
          open_csv_20190601_event_territory_cession[,1:2])
open_csv_20190601_event_territory_cession <-
  rbind(open_csv_20190601_event_territory_cession,
        res)

setwd('/Users/francesco/public_git/ScrapeOpen/sistat.istat.it/')
write.csv(open_csv_20190601_comuni, 
          file = 'open_csv_20190601_comuni.csv', row.names = F)
write.csv(open_csv_20190601_comuni_variations, 
          file = 'open_csv_20190601_comuni_variations.csv', row.names = F)
write.csv(open_csv_20190601_events, 
          file = 'open_csv_20190601_events.csv', row.names = F)
write.csv(open_csv_20190601_event_change_code, 
          file = 'open_csv_20190601_event_change_code.csv', row.names = F)
write.csv(open_csv_20190601_event_change_name, 
          file = 'open_csv_20190601_event_change_name.csv', row.names = F)
write.csv(open_csv_20190601_event_change_part_of, 
          file = 'open_csv_20190601_event_change_part_of.csv', row.names = F)
write.csv(open_csv_20190601_event_creation, 
          file = 'open_csv_20190601_event_creation.csv', row.names = F)
write.csv(open_csv_20190601_event_extinction, 
          file = 'open_csv_20190601_event_extinction.csv', row.names = F)
write.csv(open_csv_20190601_event_territory_acquisition, 
          file = 'open_csv_20190601_event_territory_acquisition.csv', row.names = F)
write.csv(open_csv_20190601_event_territory_cession, 
          file = 'open_csv_20190601_event_territory_cession.csv', row.names = F)
