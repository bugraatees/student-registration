import mysql.connector
   
connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "mysql123",
        auth_plugin = "mysql_native_password",
        database = "schooldb"
    )

