import random, time
find = random.randint(0, 999999999)
x = 0
s = int(input('how many seconds to run: '))
start = time.time()
while (time.time() - start) < s:
    guess = random.randint(0, 999999)
    x += 1
    #print('guessed {}'.format(guess))
    if guess == find:
        print('match: {}'.format(guess))
        break
end = time.time()
second = str(x)
use = second[::-1]
i = 0
new = ''
for y in use:
    if (i % 3) == 0:
        new = new + ','
    i += 1
    new = new + y
second = new[::-1][:-1]
print('tried {} times in {}s'.format(second, str(end - start)[:5]))
