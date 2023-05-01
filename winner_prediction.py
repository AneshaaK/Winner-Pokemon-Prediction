# winner_prediction.py

import sys
import torch
model_save_name = 'pokemon_rf.pt'
path = f"C:\\Users\\ak\\Downloads\\{model_save_name}" 
torch.save(rf_model, path)
model = torch.load(path)

player1 = sys.argv[0]
player2 = sys.argv[1]

def torcall(first_poke,second_poke):
    x = pokemon.loc[pokemon["Name"]==first_poke].values[:, 2:][0]
    y = pokemon.loc[pokemon["Name"]==second_poke].values[:, 2:][0]
    z = np.concatenate((x,y))
    z = np.asarray(z)
    X_sample = z[:].astype(int)
    dt_pred = dt_model.predict([X_sample])
    if dt_pred ==0:
        print(f"Predicted winner : {first_poke}")
    else:
        print(f"Predicted winner : {second_poke}")

torcall(player1,player2)