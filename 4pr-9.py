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
      
    m=weeks[day.lower()]
    return(m)
print(index('1'))
print(index('MON')) 