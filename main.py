import json
import random
import tkinter as tk


# TODO:
# class specific option
# no stock option
# no funny option maybe
# GUI STUFF
class Generator:

    # GUI STUFF
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("TF2LG")  # title

        self.title_label = tk.Label(self.root, text="TF2 Loadout Generator", font=("Arial", 17))
        self.title_label.pack(padx=5)
        self.title_label2 = tk.Label(self.root, text="version 1.1", font=("Arial", 10))
        self.title_label2.pack()

        # .menubar = tk.Menu(self.root)

        # self.help_menu = tk.Menu(self.menubar, tearoff=0)
        # self.help_menu.add_command(label="Info")
        # self.help_menu.add_command(label="Disclaimer")

        # self.menubar.add_cascade(menu=self.help_menu, label="Help")
        # self.root.config(menu=self.menubar)

        self.box_frame0 = tk.Frame(self.root, borderwidth=2, relief="solid")  # labels and frames surrounding
        self.box_frame0.pack(padx=10, pady=5, fill='x')
        self.label_0 = tk.Label(self.box_frame0, text=":D", font=("Arial", 12, "bold"))  # Class name
        self.label_0.pack()
        self.box_frame1 = tk.Frame(self.root, borderwidth=2, relief="solid")  # primary
        self.box_frame1.pack(padx=10, pady=5, fill='x')
        self.label_1 = tk.Label(self.box_frame1, text=":]", font="Arial")
        self.label_1.pack()
        self.box_frame2 = tk.Frame(self.root, borderwidth=2, relief="solid")  # secondary
        self.box_frame2.pack(padx=10, pady=5, fill='x')
        self.label_2 = tk.Label(self.box_frame2, text=":v", font="Arial")
        self.label_2.pack()
        self.box_frame3 = tk.Frame(self.root, borderwidth=2, relief="solid")  # melee
        self.box_frame3.pack(padx=10, pady=5, fill='x')
        self.label_3 = tk.Label(self.box_frame3, text="(:", font="Arial")
        self.label_3.pack()
        self.box_frame4 = tk.Frame(self.root, borderwidth=2, relief="solid")  # 4th slot
        self.box_frame4.pack(padx=10, pady=5, fill='x')
        self.label_4 = tk.Label(self.box_frame4, text=":)", font="Arial")
        self.label_4.pack()

        self.generate_button = tk.Button(self.root, text="Random",
                                         command=lambda: self.pick_loadout(random.randint(1, 9)))
        self.generate_button.pack(pady=5)
        self.scout_button = tk.Button(self.root, text="Scout", font=("Arial", 8), command=lambda: self.pick_loadout(1))
        self.scout_button.pack(side=tk.LEFT, pady=5, padx=(5, 0))
        self.soldier_button = tk.Button(self.root, text="Soldier", font=("Arial", 8),
                                        command=lambda: self.pick_loadout(2))
        self.soldier_button.pack(side=tk.LEFT)
        self.soldier_button = tk.Button(self.root, text="Pyro", font=("Arial", 8), command=lambda: self.pick_loadout(3))
        self.soldier_button.pack(side=tk.LEFT)
        self.soldier_button = tk.Button(self.root, text="Demo", font=("Arial", 8), command=lambda: self.pick_loadout(4))
        self.soldier_button.pack(side=tk.LEFT)
        self.soldier_button = tk.Button(self.root, text="Heavy", font=("Arial", 8), command=lambda: self.pick_loadout(5))
        self.soldier_button.pack(side=tk.LEFT)
        self.soldier_button = tk.Button(self.root, text="Engie", font=("Arial", 8), command=lambda: self.pick_loadout(6))
        self.soldier_button.pack(side=tk.LEFT)
        self.soldier_button = tk.Button(self.root, text="Medic", font=("Arial", 8), command=lambda: self.pick_loadout(7))
        self.soldier_button.pack(side=tk.LEFT)
        self.soldier_button = tk.Button(self.root, text="Sniper", font=("Arial", 8),
                                        command=lambda: self.pick_loadout(8))
        self.soldier_button.pack(side=tk.LEFT)
        self.soldier_button = tk.Button(self.root, text="Spy", font=("Arial", 8), command=lambda: self.pick_loadout(9))
        self.soldier_button.pack(side=tk.LEFT, padx=(0, 5))
        # self.stock_button = tk.Button(self.root, text="No stock")
        # self.stock_button.pack(side=tk.RIGHT, anchor=tk.CENTER)
        # self.no_stock_button = tk.Button(self.root, text="No stock"

        # todo : add more buttons pack properly

        self.root.mainloop()

    def pick_loadout(self, chosen_class):
        class_name = {1: "Scout", 2: "Soldier", 3: "Pyro", 4: "Demoman", 5: "Heavy",
                      6: "Engineer", 7: "Medic", 8: "Sniper", 9: "Spy"}.get(chosen_class, 0)
        file_name = class_name + ".json"

        with open(file_name, 'r') as json_file:
            data = json.load(json_file)

        weapon_slots = {slot: [weapon for weapon in data['weapons'] if weapon['slot'] == slot] for slot in range(1, 5)}

        if chosen_class == 9:
            slot_count = 4  # because spy has 4 slots
        else:
            slot_count = 3
        weapon_list = []

        for i in range(slot_count):  # adds a random weapon (from slot 1, 2, 3, 4 into weapon_list
            i = i + 1
            current_weapon = random.choice(weapon_slots[i])
            weapon_list.append(current_weapon['name'])
        self.label_0.config(text=f"{class_name}")
        self.label_1.config(text=f"{weapon_list[0]}")
        self.label_2.config(text=f"{weapon_list[1]}")
        self.label_3.config(text=f"{weapon_list[2]}")
        if chosen_class == 9:
            self.label_4.config(text=f"{weapon_list[3]}")
        else:
            self.label_4.config(text=":)")


Generator()

