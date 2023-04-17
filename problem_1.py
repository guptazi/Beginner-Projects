import pandas as pd # importing the pandas for handling data 
from datetime import datetime
import osmnx as ox
import networkx as nx

data = pd.read_csv(r"C:\Users\Shuhb.000\Desktop\IISc\bike_data_new.csv")




#--------------------------- SOLUTION FOR PROBLEM 1 -------------------------#
 # data stores the all the csv files in it
def remove_data(data):
    data['started_at'] = data['started_at'].apply(lambda x: datetime.strptime(x, '%d-%m-%Y %H:%M')) #this converts started_at and ended_at into date and time
    data['ended_at'] = data['ended_at'].apply(lambda x: datetime.strptime(x, '%d-%m-%Y %H:%M'))
    data['dur'] = (data['ended_at'] - data['started_at']).dt.total_seconds() / 60 # to find the difference between the started and ended duration time
    data = data.query('dur > 0') #this checks whether the duration has null values
    return data  # prints the data without zero duration

data=remove_data(data)
max_dur = data['dur'].max()
min_dur = data['dur'].min()

min_trips = data[data['dur'] == min_dur]
no_min_duration_trips = len(min_trips)

#............. this calculates the percentage of circular trips ...........#
data['circular'] = (data['start_lat'] == data['end_lat']) & (data['start_lng'] == data['end_lng']) # checks for the circular trip
no_circular_trips = data['circular'].sum()
total_trips = len(data)
per_circular_trips = no_circular_trips / total_trips * 100


print('The maximum duration of trip is', max_dur , 'minutes')
print('The minimum duration of trip is', min_dur, 'minutes')
print('The total number of trips corresponding to minimum duration is', no_min_duration_trips)
print("Percentage of total circular trips:", per_circular_trips, "%")

#................................... PROBLEM 1 ENDS ..................................................#











#------------------------------------- SOLUTION FOR PROBLEM 2 STARTS -------------------------------------------#

# org_data = pd.read_csv(r"C:\Users\Shuhb.000\Desktop\IISc\bike_data_new.csv")
# org_data['started_at'] = org_data['started_at'].apply(lambda x: datetime.strptime(x, '%d-%m-%Y %H:%M')) #this converts started_at and ended_at into date and time
# org_data['ended_at'] = org_data['ended_at'].apply(lambda x: datetime.strptime(x, '%d-%m-%Y %H:%M'))

#  # filtering the data between 6 AM and 6 PM

# org_data = org_data[(org_data['started_at'].dt.hour >= 6) & (org_data['started_at'].dt.hour < 18)]


# # modified refers to dataframe that will be shifted by one step because I have to check whether the succession bicycle location trips are same
#  # Here I'll create one new dataframes for checking succesion

# new_data = org_data[['trip_id', 'started_at', 'start_lat', 'start_lng']].shift(1).rename(columns={
#     'trip_id': 'trip_id_n',
#     'started_at': 'started_at_n',
#     'start_lat': 'start_lat_n',
#     'start_lng': 'start_lng_n'
# })

# tot_dataset = pd.concat([org_data, new_data], axis=1)

# # filtering out the data that has start time of new trip > start time of org data

# filtered = tot_dataset[tot_dataset['started_at_n'] >= tot_dataset['ended_at']]
# filtered['duration'] = (filtered['started_at_n'] - filtered['ended_at']).dt.total_seconds() / 60
# no_feasible_pairs = len(filtered)
# print(no_feasible_pairs)

#----------------PROBLEM 2 SOLUTION ENDS -----------------------------#










#------------------------SOLUTION FOR PROBLEM 3 STARTS ----------------------------#

# dataset= pd.read_csv(r"C:\Users\Shuhb.000\Desktop\IISc\bike_data_new.csv")

# mod_data = dataset.loc[(dataset['trip_id']<=100 )]
# print(mod_data)

# # to provide unique depot locations we have to choose unique start and unique end locations
# start_loc= mod_data['start_lat'].unique()
# end_loc = mod_data['end_lat'].unique()

# # now combining these set of start and end locations 
# set_loc = set(list(start_loc)+ list(end_loc))
# print(set_loc)

# # unique locations 
# unique = len(set_loc)

# print('The number of unique depots are ',unique)



# # DefinING the location of the AND size
# location = start_loc, end_loc
# dist = 10000

# # DownloaDING THE STREET NETWORK
# graph = ox.graph_from_address(location, dist=dist, network_type="drive")

# ox.plot_graph(graph)

# mod_data["node"] = mod_data["start_lat"].apply(lambda x: ox.distance.nearest_nodes(graph, x))
# print(mod_data)



# # to run the shortset path algorith

# # Define the source and target nodes
# source_node = mod_data.loc[0, "node"]
# target_node = mod_data.loc[1, "node"]

# # Get the length of the shortest path
# try:
#     shortest_path_length = nx.shortest_path_length(graph, source_node, target_node)
# except nx.NetworkXNoPath:
#     shortest_path_length = -1

# # Print the result
# print(f"The shortest path length between nodes {source_node} and {target_node} is {shortest_path_length}")


#--------------------------PROBLEM 3 SOLUTION ENDS ---------------------------------------#