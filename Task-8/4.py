import pandas as pd
ser = pd.Series(['amrita', 'school', 'of','engineering','chennai','campus'])
new_ser= ser.str.title()  
print("The original series: ")
print(ser)
print("The new series: ")
print(new_ser)