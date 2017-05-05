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

# Set the weights of the restrictions.
# WEIGHTS = [0.25, 0.25, 0.25, 0.25]
WEIGHTS = [0.1, 0.3, 0.3, 0.3]
HopLimit_WEIGHT = WEIGHTS[0]
MustEdge_WEIGHT = WEIGHTS[1]
ForbidEdge_WEIGHT = WEIGHTS[2]
MustNode_WEIGHT = WEIGHTS[3]

# Specify the detailed settings of the restrictions.
# Hop Limit
HopLimit_NUM = 9
# MustEdge
MustEdge_NUM = 2
MustEdge = [['s2', 's4'], ['s13', 's14']]
# ForbidEdge
ForbidEdge_NUM = 1
ForbidEdge = [['s11', 's12']]
# MustNode
MustNode_NUM = 2
MustNode = ['s7', 's12']

# If don't care about the limitation of Hop
Hop_MAX = 12

# Input the network topology.
LINK_BANDWIDTH = 1000   # Link bandwidth (unit: Kbit/s).
switches = ['s100', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14', 's15', 's16', 's200']
hosts = ['h100', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10', 'h11', 'h12', 'h13', 'h14', 'h15', 'h16', 'h200']
switch_links = [
['s100', 's1', 3], ['s100', 's2', 1], ['s100', 's3', 1],
['s1', 's2', 1], ['s1', 's4', 1], ['s1', 's9', 4],
['s2', 's3', 1], ['s2', 's4', 2], ['s2', 's5', 1],
['s3', 's5', 2], ['s3', 's6', 2], ['s3', 's7', 1],
['s4', 's5', 1], ['s4', 's9', 1],
['s5', 's6', 1], ['s5', 's9', 3], ['s5', 's10', 1], ['s5', 's12', 3],
['s6', 's7', 1], ['s6', 's8', 2], ['s6', 's12', 2],['s6', 's13', 4], ['s6', 's14', 3],
['s7', 's8', 1],
['s8', 's14', 1], ['s8', 's15', 3],
['s9', 's10', 1], ['s9', 's11', 1],
['s10', 's11', 1], ['s10', 's12', 2],
['s11', 's12', 1], ['s11', 's16', 1],
['s12', 's13', 2], ['s12', 's16', 1],
['s13', 's14', 1], ['s13', 's15', 2], ['s13', 's16', 2], ['s13', 's200', 1],
['s14', 's15', 1],
 ['s15', 's200', 1],
['s16', 's200', 1],
]
host_links = [
['s100', 'h100'], ['s1', 'h1'], ['s2', 'h2'], ['s3', 'h3'], ['s4', 'h4'], ['s5', 'h5'],
['s6', 'h6'], ['s7', 'h7'], ['s8', 'h8'], ['s9', 'h9'], ['s10', 'h10'], ['s11', 'h11'],
['s12', 'h12'], ['s13', 'h13'], ['s14', 'h14'], ['s15', 'h15'], ['s16', 'h16'], ['s200', 'h200']
]

# Common setting of the SDN controller.
DISCOVERY_PERIOD = 10   # For discovering network topology.
initiation_delay = 10   # For the controller to discover the network topology.
TOSHOW = True	   # For showing network monitoring statistics in the terminal or not.
enable_Flow_Entry_L4Port = False   # For including L4 port in the installing flow entries or not.
