import cryptography.hazmat.primitives.ciphers.aead
import base64


#"vault:v1:42hL9BxGxug9InQeI2gh3eI3kRTTHHS+2Zfz+Z5HS2toZToROgRT"
#"vault:v1:FwpB14s1mYFmlhTxCNlg4s0Dprhf/oqI2yALaeAoYwE+Yt6AWrZvR4bZnt44S9V/"
#vault:v1:N3QrAHiRY3ziOA6LeM3ZESEevfw3DrxEnn2lfp9WzeE90geL+v8Ur+G4/2Uj4mukX4uPDPdEO6UX7fdLr/58fV48n3x4BlsqtsLD234pDZRbLiLv0hLaPDkJ1DN4dIulpbtEeHWu3DQlOYRefIEJGGOOfrXEss++xBgiwG7pjyepKU4j+Vho5r9KnrNSWZ5YOe63R75ieWm9mMG69puvuPE+049bygivarPZV4SaG8M7bb+3kdbY8jExpgT8uw/B9CxSgNaeObFAq5z0yF3OEMc/xO4XsbWuzxv2G4n7hmxTZst5vlDOwyGQiXxbEZxaGQNws9Z2dVQZxkr9VHVXyQ==
encoded = "FwpB14s1mYFmlhTxCNlg4s0Dprhf/oqI2yALaeAoYwE+Yt6AWrZvR4bZnt44S9V/"

iv_and_ciphertext = base64.b64decode(encoded)
iv_bytes = iv_and_ciphertext[:12]
ciphertext_bytes = iv_and_ciphertext[12:]

key_bytes = base64.b64decode("5/xYXHtPSa6IyOvEDbE264zbEs/SHSu+X+MoACxs800=")




aead_cipher = cryptography.hazmat.primitives.ciphers.aead.AESGCM(key_bytes)
result = aead_cipher.decrypt(iv_bytes, ciphertext_bytes, None)
print(result)



