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
    return((weeks[day]))


print(index('mon'))