import keyring
from keyrings.alt.file import PlaintextKeyring
keyring.set_keyring(PlaintextKeyring())
keyring.set_keyring(PlaintextKeyring())
keyring.set_password('cryptomodel', 'LOCAL_MONGO_USERNAME', 'admin')
keyring.set_password('cryptomodel', 'admin', 'admin')
keyring.set_password('cryptomodel', 'CENTRAL_MONGO_USERNAME', 'admin')
keyring.set_password('cryptomodel', 'admin', 'admin')