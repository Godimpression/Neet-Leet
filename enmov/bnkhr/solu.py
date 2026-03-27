
class bankhours:
    def __init__(self,selected_hours):
        self.dict=set(selected_hours)
        
    def trade(self,trade_hours):
        starting=[]
        ending=[]
        
        for i in self.dict:
            start=int(i[0:2])
            end=int(i[6:8])
            starting.append(start)
            ending.append(end)
        
        min_start=min(starting)
        max_ending=max(ending)
        if int(trade_hours[0:2])>=min_start and int(trade_hours[6:8])<=max_ending:
            return "Success"
        return "Failure"
bofa=bankhours(["09:00-16:00","11:00-17:00","11:00-14:00"])
bofa.trade(("09:00-17:00"))
