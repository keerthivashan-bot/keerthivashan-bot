import random
point=1
class game:
  def __init__(self,head_of_snake,tail_of_snake,start_of_ladder,end_of_ladder):
    self.head_of_snake=head_of_snake
    self.tail_of_snake=tail_of_snake
    self.start_of_ladder=start_of_ladder
    self.end_of_ladder=end_of_ladder

  def start_game(self):
    #global point
    def player_two():
      position=random.randint(1,6)
      global point
      point=point+position
      if point == self.head_of_snake[0]:
        point=self.tail_of_snake[0]
      if point == self.head_of_snake[1]:
        point=self.tail_of_snake[1]
      if point==self.start_of_ladder[0]:
        point=self.end_of_ladder[0]
      if point==self.start_of_ladder[1]:
        point=self.end_of_ladder[1]
      print("player 2 point is {}".format(point))
      if(point>100):
        point-=position
      if(point==100):
        print("player2")
        exit(0)
      player_one();

    def player_one():
      position=random.randint(1,6)
      global point
      point=point+position
      if point == self.head_of_snake[0]:
        point=self.tail_of_snake[0]
      if point == self.head_of_snake[1]:
        point=self.tail_of_snake[1]
      if point==self.start_of_ladder[0]:
        point=self.end_of_ladder[0]
      if point==self.start_of_ladder[1]:
        point=self.end_of_ladder[1]
      print("player 1 point is {}".format(point))
      if(point>100):
        point-=position
      if(point==100):
        print("player1")
        exit(0)
      else:
        player_two();
      #flip_player()
    
  
       
   
    

    a=player_one();
    return a

head_of_snake=[5,35]
tail_of_snake=[1,3]
start_of_ladder=[7,41]
end_of_ladder=[81,53]
player1="keerthi"
player2="vashan"

obj=game(head_of_snake,tail_of_snake,start_of_ladder,end_of_ladder)
print(obj.start_game())
