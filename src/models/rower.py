class Rower:
    def __init__(self, rower_index):
        self.rower_index = rower_index
        self.seat = self.getSeat(rower_index)

    def getSeat(self, rower_index):
        seats = {
            0 : "Stroke",
            1 : "Stroke 2",
            2 : "Bow 2",
            3 : "Bow"
        }

        return seats[rower_index]