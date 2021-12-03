love_quartz = {
    "name": "Love Quartz",
    "description": "Love quartz or also known as Rose quartz is known as the crystal of unconditional love. It's said to boost feelings of self-love and foster loving relationships with others. It is a stone that you should always have near to you because of its universal love properties, and its ability to heal so many different things \n",
    "value": 0
}
cLear_crystals = {
    "name": "Clear Crystal",
    "description": "Clear crystal is considered a “master healer.” It's said to amplify energy by absorbing, storing, releasing, and regulating it. It's also said to aid concentration and memory. Physically, clear crystals are claimed to help stimulate the immune system and balance out your entire body. \n",
    "value": 0
}
adventurine = {
    "name": "Adventurine",
    "description": " Adventurine crystal is a comforter, a harmonizer, and a super handy stone to have stashed on the self for all those who want to bring a little more luck into their world. Whether you need a little flush of added wealth, an extra abundance of love and friendship, or just a bit more growth, Aventurine wants one thing – for you to succeed in all your amazing endeavours, no matter how big or small they may be. \n",
    "value": 0
}
amethyst = {
    "name": "Amethyst",
    "description": "Amethyst crystal is said to be incredibly protective, healing, and purifying. It's claimed it can help rid the mind of negative thoughts and bring forth humility, sincerity, and spiritual wisdom. \n",
    "value": 0
}
carnelian = {
    "name": "Carnelian",
    "description": "Carnelian crystal is known for being a stone of courage, endurance, energy, leadership, and motivation. Carnelians have inspired and protected us throughout history thanks to their bright, rich coloring. \n",
    "value": 0
}

print('Welcome to the crystal quiz where you ca find out what crystal best fits you!')
cq_1 = input('Do you want to take this quiz to see what crystal best suits you? \n')
if cq_1 == "yes":
    print("yayy")
else:
    print("Boo you suck!")

cq_2 = input('What have you been feeling lately? \na) in love/happy, \nb) sick , \nc) stressed, \nd) anxious, \ne) anger \n')    #[5, 5, 5, 5, 5
if cq_2 == "a":
    love_quartz["value"] += 5
elif cq_2 == "b":
    cLear_crystals["value"] += 5
elif cq_2 == "c":
    adventurine["value"] += 5
elif cq_5 == "d":
    amethyst["value"] += 5
elif cq_6 == "e":
    carnelian["value"] += 5
else:
    print("Sorry, I don't understand that answer.")


cq_3 = input('What do you wish to improve? \na) yourself , \nb) health , \nc) creativity, \nd) mind , \ne) motivation \n')      #[5, 5, 5, 5, 5])
if cq_3 == "a":
    love_quartz["value"] += 5
elif cq_3 == "b":
    cLear_crystals["value"] += 5
elif cq_3 == "c":
    adventurine["value"] += 5
elif cq_3 == "d":
    amethyst["value"] += 5
elif cq_3 == "e":
    carnelian["value"] += 5
else:
    print("Sorry, I don't understand that answer.")

cq_4 = input('Would you rather: \na) spend time with your loved ones , \nb) spend time for yourself , \nc) runaway , \nd find peace , \ne) control your emotions \n') #[5, 5, 5, 5, 5])
if cq_4 == "a":
    love_quartz["value"] += 5
elif cq_4 == "b":
    cLear_crystals["value"] += 5
elif cq_4 == "c":
    adventurine["value"] += 5
elif cq_4 == "d":
    amethyst["value"] += 5
elif cq_4 == "e":
    carnelian["value"] += 5
else:
    print("Sorry, I don't understand that answer.")

cq_5 = input('How do you see yourself in 10 years? \na) Living a good life with your dream job, \nb) healthy and living your best life, \nc living a stressed free life where you have enough money to support yourself and loved ones, \nd) living a creative lifestyle (art, films, pottery, codeing, potographer etc), \ne) living in the cabins to be part of nature and calm setting. \n') #[5, 5, 5, 5, 5])
if cq_5 == "a":
    love_quartz["value"] += 5
elif cq_5 == "b":
    cLear_crystals["value"] += 5
elif cq_5 == "c":
    adventurine["value"] += 5
elif cq_5 == "d":
    amethyst["value"] += 5
elif cq_5 == "e":
    carnelian["value"] += 5
else:
    print("Sorry, I don't understand that answer.")

cq_6 = input('How do you see youself now? \na) happy, \nb in love, \nc disgusted with yourself, \nd wanting to make changes, \ne undistructive')
if cq_6 == "a":
    love_quartz["value"] += 5
elif cq_6 == "b":
    cLear_crystals["value"] += 5
elif cq_6 == "c":
    adventurine["value"] += 5
elif cq_6 == "d":
    amethyst["value"] += 5
elif cq_6 == "e":
    carnelian["value"] += 5
else:
    print("Sorry, I don't understand that answer.")

crystals_list = [love_quartz, cLear_crystals, adventurine, amethyst, carnelian]
for crystal in crystals_list:
    winning_crystal = crystal
    if winning_crystal > 0:
        crystals_list.append
print("Your crystal is the " + winning_crystal["name"] + winning_crystal["description"])
