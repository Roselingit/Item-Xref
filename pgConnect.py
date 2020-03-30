import psycopg2

try:

    connection = psycopg2.connect(
        database = "bsd_integration",
        user = "salesforce",
        password = "An6a4VyP",
        host = "post-salesforce-dev.ctfgj6jo5ng6.us-east-1.rds.amazonaws.com",
        port = "5432"
    )

    print("connected to postgres");

    cursor = connection.cursor()
    postgres_insert_query = "INSERT INTO \"bsd_integration_SFDC\".\"BSD_XREF_WORKBOOK_FILE_STATUS\" (\"QUOTE_ID\", \"FILE_ID\", \"FILE_NAME\", \"FILE_SOURCE\", \"STATUS\") VALUES (%s,%s,%s,%s,%s)"
    record_to_insert = ('TestQuoteid', 'Blah Blah file id', 'Blah Blah file name.xlsx', 's3', 'Init')
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print (count, "Record inserted successfully into BSD_XREF_WORKBOOK_FILE_STATUS table")

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")