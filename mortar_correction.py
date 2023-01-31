##############################                 Mortar Fire Fix calculation                ##############################
#                                                                                                                      #
#                              This project uses the following formula: "M = 1000 * F / D"                             #
#              Functionality for a fire simplified command, with direct changes on mortar bipod mechanisms             #
# If overpassing mechanisms capacity (25 rounds on elevation mech/ 14 rounds on direction mech), insert new data-fire  #
#                                                                                                                      #
########################################################################################################################

###############################             LIMIT OF 120 CHARACTER BY LINE              ################################

import time

class Mortar:

    mec_dir = 15                              # Direction Mechanism - total of rounds
    mec_elev = 9                              # Elevation Mechanism - total of rounds

    def __init__(self):
        self.type_mortar = "Royal Ordnance"

    def calculate_direction(self):
        while True:                 
            try:
                self.distance = int(input("What DISTANCE of target? (METERS) \n"))
                self.front_variation = int(input("What variation of launch in DIRECTION? (METERS) \n"))
                break
            except ValueError:
                print('Enter valid data...')
        millesimal = (1000 * self.front_variation) / self.distance
        rounds = millesimal / self.mec_dir   # Millesimal result convertion to direction mechanism rounds
        if rounds > 13:
            self.change_datafire_dir()       # It alerts of a necessity to make new command with new datafire
        launch_trend = input("The shot landed RIGHT or LEFT? \n")

        try:
            if launch_trend.lower() == "right":
                print("\n CORRECTION ============> Turn 'LEFT' {:.1f} rounds. \n".format (rounds))  # Final Result
            elif launch_trend.lower() == "left":
                print("\n CORRECTION ============> Turn 'RIGHT' {:.1f} rounds. \n".format (rounds)) # Final Result
            self.verify()
        except:
            print("You did not enter a valid data, try again.")
            self.calculate_direction()
        return rounds

    def calculate_range(self):
        while True:
            try:
                self.distance = int(input("What DISTANCE of target? (METERS) \n"))
                self.front_variation = int(input("What variation of launch in RANGE? (METERS) \n"))
                break
            except ValueError:
                print('Enter valid data...')
        millesimal = (1000 * self.front_variation) / self.distance
        rounds = millesimal / self.mec_elev   # Millesimal result convertion, to range mechanism rounds
        if rounds > 24:
            self.change_datafire_range()      # It alerts of a necessity to make new command with new datafire
        launch_trend = input("The shot landed ABOVE or BELOW? \n")

        try:
            if launch_trend.lower() == "above":
                print("\n CORRECTION ============> 'SHORTEN' {:.1f} rounds. \n".format (rounds))  # Final Result
            elif launch_trend.lower() == "below":
                print("\n CORRECTION ============> 'LENGTHEN' {:.1f} rounds. \n".format (rounds)) # Final Result
            self.verify()
        except:
            print("You did not enter a valid data, try again.")
            self.calculate_range()
        return rounds

    def correct_launch(self):
        self.message = input("Do you want to correct the launch? (enter 'yes' to continue...) \n")
        try:
            if self.message.lower() in ['yes', 'y']:
                self.fix = input(
                    "For DIRECTION correction, enter 'DIR', or \nFor RANGE correction, enter 'RANGE': \n"
                )
                if self.fix.lower() in ["dir", "direction"]:
                    self.calculate_direction()
                elif self.fix.lower() == "range":
                    self.calculate_range()
                else:
                    print("You did not enter a valid data.")
                    self.verify()
            else: self.verify()   
        except:
            print('THERE WERE AN ERROR AT YOUR APLICATION AND WE ARE QUITTING! \n')
    
    def verify(self):
        self.verificacao = input("Do you want to keep on the aplication? \n")
        while self.verificacao.lower() in ['yes', 'y']:
            return self.correct_launch()
        for i in "\n FINISHING \n":
            time.sleep(0.2)
            print(i)
        print('You are out the aplication! \n')

    def change_datafire_dir(self):
        print("You need change your DIRECTION Datafire, because mechanism is over")
        self.verify()

    def change_datafire_range(self):
        print("You need change your RANGE Datafire, because mechanism is over")
        self.verify()

###############################             LIMIT OF 120 CHARACTER BY LINE              ################################

if __name__ == "__main__":
    Mortar().correct_launch()