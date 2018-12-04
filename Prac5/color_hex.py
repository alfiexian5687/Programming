COLORS = {"AliceBlue": "#f0f8ff","AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
         "black": "#000000", "blue1": "	#0000ff", "brown": "#a52a2a", "burlywood": "#deb887",
         "CadetBlue": "	#5f9ea0", "coral": "#ff7f50", "cyan1": "#00ffff" }

color = input("Enter a color: ")
while color != "":
    if color in COLORS:
        print("Color code for", color, "is", COLORS[color])
    else:
        print("Invalid color")
    color = input("Enter a color: ")