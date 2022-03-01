# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[],own_history=[],play_order=[{"RP":0,"RR":0,"RS":0,"PR":0,"PP":0,"PS":0,"SP":0,"SR":0,"SS":0}]):
  if prev_play != '':
    opponent_history.append(prev_play)
  else:
    del opponent_history[:]
    del own_history[:]
    del play_order[:]
    play_order.append({
                "RR": 0,
                "RP": 0,
                "RS": 0,
                "PR": 0,
                "PP": 0,
                "PS": 0,
                "SR": 0,
                "SP": 0,
                "SS": 0,
            })
  basic_response = {'P': 'S', 'R': 'P', 'S': 'R'}
  next_response = {'S': 'P', 'P': 'R', 'R': 'S'}
  if len(own_history) < 1:
    guess = "R"
    own_history.append(guess)
  else:
    guess = own_history[-1]
  last_two = ''.join(own_history[-2:])
  if len(last_two) == 2:
    play_order[0][last_two] += 1
  potential_plays = [guess+'R',guess+'P',guess+'S']
  sub_order = { k:play_order[0][k] for k in potential_plays if k in play_order[0]}
  prediction = max(sub_order, key=sub_order.get)[-1:]
  my_response = next_response[prediction]
  if len(opponent_history) > 4:
    last_five = ''.join(opponent_history[-5:])
    verify_mutta = ''.join(["R", "R", "P", "P", "S"]*2)
    index = verify_mutta.find(last_five)
    if index > -1:
      response = basic_response[verify_mutta[index + 5]]
      own_history.append(response)
      return response
    if len(opponent_history) > 2:
        guess = opponent_history[-2]
  if len(opponent_history) > 4:
    verify_rico = [basic_response[x] for x in own_history[-5:-1]]
    if verify_rico == opponent_history[-4:]:
      response = next_response[own_history[-1]]
      own_history.append(response)
      return response
  if len(opponent_history) > 3:
    if len(opponent_history) < 10:
      run = len(opponent_history)
    else:
      run = 10
    moonlight = True
    for x in range(run-2):
      x = x + 1
      last_ten = own_history[-10-x:-x]
      most_frequent = max(set(last_ten), key=last_ten.count)
      if opponent_history[-x] != basic_response[most_frequent]:
        moonlight = False
    if moonlight:
      last_own_ten = own_history[-10:]
      most_frequent = max(set(last_own_ten), key=last_own_ten.count)
      response = next_response[most_frequent]
      own_history.append(response)
      return response
  own_history.append(my_response)
  return my_response