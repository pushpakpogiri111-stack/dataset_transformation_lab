import pandas as pd
import numpy as np

df = pd.read_csv("day02_usage.csv")
chat = df["Chat"].to_numpy()
video = df["Video"].to_numpy()
study = df["Study"].to_numpy()
games = df["Games"].to_numpy()

print(len(chat))
print(np.sum(chat))
print(round(np.mean(chat), 1))

print(np.sum(video))
print(round(np.mean(video), 1))

print(np.sum(study))
print(round(np.mean(study), 1))

print(np.sum(games))
print(round(np.mean(games),1))

difference = study - games

best = np.argmax(difference)
worst = np.argmin(difference)

print(best + 1)
print(worst + 1)

apps = ["Chat", "Video", "Study", "Games"]

for i in range(30):
    values = np.array([chat[i], video[i], study[i], games[i]])
    winner = np.argmax(values)
    print(i + 1, apps[winner])

total = chat+games+video+study

chat_share = chat/total*100
games_share = games/total*100
video_share = video/total*100
study_share = study/total*100

print(chat_share,games_share,video_share,study_share)