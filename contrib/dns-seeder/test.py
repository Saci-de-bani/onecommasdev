import socket

seeders = [
    'bwkseed.mempool.pw',
    'bwkseed1.onecommascrypto.com',
    'bwkseed2.onecommascrypto.com',
    'bwkseed3.onecommascrypto.com',
    'bwkseed4.onecommascrypto.com',
    'bwkseed5.onecommascrypto.com',
    'bwkseed1.onecommascrypto.site',
    'bwkseed2.onecommascrypto.site',
    'bwkseed3.onecommascrypto.site',
    'bwkseed4.onecommascrypto.site',
    'bwkseed5.onecommascrypto.site'
]

for seeder in seeders:
    try:
        ais = socket.getaddrinfo(seeder, 0)
    except socket.gaierror:
        ais = []
    
    # Prevent duplicates, need to update to check
    # for ports, can have multiple nodes on 1 ip.
    addrs = []
    for a in ais:
        addr = a[4][0]
        if addrs.count(addr) == 0:
            addrs.append(addr)
    
    print(seeder + ' = ' + str(len(addrs)))
