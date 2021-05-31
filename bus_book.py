class bus:
  def __init__(self,conductor_name,total_seats,seats_booked,bus_no,driver_name):
    self.con_name=conductor_name
    self.total_seats=total_seats
    self.seats_booked=seats_booked
    self.bus_no=bus_no
    self.driver_name=driver_name
  
  def bus_deatails(self):
    return "the conductor name is {}".format(self.con_name)
    return "the total seats are {}".format(self.total_seats)
    return "the booked seats are {}".format(self.seats_booked)
    return "the bus number is {}".format(self.bus_no)
    return "the driver_name {}".format(self.driver_name)

  def is_seat_available(self):
    if self.total_seats-self.seats_booked>0:
      return "the availabe seats are {}".format(self.total_seats-self.seats_booked)
    else:
      return "the availabe seats are {}".format(self.total_seats-self.seats_booked)
  def book_seats(self,no_of_seats):
    if no_of_seats<=self.total_seats-self.seats_booked:
      self.seats_booked+=no_of_seats
      return "seats booked successflly"
    else:
      return "seats not available"


obj=bus("joe",25,12,"TN101","john")
print(obj.book_seats(1))
print(obj.book_seats(12))
print(obj.book_seats(21))
print(obj.is_seat_available())
