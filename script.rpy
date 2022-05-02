# Define character emotes in relation to dialogue. (Green Haired Oracle)


define t = Character(_("Oracle"), color="#7851a9")
default book = False


# The game starts here.

label start:

    play music "physical_layer.ogg" fadein 3.0

    define counter = 0

label warp:

    scene bg room
    with fade

label four:

    show trinity neutral

    t "Mesologie..."

    show trinity smile

    "Start fresh with gratitude and healing!"

    hide trinity smile

label main_zero:

    menu:

        "Travel.":
            jump travel

        "Draw a card.":
            jump draw

        "Weekly.":
            jump weekly

        "Starting / Ending the day.":
            jump qi

        "Relativity engine.":
            jump relative

        "Exit.":
            jump exit


label relative:

    show trinity neutral

    t "Lesser of 🃏101 or fatigue timer."

    hide trinity neutral



    menu:

        "Shower.":
            jump shower

        "Recovery.":
            jump rest

        "Groceries.":
            jump groceries

        "Personal dev.":
            jump dev

        "Cooking.":
            jump cuisine

        "Go back one level.":
            jump main_zero

label rest:

    show trinity think

    t "Don't be afraid to schedule lux 20 hour breaks if time allows.  Stress kills, and don't you wish to hug your grandchildren?"

    hide trinity think

    jump relative


label dev:

    stop music fadeout 4

    show trinity smile

    t "Inject music into your system!"

    show trinity neutral

    play music "Deathsmiles ~ For Lost and Beloved Souls ~ OST.ogg" fadein 3.0

    t "Set timer based on fatigue."

    show trinity smile

    t "Draw a card if lacking in inspiration! :D"

    hide trinity smile

    jump main_zero



label cuisine:

    "Look at `recipes` folder if uninspired."

    "0.  Grab a pair of nitrile gloves for washing dishes."

    show trinity neutral

    t "1.  Wash the porcelain bowl for mixing. ⏳ 1"

    t "2.  Play some music~ 🎹 256m timer."

    t "3.  Take out the meat used for cooking."

    show trinity think

    "4.  Then the cutting board, and garlic. ⏳ check timer."

    t "5.  The pan, sesame oil & herbs used for cooking."

    t "6.  ❤️‍🔥 10:  Turn on the stovetop ~"

    show trinity smile

    "At least an hour of uninterrupted eating!  Then relax for one more."

    jump main_zero



label qi:

    # Incomplete.
    # `What time is it` section > relative time.

    menu:

        "Starting the day.":
            jump seven

        "Ending the day...":
            jump nineteen

        "(Take me back one level.)":
            jump main_zero

label seven:

    show trinity neutral

    t "Set timer for end of work to avoid burnout."

    hide trinity neutral

    show trinity smile

    t "Start the day with a sense of gratitude! You could've woken up dead lol."

    show trinity ardent

    'Give yourself 30 minutes of dev/creative time!'

    hide trinity ardent

    t "Music might wake you up!  Set timer for next action."

    jump main_zero


label nineteen:

        "Winding Down:"

        "Set a sleep timer."

        "Read tomorrow's entry for 🃏3 while the melatonin kicks in."

        "Sweet oblivion.."

        jump main_zero


label acupressure:

    show trinity neutral

    t "check out the historic document for a sample itinerary including travel times."

    hide trinity neutral
    with dissolve

    "Usually you want to have at least four hours of action time."

    show trinity neutral

    t "And then, two days of breaking in new... flesh."

    show trinity think

    t "Like breaking in those Vibrams..."

    jump main_zero


label code:

    show trinity neutral

    t "Use Joystick Mapper for dual wielding."

    hide trinity neutral

    "start with a general outline by defining the main categories and labels."

    show trinity think

    t "Start filling labels then the order you choose, adding an emoji checkmark and folding completed code."

    show trinity smile

    t "then clean up the syntax and bugs using the element of water & music!"



label oracle:

    show trinity ardent

    t "Refer to original app when in need of motivation."

    hide trinity ardent

    jump relative

label travel:

    stop music fadeout 4

    "Recall the mindset that you will leave your city.  Check weather for appropriate clothing."

    play music "ace.ogg" fadein 3.0

    t "Set timer to leave."

    "Foot covering, TENS unit, headband & mask."

    "Clothing for outside."

    "Compression gloves, glasses, keys/wallet."

    "phone/watch/earphones."

    "Chargers."

    jump main_zero


label weekly:

    show trinity think

    t "Which day do you wanna look at?"

    hide trinity think

    menu:

        "Sunday - Monday.":
            jump sunday

        "Tuesday.":
            jump tuesday

        "Wednesday.":
            jump wednesday

        "Thursday - Friday.":
            jump thursday

        "Saturday.":
            jump saturday

        "(Take me back one level.)":
            jump main_zero

label sunday:

    "Dev, laundry & reconcile accounting balances."

    t "Reconcile journal entries."

    jump weekly

label tuesday:

    "Just work & rest, no huge transactions."

    "The middle of the week is most difficult, so takeout is okay."

    jump weekly

label wednesday:

        "No unnecessary transactions, but having breakfast catered is okay."

        jump weekly

label thursday:

    "Plan transactions for the next 72 hours."

    "Strictly work & adequate rest."

    jump weekly

label saturday:

    "At home with dumplings & a journal."

    jump weekly

# This starts the card draw subroutine.

label shower:

    hide trinity think

    'Recall the mindset that you will exit your city.'

    'Set timer.'

    'Gather underwear, shirt, headband & greaves.'

    jump main_zero

label groceries:

    show trinity neutral

    "Wallet, keys, phone, headset & clothing."

    "Greater of fatigue counter or 🃏101."

    hide trinity neutral

    jump main_zero

label draw:

label card:

    "Discard an axiom."

label one:

    $ counter += 1

    hide trinity ardent

    $ d20roll = renpy.random.randint(1, 7)

    if d20roll == 1:

# Lv2 indent.

        show trinity neutral

        t "11 - Harmony."

        hide trinity neutral

#L1

    else:

#2

        if d20roll == 2:

#3

            show trinity think

            "15 - Mangroves / Innovation."

            hide trinity think

#2

        else:

#3

            if d20roll == 3:

#4

                show trinity ardent

                t "25 - Rough Seas - The Unexpected."

                hide trinity ardent

            else:

                if d20roll == 4:

                    show trinity smile

                    t "Altar of fire / Burning bridges."

                    hide trinity smile

                    "Discard an axiom!"

                else:

                    if d20roll == 5:

                        show trinity ardent

                        t "33 - Starfish - Symbols."

                        hide trinity ardent

                    else:

                        if d20roll == 6:

                            show trinity think

                            t "24 - Rockpool - Healing."

                            hide trinity think

                        else:

                            if d20roll == 7:

                                show trinity neutral

                                t "23 - Reef - Abundance."

                                hide trinity neutral



    menu:

        "Draw a card.":
            jump one

        "Go back.":
            jump reset


label reset:

    "Set timer based on next action."

    "You have drawn [counter] card(s) so far."

    jump warp

label exit:

    scene bg night
    with fade

    show trinity neutral

    stop music fadeout 5

    t "Take good care of yourself!"

    hide trinity neutral

    with dissolve

return
