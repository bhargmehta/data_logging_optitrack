#!/usr/bin/env python3

# The natnet client library to be used can be found here https://github.com/mje-nz/python_natnet
import natnet

import csv
from csv import writer
import time

#################### Test Connection to Motive API ##################
## If you want to test connection between your PC and the Motive API, uncomment the next three lines and comment the rest of the code below the "Test Connection to Motive API" section
 
#client = natnet.Client.connect()
#client.set_callback(lambda rigid_bodies, markers, timing: print(f"markers: {markers}, {rigid_bodies}"))
#client.spin()

## If the connection is not established, line 14 will throw [Errno 101] Network is unreachable. Go to your PC's Setting -> Network -> Wired, and check if the PC is connected to desired network.
## If the connection is established but no data is coming through, Go the Motive application -> View -> Data Streaming Pane, and ensure that labelled_markers, unlabelled_markers and rigid_bodies are toggled on 
################ End of the Test Connection Section##################

class NatNetClient():
	def __init__(self):
		#self.data = dict()
		named_tuple = time.localtime()
		time_string = time.strftime("%m_%d_%Y_%H_%M_%S", named_tuple)
		self.markers_filename = "data_markers_" + time_string + ".csv"
		self.rigid_bodies_filename = "data_rigid_bodies_" + time_string + ".csv"
		
		with open(self.markers_filename, mode='w') as markers_csv_file:
			self.markers_fieldnames = ['timestamp', 'model_id', 'marker_id', 'pos_x', 'pos_y', 'pos_z', 'size', 
							'residual', 'has_model', 'model_solved', 'occluded', 'point_cloud_solved', 'unlabelled']
			writer = csv.DictWriter(markers_csv_file, fieldnames=self.markers_fieldnames)
			writer.writeheader()
			
		with open(self.rigid_bodies_filename, mode='w') as rigid_bodies_csv_file:
			self.rigid_bodies_fieldnames = ['timestamp', 'id_', 'pos_x', 'pos_y', 'pos_z', 'orient_x', 'orient_y', 'orient_z', 'orient_w', 'mean_error']
			writer = csv.DictWriter(rigid_bodies_csv_file, fieldnames=self.rigid_bodies_fieldnames)
			writer.writeheader()

	def connect(self):
		self.client = natnet.Client.connect()
		return self.client

	def run(self):
		self.client.set_callback(self.callback)
		self.client.spin()

	def callback(self, rigid_bodies, markers, timing):
		# Data type of incoming rigid_bodies and markers -> list
		
		# Each data point in the markers list is an object of class -> natnet.protocol.MocapFrameMessage.LabelledMarker
		# Each data point in the rigid_bodies is an object of class -> natnet.protocol.MocapFrameMessage.RigidBody
		
		# More details about the definition of MocapFrameMessage can be found on -> https://python-natnet.readthedocs.io/en/latest/reference/natnet.protocol.MocapFrameMessage.html
		
		#print(f"No. of markers detected: {len(markers)}, no. of rigid bodies: {len(rigid_bodies)}")
		#print(f"Marker -> model_id: {markers[0].model_id}, marker_id: {markers[0].marker_id}, position: {markers[0].position}, size: {markers[0].size}, residual: {markers[0].residual}, 				has_model: {markers[0].has_model}, model_solved: {markers[0].model_solved}, occluded: {markers[0].occluded}, point_cloud_solved: {markers[0].point_cloud_solved}, 				unlabelled: {markers[0].unlabelled}")
		#print(f"Rigid_body -> rigid_body_id: {rigid_bodies[0].id_}, position: {rigid_bodies[0].position}, orientation: {rigid_bodies[0].orientation}, mean_error: {rigid_bodies[0].mean_error}, 				is tracking valid:{rigid_bodies[0].tracking_valid}")
		
		
		with open(self.markers_filename, mode='a+', newline='') as markers_csv_file:
			csv_writer = writer(markers_csv_file)
			for marker in markers:
				csv_writer.writerow([timing.timestamp, marker.model_id, marker.marker_id, marker.position[0], marker.position[1], marker.position[2], marker.size, 
							marker.residual, marker.has_model, marker.model_solved, marker.occluded, marker.point_cloud_solved, marker.unlabelled])
		
		with open(self.rigid_bodies_filename, mode='a+', newline='') as rigid_bodies_csv_file:
			csv_writer = writer(rigid_bodies_csv_file)
			for rigid_body in rigid_bodies:
				csv_writer.writerow([timing.timestamp, rigid_body.id_, rigid_body.position[0], rigid_body.position[1], rigid_body.position[2], 
							rigid_body.orientation[0], rigid_body.orientation[1], rigid_body.orientation[2], rigid_body.orientation[3], rigid_body.mean_error])
			

def main():
	try:
		natnet_client = NatNetClient()
		natnet_client.connect()
		natnet_client.run()

	except natnet.DiscoveryError as e:
		print('Error:', e)

if __name__ == "__main__":
	main()
