violator_songs = [
    ["World in My Eyes", 4.86],
    ["Sweetest Perfection", 4.43],
    ["Personal Jesus", 4.56],
    ["Halo", 4.9],
    ["Waiting for the Night", 6.07],
    ["Enjoy the Silence", 4.20],
    ["Policy of Truth", 4.76],
    ["Blue Dress", 4.29],
    ["Clean", 5.83]
]

name_song = []
playing_time = 0
num_song = int(input("Сколько песен выбрать? "))

for i in range(1, num_song + 1):
    song = input(f"Название {i} песни ")
    if any(song in _ for _ in violator_songs):
        name_song.append(song)
    else:
        print("Такой песни нету(")

for k in violator_songs:
    if k[0] in name_song:
        playing_time += k[1]

print("Общее время звучания песен ", round(playing_time, 2))

# зачет!
