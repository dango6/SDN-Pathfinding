#!/usr/bin/python3

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel

def simple_topo():
    net = Mininet(controller=RemoteController)
    net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)
    
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    s1 = net.addSwitch('s1')

    net.addLink(h1, s1)
    net.addLink(h2, s1)

    net.start()
    h1.cmd('ping -c 4 h2')
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    simple_topo()


# source venv/bin/activate
# deactivate