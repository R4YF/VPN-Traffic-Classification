# VPN-Traffic-Classification

This project utilizes a convolutional neural network (CNN) to differentiate different types of VPN traffic based on the payload data of network packets.

### Dataset

The VPN portion of data from [VPN-nonVPN dataset (ISCXVPN2016)](https://www.unb.ca/cic/datasets/vpn.html) was used for training the model.

>Gerard Drapper Gil, Arash Habibi Lashkari, Mohammad Mamun, Ali A. Ghorbani, "Characterization of Encrypted and VPN Traffic Using Time-Related Features", In Proceedings of the 2nd International Conference on Information Systems Security and Privacy(ICISSP 2016) , pages 407-414, Rome, Italy.

### Data Extraction

To extract the payload data from the packets, [nPrint](https://nprint.github.io/nprint/) is required to be installed either on Debian or MacOS.

>Holland, Jordan and Schmitt, Paul and Feamster, Nick and Mittal, Prateek, "nPrint: A Standard Data Representation for Network Traffic Analysis", arXiv:2008.02695

* Output packet payload bits from the Pcap file into a CSV file.
```
$ nprint -P filename.pcap -p 1024 -W filename.csv
```

* Generate images from CSV files for training, use `--i` to specify the starting index of images.
```
$ python csv2img.py --r filename.csv --w ./image_path/ --i 0
```

### Training

