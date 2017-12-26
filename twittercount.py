import urllib.request, urllib.parse, urllib.error
import twurl
import ssl
import json
import datetime


#https://apps.twitter.com/


TWITTER_URL = 'https://api.twitter.com/1.1/search/tweets.json'

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Represent the current time 
a = datetime.datetime.utcnow()
year2 = a.year
month2 = a.month
day2 = a.day
hour2 = a.hour
minute2 = a.minute
second2 = a.second


print('current time: ',a)


#Total tweet counts over the course of requested timeframe
totalcounter = 0

#Used for max_id
identity = ""

while True:
    print('')
    keyword = input('Enter Your Search Keyword:')
    if (len(keyword) < 1): break

#Represents the 2min timeframe
    minutetime = 2

#Describes the number of timeframes you wish to retrieve
    for  x in range(0, 3):


#max_id is used to set an ending marker of each timeframe
        url = twurl.augment(TWITTER_URL,
                            {'q': keyword, 'count': '100', 'max_id': identity, 'result_type': 'recent'})
        connection = urllib.request.urlopen(url, context=ctx)
        data = connection.read().decode()
        jsondata = json.loads(data)

#Count for each timeframe
        counter = 0



        for id in jsondata['statuses']:
            a = id['created_at']
            b = list(a)
            del b[0:4]

#Parsing 'created_at' into data that can be used as datetime
            year = b[22:26]
            month = b[0:3]
            day = b[4:6]
            hour = b[7:9]
            minute = b[10:12]
            second = b[13:15]

            yr = int(''.join(year))
            mo = 0
            d = int(''.join(day))
            hr = int(''.join(hour))
            minute1 = int(''.join(minute))
            sec = int(''.join(second))

            if ''.join(month) == "Jan":
                mo = 1
            elif ''.join(month) == "Feb":
                mo = 2
            elif ''.join(month) == "Mar":
                mo = 3
            elif ''.join(month) == "Apr":
                mo = 4
            elif ''.join(month) == "May":
                mo = 5
            elif ''.join(month) == "Jun":
                mo = 6
            elif ''.join(month) == "Jul":
                mo = 7
            elif ''.join(month) == "Aug":
                mo = 8
            elif ''.join(month) == "Sep":
                mo = 9
            elif ''.join(month) == "Oct":
                mo = 10
            elif ''.join(month) == "Nov":
                mo = 11
            else:
                mo = 12





            delta = datetime.timedelta(minutes = minutetime)
            time1 = datetime.datetime(year = year2, month = month2, day = day2, hour = hour2, minute = minute2, second = second2)\
                    - delta
            time2 = datetime.datetime(year = yr, month = mo, day = d, hour = hr, minute = minute1, second = sec)
            print(time2,time1)



#This loop breaks only when 'created_at' is dated minutetime before the current time
            if time2 < time1:
                print("count for ",minutetime - 2, " - ", minutetime, "min before the current time: ", counter)


#Update identity so it is set correctly for the loop of next timeframe
                identity = id['id_str']
                break

            else:
                totalcounter += 1
                counter += 1
        minutetime += 2
    print("total count: ", totalcounter)

    print('---------------------------------------------------------')
    headers = dict(connection.getheaders())
    # print headers
    print('Remaining', headers['x-rate-limit-remaining'])
