import random

class Environment:
    def __init__(self):
        self.locationCondition = {
            'A': random.randint(0, 1),
            'B': random.randint(0, 1),
            'C': random.randint(0, 1),
            'D': random.randint(0,1)
        }

class VacuumAgent:
    def __init__(self, env):
        print("Initial State:", env.locationCondition)

        battery = 100
        score = 0
        vacuumLocation = random.randint(0, 3)

       
        visited = set()  

        if vacuumLocation == 0:
            print("Vacuum is randomly placed at Location A")

            if env.locationCondition['A'] == 1:
                visited.add('A')
                print("Location A is Dirty")
                env.locationCondition['A'] = 0
                score += 1
                battery -= 15    
                print("Location A has been Cleaned")

            if env.locationCondition['B'] == 1:
                visited.add('B')
                print("Location B is Dirty")
                print("Moving to Location B...")
                battery -= 25   
                score -= 1
                env.locationCondition['B'] = 0
                score += 1
                print("Location B has been Cleaned")

            if env.locationCondition['C'] ==1:
                visited.add('C')
                print("Location C is dirty")
                print("Moving to Location C")
                battery -= 25
                score -= 1
                env.locationCondition['C']=0
                score+=1
                print("Location C has been Cleaned")

            if env.locationCondition['D']==1:
                visited.add('D')
                print("Location D is dirty")
                print("Moving to location D")
                battery -=25
                score-=1
                env.locationCondition['D']=0
                score+=1
                print("Location D has been Cleaned")

        elif vacuumLocation==1:
            print("Vacuum is randomly placed at Location B")

            if env.locationCondition['B'] == 1:
                visited.add('B')
                print("Location B is Dirty")
                env.locationCondition['B'] = 0
                score += 1
                battery -= 15    
                print("Location B has been Cleaned")

            if env.locationCondition['A'] == 1:
                visited.add('A')
                print("Location A is Dirty")
                print("Moving to Location A...")
                battery -= 25   
                score -= 1
                env.locationCondition['A'] = 0
                score += 1
                print("Location A has been Cleaned")

            if env.locationCondition['C'] ==1:
                visited.add('C')
                print("Location C is dirty")
                print("Moving to Location C")
                battery -= 25
                score -= 1
                env.locationCondition['C']=0
                score+=1
                print("Location C has been Cleaned")

            if env.locationCondition['D']==1:
                visited.add('D')
                print("Location D is dirty")
                print("Moving to location D")
                battery-= 25
                score-=1
                env.locationCondition['D']=0
                score+=1
                print("Location D has been Cleaned")

        elif vacuumLocation==2: 
            print("Vaccum is randomy placed at Location C")

            if env.locationCondition['C'] == 1:
                visited.add('C')
                print("Location C is Dirty")
                env.locationCondition['C'] = 0
                score += 1
                battery -= 15    
                print("Location C has been Cleaned")

            if env.locationCondition['B'] == 1:
                visited.add('B')
                print("Location B is Dirty")
                print("Moving to Location B...")
                battery -= 25
                score -=1
                env.locationCondition['B'] = 0
                score += 1    
                print("Location B has been Cleaned")

            if env.locationCondition['A'] == 1:
                visited.add('A')
                print("Location A is Dirty")
                print("Moving to Location A...")
                battery -= 25   
                score -= 1
                env.locationCondition['A'] = 0
                score += 1
                print("Location A has been Cleaned")

            if env.locationCondition['D']==1:
                visited.add('D')
                print("Location D is dirty")
                print("Moving to location D")
                battery-=25
                score-=1
                env.locationCondition['D']=0
                score+=1
                print("Location D has been Cleaned")

        else:
            print("Vaccum is randomy placed at Location D")
            
            if env.locationCondition['D'] ==1:
                visited.add('D')
                print("location D is Dirty")
                env.locationCondition['D'] =0
                score += 1
                battery -= 15
                print("Location D is Cleaned")

            if env.locationCondition["C"]==1:
                visited.add('C')
                print("loaction C is Dirty")
                print("Moving to location C")
                battery -= 25
                score -= 1
                env.locationCondition['C'] =0               
                score += 1
                print("Loaction C is Cleaned")

            if env.locationCondition['B'] ==1:
                visited.add('B')
                print("Location B is dirty")
                print("Moving to Loaction B")
                battery -= 25
                score -= 1
                env.locationCondition['B'] =0
                score += 1
                print("loaction B is cleaned")

            if env.locationCondition['A']==1:
                visited.add('A')
                print("location A is dirty")
                print("Moving to location A")
                score -= 1
                battery -= 25
                env.locationCondition['A'] =0
                score += 1
                print("Location A is cleaned")

        #Battery check (auto charging)
        if battery <= 20:
            print("Battery low! Going to charging station...")
            battery = 100
            print("Battery fully recharged!")

        #Goal check
        if all(v == 0 for v in env.locationCondition.values()):
            print("All locations are clean!")

        total_rooms = len(env.locationCondition)
        clean_rooms = list(env.locationCondition.values()).count(0)
        efficiency = clean_rooms / total_rooms

        print("\nPerformance Metrics:")
        print("Total Rooms:", total_rooms)
        print("Clean Rooms:", clean_rooms)
        print("Efficiency:", round(efficiency * 100, 2), "%")


        print("Visited Locations:", visited)  #show memory
        print("Final State:", env.locationCondition)
        print("Score:", score)
        print("Battery Percentage",battery,"%")


env = Environment()
agent = VacuumAgent(env)
