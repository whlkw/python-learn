
import time,asyncio,random
async def mygen(alist):
    print('The parameter is {}' % alist)
    while len(alist) > 0:
        c = random.randint(0, len(alist)-1)
        print(alist.pop(c))
        await asyncio.sleep(1)
        print ('Has get one value')

def generate_nums():
    num = 0
    while True:
        yield num
        num = num + 1


nums = generate_nums()

for x in nums:
    print(x)

    if x > 9:
        break

async def main():
  strlist = ['this', 'is', 'a', 'corrutine', 'end']
  intlist=[1,2,5,6,7]
  c1=mygen(strlist)
  c2=mygen(intlist)
  await asyncio.wait([c1, c2]);

if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        #asyncio.ensure_future(c1)
        #asyncio.ensure_future(c2)

        loop.run_until_complete(main())

        print('All fib finished.')
        loop.close()
