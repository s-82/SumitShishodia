

weeks={
    'mon':'monday',
    'tue':'tuesday',
    'wed':'wednesday',
    'thu':'thursday',
    'fri':'friday',
    'sat':'saturaday',
    'sun':'sunday'
    }

def index(day):
    if(day.isdigit()):
        keylist=list(weeks.keys())
        return((weeks[keylist[int(day)-1]]))
    else:
        return((weeks[day]))
print(index('1'))