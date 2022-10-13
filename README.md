# Data Logging for Optitrack MoCap system
The script stores data corresponding to labelled and unlabelled markers in one csv file and pose of rigid bodies in another csv file. 

### Requirements
* Python - 3.6
* pip3
* git
* [python_natnet](https://github.com/mje-nz/python_natnet) _(follow installation steps mentioned in the python\_natnet repository)_

### Checking for connection 
In terminal, run:
```
cd ~/<file_path>/data_logging_optitrack
python test_natnet_client_datareader.py
```
If the dependencies are correctly installed and the connection (IP address on Motive2.0) is correctly configured, the script will run without any errors or else will show _"Error"_

### Running script and logging data
In terminal, run:
```
cd ~/<file_path>/data_logging_optitrack
python natnet_client_datareader.py
```

If all the dependencies are correctly installed, the script would keep running and generate two different CSV files with names _"data\_markers\_%m\_%d\_%Y\_%H\_%M\_%S.csv"_ and _"data\_rigid\_bodies\_%m\_%d\_%Y\_%H\_%M\_%S.csv"_.


