from time import *

class Date:
    def updateTime(self):
        self.time = localtime(time())

    def getsecond(self):
        self.updateTime()
        return self.time.tm_sec
    
    def getminute(self):
        self.updateTime()
        return self.time.tm_min
    
    def gethour(self):
        self.updateTime()
        return self.time.tm_hour
    
    def getday(self):
        self.updateTime()
        return self.time.tm_mday
    
    def getmonth(self):
        self.updateTime()
        return self.time.tm_mon
    
    def getyear(self):
        self.updateTime()
        return self.time.tm_year
    
    def getDayOfYear(self):
        self.updateTime()
        return self.time.tm_yday
    
    def getDayOfWeek(self):
        self.updateTime()
        return self.time.tm_wday

    def getFormatTime(self,format="%Y-%m-%d %H:%M:%S"):
        self.updateTime()
        return strftime(format,self.time)
    
if __name__ == "__main__":
    d = Date()
    print(d.getFormatTime())
