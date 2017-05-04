# Copyright (C) 2017 Huang MaChi at Chongqing University
# of Posts and Telecommunications, Chongqing, China.
# Copyright (C) 2017 Wang Xiong at Chongqing University
# of Posts and Telecommunications, Chongqing, China.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, Intf, TCLink
from mininet.topo import Topo

import logging
import os

import setting


class Topology(Topo):
	"""
		Class of network topology.
	"""
	SwitchList = []
	HostList = []

	def __init__(self):
		Topo.__init__(self)

	def createNodes(self):
		"""
			Create switches and hosts.
		"""
		for sw in setting.switches:
			self.SwitchList.append(self.addSwitch(sw))

		for host in setting.hosts:
			self.HostList.append(self.addHost(host))

	def createLinks(self, bw=1):
		"""
			Add network links.
		"""
		for link in setting.switch_links:
			self.addLink(link[0], link[1], bw=bw, max_queue_size=100)

		for link in setting.host_links:
			self.addLink(link[0], link[1], bw=bw, max_queue_size=100)

	def set_ovs_protocol(self):
		"""
			Set the OpenFlow version for switches.
		"""
		for sw in setting.switches:
			cmd = "sudo ovs-vsctl set bridge %s protocols=OpenFlow13" % sw
			os.system(cmd)


def createTopo():
	"""
		Create the network topology and start up.
	"""
	# Create Topo.
	topo = Topology()
	topo.createNodes()
	topo.createLinks(bw=(setting.LINK_BANDWIDTH/float(1000)))

	# Start Mininet.
	net = Mininet(topo=topo, link=TCLink, controller=RemoteController, autoSetMacs=True)
	net.start()

	# Set OpenvSwitch's protocol as OpenFlow13.
	topo.set_ovs_protocol()

	CLI(net)
	net.stop()


if __name__ == '__main__':
	setLogLevel('info')
	if os.getuid() != 0:
		logging.debug("You are NOT root!")
	elif os.getuid() == 0:
		createTopo()
