import kotowaza as kw

class Cache:
    def __init__(self):
        self.cache = []
        self.length = int(kw.returnLength())
    
    def getLength(self) -> int:
        return self.length

    def getCacheLength(self) -> int:
        return int(len(self.cache))
    
    def getCache(self) -> list:
        return self.cache

    def addValue(self, val):
        self.cache.append(val)
    
    def resetCache(self):
        self.cache = []
