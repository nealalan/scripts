import hashlib
print('Guaranteed:\n{}\n'.format(', '.join(sorted(hashlib.algorithms_guaranteed))))


print('Available:\n{}'.format(', '.join(sorted(hashlib.algorithms_available))))

#Guaranteed:
#blake2b, blake2s, md5, sha1, sha224, sha256, sha384, sha3_224, sha3_256, sha3_384, sha3_512, sha512, shake_128, shake_256

#Available:
#DSA, DSA-SHA, MD4, MD5, MDC2, RIPEMD160, SHA, SHA1, SHA224, SHA256, SHA384, SHA512, blake2b, blake2s, dsaEncryption, dsaWithSHA, ecdsa-with-SHA1, md4, md5, mdc2, ripemd160, sha, sha1, sha224, sha256, sha384, sha3_224, sha3_256, sha3_384, sha3_512, sha512, shake_128, shake_256, whirlpool
