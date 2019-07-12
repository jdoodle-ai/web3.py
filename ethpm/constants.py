REGISTRY_URI_SCHEME = "erc1319"

PACKAGE_NAME_REGEX = "[a-zA-Z][-_a-zA-Z0-9]{0,255}"

DEFAULT_IPFS_BACKEND = "ethpm.backends.ipfs.InfuraIPFSBackend"

IPFS_GATEWAY_PREFIX = "https://ipfs.io/ipfs/"

# TODO Deprecate in favor of a better scheme for fetching registry URIs.
# Please play nice and don't use this key for any shenanigans, thanks!
ETHPM_INFURA_API_KEY = "4f1a358967c7474aae6f8f4a7698aefc"

INFURA_GATEWAY_MULTIADDR = "/dns4/ipfs.infura.io/tcp/5001/https/"

GITHUB_API_AUTHORITY = "api.github.com"

SUPPORTED_CHAIN_IDS = {
    1: "mainnet",
    3: "ropsten",
    4: "rinkeby",
    5: "goerli",
    42: "kovan",
}
