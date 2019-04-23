LINES = [
    "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iure harum "
    "suscipit aperiam aliquam ad, perferendis ex molestias reiciendis "
    "accusantium quos, tempore sunt quod veniam, eveniet et necessitatibus "
    "mollitia. Quasi, culpa.",
    "Hi, my name is Alex and I am 18 years old.",
    "Oh, my sweet summer child, what do you know of fear? Fear is for the "
    "winter, my little lord, when the snows fall a hundred feet deep and the "
    "ice wind comes howling out of the north. Fear is for the long night, "
    "when the sun hides its face for years at a time, and little children are "
    "born and live and die all in darkness while the direwolves grow gaunt "
    "and hungry, and the white walkers move through the woods.",
    "Well, technology is a glittering lure, but there is the rare occasion "
    "when the public can be engaged on the level beyond flash, if they have a "
    "sentimental bond with the product. My first job, I was in house at a fur "
    "company with this old pro copyrighter, a Greek named Teddy. And Teddy "
    "told me the most important idea in advertising is \"new.\" Creates an "
    "itch. You simply put your product in there as a kind of calamine lotion. "
    "He also talked about a deeper bond with the product. Nostalgia. It's "
    "delicate but potent. Teddy told me that in Greek, nostalgia literally "
    "means the pain from an old wound. It's a twinge in your heart far more "
    "powerful than memory alone. This device isn't a space ship. It's a time "
    "machine. It goes backwards, forwards. It takes us to a place where we "
    "ache to go again. It's not called the Wheel. It's called the Carousel. "
    "It lets us travel the way a child travels. Around and around and back "
    "home again to a place where we know we are loved.",
    ]

TEXTS = (
    (LINES[0], 38, 'l',
     '''Lorem ipsum dolor sit amet,
consectetur adipisicing elit. Iure
harum suscipit aperiam aliquam ad,
perferendis ex molestias reiciendis
accusantium quos, tempore sunt quod
veniam, eveniet et necessitatibus
mollitia. Quasi, culpa.'''),
    (LINES[0], 30, 'c',
     ''' Lorem ipsum dolor sit amet,
consectetur adipisicing elit.
 Iure harum suscipit aperiam
  aliquam ad, perferendis ex
     molestias reiciendis
accusantium quos, tempore sunt
   quod veniam, eveniet et
   necessitatibus mollitia.
        Quasi, culpa.'''),
    (LINES[0], 50, 'r',
     '''           Lorem ipsum dolor sit amet, consectetur
     adipisicing elit. Iure harum suscipit aperiam
   aliquam ad, perferendis ex molestias reiciendis
       accusantium quos, tempore sunt quod veniam,
 eveniet et necessitatibus mollitia. Quasi, culpa.'''),
    (LINES[0], 45, 'j',
     '''Lorem   ipsum  dolor  sit  amet,  consectetur
adipisicing elit. Iure harum suscipit aperiam
aliquam    ad,   perferendis   ex   molestias
reiciendis  accusantium  quos,  tempore  sunt
quod   veniam,   eveniet   et  necessitatibus
mollitia. Quasi, culpa.'''),

    (LINES[1], 20, 'l',
     '''Hi, my name is Alex
and I am 18 years
old.'''),
    (LINES[1], 20, 'c',
     '''Hi, my name is Alex
 and I am 18 years
        old.'''),
    (LINES[1], 20, 'r',
     ''' Hi, my name is Alex
   and I am 18 years
                old.'''),
    (LINES[1], 20, 'j',
     '''Hi,  my name is Alex
and  I  am  18 years
old.'''),

    (LINES[2], 35, 'l',
     '''Oh, my sweet summer child, what do
you know of fear? Fear is for the
winter, my little lord, when the
snows fall a hundred feet deep and
the ice wind comes howling out of
the north. Fear is for the long
night, when the sun hides its face
for years at a time, and little
children are born and live and die
all in darkness while the
direwolves grow gaunt and hungry,
and the white walkers move through
the woods.'''),
    (LINES[2], 10, 'c',
     '''  Oh, my
  sweet
  summer
  child,
 what do
 you know
 of fear?
 Fear is
 for the
winter, my
  little
lord, when
the snows
  fall a
 hundred
feet deep
 and the
 ice wind
  comes
 howling
out of the
  north.
 Fear is
 for the
   long
  night,
 when the
sun hides
 its face
for years
at a time,
and little
 children
 are born
 and live
 and die
  all in
 darkness
while the
direwolves
grow gaunt
   and
 hungry,
 and the
  white
 walkers
   move
 through
the woods.'''),
    (LINES[2], 67, 'r',
     '''   Oh, my sweet summer child, what do you know of fear? Fear is for
the winter, my little lord, when the snows fall a hundred feet deep
   and the ice wind comes howling out of the north. Fear is for the
   long night, when the sun hides its face for years at a time, and
little children are born and live and die all in darkness while the
       direwolves grow gaunt and hungry, and the white walkers move
                                                 through the woods.'''),
    (LINES[2], 15, 'j',
     '''Oh,   my  sweet
summer   child,
what   do   you
know  of  fear?
Fear is for the
winter,      my
little    lord,
when  the snows
fall  a hundred
feet  deep  and
the   ice  wind
comes   howling
out    of   the
north.  Fear is
for   the  long
night, when the
sun  hides  its
face  for years
at  a time, and
little children
are   born  and
live   and  die
all in darkness
while       the
direwolves grow
gaunt       and
hungry, and the
white   walkers
move    through
the woods.'''),

    (LINES[3], 21, 'l',
     '''Well, technology is a
glittering lure, but
there is the rare
occasion when the
public can be engaged
on the level beyond
flash, if they have a
sentimental bond with
the product. My first
job, I was in house
at a fur company with
this old pro
copyrighter, a Greek
named Teddy. And
Teddy told me the
most important idea
in advertising is
"new." Creates an
itch. You simply put
your product in there
as a kind of calamine
lotion. He also
talked about a deeper
bond with the
product. Nostalgia.
It's delicate but
potent. Teddy told me
that in Greek,
nostalgia literally
means the pain from
an old wound. It's a
twinge in your heart
far more powerful
than memory alone.
This device isn't a
space ship. It's a
time machine. It goes
backwards, forwards.
It takes us to a
place where we ache
to go again. It's not
called the Wheel.
It's called the
Carousel. It lets us
travel the way a
child travels. Around
and around and back
home again to a place
where we know we are
loved.'''),
    (LINES[3], 58, 'c',
     ''' Well, technology is a glittering lure, but there is the
rare occasion when the public can be engaged on the level
  beyond flash, if they have a sentimental bond with the
  product. My first job, I was in house at a fur company
 with this old pro copyrighter, a Greek named Teddy. And
 Teddy told me the most important idea in advertising is
  "new." Creates an itch. You simply put your product in
there as a kind of calamine lotion. He also talked about a
deeper bond with the product. Nostalgia. It's delicate but
 potent. Teddy told me that in Greek, nostalgia literally
 means the pain from an old wound. It's a twinge in your
  heart far more powerful than memory alone. This device
     isn't a space ship. It's a time machine. It goes
backwards, forwards. It takes us to a place where we ache
 to go again. It's not called the Wheel. It's called the
   Carousel. It lets us travel the way a child travels.
Around and around and back home again to a place where we
                    know we are loved.'''),
    (LINES[3], 12, 'r',
     '''       Well,
  technology
        is a
  glittering
   lure, but
there is the
        rare
    occasion
    when the
  public can
  be engaged
on the level
      beyond
   flash, if
 they have a
 sentimental
   bond with
the product.
    My first
  job, I was
 in house at
       a fur
company with
this old pro
copyrighter,
     a Greek
named Teddy.
   And Teddy
 told me the
        most
   important
     idea in
 advertising
   is "new."
  Creates an
   itch. You
  simply put
your product
 in there as
   a kind of
    calamine
  lotion. He
 also talked
     about a
 deeper bond
    with the
    product.
  Nostalgia.
        It's
delicate but
     potent.
  Teddy told
  me that in
      Greek,
   nostalgia
   literally
   means the
pain from an
  old wound.
      It's a
   twinge in
  your heart
    far more
    powerful
 than memory
 alone. This
device isn't
     a space
ship. It's a
        time
 machine. It
        goes
  backwards,
forwards. It
 takes us to
     a place
    where we
  ache to go
 again. It's
  not called
  the Wheel.
 It's called
         the
Carousel. It
     lets us
  travel the
 way a child
    travels.
  Around and
  around and
   back home
  again to a
 place where
  we know we
  are loved.'''),
    (LINES[3], 27, 'j',
     '''Well,   technology   is   a
glittering  lure, but there
is  the  rare occasion when
the  public  can be engaged
on  the level beyond flash,
if  they have a sentimental
bond  with  the product. My
first  job,  I was in house
at  a fur company with this
old   pro   copyrighter,  a
Greek   named   Teddy.  And
Teddy   told  me  the  most
important      idea      in
advertising    is    "new."
Creates an itch. You simply
put  your  product in there
as   a   kind  of  calamine
lotion.   He   also  talked
about  a  deeper  bond with
the   product.   Nostalgia.
It's  delicate  but potent.
Teddy   told   me  that  in
Greek,  nostalgia literally
means  the pain from an old
wound.  It's  a  twinge  in
your    heart    far   more
powerful than memory alone.
This  device  isn't a space
ship.  It's a time machine.
It      goes     backwards,
forwards.  It takes us to a
place  where  we ache to go
again.  It's not called the
Wheel.   It's   called  the
Carousel. It lets us travel
the  way  a  child travels.
Around  and around and back
home again to a place where
we know we are loved.'''),
    )

TESTS = {'Basics': [], 'Extra': []}
for n, (*args, formatted_text) in enumerate(TEXTS):
    category = ('Basics', 'Extra')[n >= 4]
    TESTS[category].append({'input': args,
                            'answer': formatted_text})
