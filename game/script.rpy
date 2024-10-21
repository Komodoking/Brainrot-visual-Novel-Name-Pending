# Character Definitions
define player_name = Character("[player_name]", color="#0000fa")
define doctor = Character("Doctor", color="#ffffff") # Static doctor character
define heroine = Character("Heroine", color="#d400ff", what_prefix="H: ") # Heroine with prefix
define grandma = Character("Grandma", color="#ffffff") 
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

    jump scene_3_home

# Scene 3: Home
label scene_3_home:

    scene home_background with fade

    narrator "Back at our apartment, I don't feel as easygoing. Maybe it's all her brainrot I was listening to, or maybe reality is setting in?"

    show heroine normal at right with dissolve

    heroine "Hey [player_name]! Don’t worry about that beta yapper! You mog his gyatt any day of the week!"

    narrator "Despite whatever the doctor says and 'heroine_name'’s incomprehensible brainrot speech, I can feel that 'heroine_name' seems to care about me as normal."
    narrator "How could the doctor even suggest doing that to 'heroine_name'?"
    narrator "I’ll try to think more helpful thoughts for now."

    heroine "Come on [player_name]! Let's go play some fortnite festival! Let's jelq the skibidi and get some gyatts! Although I am hungry, I could fanum tax some grimace shake from ohio."

    menu:
        "Play fortnite festival with her.":
            $ choice = "play_fortnite"
            jump play_fortnite_festival

        "Go to my room and try to make sense of this situation.":
            $ choice = "go_room"
            jump go_to_room

label play_fortnite_festival:

    player_name "Ok, let's play some fortnite festival. As for your grimace shake, I’ll order one. Do you want anything else?"

    narrator "'heroine_name' looks at me with an excited glimmer in her eyes, like a child in a candy store."

    heroine "Thanks [player_name], you’re the best!"

    scene fortnite_festival_cg with fade

    narrator "We sit together on the couch playing Fortnite festival."
    narrator "We jam out to Metallica's Ride the Lightning."

    heroine "Ahaha, you are just like baby gronk [player_name]! You really rizz up the sigmas!"

    narrator "I try my best to give her a smile. I’m already growing tired of her newfound… eloquence."
    narrator "She seems the same as ever, but she has been quite difficult to understand since she was infected. Will she ever be cured?"

    narrator "My thoughts bring me back to the hospital room."
    narrator "Mercy…is what the doctor called it. I scoff at the idea, but the word keeps coming back into my head."
    narrator "Could it be possible that she is suffering, and I can’t even see it?!?!?"

    player_name "Thanks 'heroine_name', I'm really having fun with you."

    narrator "A notification pops up on my phone."

    player_name "Looks like our food will be here shortly."

    heroine "Thanks rizzler, this grimace shake from Ohio is just what I needed to keep mogging betas on fortnite festival."

    player_name "From Ohio?"

    narrator "Seeing her in high spirits makes me question if she understands the gravity of her situation, but at the same time, it eases my mind a little knowing we can still have fun together just like normal."

    narrator "We continue to have fun playing Fortnite festival."

    jump continue_after_choice

label go_to_room:

    player_name "Sorry 'heroine_name', but not today. I’ll be in my room if you need me."

    narrator "'heroine_name' pouts, looking dejected at my response."

    heroine "Ok… gooner."

    narrator "I go to my room to think about what happened at the hospital. How could this happen? There’s no way that I am going to go through with what the doctor said. 'heroine_name' is my girlfriend, and I love her."
    narrator "Our relationship might not be the most conventional from here on out, but I am willing to fight for it."

    narrator "My thoughts bring me back to the hospital room."
    narrator "Mercy… is what the doctor called it. I scoff at the idea, but the word keeps coming back into my head."
    narrator "Could it be possible that she is suffering, and I can’t even see it?!?!?"

    play sound "knock_door.mp3"

    heroine "Ummm [player_name]? Can I come in?"

    narrator "????!? She spoke normally?"

    player_name "Yeah, what's up?"

    heroine "Did you not want to jelq to fortnite festival? We can mog something else if you would want to sigma? I want to be with you right now."

    narrator "There are still some traces of brainrot in her sentences, but I can understand her intentions clearly. With or without brainrot, 'heroine_name' is still my girlfriend."
    narrator "She has the capacity to speak normally it seems, but how?"
    narrator "Is it because it is the first time we went out in a while? Maybe she understood what the doctor was saying and wants me to stay with her?"
    narrator "Whatever it is I don’t know."

    player_name "Sure, let's stay together. We can watch that new show you were talking about or something."

    scene cuddle_cg with fade

    narrator "I hold her while we watch the unnamed isekai anime number 57(they are all the same at this point let's be real)."
    narrator "A scene where the protagonist defeats a villain without any struggle happens."
    narrator "'heroine_name' seems to be enjoying herself, which I guess is all that matters."

    heroine "Chat is this real?"

    narrator "'heroine_name' exclaims when the dragon is easily defeated. Love interest number 1 then bickers with love interests number 2 and 3 about how awesome the blank protagonist is."

    heroine "Can’t let gang know I fw this."

    narrator "I’ve been working a lot, so I haven’t had much time to spend like this."

    jump continue_after_choice

label continue_after_choice:
    scene home_bg with fade
    narrator "After spending quality time with 'heroine_name', I am reassured that she is still the girlfriend I’ve known and loved, and despite what the doctor says, I believe there is still a chance for her."
    narrator "I think now that it is the weekend, and that I have time to spend with her, I should make her go out again tomorrow. It has been a while since we went somewhere on a date."
    narrator "She always wants to spend time inside, but with technology being the reason for her brainrot, I think it would be best for her to go somewhere outside tomorrow."

    menu:
        "Park":
            $ destination = "Park"
            jump next_scene

        "Mall":
            $ destination = "Mall"
            jump next_scene

        "Aquarium":
            $ destination = "Aquarium"
            jump next_scene

label next_scene:

    narrator "I decide to take her to the [destination]."

    jump scene_4_home_before_trip

label scene_4_home_before_trip:

    scene home_bg with fade

    narrator "I stir awake before 'heroine_name' does. I open my eyes and see that 'heroine_name' is hugging me in the same position we fell asleep in."

    narrator "In the moment, it feels like nothing is wrong. Maybe nothing is."

    narrator "She is clutching onto me so tightly that I worry I’d wake her trying to get up, but I manage."

    narrator "She doesn’t usually rise until late in the afternoon, so I use this time to think about how I will wake her."

    narrator "Every morning she struggles to get out of bed, so we've adopted a system where I find fun and creative ways to get her out of our room. I could carry her out of bed while she is still asleep. It would be a playful and romantic way to wake her up."
    narrator "I could also play a joke on her and splash her with a bucket of cold water. It would be maybe more mean, but also more effective. She isn’t the type of person to get mad at something like this either; she will probably laugh it off or forget about it later."

    menu:
        "Carry her out of bed to wake her up":
            $ choice = "carry"
            jump carry_wake_up

        "Get a bucket of cold water and pour it on her head":
            $ choice = "water"
            jump water_wake_up

label carry_wake_up:

    scene carry_cg with fade

    narrator "I carry her out of bed playfully."

    heroine "Gwaaa what the sigma?!? What are you mewing [player_name]?!?"

    narrator "She awakens groggily. After fully awakening, she begins to raise her voice in annoyance."

    heroine "Put my skibidi gyatt down or I’m gonna mog you!!!"

    player_name "Okay, it looks like you're awake now. We are going to the [destination] today."

    narrator "'heroine_name' pouts at me with dark circles under her eyes, tired from staying up late last night probably."

    heroine "The [destination]? That's for betas! Not for sigmas with skibidi rizz like me."

    narrator "As expected, she is reluctant to go. Luckily, I planned for this."

    player_name "Come on, it will be fun! We haven’t had a lot of time to spend together."

    narrator "This is how I got her to go to the hospital yesterday. I know she still likes to spend time with me, despite her condition. She’s a bit scared to go out these days, but if I go with her, it should be fine."

    heroine "Can’t we just stay inside? There are betas trying to edge me out there."

    player_name "I can protect you. Besides, it will be like a new adventure! We haven’t gone out just to hang out in a while. The hospital yesterday doesn’t count. We can get a grimace shake on the way. Besides, I want to spend time with you, you are my girlfriend after all."

    narrator "'heroine_name' looks away from me, embarrassed for some reason."

    heroine "Ok if you say so…"

    narrator "She blushes slightly."

    heroine "But we have to get the grimace shake first!"

    player_name "Sure, we can do that."

    narrator "I smile at her. This outing was needed for both of us. I’ve been a bit busy at work, and I miss being able to go out and spend time with her."

    heroine "Ok, we can get a grimace shake before we go."

    scene home_bg with fade

    show heroine normal at right

    # Exclusive destination dialogue
    if destination == "Park":
        narrator "Perhaps I can prepare something for the park, make some nice healthy picnic food or something."
        narrator "A good nutritious sandwich, a cool bento box, or fresh pasta might be a good change of taste for 'heroine_name'."
        narrator "Eating a good meal in a serene park might be just what she needs in order to help cure her of the brainrot."

    elif destination == "Aquarium":
        narrator "The aquarium is closer to the center of town, perhaps we can go to a restaurant afterward."
        narrator "I do enjoy a good steakhouse, but there are some other good options we could try, like an izakaya or seafood place."
        narrator "A nice meal in a good atmosphere might be a welcome change of pace for 'heroine_name'."

    elif destination == "Mall":
        narrator "Mall food isn’t much better than the usual slop we get, but it might be a nice change of pace."
        narrator "Some options in the mall can be quite exotic, and the atmosphere of the food court hits different sometimes."

    narrator "I help her get ready, and we head off to the [destination]."

    if destination == "Park":
        jump scene_5_trip_to_park

    elif destination == "Mall":
        jump scene_5_trip_to_mall  

    elif destination == "Aquarium":
        jump scene_5_trip_to_aquarium  

label water_wake_up_cg:

    narrator "I go to the laundry room and fill up a basin with cold water. I return to the bedroom and dump the cold water on 'heroine_name'."

    play sound "water splash.mp3"

    heroine "What the skibidi?!?"

    narrator "She jumps out of bed, soaking wet."

    heroine "Kyaa, what the sigma, [player_name]! What was that for?!?"

    player_name "Just a little bit of trolling. We are going to the [destination] today."

    narrator "She glares at me angrily."

    heroine "Not without my revenge. I’m going to mog you!"

    narrator "She grabs the nearby broom and begins to chase me around the room."

    player_name "Hey, wait! Save that energy for the [destination]!"

    narrator "She stops her assault when she hears what I said."

    heroine "W-what!? Why would I go to the [destination]?"

    scene home_bg with fade

    show heroine normal at right

    # Exclusive destination dialogue
    if destination == "Aquarium":
        player_name "Because there are cool fish there! Not only fish, but also penguins, crabs, seals, and other cool aquatic creatures. Don’t you want to hang out with the fishes?"

        heroine "Erm what the skibidi? You fanum taxed me so early in the morning just to go see le fishe? I am going to send you to Ohio!"

        narrator "Despite her protest, she senses my disappointment and relents."

        heroine "Hmm, spending time with Le Fishe might be kinda meta. Very well, we will traverse to Paradise Palms to goon with Le Fishe!"

        player_name "Great!"

    elif destination == "Park":
        player_name "Come on, it’s time to touch grass! You’ll feel the nice fall weather, and get a break from rotting in the room so much. It will be a cool adventure!"

        heroine "Erm, what the ligma? I don’t understand. Can you explain it in League of Legends terms?"

        narrator "I sigh. This kind of behavior can be exhausting, but I feel happy spending time with 'heroine_name' anyway."

        player_name "It’s like you’ve been setting up a gank bot for too long, so you need to start pathing elsewhere to help other lanes or clear your camps."

        narrator "'heroine_name' seems to understand."

        heroine "Oh, yes, [player_name]. Very well, sigma. Chat, we will go to Pleasant Park today!"

    elif destination == "Mall":
        player_name "Because we can buy cool stuff there!"

        heroine "But we can just spend V-bucks at the item shop to clothesmax?"

        narrator "'heroine_name' enjoys online shopping, and we get a package to the house every other day at this point."

        player_name "It’s different to go see it in person. Remember all the times you buy something online, and it doesn’t look like it should? Plus, there’s an arcade at the mall, with the cool claw machine."

        heroine "Aren’t those usually a scammax?"

        player_name "You’re just scared I’m going to mog you in the arcade."

        narrator "'heroine_name' perks up immediately."

        heroine "W-What!? I am the sigma! I do the mogging! Very well, I won’t back down from your 1v1! Prepare to get fullboxed! And we can clothesmax while we’re there, I guess."

        player_name "Great!"

    narrator "I smile, happy that she’s deciding to go with me. I sincerely hope the day goes well."

    label scene_5_chain:

    if destination == "Park":
        jump scene_5_trip_to_park

    elif destination == "Mall":
        jump scene_5_trip_to_mall  

    elif destination == "Aquarium":
        jump scene_5_trip_to_aquarium  

#park scene
label scene_5_trip_to_park:

    narrator "As 'heroine name' is getting ready, I start thinking about what food I can cook to bring to the park. I lied to her; I will not be getting her a Grimace shake on the way. I haven’t cooked for her in some time, and maybe eating some home-cooked cuisine will help her condition. What should I prepare for this outing?"

    menu:
        "Pesto Chicken Sandwich":
            $ food_choice = "Pesto Chicken Sandwich"
            jump food_prepared

        "Katsu Bento Box":
            $ food_choice = "Katsu Bento Box"
            jump food_prepared

        "Spaghetti":
            $ food_choice = "Spaghetti"
            jump food_prepared

label food_prepared:

    narrator "After finishing up the [food_choice], 'heroine name' comes down just as I wrap up cooking, saving the surprise."

    player_name "Ready to go?"

    heroine "Yes, group leader! So sigma!"

    scene park_pathway with dissolve

    narrator "On the way to the park, we see people walking their dogs, children playing, and a decent number of people hanging out. For a Saturday, it isn’t busy at all. It’s nice and peaceful."
    narrator "Still, 'heroine name' nervously clings to my arm."

    heroine "[player_name], there are too many betas here, I’m losing aura."

    narrator "We arrive at the park, and it's even busier, but not overbearingly so."

    narrator "As we continue to walk, I spot an empty bench in the middle of the park. I decide to have her take a break. I am practically dragging her as she clings to my arm, and since I’m also carrying the lunch I prepared, both my arms are fatigued."

    # Start CG here 
    scene park_sit_cg with dissolve

    narrator "I sit her down on the bench."

    player_name "Ahhh…"

    narrator "At first, I didn’t notice because of the stressful walk, but the day is nice. The crisp autumn breeze perfectly cuts through the already pleasant heat of the sun, and the bench has a perfect view of the romantic brown and orange scenery."

    player_name "Don’t you think it’s beautiful?"

    heroine "Yeah… bro likes weather in Ohio."

    narrator "I still haven’t figured out if she thinks Ohio is the best or worst place in the world."

    player_name "Here, this might be a good place to eat."

    # Change to feeding CG based on the chosen food
    if food_choice == "Pesto Chicken Sandwich":
        scene park_feed_pesto with dissolve
    elif food_choice == "Katsu Bento Box":
        scene park_feed_bento with dissolve
    elif food_choice == "Spaghetti":
        scene park_feed_spaghetti with dissolve

    narrator "I take some of the [food_choice] and start feeding it to her."

    heroine "H-Hey! These aren’t Skibidi Slicers!? But it tastes good?!"

    narrator "She perks up after trying the [food_choice]. I haven’t had time to cook in general because I’ve been working so much. I’m glad she enjoys it."

    heroine "This is pretty sigma! Let him cook!"

    narrator "I think she’s saying it's good? That's good to hear. She didn’t like my cooking at first, but once I started improving, I know she’s enjoyed it. I should start cooking for her more often."

    player_name "Thanks, I’m glad you like it. I think I’ll try and cook for you more often. Healthier after all."

    narrator "I say as I continue to chew my [food_choice]."

    narrator "She smiles in delight. We continue eating together until both of our food is almost finished."

    heroine "Thanks [player_name]! I do enjoy the Skibidi Grimace Shake, but your cooking mogs them. In fact…"

    narrator "She reaches out and takes some of my food."

    heroine "Get fanum taxed!"

    narrator "She giggles as she steals some of my food and puts it in her mouth."

    player_name "Hey, I’ll get you back for this."

    narrator "I reach over and try to get my revenge. However, she pulls away from me, anticipating my movements. She moves surprisingly swiftly for somebody who stays home all day."

    heroine "I don’t think so, sir skibidi! I mog you!"

    scene park_pathway with dissolve
    show heroine suprised at right with dissolve

    narrator "She looks surprised as I lunge forward in an attempt to reclaim my food."

    menu:
        "Use force and take the food":
            jump force_take_food

        "Try and strategically take the food":
            jump strategic_take_food

        "Relent and let it go":
            jump let_it_go

label force_take_food:

    show heroine angry at right with dissolve

    narrator "I use the element of surprise to grab her and hold her down to reclaim some of the food I lost."

    player_name "Take this!"

    narrator "I lunge towards her in one fell swoop to take my food, but she tries to resist again."

    heroine "H-Hey [player_name]! You already tried to mog me and it didn’t work! So give u—"

    show heroine suprised at right with dissolve

    narrator "In an attempt to get away from me, she clumsily knocks over my food. In surprise, or just out of reflex, she drops her food as well."

    heroine "Grrr [player_name]! Look what you've done. I lookmaxxed this morning and everything. Now my gyatt is cooked!"

    narrator "I laugh in embarrassment as people around the park start to stare at us. Our antics have been quite noisy and may have disturbed the denizens of the park."

    player_name "O-ok, my bad. Let's go home."

    narrator "We start heading home."

    return

label strategic_take_food:

    show heroine thinking at right with dissolve

    narrator "I try to get her to go on a rant about something. Maybe a show she’s watching or a game she’s playing."

    player_name "Hey 'heroine name'? What have you been up to these days? Any cool things you've been doing?"

    narrator "'heroine name' puts her finger to her chin and ponders the question before knowing what she wants to say."

    heroine "Yeah, I’ve been grinding for the new character in my gacha game! She’s a sigma counter-based unit who can mog with massive damage if the enemy attacks at the right time…"

    narrator "As she continues, I subtly sneak my hand towards the food."

    heroine "…with this you can send most endgame betas to Ohio."

    show heroine suprised at right with dissolve

    narrator "At just the right moment, I steal some of her food successfully. As if breaking out of her trance, she notices."

    heroine "H-Hey sigma! Did you just fanum tax me? Grr, I guess that was a pretty Kai Cenat move of you, you truly are the group leader."

    narrator "She starts eating her food faster now. I decide to do the same. I know if she finishes before me, she’ll come for my food again, and I can’t have that happening."

    return

label let_it_go:

    show heroine confused at right with dissolve

    narrator "I decide to let it go. However, I must have looked sad or something because 'heroine name' speaks up."

    heroine "What’s wrong sigma? Mad that you couldn’t successfully tax me? I feel Duke Dennis, here!"

    show heroine happy at right with dissolve

    narrator "She shows me some of her food, gesturing for me to eat some."

    heroine "I am feeling like group leader right now. So eat up Turkish Quandale Dingle!"

    narrator "I guess I ended up winning in the end. I reach over and eat it off her chopstick/hand/fork (depending on the [food_choice])."

    show heroine embarrassed at right with dissolve

    narrator "She blushes with embarrassment, shocked that I ate directly from the utensil instead of picking it up myself. She backs up, hitting her elbow against the bench, and promptly drops food all over the both of us."

    heroine "[player_name]! Are you Baby Gronk? I meant for you to take the food, not eat it directly from my skibidi! Look what you've done now!"

    player_name "M-my bad! I thought you were feeding it to me! We used to do that all the time at home!"

    narrator "She blushes again as she starts cleaning herself up."

    heroine "T-t-that’s at home! This is different! Look, now there are betas talking about us!"

    narrator "Unbeknownst to me, there is a nearby old lady who heard our antics."

    grandma "Hehe, next time bring some more food, young man!"

    narrator "MIND YOUR OWN BUSINESS, GRANDMA!"

    player_name "Haha, yeah!"

    narrator "People in the park are laughing at our antics. Still, I understand why 'heroine name' might be embarrassed."

    player_name "Let's clean up and finish the rest at home."

    heroine "Y-yeah, that move was -100 aura."

    narrator "We clean up and get going."

    return



