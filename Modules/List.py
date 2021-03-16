

#create a list of states
def create_a_list_of_states_and_only_return_those_starting_with_m():
    states = ["Alabama","Alaska","Arizona","Arkansas", "Caifornia","Colorado", "Conneticut", "Deleware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinos", "Indiana", "Iowa", "Kansas", "Kentucky","Louisiana", "Main", "Maryland", "Massachusettes", "Michigan", "Minnisota", "Mississippi", "Missori", "Montana", "Nebraska", "Nevada", "New Hapshire", "New Jersey", "New Mexico", "New York", "North Carolina","North Dakota", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennesse", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    print(len(states))
    for state in states:
        if state[0].lower == "m":
            print(state)


