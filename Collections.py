from collections import deque

deque_list = deque()
for i in range(5):
    deque_list.append(i)


print(deque(reversed(deque_list)))

deque_list.extend([5,6,7])
print(deque_list)


from collections import OrderedDict
d = OrderedDict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 500

for k, v in d.items():
    print(k, v)

for k, v in OrderedDict(sorted(d.items(), key=lambda t: t[1])).items():
    print(k,v)

from collections import defaultdict
d = defaultdict(object) # Default dictionary를 생성
d = defaultdict(lambda: 0) # Default 값을 0으로 설정한다.
print(d["first"])
from collections import OrderedDict
from collections import defaultdict
text = """Code navigation is available!
Navigate your code with ease. Click on function and method calls to jump to their definitions or references in the same repository. Learn more""".lower().split()
print(text)

word_count = defaultdict(object)
word_count = defaultdict(lambda: 0)
for word in text:
    word_count[word] += 1
print(word_count)
for i, v in OrderedDict(sorted(
    word_count.items(), key=lambda t: t[1], reverse=True)).items():
    print(i, v)


from collections import Counter
c = Counter() # 빈객체 생성..
c = Counter(text)
print(c)

from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(11, y=22)
print(p[0] + p[1])