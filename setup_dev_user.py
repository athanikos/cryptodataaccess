import keyring
from keyrings.alt.file import PlaintextKeyring
keyring.set_keyring(PlaintextKeyring())
keyring.set_keyring(PlaintextKeyring())
keyring.set_password('cryptodataaccess', 'LOCAL_MONGO_USERNAME', 'admin')
keyring.set_password('cryptodataaccess', 'admin', 'admin')
keyring.set_password('cryptodataaccess', 'CENTRAL_MONGO_USERNAME', 'admin')
keyring.set_password('cryptodataaccess', 'admin', 'admin')
