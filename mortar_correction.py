##############################                              Mortar Fire Fix calculation                                   ##############################
##                                                                                                                                                    ##
##                                          This project uses the following formula: "M = 1000 * F / D"                                               ##
##                           Functionality for a fire simplified command, with direct changes on mortar bipod mechanisms                              ##
##   For variations overpass the mechanisms capacity (25 rounds on elevation mech and 14 rounds on direction mech), realize data-fire modification    ##
##                                                                                                                                                    ##
########################################################################################################################################################

import time

class Mortar:

    def __init__(self):
        self.type_mortar = "Royal Ordnance"

    def calculate_direction(self,front_variation,distance):                       # This Method calculates direction fix
        self.front_variation = front_variation                                    # front_variation is the direction variation launch
        self.distance = distance                                                  # Distance from Mortar to target
        while True:                 
            try:                                                                  # Exception to treat Value Error
                self.distance = int(input("What DISTANCE of target? (METERS) \n"))
                self.front_variation = int(input("What variation of fire in DIRECTION? (METERS) \n"))
                break
            except ValueError:
                print('Enter valid data...')

        millesimal = (1000 * self.front_variation) / self.distance                # Use of thousandth formula
        mec_dir = 15                                                              # Millesimal equivalence by round (15''' each round)
        rounds = millesimal / mec_dir                                             # Millesimal result convertion, to direction mechanism rounds
        if rounds > 13:                                                           # If round correction overpass the capacity of 14 rounds each side, other method is outcoming
            Mortar().change_datafire_dir()                                        # This Method alerts of a necessity to make a new fire command with new datafire

        sentido_launch = input("The shot landed RIGHT or LEFT? \n")
        if sentido_launch in ["RIGHT", "Right", "right"]:
            print("\n CORRECTION ====================================> Turn 'LEFT' {:.1f} rounds. \n".format (rounds))   # Final Result
        elif sentido_launch in ["LEFT", "Left", "left"]:
            print("\n CORRECTION ====================================> Turn 'RIGHT' {:.1f} rounds. \n".format (rounds))  # Final Result
        else: Mortar().exception_dir()
        Mortar().verify()
        return rounds

    def calculate_range(self,front_variation,distance):                           # This Method calculates range fix
        self.front_variation = front_variation                                    # front_variation is the direction variation launch
        self.distance = distance                                                  # Distance from Mortar to target
        while True:
            try:                                                                  # Exception to treat Value Error
                self.distance = int(input("What DISTANCE of target? (METERS) \n"))
                self.front_variation = int(input("What variation of fire in RANGE? (METERS) \n"))
                break
            except ValueError:
                print('Enter valid data...')

        millesimal = (1000 * self.front_variation) / self.distance                # Use of thousandth formula
        mec_elev = 9                                                              # Millesimal equivalence by round (9''' each round)
        rounds = millesimal / mec_elev                                            # Millesimal result convertion, to range mechanism rounds
        if rounds > 24:                                                           # If round correction overpass the capacity of 14 rounds each side, other method is outcoming
            Mortar().change_datafire_range()                                      # This Method alerts of a necessity to make a new fire command with new datafire

        sentido_launch = input("The shot landed ABOVE or BELOW? \n")
        if sentido_launch in ["ABOVE", "Above", "above"]:
            print("\n CORRECTION ====================================> 'SHORTEN' {:.1f} rounds.".format (rounds))    # Final Result
        elif sentido_launch in ["BELOW", "Below", "below"]:
            print("\n CORRECTION ====================================> 'LENGTHEN' {:.1f} rounds.".format (rounds))   # Final Result
        else: Mortar().exception_range()
        Mortar().verify()
        return rounds

    def correct_launch(self):                                                                     # This Method calls the specific correction according to the necessity 
        self.message = input("Do you want to correct the launch? (enter 'yes' to continue...) \n")
        try:
            if self.message in ["YES","Y","Yes",'yes','y']:
                self.fix = input("For correction in DIRECTION, enter 'DIR', or \nFor correction in RANGE, enter 'RANGE': \n")
                if self.fix in ["DIR", "Dir", "dir", "direction", "Direction", "DIRECTION"]:
                    Mortar().calculate_direction(0,0)
                elif self.fix in ["RANGE", "Range", "range"]:
                    Mortar().calculate_range(0,0)
                else:
                    print("You did not enter a valid data.")
                    Mortar().verify()
            else: Mortar().verify()   
        except:
            print('THERE WERE AN ERROR AT YOUR APLICATION AND WE ARE ENDING! \n')
    
    def verify(self):                                                                              # This Method verify at the final or after a error, if user wants to keep correcting
        self.verificacao = input("Do you want to keep on the aplication? \n")
        while self.verificacao in ["YES", "Y", "Yes", 'yes', 'y']:
            return Mortar().correct_launch()
        array = ['\n E','N','D','I','N','G \n']
        for i in array:
            time.sleep(0.2)
            print(i)
        print('You are out the aplication! \n')

    def exception_dir(self):                                                                       # This Method correct user typo at calculate_direction() Method
        print("You did not enter a valid data, try again.")
        Mortar().calculate_direction(0,0)

    def exception_range(self):                                                                     # This Method correct user typo at calculate_range() Method
        print("You did not enter a valid data, try again.")
        Mortar().calculate_range(0,0)

    def change_datafire_dir(self):                                                                 # This Method treat direction mechanism loss of capacity at calculate_direction() Method
        print("You need change your DIRECTION Datafire, because mechanism is over")
        Mortar().verify()

    def change_datafire_range(self):                                                               # This Method treat range mechanism loss of capacity at calculate_range() Method
        print("You need change your RANGE Datafire, because mechanism is over")
        Mortar().verify()


if __name__ == "__main__":
    Mortar().correct_launch()