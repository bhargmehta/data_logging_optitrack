#!/usr/bin/env python3

# The natnet client library to be used can be found here https://github.com/mje-nz/python_natnet
import natnet

import csv
from csv import writer
import time

#################### Test Connection to Motive API ##################
## If you want to test connection between your PC and the Motive API, uncomment the next three lines and comment the rest of the code below the "Test Connection to Motive API" section
 
client = natnet.Client.connect()
client.set_callback(lambda rigid_bodies, markers, timing: print(f"markers: {markers}, {rigid_bodies}"))
client.spin()

## If the connection is not established, line 14 will throw [Errno 101] Network is unreachable. Go to your PC's Setting -> Network -> Wired, and check if the PC is connected to desired network.
## If the connection is established but no data is coming through, Go the Motive application -> View -> Data Streaming Pane, and ensure that labelled_markers, unlabelled_markers and rigid_bodies are toggled on 
################ End of the Test Connection Section##################



def main():
	try:
		natnet_client = NatNetClient()
		natnet_client.connect()
		natnet_client.run()

	except natnet.DiscoveryError as e:
		print('Error:', e)

if __name__ == "__main__":
	main()
