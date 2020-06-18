import mysql.connector


connection = mysql.connector.connect(host='localhost',
                                     database='twitter_analysis',
                                     user='root',
                                     password='nineleaps')
conn = connection.cursor()