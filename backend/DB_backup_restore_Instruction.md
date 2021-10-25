##Backup
docker exec -t finwise_database  pg_dumpall -c -U finwise | gzip > dump_$(date +"%Y-%m-%d_%H_%M_%S").gz


##RESTOR
cat dump_2021-10-23_13_25_20 | docker exec -i finwise_databse psql -U finwise -d finwiseDB
