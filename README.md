# VPN-Traffic-Classification
This project utilizes a convolutional neural network (CNN) to differentiate different types of VPN traffic based on the payload data of network packets.

### Dataset
The VPN portion of data from [VPN-nonVPN dataset (ISCXVPN2016)](https://www.unb.ca/cic/datasets/vpn.html) was used for training the model.
>Gerard Drapper Gil, Arash Habibi Lashkari, Mohammad Mamun, Ali A. Ghorbani, "Characterization of Encrypted and VPN Traffic Using Time-Related Features", In Proceedings of the 2nd International Conference on Information Systems Security and Privacy(ICISSP 2016) , pages 407-414, Rome, Italy.

### Data Extraction
To extract the payload data from the packets, [nPrint](https://github.com/nprint/nprint) is required to be installed.
