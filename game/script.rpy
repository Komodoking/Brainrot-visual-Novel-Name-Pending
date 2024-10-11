# Character Definitions
define player_name = Character("[player_name]", color="#c8c8ff")
define doctor = Character("Doctor", color="#ff8c8c") # Static doctor character
define heroine = Character("Heroine", color="#8cff8c", what_prefix="H: ") # Heroine with prefix

# Enter Name Subscene
label start:
    $ player_name = renpy.input("Please enter your name:")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Player"

    jump scene_1_hospital_office

# Scene 1: Hospital Office
label scene_1_hospital_office:

    scene hospital_office with dissolve

    narrator "I can’t believe my ears…"

    show doctor static at left with dissolve
    doctor "I have nothing else to say, this disease is terminal and cannot be cured at this stage. I am sorry."

    show heroine normal at right with dissolve
    heroine "Erm, what the sigma."

    narrator "I’m a 22-year-old salaryman that works at a corporation, and the girl spouting nonsense in the hospital bed is *heroine_name*, my girlfriend."
    narrator "We met online as gaming buddies and eventually found out we lived in the same city. Meeting in real life at first was awkward. We had both always spent a considerable amount of our time online."

    player_name "Doctor, are you sure there is nothing we can do?"

    heroine "Chat, is this real? Is blud really yapping?"

    narrator "A couple of months ago, a disease known as brainrot began to spread throughout the populace."
    narrator "Those afflicted could only communicate in incomprehensible internet lexicon, which you wouldn’t understand unless you were terminally online."
    narrator "*heroine_name* is 4 years older than me and still got it."
    narrator "In the past, *heroine_name* always spent significantly more time than me on the internet because I had to study for school. She doesn’t go outside too often. Even getting her to the hospital was its own ordeal."

    doctor "I’m afraid not. From the way she talks, she is far beyond saving."
    doctor "We do not yet have a cure for this disease, but intensive palliative care is not yet necessary."
    doctor "You can care for her at home, although if you do not take the proper precautions, you yourself may become infected."

    narrator "The doctor looks away, but his expression doesn’t change."

    doctor "As another option, you could provide her with a mercy that has recently been legalized for patients suffering from this specific sickness."

    narrator "Is this guy for real?? That's my girlfriend he’s talking about."

    menu:
        "Angrily reprise the doctor for even suggesting such a thing.":
            $ choice = "angry"
            narrator "I stand up abruptly, scraping my chair against the floor. The anger boils over, and I snap at the doctor."
            player_name "How can you call yourself a doctor! How can you even suggest something like taking the patient's life? You should be ashamed of yourself! Come on, *heroine_name*. Let's get out of here."

            doctor "I see. I am sorry I brought it up. Please be mindful to not get infected yourself and try to keep her away from the internet. Have a nice day."

            jump end_scene_1

        "Respond calmly and leave.":
            $ choice = "calm"
            narrator "I take a deep breath, trying to keep my emotions in check. The doctor's suggestion lingers in the back of my mind, but I should stay composed for my name's sake."
            player_name "I see. Well, there is much to consider. We will be going now. Good day to you."

            doctor "If you choose to care for her at home long-term, it seems that limiting the use of the internet and touching grass are effective ways of managing symptoms. I’ll let you know if anything important arises. Have a nice day."

            jump end_scene_1

label end_scene_1:

    narrator "With a lot to think about, I take *heroine_name*'s hand, and we leave the hospital office."

    heroine "Hey, wait. What the skibidi?!?"

    narrator "I drag her out of the hospital and to our car."

    jump scene_2_car

# Scene 2: Car
label scene_2_car:

    scene car_interior with dissolve

    narrator "The car ride home is mostly quiet."

    narrator "Listening instead to the light pattering of rain on my windshield, I try my best to collect my thoughts about the recent visit at the hospital, but this is interrupted by:"

    show heroine normal at right with dissolve
    heroine "Sigma so quiet? Are you mewing?"

    narrator "'heroine_name' interrupts me with some brain rot sentence, I respond:"

    menu:
        "In brain rot speech so she can better understand me.":
            $ choice = "brainrot"
            player_name "I have a lot to goon about skibidi, soz."

            heroine "Don’t worry gooner! That doctor was a skibidi toilet from Ohio anyways."

        "Normally because I don’t want to get infected.":
            $ choice = "normal"
            player_name "Sorry, I have a lot to think about."

            narrator "She gives me a questioning look, not fully comprehending what I said. Still, she tries to reassure me anyways."
            heroine "Don’t worry gooner! That doctor was a skibidi toilet from Ohio anyways."

    narrator "I try to cheer up and not think about it too much. I try to force a smile. 'heroine_name is in a good mood despite the fuss she made about going outside this morning."
    
    narrator "As I continue to drive, 'heroine_name' puts on some music."

    show heroine happy at right
    heroine "See! This is some sigma beats, this should give you mad rizz!"

    narrator "The music she puts on is a brainrot remix of the song 'Closer' by The Chainsmokers."
    narrator "Most of the lyrics have been swapped out for more brainrot terms. For example, the chorus is changed from 'we ain’t never getting older' to 'we ain’t never not the rizzler'."
    narrator "That sentence is still to this day kinda crazy to me. It works for the sake of maintaining the same feel for the song, but three instances of negation is pretty funny."

    player_name "Haha, yeah…"

    narrator "Thinking about the three instances of negation helps me take my mind off what happened at the doctor’s office."

    narrator "We keep driving, the music playing. It helps a bit, I suppose, but I cannot help but think about what the doctor said at the hospital."
    narrator "The world outside zooms by, but inside the car, the weight on my shoulders feels a bit lighter."

    return
