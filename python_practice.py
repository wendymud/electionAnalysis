# print("Hello World")

#counties = ["Arapahoe", "Denver", "Jefferson"]
#if counties[1] == 'Denver':
    #print(counties[1])

#if "El Paso" in counties:
#    print("El Paso is in the list of counties.")
#else: 
#    print("El Paso is not in the list of counties.")

#for county  in counties:
#    print(county)

#numbers = [0, 1, 2, 3, 4]
#for num in numbers:
#    print(num)

#for num in range(5):
#    print(num)

#for i in range(len(counties)):
#    print(counties[i])


#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county, voters in counties_dict.items():
 #   print(county + " county has " + str(voters) + " registered voters.")
#    print(f"{county} county has {voters} registered voters.")


#for county in counties_dict:
#    print(county)

#for county in counties_dict.keys():
#    print(county)

#for voters in counties_dict.values():
#    print(voters)

#for county in counties_dict:
#   print(counties_dict[county])

#for key, value in counties_dict.items():
#    print(key, value)

#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                {"county":"Denver", "registered_voters": 463353},
#                {"county":"Jefferson", "registered_voters": 432438}]

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
        print(f"{county} county has {voters} registered voters.")


#    print(county_dict['county'])

#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#percentage_votes = (my_votes / total_votes) * 100
#print(f"I received {my_votes/total_votes * 100}% of the total votes.")

#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
#    f"You received {candidate_votes:,} number of votes. "
#    f"The total number of votes in the election was {total_votes:,}. "
#    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
    

#print(message_to_candidate)