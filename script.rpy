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
    $nice = 0
    $rude = 2

    scene bg Kitchen
    show Hunk at right
    show Lance Casual at left

    h "I’m just saying, that at this rate, we’re going to have to turn around and restock. I’m not working with just a few vegetables, some weird alien excuse for flour and—"
    n "Lance watches with dull eyes as Hunk pokes around the cabinet."
    h "... stop by one of those trade planets Allura mentioned."
    n "One of the mice scurries across the molding of the far wall and Lance wonders what he’ll do today. Probably train. That’s what Shiro would want him to do anyway."
    h "I‘m not working with just a few vegetables, some weird alien excuse for flour and—"
    h "Lance? You in there, bro?"
    l "Huh? Oh, yeah. Just... zoned out for a bit there, dude. Keep going. What’s up with the flour?"
    h "Ok, it’s not really flour and I can’t really bake with it, but that’s not the point."
    h "Pidge and I are making another presentation to try to convince Coran that humans need actual things like fruits and protein in their diet."
    h "I don’t think the last one really stuck. But this time we’re really planning on one of those crowd pleasers! Who doesn’t like fireworks, am I right? You wanna help out?"
    menu:
        "Not really feeling it, my dude...":
            jump A1
        "Oh, you came to the right guy!":
            jump A2

label A1:
    l "Not really feeling it, my dude, but I’ll totally check out those fireworks when you’re done."
    h "Oh, that's too bad. But the offer's open, buddy! And, yeah, they’re going to be totally amazing."
    jump main1

label A2:
    l "Oh, you came to the right guy! I am Coran’s favourite, after all. He’s gonna be food goo in these hands."
    h "Knew I could count on my best bro! Also, that’s kinda gross, dude."

label main1:
    scene bg Kitchen
    show Shiro at center
    show Hunk at right
    s "Lance. Hunk. The princess wants us on the bridge."
    n "Lance slowly slides off of his stool, his muscles protesting every movement he makes."
    n "He doesn’t have the energy to wonder why Hunk feels up for puttering around in the kitchen when all he can do is lean heavily on the counter while his eyelids droop."
    n "He’s been on one too many deadly recon missions running for his life and too many crusty diplomatic dinners where he’s left tostare at the ceiling while looking pretty so Allura can do all the talking."
    n "The last thing he needs right now is another mission. But who is he to tell the fair princess no?"
    n "He tries anyway."
    l "Is this mission really all that important? I mean, we just got back from the last escapade."
    l "My stomach is still rolling and my bruises have bruises. We should be fine for at least a little while, right?"
    s "Orders are orders.The sooner we get this done, the sooner we can rest."
    n "Lance groans as he drapes himself over the counter tops. Hunk places a reassuring hand on his shoulder."
    h "Come on, Lance. Maybe it’ll be a fun mission! Like, we’ll get to see another space mall!"
    h "Or better yet, a space farmer’s market- Where the vacuum of space seals in the freshness! Farm to table, man. Healthy and tasty."
    l " Yeah, I guess..."
    s "Get moving, you two. She said it was important. Oh, and Lance..."
    l "Yeah?"
    s "Go grab Keith, will you?"
    menu:
        "Why do I have to do it?":
            jump B1
        " I don’t know... ":
            jump B1

label B1:
    l "He hates me right now!"
    s "Lance, please. We don’t have time for dramatics."
    l "But I really mean it this time!"
    jump main2

label B2:
    l "I don't think Keith is in the mood to listen to me."
    s "Keith just needs some space. It’s been a long week for all of us, but the Princess wants us all on the bridge ASAP."
    s "Coran and Pidge are already there. Since I have to discuss some things with Hunk, you’re the only one free to get him."
    s "If Keith doesn’t come with, I’ll do it, but how about giving it a shot, Lance?"
    l "Shiro, I really don’t think..."
    jump main2

label main2:
   s "{i}*sighs*{/i}"
   s "I know we’re all tired Lance, but, please, do it for Voltron. For defending the universe."
   l "...okay."
   jump training1

label training1:
    scene bg train
    show Keith Casual
    show Lance Casual
    n "Keith is completely focused on his sparring match, sweat dripping from his forehead as he clashes with the bot, sword arcing through the air gracefully."
    n "It’s a sight to see until Lance realizes that Keith knows he’s there."
    n "Keith shoots him a dirty look as he stabs his sword through the heart of the bot, deactivating it."
    menu:
        "We got another mission so go get cleaned up.":
            $rude += 1
            jump training2

        "Nice sword stuff you got going on there. Can I interrupt for a sec?":
            $nice += 1
            jump training2

label training2:
    k "..."
    n "Keith ignores Lance, placing his foot on the chest of the bot and violently yanks his sword back out."
    n "The bot sparks, and then is still."
    l "I know you heard me, Keith."
    k "..."

    return
