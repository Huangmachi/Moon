## Moon

Moon is an implementation of the Algorithm Challenge of ZTE Corporation with Software-Defined Networking. All the routing paths are calculated and installed by the Ryu controller.

The detailed information of the modules is shown below:

* 'setting.py' contains the settings, including the network topology, the detailed settings of the restrictions, and the setting of the SDN controller, and it can be modified by the user at will;

* 'topo.py' is for creating the network environment according to 'setting.py' module;

* 'network_awareness.py' is for collecting network information;

* 'SDN.py' is the main module of Moon.

We make use of networkx's data structure to store topology. Meanwhile, we also utilize networkx's built-in algorithm to calculate shortest paths.


### Prerequisites

The following softwares should have been installed in your machine.
* Mininet: git clone git://github.com/mininet/mininet; mininet/util/install.sh -a
* Ryu: git clone git://github.com/osrg/ryu.git; cd ryu; pip install .
* Networkx: pip install networkx


### Download

Download files into Ryu directory, for instance, 'ryu/ryu/app/Moon' is OK.


### Start

Firstly, start up the network. An example is shown below:

    $ sudo python ryu/ryu/app/Moon/topo.py

And then, open a new ternimal, and run the application. An example is shown below:

    $ cd ryu
    $ ryu-manager --observe-links ryu/app/Moon/SDN.py

NOTE: After these, we should wait for the network to complete the initiation for several seconds, because LLDP needs some time to discovery the network topology. We can't operate the network until "[GET NETWORK TOPOLOGY]" and "[BEST PATHS ARE READY]" are printed in the terminal of the Ryu controller, otherwise some errors will occur.

After that, test the correctness of Moon:

    mininet> h100 ping -c1 h200
    mininet> pingall

And you can see the paths' information shown in the terminal of the Ryu controller.


### Authors

Brought to you by Huang MaChi (Chongqing University of Posts and Telecommunications, Chongqing, China.) and Wang Xiong (Chongqing University of Posts and Telecommunications, Chongqing, China.).

If you have any question, email me at huangmachi@foxmail.com. Don't forget to STAR this repository!

Enjoy it!
