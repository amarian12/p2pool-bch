from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['bitcoinbch']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = '08c1a579b023ef62'.decode('hex')
PREFIX = '90aa4e3ade1ff9f2'.decode('hex')
P2P_PORT = 5984
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = True
WORKER_PORT = 5964
BOOTSTRAP_ADDRS = 'p2pool.e-pool.net:5984 '.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: None if 100000 <= v else 'Bitcoin version too old. Upgrade to 0.11.2 or newer!' # not a bug. BIP65 support is ensured by SOFTFORKS_REQUIRED
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65', 'csv'])
MINIMUM_PROTOCOL_VERSION = 1600
