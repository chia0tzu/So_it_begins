import pprint

message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris faucibus, nisi a aliquam blandit, nibh ante convallis augue, ut euismod orci sapien non diam. Morbi ut ex orci. Aenean porttitor neque at odio bibendum laoreet. Aliquam tristique dui justo. Curabitur a enim lacus. Ut accumsan interdum risus ac ornare. Maecenas tempor a nunc vel rutrum.'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
