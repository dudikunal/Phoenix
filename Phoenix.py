from tkinter import *
import os


root = Tk()

root.geometry("650x270")

root.title("PHENOIX!!")

root.minsize(300, 100)

# root.maxsize(1534, 780)

def game():

    delta = 10
    play = Toplevel(root)

    def back():
        play.destroy()

    canv = Canvas(play, height=1000, width=500, bg="black")
    canv.pack(fill=BOTH)

    canv_t = canv.create_text(200, 50, text=" ", font="Helvetica 18 bold", anchor=NW, fill="white")



    our_text = "Welcome to Phoenix. It's an adventure game for you. Use your imagination and enjoy the game...\n\n\n\n\n" \
               "There was a sailor who went on a journey to explore the oceans and travel all around the world. \n" \
               "But recently have lost his way and is wondering in the ocean and hasn't eaten in last 3 days. \n" \
               "There are a lot of clouds in the sky. Seems like a storm coming. Here it's. Huge waves are swinging\n" \
               "the boat.It's getting really hard to handle the boat. They may not make it. These little Tsunami \n" \
               "like waves are slowly taking the sailor towards the  grave and he is resiting it with all he got.\n" \
               "He didn't realise but the boat was heading towards some rocks and the boat suddenly clashed with rocks\n" \
               "the sailor fell on the floor became unconcious...\n\n" \
               "Next day. The storm has passed and there is a clear sky. The sailor wakes up and recollect what has happened.\n " \
               "He is on an Island, his sailing boat is in the beach and is damaged by the rocks.\n " \
               "He might be able to repair it. All he can see is water around the island. He needs to get out of this island\n" \
               "but first need to drink and eat something. He has become weak since he hasn't had food for 4 days now.\n\n\n" \
               "I should go into the forest and find something to eat.The sailor now enters the jungle..\n" \

    delay = 1

    for x in range(len(our_text) + 1):
        s = our_text[:x]
        new_text = lambda s=s: canv.itemconfig(canv_t, text=s)
        canv.after(delay, new_text)
        delay += delta

    play.attributes('-fullscreen', True)


    Button(play, text="RETURN", command=back, height=3, width=10).place(x=750, y=800)
    Button(play, text="CONTINUE", command=ne, height=3, width=10).place(x=680, y=800)


def ne():
    game = Toplevel(root)
    game.config(bg="black")

    def b_a_c_k():
        game_2 = Toplevel(game)
        game_2.config(bg="black")
        game_2.attributes('-fullscreen', True)

        def last():
            game_3 = Toplevel(game_2)
            game_3.config(bg="black")
            game_3.attributes('-fullscreen', True)


            def riddle():
                game_4 = Toplevel(game_3)
                game_4.config(bg="black")
                game_4.attributes('-fullscreen', True)

                def qr_code():
                    choice = puzzle_answer.get()
                    if choice == "N6vP6bKs":
                        puzzle_answer.config(state="readonly")
                        cann_v = canvi.create_text(350, 550, text="HURRAY!!\n YOU HAVE COMPLETED THE FIRST LEVEL.", font="Helvetica 40 bold", anchor=NW, fill="red")

                    else:
                        cann_i = canvi.create_text(400, 600, text="Try Again..\nI Guess You Are Not That Smart", font="Helvetica 30 bold", anchor=NW, fill="white")


                dely = 1
                deta = 100

                canvi = Canvas(game_4, height=1000, width=500, bg="black")
                canvi.pack(fill=BOTH)

                canvi_txt = canvi.create_text(80, 100, text="THE BOOK SAYS!! ", font="Helvetica 30 bold", anchor=NW, fill="white")
                canvi_too = canvi.create_text(150, 200, text="", font="Helvetica 30 bold", anchor=NW, fill="white")

                puzzle = "I live around the corner but can make you travel around the world. \nI have a million stories to tell but can't speak. What am I?"

                for x in range(len(puzzle) + 1):
                    s = puzzle[:x]
                    new_text = lambda s=s: canvi.itemconfig(canvi_too, text=s)
                    canvi.after(dely, new_text)
                    dely += deta

                puzzle_ans = StringVar()

                puzzle_answer = Entry(game_4, width=40, textvariable=puzzle_ans, bg="white", font="Verdana 20 bold")
                puzzle_answer.place(relx=0.2, rely=0.5)

                b3 = Button(game_4, text="EXIT", command=close, font="Castellar 11 bold", borderwidth=6, relief=RIDGE)
                b3.place(relx=0.8, rely=0.9)

                Button(game_4, text="FINISH", command=qr_code, font="Verdana 11 bold", width=9, height=2).place(relx=0.8, rely=0.8)

            user_var_1_1 = StringVar()
            user_var_2_1 = StringVar()
            user_var_3_1 = StringVar()
            user_var_4_1 = StringVar()
            user_var_5_1 = StringVar()
            user_var_6_1 = StringVar()


            my_options_1 = "Let's find food!\ngo north\ngo south\ngo west\ngo east"
            labels_options = Label(game_3, text=my_options_1, bg="black", fg="white", font="Helvetica 15 bold")
            labels_options.place(relx=0.1, rely=0.1)

            user_entry_1 = Entry(game_3, textvariable=user_var_1_1, bg="white", font="Verdana 14 bold")
            user_entry_1.place(relx=0.1, rely=0.27)

            def check_choice_1_1():
                choice = user_entry_1.get()
                if choice.lower() == "go north":
                    user_entry_1.config(state="readonly")
                    label_1.config(text="More trees nothing to eat. Should look ahead.")
                    next_loop_1_1()
                elif choice.lower() in ["go east", "go south", "go west"]:
                    label_1.config(text="The forest is too dense can't go ahead.")

            label_1 = Label(game_3, font="Helvetica 14 bold", bg="black", fg="white", )
            label_1.place(relx=0.1, rely=0.32)

            def next_loop_1_1():
                global button
                my_options_2 = "So hungry! Where to head??\ngo north\ngo west\ngo south\ngo east"
                label_options_1 = Label(game_3, text=my_options_2, bg="black", fg="white", font="Helvetica 14 bold")
                label_options_1.place(relx=0.1, rely=0.38)
                user_entry_2_1 = Entry(game_3, textvariable=user_var_2_1, bg="white", font="Verdana 14 bold")
                user_entry_2_1.place(relx=0.1, rely=0.54)
                bun1.config(command=check_choice_2_1(user_entry_2_1))

            def check_choice_2_1(user_entry):
                choice = user_var_2_1.get()
                if choice.lower() == "go north":
                    user_entry.config(state="readonly")
                    label_2.config(
                        text="How far will I have to go in search of food?\nWait what's that? I can hear the\nbirds singing nearby...")
                    next_loop_2_1()
                elif choice.lower() in ["go north", "go south", "go west"]:
                    label_2.config(text="The forest is too dense can't go ahead.")

            def next_loop_2_1():
                global button
                my_options_3 = "From where is the sound coming?\nnorth\nwest\nsouth\neast"
                label_options_2 = Label(game_3, text=my_options_3, bg="black", fg="white", font="Helvetica 14 bold")
                label_options_2.place(relx=0.1, rely=0.7)
                user_entry_3_1 = Entry(game_3, textvariable=user_var_3_1, bg="white", font="Verdana 14 bold")
                user_entry_3_1.place(relx=0.1, rely=0.85)
                bun1.config(command=check_choice_3_1(user_entry_3_1))

            def check_choice_3_1(user_entry):
                choice = user_var_3_1.get()
                if choice.lower() == "east":
                    user_entry.config(state="readonly")
                    label_3.config(text="Man I got good hearing")
                    label_4.config(
                        text="Oh from where the sound is coming.\nI can see a nest up there.\nI may find some eggs there.")
                    next_loop_3_1()
                elif choice.lower() in ["north", "south", "west"]:
                    label_3.config(
                        text="Nope that's not it maybe I should clean\nmy ears haven't done that in a long time")

            def next_loop_3_1():
                global button
                my_options_4 = "What do you want to do?\nClimb tree\nLeave it be\nGo North?"
                label_options_4 = Label(game_3, text=my_options_4, bg="black", fg="white", font="Helvetica 14 bold")
                label_options_4.place(relx=0.5, rely=0.2)
                user_entry_4_1 = Entry(game_3, textvariable=user_var_4_1, bg="white", font="Verdana 14 bold")
                user_entry_4_1.place(relx=0.5, rely=0.35)
                bun1.config(command=check_choice_4_1(user_entry_4_1))

            def check_choice_4_1(user_entry):
                choice = user_var_4_1.get()
                if choice.lower() == "climb tree":
                    user_entry.config(state="readonly")
                    label_5.config(text="Aw man!! there is nothing in the nest Aghh..")
                    next_loop_4_1()
                elif choice.lower() == "leave it be":
                    label_5.config(text="Please no, I am hungry! Let's see above the tree.")
                elif choice.lower() == "go north":
                    label_5.config(text="no, climb the tree na please!!")

            def next_loop_4_1():
                global button
                my_options_5 = "Where to head?\nnorth or east or west?"
                label_options_5 = Label(game_3, text=my_options_5, bg="black", fg="white", font="Helvetica 14 bold")
                label_options_5.place(relx=0.5, rely=0.45)
                user_entry_5_1 = Entry(game_3, textvariable=user_var_5_1, bg="white", font="Verdana 14 bold")
                user_entry_5_1.place(relx=0.5, rely=0.55)
                bun1.config(command=check_choice_5_1(user_entry_5_1))

            def check_choice_5_1(user_entry):
                choice = user_var_5_1.get()
                if choice.lower() == "west":
                    user_entry.config(state="readonly")
                    label_6.config(
                        text="That's a banana tree. Finally found something to eat.\n I'm full. Now I should find something to fix my boat with. ")
                    next_loop_5_1()
                elif choice.lower() == "north":
                    label_6.config(text="There's nothing here...")
                elif choice.lower() == "east":
                    label_6.config(text="The forest is too dense can't go ahead.")

            def next_loop_5_1():
                global button
                my_options_6 = "Wait I see a Gate?\nHead to the gate\nLeave it be?"
                label_options_6 = Label(game_3, text=my_options_6, bg="black", fg="white", font="Helvetica 14 bold")
                label_options_6.place(relx=0.5, rely=0.68)
                user_entry_6_1 = Entry(game_3, textvariable=user_var_6_1, bg="white", font="Verdana 14 bold")
                user_entry_6_1.place(relx=0.5, rely=0.78)
                bun1.config(command=check_choice_6_1(user_entry_6_1))

            def check_choice_6_1(user_entry):
                choice = user_var_6_1.get()
                if choice.lower() == "head to the gate":
                    user_entry.config(state="readonly")
                    label_7.config(
                        text="Wait what's that? A book, here in the middle of nowhere. Let's check it out...")
                    next_bun1.config(state="normal")
                elif choice.lower() == "leave it be":
                    label_7.config(text="C'mon no! Let's check the gate out")

            label_2 = Label(game_3, font="Helvetica 14 bold", bg="black", fg="white")
            label_2.place(relx=0.1, rely=0.6)

            label_3 = Label(game_3, font="Helvetica 14 bold", bg="black", fg="white")
            label_3.place(relx=0.1, rely=0.9)

            label_4 = Label(game_3, font="Helvetica 14 bold", bg="black", fg="white")
            label_4.place(relx=0.5, rely=0.1)

            label_5 = Label(game_3, font="Helvetica 14 bold", bg="black", fg="white")
            label_5.place(relx=0.5, rely=0.4)

            label_6 = Label(game_3, font="Helvetica 14 bold", bg="black", fg="white")
            label_6.place(relx=0.5, rely=0.6)

            label_7 = Label(game_3, font="Helvetica 14 bold", bg="black", fg="white")
            label_7.place(relx=0.5, rely=0.83)

            bun1 = Button(game_3, text="GO", command=check_choice_1_1, bg="white", fg="black", font="Verdana 14 bold")
            bun1.place(relx=0.85, rely=0.88)
            next_bun1 = Button(game_3, text="next", state="disable", command=riddle, bg="white", fg="black", font="Verdana 14 bold")
            next_bun1.place(relx=0.85, rely=0.93)

        options = "What would you like to do?\ngo north\ngo south\ngo east\ngo west\n"

        options_lab = Label(game_2, text=options, bg="black", fg="white", font="Helvetica 15 bold")
        options_lab.place(relx=0.1, rely=0.1)

        player_var1 = StringVar()
        player_var2 = StringVar()
        player_var3 = StringVar()
        player_var4 = StringVar()
        player_var5 = StringVar()
        player_var6 = StringVar()

        player_entry = Entry(game_2, textvariable=player_var1, bg="white", font="Verdana 14 bold")
        player_entry.place(relx=0.1, rely=0.27)

        def check_choice():
            choice = player_entry.get()
            if choice.lower() == "go east":
                player_entry.config(state="readonly")
                lab1.config(
                    text="There are some shrubs here and near that \nthere is a medicinal plant.Should collect\nit, might help me ahead")
                next_LOOOP()
            elif choice.lower() in ["go north", "go south"]:
                lab1.config(text="The forest is too dense can't go ahead.")
            elif choice.lower() in ["go west"]:
                lab1.config(text="There are bushes ahead full of thorns.\nWon't prefer to go there.")

        lab1 = Label(game_2, font="Helvetica 14 bold", bg="black", fg="white", )
        lab1.place(relx=0.1, rely=0.32)

        def next_LOOOP():
            global button
            my_options = "How would you like to continue?\nCollect medical plant\ngo west\ngo north\ngo east"
            lab_options = Label(game_2, text=my_options, bg="black", fg="white", font="Helvetica 14 bold")
            lab_options.place(relx=0.1, rely=0.43)
            player_entry_2 = Entry(game_2, textvariable=player_var2, bg="white", font="Verdana 14 bold")
            player_entry_2.place(relx=0.1, rely=0.59)
            B1.config(command=check_input_2(player_entry_2))

        def check_input_2(player_entry_2):
            choice = player_var2.get()
            if choice.lower() == "collect medical plant":
                player_entry_2.config(state="readonly")
                lab2.config(text="medical plant collected")
                next_LOOOP_2()
            elif choice.lower() in ["go east", "go north", "go west"]:
                lab2.config(text="The forest is too dense can't go ahead.")

        def next_LOOOP_2():
            global button
            my_options = "Which direction this time?\ngo north\ngo west\ngo east\ngo south"
            lab_options = Label(game_2, text=my_options, bg="black", fg="white", font="Helvetica 14 bold")
            lab_options.place(relx=0.1, rely=0.7)
            player_entry_3 = Entry(game_2, textvariable=player_var3, bg="white", font="Verdana 14 bold")
            player_entry_3.place(relx=0.1, rely=0.86)
            B1.config(command=check_input_3(player_entry_3))

        def check_input_3(player_entry_3):
            choice = player_var3.get()
            if choice.lower() == "go south":
                player_entry_3.config(state="readonly")
                lab3.config(text='''There is nothing much here but just more trees.''')
                next_LOOOP_3()
            elif choice.lower() in ["go east", "go north", "go west"]:
                lab3.config(text="The forest is too dense can't go ahead.")

        def next_LOOOP_3():
            global button
            my_options = "How would you continue?\ngo west\ngo north\ngo east\nclimb tree"
            lab_options = Label(game_2, text=my_options, bg="black", fg="white", font="Helvetica 14 bold")
            lab_options.place(relx=0.5, rely=0.15)
            player_entry_4 = Entry(game_2, textvariable=player_var4, bg="white", font="Verdana 14 bold")
            player_entry_4.place(relx=0.5, rely=0.3)
            B1.config(command=check_input_4(player_entry_4))

        def check_input_4(player_entry_4):
            choice = player_var4.get()
            if choice.lower() == "go north":
                player_entry_4.config(state="readonly")
                lab4.config(text="Wait what's that sound? I can hear the water flowing.")
                next_LOOOP_4()
            elif choice.lower() == "climb tree":
                lab4.config(text="You don't have enough guts.")
            elif choice.lower() in ["go west", "go east"]:
                lab4.config(text="The forest is too dense can't go ahead.")

        def next_LOOOP_4():
            global button
            my_options = "Move to the water?\ngo west\ngo north\ngo east\ngo south"
            lab_options = Label(game_2, text=my_options, bg="black", fg="white", font="Helvetica 14 bold")
            lab_options.place(relx=0.5, rely=0.4)
            player_entry_5 = Entry(game_2, textvariable=player_var5, bg="white", font="Verdana 14 bold")
            player_entry_5.place(relx=0.5, rely=0.55)
            B1.config(command=check_input_5(player_entry_5))

        def check_input_5(player_entry_5):
            choice = player_var5.get()
            if choice.lower() == "go north":
                player_entry_5.config(state="readonly")
                lab5.config(text="That's a waterfall!!! Aah, finally some fresh water to drink...")
                next_LOOOP_5()
            elif choice.lower() in ["go west", "go east", "go south"]:
                lab5.config(text="Naah the waterfall ain't here!")

        def next_LOOOP_5():
            global button
            my_options = "Can take a bath as well probably. Will feel fresh.?\nTake Bath\nNaah"
            lab_options = Label(game_2, text=my_options, bg="black", fg="white", font="Helvetica 14 bold")
            lab_options.place(relx=0.5, rely=0.65)
            player_entry_6 = Entry(game_2, textvariable=player_var6, bg="white", font="Verdana 14 bold")
            player_entry_6.place(relx=0.5, rely=0.78)
            B1.config(command=check_input_6(player_entry_6))

        def check_input_6(player_entry_6):
            global next_button
            choice = player_var6.get()
            if choice.lower() == "take bath":
                player_entry_6.config(state="readonly")
                lab_6.config(text="Oh man I'm feeling so good and refreshed")
                lab_7.config(text="Feeling hungry. Now I should find something to eat...")
                next_B1.config(state="normal")
            elif choice.lower() == "naah":
                lab_6.config(text="I like to stay dirty. Hehe")
                lab_7.config(text="Feeling hungry. Now I should find something to eat...")
                next_B1.config(state="normal")

        lab2 = Label(game_2, font="Helvetica 14 bold", bg="black", fg="white")
        lab2.place(relx=0.1, rely=0.64)

        lab3 = Label(game_2, font="Helvetica 14 bold", bg="black", fg="white")
        lab3.place(relx=0.5, rely=0.1)

        lab4 = Label(game_2, font="Helvetica 14 bold", bg="black", fg="white")
        lab4.place(relx=0.5, rely=0.35)

        lab5 = Label(game_2, font="Helvetica 14 bold", bg="black", fg="white")
        lab5.place(relx=0.5, rely=0.6)

        lab_6 = Label(game_2, fg="white", bg="black", font="Helvetica 14 bold")
        lab_6.place(relx=0.5, rely=0.83)

        lab_7 = Label(game_2, fg="white", bg="black", font="Helvetica 14 bold")
        lab_7.place(relx=0.5, rely=0.86)

        B1 = Button(game_2, text="GO", command=check_choice, bg="white", fg="black", font="Verdana 14 bold")
        B1.place(relx=0.85, rely=0.88)
        next_B1 = Button(game_2, command=last, state="disable", text="next", bg="white", fg="black", font="Verdana 14 bold")
        next_B1.place(relx=0.85, rely=0.93)

    start = Label(game, text="Start !!!", bg="black", fg="white", font="Helvetica 18 bold")
    start.place(relx=0.1, rely=0.1)

    options = "What would you like to do?\ngo north\ngo south\ngo east\ngo west\n"

    options_label = Label(game, text=options, bg="black", fg="white", font="Helvetica 15 bold")
    options_label.place(relx=0.1, rely=0.2)

    user_variable = StringVar()
    user_var_2 = StringVar()
    user_var_3 = StringVar()
    user_var_4 = StringVar()

    user_entry = Entry(game, textvariable=user_variable, bg="white", font="Verdana 14 bold")
    user_entry.place(relx=0.1, rely=0.4)

    def check_choice():
        choice = user_entry.get()
        if choice.lower() == "go north":
            user_entry.config(state="readonly")
            label1.config(text="There is a stone with some symbols carved on it. ")
            next_loop()
        elif choice.lower() == "go south":
            label1.config(text="It's the ocean. I haven't still gathered enough resources.")
        elif choice.lower() in ["go east", "go west"]:
            label1.config(text="The forest is too dense can't go ahead.")

    label1 = Label(game, font="Helvetica 14 bold", bg="black", fg="white")
    label1.place(relx=0.1, rely=0.45)

    def next_loop():
        global button
        my_options = "What's in your mind?\nUnderstand the carvings\ngo west\ngo north\ngo east"
        label_options = Label(game, text=my_options, bg="black", fg="white", font="Helvetica 14 bold")
        label_options.place(relx=0.1, rely=0.53)
        user_entry_2 = Entry(game, textvariable=user_var_2, bg="white", font="Verdana 14 bold")
        user_entry_2.place(relx=0.1, rely=0.71)
        b1.config(command=check_choice_2(user_entry_2))

    def check_choice_2(user_entry_2):
        choice = user_var_2.get()
        if choice.lower() == "go west":
            user_entry_2.config(state="readonly")
            label2.config(text="There is a clear path.")
            next_loop_2()
        elif choice.lower() == "understand the carvings":
            label2.config(text="Can't understands them. You are not that smart.")
        elif choice.lower() in ["go east", "go north"]:
            label2.config(text="The forest is too dense can't go ahead.")

    def next_loop_2():
        global button
        my_options = "Let's explore more?\ngo north\ngo west\ngo east\njump"
        label_options = Label(game, text=my_options, bg="black", fg="white", font="Helvetica 14 bold")
        label_options.place(relx=0.5, rely=0.2)
        user_entry_3 = Entry(game, textvariable=user_var_3, bg="white", font="Verdana 14 bold")
        user_entry_3.place(relx=0.5, rely=0.4)
        b1.config(command=check_choice_3(user_entry_3))

    def check_choice_3(user_entry_3):
        choice = user_var_3.get()
        if choice.lower() == "go west":
            user_entry_3.config(state="readonly")
            label3.config(text='''There is a huge tree in front of you.\nUnder the tree, there are some dry twigs.\nThey might come in handy in lighting the fire.
    This whole place is wet due to rain.\nIt's hard to find dry wood.''')
            next_loop_3()
        elif choice.lower() == "jump":
            label3.config(text="Hehe! Was fun!")
        elif choice.lower() in ["go east", "go north"]:
            label3.config(text="The forest is too dense can't go ahead.")

    def next_loop_3():
        global button
        my_options = "Now What?\nCollect dry wood\ngo west\ngo north\ngo east"
        label_options = Label(game, text=my_options, bg="black", fg="white", font="Helvetica 14 bold")
        label_options.place(relx=0.5, rely=0.65)
        user_entry_4 = Entry(game, textvariable=user_var_4, bg="white", font="Verdana 14 bold")
        user_entry_4.place(relx=0.5, rely=0.8)
        b1.config(command=check_choice_4(user_entry_4))

    def check_choice_4(user_entry_4):
        global next_button
        choice = user_var_4.get()
        if choice.lower() == "collect dry wood":
            user_entry_4.config(state="readonly")
            label4.config(text="Dry wood collected")
            next_b1.config(state="normal")
        elif choice.lower() == "go east":
            label4.config(text="Ouch!! the damn thorns they hurt.\nThere is nothing here. Coming here was a waste.")
        elif choice.lower() in ["go west", "go north"]:
            label4.config(text="The forest is too dense can't go ahead.")

    label2 = Label(game, font="Helvetica 14 bold", bg="black", fg="white")
    label2.place(relx=0.1, rely=0.76)

    label3 = Label(game, font="Helvetica 14 bold", bg="black", fg="white")
    label3.place(relx=0.45, rely=0.45)

    label4 = Label(game, font="Helvetica 14 bold", bg="black", fg="white")
    label4.place(relx=0.5, rely=0.85)

    b1 = Button(game, text="GO", command=check_choice, bg="white", fg="black", font="Verdana 14 bold")
    b1.place(relx=0.85, rely=0.85)
    next_b1 = Button(game, command=b_a_c_k, state="disable", text="next", bg="white", fg="black", font="Verdana 14 bold")
    next_b1.place(relx=0.85, rely=0.9)

    game.attributes('-fullscreen', True)

def help():
    instruction = Toplevel(root)

    def back():
        instruction.destroy()

    instruction.config(bg="black")

    Label(instruction, text="HOW TO PLAY?", bg="black", fg="white", font="Helvetica 30 bold").pack()

    how = "Phoenix is a text based game which makes you imagine and takes you to a different world.\n" \
          "You are given a situation along with three options.\n" \
          "Type one of the given options for that situation ,then the game will proceed and\n" \
          " will give you different scenarios and options according to the story." \
          "\nAfter advancing a bit in this game you will be given a riddle to solve.\n" \
          " You have to visit the place which is best suited as the answer to the riddle and " \
          "\nthen you will find a qr code there. You have to scan it and then it will allow you to go to the next level. " \
          " \nEnjoy the game.."
    Label(instruction, text=how, bg="black", fg="white", font="Helvetica 20 bold").place(relx=0.05, rely=0.3)



    instruction.attributes('-fullscreen', True)

    Button(instruction, text="BACK", command=back, height=3, width=10).place(x=750, y=800)



def close():
    root.destroy()


def brown():
    root.config(bg="#211801")

    let = Label(root, text="PHENOIX", bg="#211801", fg="#ccc7bc", font="Algerian 100 bold")
    let.place(relx=0.5, rely=0.2, anchor="center")




def white():
    root.config(bg="white")

    let = Label(root, text="PHENOIX", bg="white", fg="black", font="Algerian 100 bold")
    let.place(relx=0.5, rely=0.2, anchor="center")



def black():
    root.config(bg="black")

    let = Label(root, text="PHENOIX", bg="black", fg="white", font="Algerian 100 bold")
    let.place(relx=0.5, rely=0.2, anchor="center")


    b1 = Button(root, text="PLAY", command=game, font="Castellar 30 bold", borderwidth=6, relief=RIDGE, width=12)
    b1.place(x=570, y=270)


    b2 = Button(root, text="INSTRUCTIONS", command=help, font="Castellar 30 bold", borderwidth=6, relief=RIDGE, width=12)
    b2.place(x=570, y=370)


    b3 = Button(root, text="EXIT", command=close, font="Castellar 30 bold", borderwidth=6, relief=RIDGE, width=12)
    b3.place(x=570, y=470)


    frame = Frame(root, bg="white", borderwidth=6, relief=RIDGE)

    lq = Label(frame, text="THEME", font="Castellar 30 bold", width=12)

    lq.pack()

    frame.place(x=570, y=570)


    b4 = Button(frame, text="BROWN", command=brown, bg="#211801", fg="#ccc7bc", borderwidth=2, relief=RIDGE, width=17,height=2)
    b4.pack(side=LEFT)


    b5 = Button(frame, text="BLACK", command=black, bg="black", fg="white", borderwidth=2, relief=RIDGE, width=18, height=2)
    b5.pack(side=LEFT)


    b6 = Button(frame, text="WHITE", command=white, bg="white", fg="black", borderwidth=2, relief=RIDGE, width=17, height=2)
    b6.pack(side=LEFT)

black()


root.attributes('-fullscreen', True)

root.mainloop()
