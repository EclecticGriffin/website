+++
title="On Asking the Wrong Questions"
date=2024-02-20
[extra]
summary="This is the story of my first real research project and why I regret working on it."
+++

I became involved in research via an REU (Research Experience for
Undergraduates) in the summer after my sophomore year. While I learned a lot
from the experience, a good deal of it wasn't positive: I learned the taste of
burnout, the ways in which my brain splits apart under extensive stress and
sleep deprivation, and, crucially, that a project's societal impact and ethical
ramifications require deep consideration rather than simple good intentions.
This last point did not properly sink in until some time later, but it's what I
want to talk about today.

My involvement with the project only lasted for 10 weeks or so and as a
stressed-and-depressed---albeit undiagnosed at the time---undergrad alone in an
unfamiliar city, I hardly made major contributions in a research sense. This is
not to say I did not do work, if anything the experience taught me to question
what drove me to sacrifice my health and wellbeing to meet unreasonable
expectations, but that most of what I did was data scraping, processing, and
visualization, rather than "deep research work". But I was an undergrad just
getting started with research so this was all to be expected. Yet even given all
this, I still feel a great deal of guilt around this project because I now
believe it to have been asking the wrong question and potentially harmful.

The elevator pitch for the REU project ended up being quite simple. When
clustering data, a simple and straightforward choice is using the K-Means
algorithm. Simply put in how many clusters you'd like to find and let the
computer do the rest. K-Means works by selecting a number of centroids equal to
the number of desired clusters, organizing the data by nearest centroid, and
finally recomputing the centroids for the new clusters. The process repeats
iteratively until convergence.

The thesis of this project was that people don't often alter the default
settings for the algorithm, like the desired number of clusters and
initialization parameters, and as such could be producing "wrong"
clusters---wrongness here is a somewhat subjective quality---depending on their
choices or lack thereof. In particular, the project focused on the distance
metric used in the algorithm which in most cases defaults to euclidean distance,
i.e., a straight line between two points. This is a reasonable choice for many
categories of data but is not suitable for data which represents points on the
Earth. Believe it or not, the Earth is a sphere so using euclidean distance
instead of a geodesic method---one which accounts for the curvature of the
earth---can produce different results if the data points occur over a large
enough space, like say that of a city.

So far, it seems reasonable right? Simply some concern about the accuracy of
clustering algorithms under certain circumstances, nothing too sinister no? I'm
sure a few of you can see where this is going. Unfortunately the data whose
clusters I was comparing was crime data from the city the REU was taking place
in, since it was readily available online.

This means that---much to my horror---the project was effectively about
"improving" predictive policing. At the time, I didn't entirely see the problem
in this since wouldn't it be better if the clusters were "more accurate"?
Suppose that there are two clusters, **L** and **H**, in our data. **L** is considered
*low-risk* while **H** is considered *high-risk*. If the clusters change based on the
choice of distance metric then some people could be moved from **L** to **H** or
vice-versa.

Thus the argument goes that if the "correct" cluster for some over-policed
populations was **L** rather than **H**, then you could say that the euclidean
clustering has the potential to cause harm to that population and is thus
biased. We can then attempt to quantify the "bias potential" based on the
percentage of such communities that were "misclassified" between the two cluster
maps.

But of course, this reasoning can also cut the other direction and could just as
easily suggest that communities of marginalized people were under-policed, i.e.,
moving people from **L** to **H**. So ultimately the argument would simply have
to be that the clusters produced with euclidean distance are wrong in their
essence, rather than impact, and geodesic distance should be used instead.

In my opinion, the end result is something that at best changes very little, and
at worse grants legitimacy to the police and the practice of predictive
policing, which we know to be deeply flawed and structurally racist. Technology
is inherently political. If you work with the police, if you give them better
tools, or suggest improvements to their practices, then you are aiding a deeply
cruel and fundamentally racist organization designed to mete out violence on the
populace. And that should be unacceptable to you.

I am extremely thankful that my time with the project was limited and that my
work likely had little to do with future efforts/impacts. And to the best of my
knowledge, there wasn't major adoption of the work. But it still haunts me and
acts as a warning going forward.

The project, as I see it, was asking the wrong question. While there may be
answers to "Can the choice of distance metric alter data clustering on
geographic data? What about if we cluster crime data? Would this impact
clustering on over-policed communities?" The question tacitly accepts the
practice of predictive policing and the role of the police, neither of which we
should find acceptable.

As researchers, particularly graduate ones, it can be easy to forget the many
chains of obligation and interest binding us. The day to day is mostly doing
the, often esoteric, work of research doing whatever needs doing at that
particular moment. In this environment, it can be easy to view our work as being
science for science's sake. Grandiosely expanding the horizon of humanity's
knowledge and building the tools of the future. If only that were true.

Sadly there is no such thing. We have limited influence on how our tools are
used once placed into the world. Worse still, someone is paying for our research
and not on a whim. They are wagering that our work might produce something
useful to them. And regardless of how long our odds may be, mapping of dead-ends
is not without benefit.

Thus we are left with a paralyzing state of affairs. We cannot control what we
unleash into the world and neither do we know what the true motivation of our
funding is---for it is naive to believe that their interest is simply spelled
out in the grant wording. All we can consider is how tools might be used and
whether or not it is good for them to exist. This is, for lack of a better term,
the toolmaker's dilemma. How do we balance these things? Is doing so even
possible with our limited foresight? How do we know if we are asking the wrong
questions?

I'd like to illustrate this with one more example. Let's imagine that you work
on formal verification. Bugs are bad so it would seem good to find ways of
making sure they are absent; what's not to like? Further imagine that you are
tasked with formally verifying and hardening an embedded operating system.
Specifically, this operating system is used in vehicles and your task is to make
these vehicles harder to hack. Oh, and you're being funded by DARPA and the
vehicle is a semi-autonomous helicopter.

It could be tempting to go "yay hack-proof helicopter" and move on with your day
but doing so skirts the recognition of the danger underneath. The above
hypothetical is of course, entirely real and part of the HACMS project. And, in
my opinion, it is nothing short of horrific.

So what's the problem? Well, let's ask ourselves, why might DARPA---and the
military more broadly---be interested in hack-proof helicopters, really
hack-proof drones? The answer is pretty troubling. The HACMS project stands for
High-Assurance Cyber Military Systems. In short: weapons.

This work has, in all likelihood, been used in drones that kill people abroad
and enable continued war crimes. This work could have helped improve systems
that massacre civilians. Even if it hasn't---which we will never know for
sure---this possibility should horrify you.

This is not to say that the members of this project should bear the
responsibility for the military's actions, but nor does it release them from
culpability. *If you help make or improve weapons then you do not get to turn
away from the consequences, however many steps removed you are.* All software, I
fear, suffers from this problem far more than we realize. Like it or not, we are
irrevocably connected with one another. Our decisions ripple outward.

A final example: Github contracts with ICE. Many of us use Github to develop our
tools, to do our research, to hopefully improve the world with our work. Does
that mean we are supporting the atrocities ICE commits by continuing to use
Github and in doing so maintaining its dominance in the space? This problem
exists for all major platforms and most tech companies: Facebook subverts
democracy, Amazon abuses workers and hosts a significant portion of the
internet, not all of which can be said to be good, and there are no shortages of
things to lambast Google over. And that is just what we, the public, happen to
know about. We can be nearly certain that there are plenty of backroom deals we
would find equally, if not more troubling.

There is the common adage that "There is no ethical consumption under
capitalism" which I often see misused with the implied follow-on: "so I'll just
do whatever". Rather, I think it is the recognition that we are tied up in
oppressive systems beyond our control which we, as individuals, cannot topple
alone nor fully divest from. But that does not absolve us of responsibility. In
our shared humanity, *we are obligated* to consider our impacts on the world.
This applies all the more for the tools we make and the institutions we support.

So, at the risk of being labeled a hyperbolic bleeding heart, let me say this:
these are the stakes. If you do not consider how the tools you make will be
used, you will ultimately aid in the killing of others. In the subjugation of
others. In the perpetuation of systems of oppression that bind us all. You will,
in your ignorance, sharpen the teeth of monsters or, worse still, teach them to
wield fire.

I wish I had some words of hope or advice to end on. But computers are
ultimately tools, and we too can use tools to make things better. I hope we do.
