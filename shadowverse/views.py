from django.shortcuts import render, HttpResponse,redirect
from .models import Reflection
from .models import Poll


# render file
def index(request):
    return render(request, 'shadowverse/index.html')


# story page
def story_page(request, trope):

    stories = {
        "mafia": {
            "title": "His Past Trained Him",
            "content": """
His past didn’t break him.
It trained him.

Feel nothing.
Trust no one.
Leave before you’re left.

That was the rule.

And then he saw her.

Not dramatic.
Not cinematic.

Bas ek normal si ladki…
with eyes
that didn’t look afraid of him.

That unsettled him.

Weaknesses usually run.
She didn’t.

So he stayed cold.

Short replies.
Sharp tone.
“I don’t like you.”

Par uski nazar?
Kabhi nahi hatti.

He noticed everything.

Who she talks to.
Why she was quiet that day.
Why she winced slightly
when she thought no one saw.

He memorized her routine
like it was a threat map.

Dushman us tak pahunchne ki himmat bhi nahi karte the.

Not because she was powerful.

Because she was his.

She never saw the shadows shift
before danger could reach her.

Problems disappeared.
Rumors died quietly.
People backed off.

Aur use laga
life bas thodi si meherbaan hai.

When pain curled inside her body —
he didn’t ask.

Chocolate appeared.
A heating pad.
Silence.
No teasing.

Bas ek line —
“Rest. I’ll handle the world.”

When she once said softly,
“I wish…”
he remembered.

Weeks later,
her wish stood in front of her
wrapped in quiet effort.

No credit taken.

He has never stepped into a kitchen.

Par us din —
burned fingers.
Messy apron.
Unsteady breath.

And almost embarrassed, he said —
“Apke liye…
yeh mafia kuch bhi ban jayega.”

He doesn’t bow.
He doesn’t bend.
He doesn’t kneel.

Log usse dekh ke darte hain.

But in front of her?

His pride lowers
without being asked.

He says,
“Stay away.”

But what he means is —

“Touch her
and you won’t live to regret it.”

Cold voice.
Controlled rage.

Obsession?
Maybe.

Protection?
Always.

And when she laughs —
really laughs —

for one unguarded second,
the war inside him goes silent.

""",
            "accent": "mafia",
            "trope_name": "Mafia Romance",
            "final_question": "Was he toxic, or just a man who only knew how to love like something worth defending?"
        },

        "office": {
            "title": "Between Meetings",
            "content": """
Office mein sirf meetings nahi hoti…
kuch nazrein bhi secret rehti hain.

Conference room full hota hai.
Files. Screens. Deadlines.

But his attention?
Always slightly tilted.

Not toward the presentation.
Toward her.

She sits straight.
Professional. Calm.

Jaise kuch hai hi nahi.

He asks tough questions.
Interrupts her mid-sentence.
Cold tone.

Employees think he’s being harsh.

Unhe kya pata…
that’s how he hides it.

Kabhi kabhi unki fingers brush ho jaati
while passing a file.

Bas ek second.

Par us ek second mein
boardroom ki hawa ruk jaati hai.

She pulls her hand back.

He doesn’t.

When her team manager overloads her—
extra reports, impossible deadlines—

She doesn’t complain.

She just works.

Late night cabin light still on.

He notices.

Next morning —
half her workload disappears.

Transferred.

Approved.

Handled.

He calls her in.

“Focus on priority.”

Boss tone.

But softer.

When she looks tired—
really tired—

He makes her sit.

Not across the desk.

Beside him.

And for a few minutes
he doesn’t talk about targets.

He listens.

Gossip.
Random frustrations.
Office politics.

Not as a boss.

As someone who remembers
how her voice sounds when she’s overwhelmed.

If someone raises their voice at her—
even slightly—

Later, cabin door closed.

He apologizes.

Not loudly.

Just —
“I won’t let that happen again.”

She never asked him to.

Meetings.

Long table.

Serious faces.

Under the table—

his fingers find hers.

Not obvious.
Not careless.

Just a slow hold.

His thumb brushing lightly
as if reminding her—

“I’m here.”

If another manager
looks at her for too long—

His hand tightens.

And without looking at her,
he says something sharp enough
for the room to shift.

Possession doesn’t need volume.

It needs confidence.

There were moments
when truth almost surfaced.

When silence felt heavier than secrecy.

She would panic.

“What if someone finds out?”

He would step closer.

Careful.

Measured.

And in the privacy of his cabin—
one quiet hug.

No desperation.

Just certainty.

Jaise keh raha ho —
“Main hoon. Sambhal lunga.”

And somehow—

the fear dissolves.

No public displays.
No dramatic confessions.

Bas ek look.

The kind that says —
“You’re mine.”

And the kind that answers —
“I know.”
""",
            "accent": "office",
            "trope_name": "Office Romance",
            "final_question": """
Was it just professionalism…

or a love
hidden
between glass walls,
signed contracts,
and stolen touches
under conference tables?
"""
        },

        "enemies": {
            "title": "Pride in Disguise",
            "content": """
They fight like it’s routine.

Every conversation
turns into a battlefield.

He rolls his eyes.
She crosses her arms.

One second together—
and the air already feels charged.

They can’t stand each other.

At least that’s what they say.

She calls him arrogant.
He calls her dramatic.

“Tum unbearable ho,” she snaps.

“Then stop standing so close,” he replies.

But neither of them steps back.

When she laughs with someone else—
really laughs—

his jaw tightens.

“Jealous?” she asks lightly.

He scoffs.

“Please.”

Par uski aankhon mein jo aag jalti hai—
woh rivalry nahi hoti.

When someone looks at her the wrong way—
his reaction is instant.

“She can handle herself,” he says coldly.

But he still steps in front of her.

Too protective
for someone who claims indifference.

They argue again.

Voices lower.
Breathing heavier.

“You don’t get to control me,” she says.

“Then stop acting like you don’t need me,” he fires back.

Silence.

One second too long.

Her eyes drop to his lips.

His hand catches her wrist—
not harsh.
Just enough
to stop her from walking away.

“Say it,” he whispers.
“Say you don’t care.”

She tries.

Nothing comes out.

Because truth trembles
when ego stands in the way.

Tum kehti ho dushman hoon main,
phir meri taraf dekhte waqt
saans kyun ruk jaati hai?

He lets go.

But not really.

The argument spills outside.

Doors slam.

Rain starts.

Heavy.
Unforgiving.

She walks fast.

He follows.

“Stop,” he says.

She doesn’t.

Water runs down her face.
Hair clinging to her cheeks.

“You don’t get to walk away every time,” he snaps.

She turns sharply.

“And you don’t get to decide everything!”

Thunder cracks.

For a second—
they’re just standing there.

Drenched.
Breathing hard.
Too close.

“You think I don’t care?” she challenges.

He steps closer.

“Then prove you don’t.”

Rain louder now.

Her fingers fist into his shirt—
not pulling him closer.

Just holding.

As if letting go
would mean losing.

He cups her face.

Firm.
Controlled.

“Say you hate me,” he whispers.

She opens her mouth.

Nothing.

Bas saans.
Bas dhadkan.
Bas woh lamha
jo nafrat se thoda zyada tha.

He leans in.

Stops.

One breath away.

And that’s their curse.

They’re always
one breath away.

“She’s my enemy,” he tells the world.

Pause.

“But she’s mine to deal with.”

Every insult hides protection.
Every argument hides fear.

Fear of surrendering.
Fear of losing.

Because love would mean
someone wins.

And neither of them
knows how to lose.

Dushmani ka naam diya tha humne is rishte ko,
par har ladai ke baad
dil wahi ruk jaata tha
jahaan tum khadi hoti thi.

""",
            "accent": "enemies",
            "trope_name": "Enemies to Lovers",
            "final_question": "Was it really war: or just two stubborn hearts pretending they weren’t already chosen?"
        },

        "hidden": {
            "title": "Six Seconds Too Long",
            "content": """
Six Seconds Too Long

Sab ke liye woh sirf Professor hai—
calm. composed. untouchable.

For her?

A man she secretly calls
home.

Years older.
Years steadier.
Too disciplined to slip.

Except around her.

In lecture hall—

He doesn’t look at her first.

He knows better.

He asks questions sharply.

“Miss Sharma, would you like to answer?”

The entire class turns.

She knows the answer.

He knows she knows.

Still, he waits.

That pause—

always one second longer than necessary.

Sometimes he challenges her arguments
just to see that spark in her eyes.

“You’re confident,” he says coolly.

She replies softly,
“Only when I’m right, sir.”

The class laughs.

But they don’t notice
how his jaw tightens slightly—
not in anger.

In control.

Once, during a presentation—

she forgot a line.

Just one.

He walked closer.

Too close.

Low voice. Calm.

“Focus.”

Not harsh.

Not gentle.

Just… for her.

Her heartbeat forgot the syllabus.

The class thought he was being strict.

They didn’t see
his fingers brush the desk near hers—
never touching.
But close enough to burn.

When someone else answers confidently,
he nods politely.

When she does—

his eyes soften.

Just a fraction.

He never praises her too much.

Never defends her too openly.

But when someone tries to outshine her
with unnecessary arrogance—

his questions become ruthless.

Not for her.

Never for her.

Outside the classroom—

“Sir.”

Inside the apartment—

she steals his hoodie
and he pretends not to notice.

Two mugs on the counter.

Two laptops open.

He corrects assignments.

She corrects his silence.

Sometimes she teases him at home—

“You enjoy embarrassing me in class.”

He looks at her calmly.

“If I wanted to embarrass you…
you’d know.”

And suddenly—

the air changes.

Not inappropriate.

Not loud.

Just thick with things unsaid.

They live like strangers to survive.

But sometimes—

in the middle of grading papers—

he pulls her notebook closer and says,

“You argued better today.”

That’s his version of
“I’m proud of you.”

Sometimes she stands behind him
while he works.

Her chin resting on his shoulder.

He doesn’t turn.

But his hand finds hers.

Automatically.

Like muscle memory.

The world sees:

Professor × Student.

Authority × Discipline.

Distance × Rules.

They don’t see—

the marriage certificate hidden in a locked drawer.

The ring she wears only at night.

The way he whispers her name
without the word “Miss.”

Love isn’t loud.

It survives in teasing questions.

Lingering glances.

Desk-side corrections.

Shared silence in the same apartment.

And eyes that hold each other
for six seconds too long.


""",
            "accent": "hidden",
            "trope_name": "Hidden Vows",
            "final_question": "Was it forbidden? Or simply a love disciplined enough to survive the world?"
        }
    }

    
    story = stories.get(trope)

    if not story:
        return HttpResponse("Story not found.")

    # ✅ HANDLE POST (Submit / Cancel)
    if request.method == "POST":

        # 🔹 If Cancel clicked
        if "cancel_action" in request.POST:
            request.session["last_trope"] = story["trope_name"]
            return redirect("shadow_chamber")

        # 🔹 If Submit clicked
        reflection_text = request.POST.get("reflection_text")
        trope_name = story["trope_name"]

        if reflection_text:
            new_reflection = Reflection.objects.create(
                trope_name=trope_name,
                reflection_text=reflection_text
            )

            # Save reflection privately
            request.session["reflection_id"] = new_reflection.id

        return redirect("shadow_chamber")

    # ✅ GET REQUEST
    return render(request, "shadowverse/story.html", {
        "story": story,
        "accent": story["accent"],
        "trope_name": story["trope_name"],
        "final_question": story["final_question"],
    })

# Temporary Shadow Chamber View (For Testing)

def shadow_chamber(request):

    # 🔹 Get session data
    reflection_id = request.session.get("reflection_id")
    last_trope = request.session.get("last_trope")

    latest_reflection = None
    observation = None
    observation_type = None
    poll_submitted = False

    # 🔹 Handle Poll Submission
    if request.method == "POST" and request.POST.get("selected_trope"):
        selected = request.POST.get("selected_trope")

        Poll.objects.create(selected_trope=selected)

        poll_submitted = True

    # 🔹 Shayari Map
    shayari_map = {
        "Mafia Romance": {
            "normal": """Some loves don’t hold hands.
They stand guard quietly.

Log use andhera samajhte hain,
par woh bas kisi ko mehfooz dekhna chahte hain.

There is nothing wrong
with wanting to protect what feels like home.""",

            "soft": """Even unspoken protection
comes from somewhere real.

Kabhi kabhi dil bas mehfooz rehna chahta hai.
And that is enough."""
        },

        "Office Romance": {
            "normal": """Some connections don’t need confession.
They grow in small pauses.

Sheeshe ke kamron mein bhi,
dil apni jagah bana leta hai.

Not every love needs to be loud
to be real.""",

            "soft": """Even silence can carry meaning.

Sheeshe ke beech bhi,
dil chup chaap baat kar leta hai."""
        },

        "Enemies to Lovers": {
            "normal": """You called it rivalry.
Dil ne use pehle hi pehchaan liya tha.

Har ladai ke baad bhi,
wahi sukoon milta tha.

Sometimes we argue the most
with what we’re afraid to lose.""",

            "soft": """Har behas ke peeche
kuch rukta hua sa ehsaas hota hai.

Kabhi kabhi zid bhi
sirf darr hoti hai."""
        },

        "Hidden Vows": {
            "normal": """Not every promise is spoken.
Kuch rishte awaaz ke bina jeete hain.

Duniya samjhe ya na samjhe,
woh apni jagah theek hote hain.

Some loves survive
because they choose silence over noise.""",

            "soft": """Jo chup reh kar bhi nibh jaye,
woh kam nahi hota.

Har sach ko duniya ki zarurat nahi hoti."""
        }
    }

    # 🔥 PRIORITY 1 — Cancel (Soft Shayari)
    if last_trope:
        observation = shayari_map.get(last_trope, {}).get("soft")
        observation_type = "soft"
        request.session.pop("last_trope", None)

    # 🔥 PRIORITY 2 — Submitted Reflection (Normal Shayari)
    elif reflection_id:
        latest_reflection = Reflection.objects.filter(id=reflection_id).first()

        if latest_reflection:
            trope_name = latest_reflection.trope_name
            observation = shayari_map.get(trope_name, {}).get("normal")
            observation_type = "normal"

    return render(request, "shadowverse/shadow_chamber.html", {
        "reflection": latest_reflection,
        "observation": observation,
        "observation_type": observation_type,
        "poll_submitted": poll_submitted
    })