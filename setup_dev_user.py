import keyring
from keyrings.alt.file import PlaintextKeyring
keyring.set_keyring(PlaintextKeyring())
keyring.set_keyring(PlaintextKeyring())
keyring.set_password('CryptoCalculatorService', 'LOCAL_MONGO_USERNAME', 'admin')
keyring.set_password('CryptoCalculatorService', 'admin', 'admin')
keyring.set_password('CryptoCalculatorService', 'CENTRAL_MONGO_USERNAME', 'admin')
keyring.set_password('CryptoCalculatorService', 'admin', 'admin')