import random, time
find = random.randint(0, 999999)
x = 0
s = int(input('how many seconds to run: '))
start = time.time()
while (time.time() - start) < s:
    guess = random.randint(0, 999999)
    x += 1
    #print('guessed {}'.format(guess))
    if guess == find:
        print('match')
        break
second = str(x)
minute = str(x*60)
hour = str(x*3600)
day = str(x*86400)
week = str(x*604800)
month = str(x*18446400)
year = str(x*220752000)
def quick(inputted):
    inputted = inputted[::-1]
    i = 0
    new = ''
    for y in inputted:
        if (i % 3) == 0:
            new = new + ','
        i += 1
        new = new + y
    return new[::-1][:-1]
print('tried {} times in {}s\nwhich comes out to {} a minute, {} an hour,\n{} a day, {} a week,\n{} a month, and {} a year'.format(quick(second), s, quick(minute), quick(hour), quick(day), quick(week), quick(month), quick(year)))
