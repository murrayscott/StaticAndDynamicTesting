### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # Operator should be == for comparison and not = which is used to assign a value.
      return True
    else # Colon missing from the end of the line
      return False
   

  dif highest_card(self, card1 card2): # The function should be defined by def and not dif and theres a comma missing between card1 and card2 
  if card1.value > card2.value: # This and the next 3  lines should be indented
    return card # This line should return card1 and not card
  else:
    return card2
  


def cards_total(self, cards): # This and the next 3  lines should be indented (but not the return line...it should be outside the for loop)
  total # This line shouldd read total = 0 to assign the variable total an initial value.
  for card in cards:
    total += card.value
    return "You have a total of" + total # The value total should have a str in front of it to concatenate it with the preceding string  i.e. str(total)
# There should also be a space at the end of the "You have a total of" line so that it reads properly before concatenating the total.
```
