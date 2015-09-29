
import urllib.request
import time
import datetime

class Quote(object):
  
  DATE_FMT = '%Y-%m-%d'
  TIME_FMT = '%H:%M:%S'
  
  def __init__(self):
    self.symbol = ''
    self.date,self.time,self.open_,self.high,self.low,self.close,self.volume = ([] for _ in range(7))

  def append(self,dt,open_,high,low,close,volume):
    self.date.append(dt.date())
    self.time.append(dt.time())
    self.open_.append(float(open_))
    self.high.append(float(high))
    self.low.append(float(low))
    self.close.append(float(close))
    self.volume.append(int(volume))
      
  def to_csv(self):
    return ''.join(["{0},{1},{2},{3:.2f},{4:.2f},{5:.2f},{6:.2f},{7}\n".format(self.symbol,
              self.date[bar].strftime('%Y-%m-%d'),self.time[bar].strftime('%H:%M:%S'),
              self.open_[bar],self.high[bar],self.low[bar],self.close[bar],self.volume[bar]) 
              for bar in range(len(self.close))])
    
  def write_csv(self,filename):
    with open(filename,'w') as f:
      f.write(self.to_csv())
        
  def read_csv(self,filename):
    self.symbol = ''
    self.date,self.time,self.open_,self.high,self.low,self.close,self.volume = ([] for _ in range(7))
    for line in open(filename,'r'):
      symbol,ds,ts,open_,high,low,close,volume = line.rstrip().split(',')
      self.symbol = symbol
      dt = datetime.datetime.strptime(ds+' '+ts,self.DATE_FMT+' '+self.TIME_FMT)
      self.append(dt,open_,high,low,close,volume)
    return True

  def __repr__(self):
    return self.to_csv()

   
class GoogleQuote(Quote):
  ''' Daily quotes from Google. Date format='yyyy-mm-dd' '''
  def __init__(self,symbol,start_date,end_date=datetime.date.today().isoformat()):
    super(GoogleQuote,self).__init__()
    self.symbol = symbol.upper()
    start = datetime.date(int(start_date[0:4]),int(start_date[5:7]),int(start_date[8:10]))
    end = datetime.date(int(end_date[0:4]),int(end_date[5:7]),int(end_date[8:10]))
    url_string = "http://www.google.com/finance/historical?q=NASDAQ%3AAAPL&hl=en&ei=8Wf3VaHmEsb1iwKOj7bADg&output=csv"
    response = urllib.request.urlopen(url_string)
    csv = response.read()
    csvstr = str(csv).strip("b'").strip("\\xef\\xbb\\xbf")
    lines = csvstr.split("\\n")
    f = open("data.csv","w")
    sum = 0
    for line in lines:
        op = line.strip('\n').split(',')
        if(not op[0]==''):
            t = float(op[1])
            #print (op[1])
            #sum = sum + int(op[1])
            #count +=1
            pass
        f.write(line+"\n")
    f.close()

if __name__ == '__main__':
  q = GoogleQuote('aapl','2011-01-01')              # download year to date Apple data
  print (q)                                           # print it out
  

''' 
This is a simplify version of the python code to read the Google page

'''

class GoogleQuote(object):
    def __init__(self):



    url_string = "http://www.google.com/finance/historical?q=NASDAQ%3AAAPL&hl=en&ei=8Wf3VaHmEsb1iwKOj7bADg&output=csv"
    response = urllib.request.urlopen(url_string)
    csv = response.read()
    csvstr = str(csv).strip("b'").strip("\\xef\\xbb\\xbf")
    lines = csvstr.split("\\n")
