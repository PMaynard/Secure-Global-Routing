#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class Router( Node ):
    "A Node with IP forwarding."

    def config( self, **params ):
        super( Router, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( Router, self ).terminate()

class NetworkTopo( Topo ):
    "Three swtiches, a router, and three hosts."

    def build( self, **_opts ):
        # Define a router!
        router = self.addNode( 'r0', cls=Router, ip='192.168.1.1/24' )

        # Add three switches
        s1, s2, s3 = [ self.addSwitch( s ) for s in ( 's1', 's2', 's3' ) ]

        # Connect each switch to the router
        self.addLink( s1, router, intfName2='r0-eth1', params2={ 'ip' : '192.168.1.1/24' } )
        self.addLink( s2, router, intfName2='r0-eth2', params2={ 'ip' : '172.16.0.1/12' } )
        self.addLink( s3, router, intfName2='r0-eth3', params2={ 'ip' : '10.0.0.1/8' } )

        # Define three hosts
        h1 = self.addHost( 'h1', ip='192.168.1.100/24', defaultRoute='via 192.168.1.1' )
        h2 = self.addHost( 'h2', ip='172.16.0.100/12',  defaultRoute='via 172.16.0.1' )
        h3 = self.addHost( 'h3', ip='10.0.0.100/8',     defaultRoute='via 10.0.0.1' )

        # Connect each host to its own switch
        for h, s in [ (h1, s1), (h2, s2), (h3, s3) ]:
            self.addLink( h, s )

def run():
    "Test linux router"
    topo = NetworkTopo()
    net = Mininet( topo=topo )  # controller is used by s1-s3
    net.start()
    info( '*** Routing Table on Router:\n' )
    info( net[ 'r0' ].cmd( 'route' ) )
    
    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    run()
