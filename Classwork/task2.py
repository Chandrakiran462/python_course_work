print("Photo Gallery: ")
photos = {
    1:"beach.png",
    2:"birthday.jpg",
    3:"trip.jpg",
    4:"sunset.png",
    5:"Dinner.jpg",
    6:"Biryani.jpg",
    7:"sky.png",
    8:"moon.png",
    9:"stars.jpg"
}
for i in photos:
    print(f"{i}. {photos[i]}")

selected=list(map(int,input("select photos to share(comma seperated): ").split(",")))
s = set(selected)
print("sharing the following photos: ")
for i in s:
    print(photos[i])
