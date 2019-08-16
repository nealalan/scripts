import hmac

digest_maker = hmac.new(
    b'secret-shared-key',
    b'',
    'sha256'
)

with open('lorem.txt', 'rb') as f:
    while True:
        block = f.read(1024)
        print("BLK:", block)
        if not block:
            break
        digest_maker.update(block)

digest = digest_maker.hexdigest()
print("DIGEST: ", digest)

print()


import base64, hashlib

with open('lorem.txt', 'rb') as f:
    body = f.read()
    print("BODY: ", body)

    hash = hmac.new(
        b'secret-shared-key',
        body,
        hashlib.sha3_256,
    )

digest = hash.digest()
print("Digest: ", base64.encodestring(digest))
