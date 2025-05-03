
from datetime import datetime
def timeConversion(s):
    t = datetime.strptime(s, '%I:%M:%S%p')
    print(t.strftime('%H:%M:%S'))
if __name__ == '__main__':

    s = input()

