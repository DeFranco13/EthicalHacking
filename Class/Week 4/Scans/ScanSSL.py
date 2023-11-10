import schedule
import time
import os

def job():
    os.system("sslscan --show-certificate --xml=outputXML.xml --targets=lijstmetsites.txt")
    os.system("python3 CSVFilter.py --input outputXML.xml --output file.csv")

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)