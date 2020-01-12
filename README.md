# score-counter
Small Python script and helper files that allow you to increment and reset win/loss scores for OBS streamers  

packages used (you may have to pip install in order for the script to work):  
  tinydb - pip install tinydb  

Arguments:\
w - increments the win counter  
l - increments the loss counter  
r - resets the counter back to 0 wins and 0 losses  

example: "python score_adjust.pyw w"  
*Argument is required in order to run script

# Instructions
Stream Deck Instructions (Advanced Launcher Required):
  1. Add advanced launcher key to stream deck
  2. Set file/app to score_adjust.pyw
  3. Set argument to the arguments above
  
Hotkey Instructions:
  1. Set to run score_adjust.pyw scipt with arguments listed above
  
OBS Instructions:
  1. Create Text component and point to winloss.txt in order to display score

Formatting:  
  If you want to customize the text that appears in winloss.txt, simply edit the format.txt file with your custom message.  
  Special data:  
    %wins - total number of wins  
    %losses - total number of losses  
    %total - total number of games  
  
  example: Out of %total games, there are %wins wins and %losses losses!