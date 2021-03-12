# Hotel Concierge Chatbot
Term Project for CMPE252 Team 10

## Install Instructions
- We recommend using Python 3.8.
- Install Rasa with `pip3 install rasa`

## Running Chatbot
- In one terminal, navigate to the project directory and run `rasa run actions` to start the custom actions server.
- In another terminal, navigate to the project directory and run `rasa shell -m models/hotel-bot-model.tar.gz`
    - This is where you will talk to the bot.
- If you need to re-train the bot you can run `rasa train --fixed-model-name hotel-bot-model`

## Conversation Tips
- Say hello
- Ask for the time
- Check to see if you have any mail (Use name Anthony, Adam, or Marshall for best results).
    - The bot will randomly decide if you have mail or not and give the corresponding response.
- Ask for directions to...
    - an airport (supports SFO or SJC, and should be able to tell you that it doesn't know the way to OAK)
    - the restroom
    - the freeway
- Make a reservation to stay at the hotel (Use name Anthony, Adam, or Marshall for best results)
    - There is no data verification when making/cancelling a reservation. The bot will just assume whatever you say makes sense. Be nice :)
    - Cancel a reservation at the hotel (Use name Anthony, Adam, or Marshall for best results)
    - Try to pick a fight (and then surrender to the mighty machine)
- Food recommendations
    - Say you're hungry then answer questions about cuisine and atmosphere
    - american, italian, japanese, chinese, mexican cuisines and popular foods in those categories should be recognized
    - family/casual, bar, fancy atmospheres
- Activity recommendations
    - Say you're bored then answer questions on activity type and cost
    - outdoors (hiking, camping), relax (beach, spa), cultural (museum, art gallery)
    - cheap/free or expensive/cost
- Parking
    - Choose between self parking and valet

## Known Issues
- The forms using a rule (e.g. restaurant form) show a warning about a slot type never sent during training.
    - This is an issue with RASA that hasn't been fixed.  https://forum.rasa.com/t/getting-warning-in-rasa-core-processor/2892