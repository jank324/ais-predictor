# Gets trip lines (arff)
# Take out values I care about (learned on)
# while current position isn't destination
#     Determine agent for current position
#     Send values to agent
#     Receive new values at sector leave from agent (e.g. leave latitude, leave longitude, time to leave)
#     Add sector travel time to entire travel time
# return entire travel time and route

def broker():
    return 324