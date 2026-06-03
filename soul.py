import time
spells = {
    "fireball": "hurl flames from the tips of your fingers. Ignites flesh on contact.",
    "Soul drain": "Shoot a necrotic bolt form your hands or eyes. The spell drains souls on contact",
    "shadow": "Vanish into darkness for 30 seconds."
}
ask = input("Wich spell do you seek master?")
if ask in spells:
    print(spells[ask])
else:
    print("You are not master vampire Leo, you will be cursed forever")
    time.sleep(5)
    exit()