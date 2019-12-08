source('https://raw.githubusercontent.com/fraba/R_cheatsheet/master/database.R')

# 20190601

db1 <- 
  "/Users/francesco/public_git/ScrapeOpen/sistat.istat.it/01_sistat_comune_variations_20190601.sqlite"
db2 <- 
  "/Users/francesco/public_git/ScrapeOpen/sistat.istat.it/02_sistat_comune_variation_details_20190601.sqlite"

comune_variation <- sqliteGetTable(db1, "comune_variation")

open_csv_20190601_comuni <- 
  unique(comune_variation[,c('comuni_sistat_id','comune_last_name','comune_last_istat_cod')])
colnames(open_csv_20190601_comuni) <- c('sistat_id', 'last_name', 'last_istat_cod')
open_csv_20190601_comuni <- open_csv_20190601_comuni[order(open_csv_20190601_comuni$last_name),]

event_scope <- sqliteGetTable(db2, "event_scope")

open_csv_20190601_comuni_variations <- unique(event_scope[,c(1:3,5,7)])
open_csv_20190601_comuni_variations$event_date <- 
  as.Date(open_csv_20190601_comuni_variations$event_date, "%d/%m/%Y")  
open_csv_20190601_comuni_variations$event_validity_from <- 
  as.Date(open_csv_20190601_comuni_variations$event_validity_from, "%d/%m/%Y")  

open_csv_20190601_events <- 
  unique(event_scope[,c('event_num','event_act','event_date','event_description','event_validity_from','event_validity_to')])

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
