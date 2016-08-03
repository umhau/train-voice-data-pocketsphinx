import re
x=["file_01.csv","file_02.csv","file_03.csv"]
print max(x,key=lambda x:re.split(r"file_|\.csv",x)[1])
