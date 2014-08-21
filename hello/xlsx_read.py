import xlsxwriter
import cx_Oracle
from ctypes.wintypes import CHAR
from tokenize import String





#########################################################    
# ???  js 처럼 script src 하는 건가??     
#########################################################    
    
# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 100)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})


# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)


#########################################################    
# oracle connection     
#########################################################    

#https://www.google.co.kr/trends/explore#q=openpyxl%2C%20XLRD%2C%20XlsxWriter%2C%20xlwt&cmpt=q
#connection = cx_Oracle.connect("scott", "tiger", "ORCL")
connection = cx_Oracle.connect("scott/tiger@localhost:1521/xe")

cursor = connection.cursor()    
cursor.execute("SELECT empno, sal FROM emp")
# row = cursor.fetchone()
# print(row)
column = 1
for column_1, column_2 in cursor.fetchall():
    column +=1 
    print( "하하하하" +  str( column)  )
    # Write some simple text.
    worksheet.write(column , 1,column_1)
    # Text with formatting.
    worksheet.write(column, 2,column_2)
        
    print( "Values:", column_1, column_2)


# Insert an image.
#worksheet.insert_image('B5', 'logo.png')

workbook.close()
    




# dsn = cx_Oracle.makedsn("localhost", 1521, "xe")
# db = cx_Oracle.connect("ID", "PASSWORD", dsn)
# cursor = db.cursor()
# cursor.execute("""SELECT * FROM TABLE_NAME""")
# row = cursor.fetchone()

#  
# import os
# os.putenv("NLS_LANG", "KOREAN_KOREA.KO16KSC5601"); 
