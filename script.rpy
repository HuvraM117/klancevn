# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Lance")
define k = Character("Keith")
define h = Character("Hunk")
define p = Character("Pidge")
define s = Character("Shiro")
define a = Character("Allura")
define c = Character("Coran")
define n = Character("")


# The game starts here.

label start:

    scene bg Kitchen
    show Hunk at right
    show Lance at Left

    h "I’m just saying, that at this rate, we’re going to have to turn around and restock. I’m not working with just a few vegetables, some weird alien excuse for flour and—"
    n "Lance watches with dull eyes as Hunk pokes around the cabinet."
    h "... stop by one of those trade planets Allura mentioned."
    n "One of the mice scurries across the molding of the far wall and Lance wonders what he’ll do today. Probably train. That’s what Shiro would want him to do anyway."
    h "I‘m not working with just a few vegetables, some weird alien excuse for flour and—"
    h "Lance? You in there, bro?"
    l "Huh? Oh, yeah. Just... zoned out for a bit there, dude. Keep going. What’s up with the flour?"
    h "Ok, it’s not really flour and I can’t really bake with it, but that’s not the point."
    h "Pidge and I are making another presentation to try to convince Coran that humans need actual things like fruits and protein in their diet. 
    h "I don’t think the last one really stuck. But this time we’re really planning on one of those crowd pleasers! Who doesn’t like fireworks, am I right?  You wanna help out?"
    menu:
        "Not really feeling it, my dude...":
            jump A1
        "Oh, you came to the right guy!"
            jump A2

label A1:

label A2:





    return
