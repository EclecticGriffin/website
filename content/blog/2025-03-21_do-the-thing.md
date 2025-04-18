+++
title="Unfortunately you sometimes need to do the thing"
date=2025-03-21
draft=false
[extra]
summary="In which I meander about creative tasks and offer some advice on learning to write Rust code (or any other programming language really)."
+++

So I am fortunate enough to write a fair bit of code in the course of my
research. Over the past several years this has primarily taken the form of Rust,
a language I really like but that has a reputation for being difficult to pick
up. So how do you go about learning Rust, or any other creative skill for that
matter?

Like many people I suffer from a bad case of perfectionist brain gremlins, which
can make it very hard to get things done. They've a paralytic effect that can be
hard to manage, particularly in the early stages of things. Writing words, the
thing I am doing now, is a real pain point. The complicated, messy process of
taking ideas from the churning mass of thought-soup that is the conscious and
pinning them down with language is something I become easily frustrated by. This
frustration stems entirely from the recognition that what I've made, that what
sits in front of me, is not what I want it to be. Either it's missing some
essential truth, feels self-indulgent, requires foreknowledge not contained
within the writing, or one of many other unavoidable imperfections of existence.

There's no getting away from this. No matter what you've made, it can almost
always be improved in some way, even if you're the only one who would notice.
And caving in to this desire to polish, to improve, is a fantastic way to get
nothing done at all, or to never even start. The most perfect version of a thing
is the imagined idea of it; and unfortunately that version will never and can
never actually exist in the world.

So here's how I think about it: our brains are lazy---or efficient depending on
your perspective---and tend to be very use-it-or-lose-it about skills. And,
unfortunately, this means you have to do whatever it is you want to learn and
that you're going to be bad at it, at first. And that, well that sucks, doesn't
it? It would be nice if thinking hard about something was enough. But I suspect
that art would be a lot less compelling if that were the case.

Boiled down to its simplest elements, I think the act of creating something, be
it art or code, looks something like this:
1. Start with an idea fragment
2. Attempt to make it
3. Assess what was made
4. Improve until "good enough"

And in my experience, my failure mode looks like jumping right to assessing what
I've made after the smallest amount of creation. It's easy to slip on the
editor's hat before the author is done, because making things is, quite often,
challenging. And while good critique is hard, criticism is quite easy. This
looks something like
1. Start with an idea
2. Make a *tiny* bit
3. Spiral
4. Go browse the web instead
5. I'll get to this project later. Totally.

But here's the thing, it's almost always the case that you don't *really*
understand what you're making until after you've finished trying to make the
first version of it. I believe this is true for writing as much for code
development. And until you actually know the shape---not merely the vibe---of
what you're making, criticism is largely paralytic and insidious in the way it
promises improvement while grinding everything to a halt.

Put another way, there are, broadly speaking, two layers at which you have to
understand a piece of work: High-level and Low-level. The former is the big
picture, the broad goal, the overall approach, while the latter is all the work
and mechanics needed to accomplish it and manage all the messy troubles of
reality.[^levels] This high-level view of the work is *necessarily incomplete*
and should be revised based on understanding gained from the actual doing, i.e.
the low-level work. Recognizing this is how we make actual progress, rather than
becoming discouraged when the high-level understanding clashes with the
low-level work. In this way, the two layers form a loop: the doing improves the
high-level understanding and the high-level understanding guides the doing lest
it get lost in the weeds.

This is starting to sound an awful lot like self help. Gross.

Okay, brass tacks, how do you learn to program rust? Well, in short, I recommend
that you first read at least the beginning of the [Rust Book] and then as soon
as possible start writing some code. Make a tiny project to do whatever silly
thing strikes your fancy. You can try [rustlings]. You could even [follow][linked lists]
[some][gentle intro] [tutorials][roguelike].
There are a ton of [educational resources][big guide] out there,
 and I'm certain some of them will work for your brain.

But remember: you should always actually write the code yourself. It is far too
easy to look at a piece of code and think "yeah I get it" without actually
understanding or retaining it. Incidentally, this is why I think LLMs are an
absolutely terrible tool for learning programming in general, though I will
accept that I trend pretty negative on the topic.[^1]

There's a good chance that stuff you write won't work correctly, won't compile,
or will otherwise frustrate you at first. This is okay. You aren't doing
anything wrong. You need to get down into the weeds and muck and really wrangle
with things to wrap your brain around them. **Unfortunately, you must do the
thing.** But fortunately with code you can run it and see if it works, no
subjective analysis required! Terrible code that works is still code that
works.[^2] And often that's the first step to good code that works. And while
technical debt is real, that's generally not a concern when you're first
learning a language.

Make something first, then worry about making it better.





[Rust Book]:https://doc.rust-lang.org/book/
[rustlings]:https://github.com/rust-lang/rustlings
[gentle intro]:https://stevedonovan.github.io/rust-gentle-intro/
[roguelike]:https://bfnightly.bracketproductions.com/rustbook/chapter_0.html
[big guide]:https://gist.github.com/noxasaxon/7bf5ebf930e281529161e51cd221cf8a
[linked lists]:https://rust-unofficial.github.io/too-many-lists/

[^levels]: In coding projects, the high-level understanding is the overall
    approach to a problem, i.e. the algorithm or pseudocode. The low-level work
    here is the actual code and all the work needed to realize the gaps in the
    pseudocode. In writing, the high-level view is the outline and general
    thesis/point while the low-level is the actual process of crafting sentences
    and paragraphs and deciding whether or not they effectively make the desired
    point.

[^1]: At time of writing there's apparently this new trend called "vibe coding",
    at least in some circles. And at the risk of sounding like an old person
    yelling at a cloud, I really worry what damage this is going to have on
    people's skills and, more generally, how LLMs will impede education. I
    cannot imagine trusting an LLM to write a full function, let alone entire
    modules or programs.
[^2]: And in my experience there is sometimes a strange, perverse satisfaction
    to solving a problem in *just the worst* way possible. More than once, I've
    called someone over to see the shuddering abomination of logic I've somehow
    made complete a task. Behold my wretched amalgam: each loop more tangled
    than the last, each variable an entropic scream of a dying world, each
    iterator a glimpse into a realm of madness. The compiler cannot save you.
    Nothing can save you.
