# Write a class Train which has methods to book a ticket, get status
# and get fare information of train running under Railway Department.

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, come, go):
        print(f"Ticket is booked for train no: {self.trainNo} coming from {come} and going to {go}")

    def getstatus(self):
        print(f"Train no: {self.trainNo} is running according to time.")
        

    def fare(self, come, go):
        print(f"Ticket fare for train no: {self.trainNo} coming from {come} and going to {go} is 999")


t = Train(1234)
t.book("PointA","PointB")
t.getstatus()
t.fare("PointA","PointB")