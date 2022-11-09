import requests, json

z = 0

with open('P2PKH_True.txt', 'r') as p:
    for addr in p.readlines():
        addr = addr.strip('\n')
        addr.strip()
        atomic_url = f'http://35.237.92.187/api/v2/address/{addr}?page=1'
        req = requests.get(atomic_url + addr).json()
        txs = dict(req)['txids']
        for i in range(len(txs)):
            txid = dict(req)['txids'][i]
            z += 1
            print(f"{z} {addr} {txid}")
            with open('txidP2pkh,txt', 'a') as t:
                t.write(f"{txid}\n")
                t.close()
