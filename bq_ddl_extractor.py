from google.cloud import bigquery


client = bigquery.Client()
file = open('myfile.txt', 'r')
Lines = file.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Table{}: {}".format(count, line.strip()))
    
    table_info=line.split(".")
    project_name= table_info[0]
    dataset_name= table_info[1]
    table_name= table_info[2].rstrip("\n")
    sql= "select ddl from `{}.{}.INFORMATION_SCHEMA.TABLES`  where table_name ='{}'".format(project_name, dataset_name, table_name)
    query_job = client.query(sql)  # Make an API request.
    for row in query_job:
        ddl=row[0]

    output_file="{}_ddl.sql".format(table_name)

    f = open(output_file, "w")
    f.write(ddl)
    f.close

file.close

