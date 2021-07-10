import base64
import sys
import json
import zlib

# Read our URI from some source and strip off the prefix
uri = sys.stdin.readline().strip().strip('shc:/')

# Looks like we're reading a sequence of 2 digit decimal numbers, so I guess
# that's as fine a place to start as anywhere
bytestrs = []
for i in range(0, len(uri), 2):
    bytestrs.append(uri[i:i+2])

# Ok, so if I add 45 to everything, I get some `ey` shit, so that sounds like
# what we're gonna be doing
chars = ''.join([chr(int(b) + 45) for b in bytestrs]).strip()

# Yoooo, not only did we get an `ey`, this looks like a jwt, so let's do that
header, body, sig = chars.split('.')

header = json.loads(base64.urlsafe_b64decode(header + ('=' * (4 - (len(header) % 4)))))
print(json.dumps(header))

# Ok, so I guess there's a {zip:DEF} option in JWTs where you can deflate the
# body, so let's figure out how to do that now
body = base64.urlsafe_b64decode(body + ('=' * (4 - (len(body) % 4))))

# Where did that -15 come from?
# https://docs.python.org/3/library/zlib.html#zlib.decompress
body = json.loads(zlib.decompress(body, wbits=-15))

# pprint.pprint(body)
print(json.dumps(body))
