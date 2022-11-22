
# import psycopg2

# #establishing the connection
# conn = psycopg2.connect(
#    database="202001448_db", user='postgres', password='admin', host='127.0.0.1', port= '5432'
# )
# #Creating a cursor object using the cursor() method
# cursor = conn.cursor()

# #Executing an MYSQL function using the execute() method
# cursor.execute("SET SEARCH_PATH TO researchHub;")
# #cursor.execute('select * from Recruitment order by professorid LIMIT 1;')
# cursor.execute("""select a.ArticleID, a.Supports from "Published" as p inner join "Article" as a 	on p.ArticleID = a.ArticleID where	p.StudProfID = 104;""")

# # Fetch a single row using fetchone() method.
# data = cursor.fetchall()
# print("Connection established to: ",data)

# #Closing the connection
# conn.close()
# #Connection established to: (
# #   'PostgreSQL 11.5, compiled by Visual C++ build 1914, 64-bit',
# #)5432

import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="202001448_db", user='postgres', password='admin', host='127.0.0.1', port= '5433'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute('SET SEARCH_PATH TO "researchHub";')
cursor.execute('select * from "UserDetails"')

# Fetch a single row using fetchone() method.
data = cursor.fetchall()
print("Connection established to: ",data)

#Closing the connection
conn.close()