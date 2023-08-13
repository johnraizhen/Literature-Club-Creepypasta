label zero:
    scene white
    pause 3
    scene black
    with Dissolve(1.0)
    pause 1.0
    call screen dialog("A fallen history spoke from his perspective.", ok_action=Return())
    call screen dialog("Someone sent a strange game to him.", ok_action=Return())
    call screen dialog("It's about a young boy playing a game.", ok_action=Return())
    call screen dialog("What make you intense... even you see something... terrifying?", ok_action=Return())
    call screen dialog("He wouldn't be a victim, is he?", ok_action=Return())
    show screen console_screen
    $ run_input(input="...")
    pause 1.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    "Email System" "You got 1 email."
    "H-huh?"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    call screen dialog("A fake console come out of nowhere. It's on the top left.", ok_action=Return())
    call screen dialog("...", ok_action=Return())
    call screen dialog("...", ok_action=Return())
    call screen dialog("It appears that it was not made by her...", ok_action=Return())
    "..."
    "Anonymous" "Just download this game and play."
    "Anonymous" "Numerous glitches ahead inside .EXE. And I don't see other .chr files in characters folder..."
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    call screen dialog("It was programmed as not-so-tool...", ok_action=Return())
    call screen dialog("Was it belong to him?", ok_action=Return())
    call screen dialog("Or his perspective?", ok_action=Return())
    "W-W-What is this?"
    "Is this some kind of .EXE game or creepypasta-based game?"
    "or a mod?"
    call screen dialog("He opened a strange game.", ok_action=Return())
    call screen dialog("Which it means...", ok_action=Return())
    call screen dialog("The tale of his terror...", ok_action=Return())
    call screen dialog("...has begun.", ok_action=Return())
    call screen dialog("The Literature Club begins.", ok_action=Return())