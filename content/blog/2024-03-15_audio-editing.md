+++
title= "So You've Decided to Start a Podcast (or you need to edit audio)"
date= 2024-03-15
draft= false
[extra]
summary="A loose collection of audio tips from someone with a small amount of experience and a lot of opinions."
+++

If you've decided to start an interview or talk-heavy unscripted podcast but
don't know the first thing about audio, then this little scrawl may be for you.
I'll take you through a few basics, common pitfalls, and approaches so that your
podcast doesn't annoy me personally, which I think we can all agree is an
egregious offense. I am, of course, far from an expert on audio engineering and
recommend you seek out more authoritative resources for deeper insights and
tooling tips.

For the purposes of this post, I am specifically concerned with interview-style
podcasts or those featuring a fair bit of unscripted talking, of which there are
many examples. I am not considering podcasts with a video component, as they
introduce more constraints on editing, nor those which are generally not edited
such as those that are livestreams first and foremost.

If there are particular topics you are interested in, feel free to skip around
using this table of contents. I won't be mad, I promise.
- [Who is this for](#who-is-this-for)
- [Recording](#recording)
  - [What You Need](#what-you-need)
    - [Microphones](#microphones)
      - [Capture patterns](#capture-patterns)
      - [Other Options](#other-options)
    - [Devices](#devices)
  - [For Remote Recordings](#for-remote-recordings)
  - [For In-Person Recordings](#for-in-person-recordings)
  - [Microphone Positioning](#microphone-positioning)
  - [Soundcheck](#soundcheck)
  - [Room tone](#room-tone)
  - [A Digression on Rooms and the Treatment Thereof](#a-digression-on-rooms-and-the-treatment-thereof)
- [Editing](#editing)
  - [Why Edit?](#why-edit)
    - [1. To make it good](#1-to-make-it-good)
    - [2. To respect people's time](#2-to-respect-peoples-time)
    - [3. To present people and ideas clearly](#3-to-present-people-and-ideas-clearly)
  - [What to edit?](#what-to-edit)
  - [Editing Software](#editing-software)
  - [Noise Removal](#noise-removal)
- [In Conclusion](#in-conclusion)

# Who is this for
So I said up top that this post is about podcasts and the editing thereof,
which is not untrue, but it might be more accurate to say that this is really
about audio-centric mediums. While my particular focus is on one
realization of this, I'm hopeful that a fair bit of it should generalize to
other domains, including those which are not _just_ audio. With that in mind, lets
dive into it.

# Recording
Before you can edit, you need to record your audio in the first place. How you
choose to record things will heavily impact your end quality. And while good
editing can do a lot, audio is sometimes unsalvageable regardless of fancy
microphones and recording equipment. Chances are you already have everything you
need to record decent audio already!

## What You Need
You need a **microphone** and some **device**, probably a computer, on which to
record your audio. Owing to ***THE EVENT***, you likely have some setup already
for video conferencing whose microphone is perfectly functional.

### Microphones
There are lots of microphones out there in the world and consequently it is easy
to get overwhelmed in analysis. Fortunately for most uses, you don't need a
super high end studio microphone, but that said there are still ones you will
want to stay away from.

While their availability may make them tempting, laptop microphones and those
embedded in webcams should usually be avoided. They frequently are not of
particularly good quality and are nearly impossible to position in the right
way. Similarly, headset microphones, while a step up from laptop mics, are also
usually not the best in terms of sound quality, plus their positioning usually
makes your breath go straight into the microphone which sounds terrible and only
gets worse when plosives are considered. Thus, in general, if one is able it is
better to use some form of external microphone separate from both your device
and your headphones. This also means one thing breaking won't require you to
replace all your equipment.

Broadly speaking there are two categories of microphones to consider based on
their connection mechanism: USB and XLR. The former is what you're most likely
to find when initially searching and are generally pretty plug-and-play. If you
don't _need_ an XLR mic, probably just go with a USB. The downside of USB mics
is that you usually have a bit less control of the signal processing since it
happens all internally. The tradeoff for XLR microphones moves in the opposite
direction where you get more control of the signal, for instance the ability to
use inline preamps and manually set the gain, but it requires additional
hardware, namely a preamp and an audio interface, though frequently the audio
interface can also act as a preamp. The basic job of a preamp is to amplify the
signal provided by the microphone to usable levels with the amount of
amplification being called the *gain*---there are other qualities of preamps
that people care about, but I won't get into those here. Audio interfaces on the
the other hand are how analog signals, such as those produced by a microphone,
are turned into digital signals which we can process in an audio editor.

Chances are you don't need a bunch of fancy audio equipment, so just stick to a
nice USB microphone until that need changes. There are plenty of budget & travel
friendly options out there that will more than meet your needs.

#### Capture patterns
Okay this really gets into the weeds, but for those interested, you might be
wondering why a bunch of mics say "cardioid" and what that means. In this case
it refers to the *capture pattern* of the microphone which is the shape of the
region around the microphone in which it can pick up sound. There are a number
of different patterns, and some mics allow more than one, but cardioid patterns
tend to be the most common. In this case, the microphone picks up sound in a
heart-shaped region, hence the name, with most of the pickup being in front of
the mic with the region tailing off around the sides and back. These microphones
are good for most uses, but can pick up a fair bit of background noise which
distinguishes them from more directional microphones.

A few other patterns of potential interest are bidirectional mics, which pick up
sound on both the front and back of the microphone with less on the sides, and
omnidirectional mics which pick up sound equally in all directions. Probably
don't worry too much about this and just go with a cardioid microphone unless
you specifically need something different, like a bidirectional mic for
interviews in the same room. For those curious, Wikipedia has a
[good breakdown](https://en.wikipedia.org/wiki/Microphone#Polar_patterns)
on both these and other patterns that I did not discuss.

#### Other Options
While ideally one will have a separate microphone, it is also possible to use a
phone held upside-down as a microphone. The quality of the result will vary
depending on the phone and what type of access it gives you to the microphone,
but the results can be shockingly good sometimes.


### Devices
While the job of the microphone is to capture audio, the job of your other
device is to store it. Usually this is just the computer/phone being recorded
into but other dedicated recorders exist such as those made by
[Zoom](https://zoomcorp.com/en/us/handheld-recorders/) (no, not that one).

Whatever you are using, it is crucial that you are *directly recording* the
microphone's input. For computers, you can use the free software [Audacity][audacity] to do
this. For phones, use some audio recording app that allows you to move the sound
file off the device. For programs/software that dumps directly to a file, be
sure that it is recording to an *uncompressed or lossless* file format such as
.wav (generally uncompressed) or .flac (lossless compression) rather than lossy
compressed formats such as mp3. Since your final audio will most likely be
distributed in a lossy compressed format, using lossy raw audio can degrade
quality and introduce artifacts, analogous to image "deep frying", though
whether or not this poses an issue depends on your objectives.

## For Remote Recordings
In situations where at least one or more participants are remote, you will need
to be communicating over some form of video/audio call. **Every member (or
device) must record their local audio separately.** A voice call may be recorded
as a backup, but in most cases this should not be your primary audio track as
speakers will not be separated and ang network artifacts and glitches will be
preserved in the track. This is the most common mistake I see and it makes for
terrible audio. So if you take nothing else away from this: please please please
don't record a zoom call.

The main reason people don't have separate recording tracks for each participant
is that it requires everyone to have some willingness or technical skill which
is not always practical, particularly when conducting an interview. In such
cases there are tools such as [Zencastr](https://zencastr.com/) and the [Craig
Discord Bot](https://craig.chat/) which can help, though they are not without
tradeoffs and limitations. If no such tool works and local recordings are not an
option for some participants, using a recorded audio-call can suffice for that
participant, but to the maximum extent possible you want separate locally
recorded audio tracks for every participant.

## For In-Person Recordings
Much of the same rules apply for recording in a single shared space. In general,
it is best to have a separate microphone on every participant with the added
caveat that microphones should be configured such that minimal noise from the
other participants. Of course this requires a fair bit of equipment and is not
always practical, especially given that it requires more robust mixing equipment
than most people will have on hand. If you only have one microphone available
then try to position all speakers at around the same distance from the mic, this
is likely to be uncomfortable for highly directional microphones but can work
well for omnidirection microphones. Be sure that you do a sound check before
recording and avoid moving too far away from the mic to avoid dropoff and
otherwise bad sound.

## Microphone Positioning

Ideally you'll have some sort of stand you can place the microphone on/in. These
can come with the microphone, be a separate mounted arm, or be assembled out of
loose cardboard and books, whatever works. Bonus points if the stand/mount
provides some sort of impact isolation! Now here's the critical part, once you
have the microphone set up and have done your sound check, try to avoid touching
it. In more video driven platforms, it can be really common to see people
holding or constantly re-adjusting the microphone, you generally want to avoid
this as it creates a bunch of noise you will have to edit out, and if you don't
edit it out I will personally be sad at you. If you're using a phone as a
microphone or otherwise don't have a stand and have to hold it, try to avoid
shifting hands too much and avoid touching near the top of the mic unless
you're trying to do ASMR.

If you have a lav mic, it belongs clipped to your shirt. It is not for holding
please I beg of you. You also want to be careful to avoid ruffling the lav mic
too much as that will also create really unpleasant noises.

For other microphones, you want to position yourself about a handspan away from
the microphone if possible. The fun memory device that I usually hear for this
is to make the "hang loose"/shaka hand sign and place the pinky right in front
of the microphone and the thumb where your mouth is going to be. You'll note
this is pretty close! It can take some getting used to and you may end up
drifting further away from the microphone without realizing.

You may also wish to position the microphone at a slight angle to you that
you're speaking past it rather than directly into the microphone. This can help
avoid plosives causing you to blow air directly into the mic, but you will need
to take some care that you are still audible and aren't drifting too far out of
the main audio pickup region. If you don't have pop-filter and are having
trouble with wind noises, you can DIY one by putting a sock or some other fabric
over the microphone, as long as you don't move it during the recording.

## Soundcheck

However you choose to set up the microphone, ensure it is comfortable enough for
the length of your recording session and do your sound check with the volume and
positioning you expect to use for your actual recording. To do a soundcheck,
either directly monitor your microphone, if possible, or record to a file while
you talk in a normal tone of voice for your audio. An easy way to do this is to
just explain something quickly, like what you ate for breakfast, to the
microphone or the other people. The goal here is simply to make sure that things
sound right, which is why what you say for your soundtrack should be in your
normal recording voice and range, whatever that means for you.

In my days of operating the high-school theater sound system, we would
occasionally run into issues if the actors did their sound check differently
from the lines/songs delivered during the rest of the show, usually causing me
to frantically adjust things on the fly to avoid clipping and feedback. With any
luck feedback won't be an issue for podcast recording but if you set your
microphone *gain* too high because your soundcheck was quiet, you will end up
clipping the microphone when you get loud, causing your voice to be cut off in a
very noticeable way. If you do the opposite then your audio could be too quiet to
pick up, and some of it may be lost or drowned out by other noise.

## Room tone
Once you're ready to record, there's one more thing to do before getting to the
actual context of the episode: record some room tone. This is just recording the
sound of the room you're in without actually speaking and is surprisingly
important for later editing. This is also called "presence" in some contexts and
is the unique background noise of a particular microphone position and
configuration on the particular day of the recording. The reason you want a
sample of this is to use when "silence" is needed on a track since true silence
sounds anywhere from ambiguously wrong to like your sound system has broken.
Think of the difference between a phone call where no one is speaking and a dead
line. The difference matters here! Humans are sometimes---emphasis on
sometimes---surprisingly good at telling when certain things sound wrong, for
instance, most people can [reliably disambiguate the sound of hot water and cold
water being poured into a
glass](https://www.npr.org/2014/07/05/328842704/what-does-cold-sound-like).

Digressions aside, all you need to do is leave a few seconds of silence at the
beginning of your recording to use later as needed. And yes, everyone should do
this as each of the recording setups will have their own different room tone.

## A Digression on Rooms and the Treatment Thereof
The space you are in can affect the sound you record more than your actual
microphone. Unfortunately, few of us have direct access to a treated
space---those which have some form of alterations, often acoustic foam or
panels, to alter their sound profile---so we tend to have to make do with what
we have available. There are lots of reasons people treat a space, but most
commonly it is done to reduce echo. If echo is a problem, there are a few things
you can do to achieve more of a "dead" space. These range from practical and
expensive, like putting foam on the wall, to unhinged yet effective, like
recording inside your closet---literally, the hanging clothes do a good job of
blocking sound reflection. Most typically people try to put up some fabric, or
create a DIY sound shield around their microphone. Cardboard can also be used to
make some DIY sound panels by aligning the corrugations perpendicular to the
wall/aligned with the sound source. Some people also just hang curtains around
their desk from a collapsible lattice made of PVC piping. There are a lot of
options! But best not to seek them out until it becomes a problem since
treatment efforts can easily become a Serious Project™️.

# Editing
So on the whole I'll have a bit less to say on this part, not because editing is
simple but because it is such a deep area that I can't possibly cover it in
robust detail and because my knowledge is limited to the particular types of
audio editing I have done in the past, namely straightforward interview and
voiceover. For more complex editing like one might find in audio fiction, you'd
be better off consulting an audio engineer!

## Why Edit?
Editing, broadly speaking, is the process by which we take our raw audio and
alter it to best meet our goals for whatever it is we're making. And in my mind,
there are a few salient reasons to edit (though this list is highly subjective
and non-exhaustive).

### 1. To make it good
Raw audio, like a rough draft, is seldom exactly what we want for our end
product. In this view, editing is the process of refining what we have until it
is good enough, with both this judgement and process being dependent on your own
goals and taste. You can lose a lot of time here if you are a perfectionist; I
know I do. I don't have good advice for recognizing when to stop polishing
something, save that done and okay is better than perfect and unfinished.

### 2. To respect people's time<a name="2-to-respect-peoples-time"></a>
With unscripted podcasts/audio, there can be a lot of functionally "dead" audio.
Jokes that didn't land, long pauses, mumbling, starting and stopping, and all
other manner of things that aren't "useful" for the end product. In this view,
the goal is to keep in only what you deem suits your objective and to cut out
everything that isn't essential. People's time is limited and when able, we
should strive to make things only as long as they need to be. This is a deeply
subjective judgement and, like the prior point, needs to be constrained by
practicality. You needn't eliminate _every_ pause and "um" in the tape.

### 3. To present people and ideas clearly
In this context I am thinking specifically about interviews and discussions, so
it is analogous to the first reason but in the opposite direction. Here the goal
is to present the other people and their ideas in the most cogent light. This
can mean a lot of things, such as reordering questions to form a clearer
narrative, cutting out unnecessary digressions in their responses, or
removing long pauses, voiced or otherwise. The potential hazard here is that
you don't want to mis-represent someone, either in their ideas or their
"essence", and it is possible to get carried away.


## What to edit?
What you want to edit depends a lot on your goals. If you are attempting to
condense an hour long interview into thirty minutes, you are going to have to
spend a fair bit of time deciding what parts are important and what you want to
communicate. If you are producing a comedy show, you'll want to consider what
jokes worked and didn't as well as their deliveries. If you're producing a
conversational podcast or a lecture, you may only care about removing background
noise, and excessive voiced pauses ("ums", "ers", and the like) but not alter or
remove large chunks of the tape.

In general editing audio takes far more time than you would expect, assuming you
are not regularly editing audio. A decent lower bound for basic edits is that it
will take you about four times as long as the actual audio segment to edit it.
This gets even longer for more complex edits or those where you're trying to
compress an hour interview into a 30 minute episode. So budget more time than
you think you need and be sure to use a variety of headphones to ensure things
are at least listenable across different devices. If there are general trends
toward audio normalization in your space, try to match whatever normalization
target is appropriate to avoid swings in loudness across different podcasts.

You'll have to balance your goals with the amount of time you have for editing.
If you don't have the time to carefully go through the whole tape and you still
want to release it, you may best benefit from just removing long pauses which
can easily be identified on the visualization. Another option is to make notes
of timestamps while recording which require edits and then only editing those,
there are plenty of programs that make this noting a single button press.

Some editing is generally better than no editing!

## Editing Software
There are a lot of options here ranging from free to
dear-god-adobe-wants-how-much??? If you don't have a lot of complex edits to do
you can get by just fine on [Audacity][audacity] and if you are willing to spend
some money, [REAPER][reaper] will more than handle your needs without breaking
the bank. There are other more expensive and specialized pieces of software, but
only seek them out if you need them and, in general, support things that don't
require an eternal subscription to use, when possible. Learning new software has
a fairly high cost, so most people tend to pick one thing and stick with it
until it creates problems.

With each of these programs, there are copious numbers of free tutorials
available online as well as documentation. These things can be unintuitive, so I
strongly encourage you to look things up! There's a lot of info out there.

## Noise Removal
Chances are that the most common non-trivial thing you'll want to do is remove
background noise. There are a number of ways to approach this. There are plenty
of free tools and plugins such as [Audacity][audacity] which can work on [some
background noise](https://manual.audacityteam.org/man/noise_reduction.html).
[iZotope](https://www.izotope.com/) also has a suite of editing plugins which
can be very helpful if you're willing to pay for them, and, while many are
prohibitively expensive, the [Elements][izotope_elements] suite tends to go on
sale regularly and meets most of the basic needs you might have. Ultimately what
you need for this depends a lot on what type of background noise you're dealing
with and what options you have to treat your recording space and your overall
budget. You can get pretty far without needing to pay for anything.


# In Conclusion
Get out there and make stuff!

[audacity]: https://www.audacityteam.org/
[reaper]: https://www.reaper.fm/
[izotope_elements]: https://www.izotope.com/en/products/elements-suite.html
