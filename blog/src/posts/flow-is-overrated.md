Title: "Flow" in software development is overrated
Subtitle: Written November 5, 2025
Description: Tackling the myth that "flow" is critical for software development. Decided not to go with the obvious "Flow considered harmful" title. You're welcome.
Modified: 2025-11-05

I might not endear myself to my software engineering colleagues with this post,
but even if mine is a minority opinion I think it's worth stating:

> The importance of the mental state called "flow" when developing software in teams is vastly overrated.

I've heard the concept of "flow" mentioned semi-regularly at work, mostly
in arguments for reducing the number of meetings or other interruptions in order
to allow for longer stretches of focused work time. And I get it! It is
_annoying_ when you are in the middle of a complex task with a lot of context in
your head and you have to stop and attend a meeting about open enrollment or
backlog refinement or whatever. Many teams _do_ have a tendency to accumulate
more meetings including more participants for whom the value steadily diminishes
over time. This is emphatically _not_ a post about how great meetings are, and
why we should have more of them actually.

What I disagree with is the following theory:

1. Interruptions break flow state...
2. And flow state is key to a software developer's productivity...
3. Therefore: interruptions inevitably reduce productivity.

The argument makes intuitive sense, but is predicated on a false assumption:
that professional software development - more than all other professions! -
uniquely benefits from long stretches of uninterrupted focus time. Reflecting on
my observations over decades, it seems to me that for the most senior engineers
I've known this just isn't true, and believing it might be actively harmful.

## The theory of "Flow"

I'm going to assume that the term "flow" has become part of the common tech
sector lexicon, but whether or not people know the origin they are implicitly
referring to the psychological theory[^1] popularized by Mihaly
Csikszentmihalyi[^2] in the 1980s and '90s.

[^1]: <sup>1</sup> See [Flow (psychology) (Wikipedia)](https://en.wikipedia.org/wiki/Flow_(psychology))
[^2]: <sup>2</sup> See [Flow: The Psychology of Optimal Experience](https://www.amazon.com/Flow-Psychology-Experience-Perennial-Classics/dp/0061339202) ![Flow book cover](../images/25-11-05/flow_cover.jpg)

In this theory "flow" is a mental state wherein you are fully immersed in a task
for an extended period of time. You might experience time passing more quickly,
and you might neglect other needs. If you find yourself deep in a flow state,
you might work for hours on a project without pausing for eating or breaks, and
in some cases only realize how long you've been working when morning sunlight
starts streaming in through the window. (I may have started speaking from my own
direct experience here...)

Initiating and maintaining a flow state is not trivial: it requires a goal that
is challenging enough to avert boredom but also attainable enough to provide
continual positive feedback from forward progress. There is an observed element
of intrinsic motivation and reward in the process, which makes working in a flow
state more enjoyable in the moment and less effortful.

While Csikszentmihalyi's research was initially done in the context of sports
training and artistic work, the idea has been enthusiastically adopted by
software developers: Allowing yourself to be carried into a flow state means
being able to spend more time working on a project without getting bored, burnt
out, or tired, and enjoying the process more as well. I will readily admit I've
done this on many a personal project, and generally been very happy with the
results.

It is not surprising, then, that we might seek to leverage this phenomenon to
become more productive and satisfied at work. Surely it's a win/win situation
for everybody, right?

## The cracks in the theory

One suggestion of a crack in the theory is to compare "flow" to
"hyperfocus"[^3], a similar mental state described as a symptom of a psychiatric
disorder such as ADHD or Autism Spectrum Disorder. Outwardly, much of the
behavior is the same: singular focus on a task for long stretches of time,
neglecting other needs or sensations. The main difference seems to be whether
the work being focused on is, in actual terms, important, versus a fixation that
the individual does not actually choose for themselves.

[^3]: <sup>3</sup> See [Hyperfocus (Wikipedia)](https://en.wikipedia.org/wiki/Hyperfocus)

One might argue that being able to _choose_ when to engage in or sustain this
level of focus differentiates flow from psychiatric disorder. However, given the
intrinsic reward inherent in the flow state, you might ask yourself: Are you
really choosing the best use of your time, or are you chasing the high of being
fully absorbed in an interesting problem?

The other crack in the theory is that while the alleged benefits of flow are
talked about exhaustively in the literature, there are drawbacks that follow
directly by definition:

- **Overwork**: Working for extended periods of time uninterrupted may not be
  the best choice for work/life balance. It may also lead to physical and mental
  exhaustion; working long hours one day only to be tired and lazy the next may
  end up being counterproductive. Neglecting bodily needs like food, sleep and
  regular movement/stretch breaks can be unhealthy in the long run as well.
- **Social disconnection**: In my experience, the benefits of working with a
  team of smart, knowledgeable people you trust far outweighs the specific
  technical work when it comes to job satisfaction. Focusing on the technical
  work to the exclusion of social interactions may harm that team dynamic. The
  teammates I've most enjoyed working with have often been the ones who are most
  open to pairing on work, answering questions, and mentoring others when they
  need help. Their physical or figurative door is always open, and they never
  express frustration at being interrupted.
- **Narrowed focus**: There are clearly attributes of some software tasks that
  lend themselves to be implemented in a flow state: tight iteration loops,
  quick feedback cycles, a constant sense of progress toward a bigger goal.
  However, this steady stream of small technical wins can hide a bigger
  technical issue - maybe the overall approach is wrong, or the project is
  taking too long and is no longer worth the sunk cost. Perhaps another task
  has increased in priority or maybe the bug you are debugging is too complex and
  you need to ask for help. When working in a flow state, it is easy to neglect
  these considerations in favor of barreling ahead to try to complete the task.

During my tenure as an engineering manager, I noticed some of the internal
contradictions of this belief model among my team. They pushed for fewer team
meetings, but they also valued knowing what everyone was working on and having
the opportunity to tackle difficult architecture or prioritization questions as
a team. They appreciated having access to teammates who are knowledgeable, easy
to pair with when needed, and give good advice, but they disliked being
interrupted while working on a challenging task. They had ambitious work/life
balance goals but hesitated to stop work at five o'clock and risk losing the
context in their head.

## The benefit of interruptions

Over the last decade my own time has become completely atomized, both at work by
the increased meeting load that comes with being part of engineering leadership,
and in my personal life since having children. When this change happens suddenly
it feels horrible, like you are never able to fully concentrate on anything. You
might wonder if you'll ever be productive again.

Over time though, I honed my skill at note-taking and documentation. I've
gradually come to realize that the context surrounding a task - decisions made,
steps remaining, issues to address, dependencies on other work - is at least as
important as the work in progress itself. Writing this down as I go is critical
to being able to put down a task and then pick it up again after a meeting, a
night's sleep or even a long vacation.

One benefit of extensive note-taking is that if anyone asks me about the status
of the task, I have a concrete answer ready to share. How many times have you
heard in a team standup: "the project is progressing, it should be done soon"?
This is a non-update, and I suspect it happens when someone is so focused on the
details of their work they lose track of the big picture. Intentionally stepping
out of flow state can help you regain that perspective, and often leads to
insights about the nature of the work and how well it's actually going.

That, and you can decide to step away from work whenever you need to in order to
recharge or be present for coworkers, family, and friends.

Other benefits emerge when you look at the team as a whole:

- More mentorship and knowledge sharing is happening as questions are answered
  immediately.
- Issues with ongoing work are surfaced and addressed immediately with input
  from everyone affected.
- Constant re-prioritization and re-estimation is happening to ensure time is
  not wasted on unimportant or impossible tasks.

## Summary

There are times as a software engineer when it is really helpful to turn off
Slack/email/phone notifications for a few hours and just focus on a challenging
task. You can write a heck of a lot of code this way! I once spent a week
completely rewriting Khan Academy's content editing infrastructure from the
ground up, and I felt pretty good about it until I realized that it was too
massive a change to be reviewed. Breaking it up into smaller changesets took
_months_, but was a much more collaborative process; a lot of seat-of-the-pants
decisions were reconsidered and the end result was unquestionably better.

Software teams do not benefit when each member of the team is deep in their own
isolated flow state, they work well when the team _as a whole_ is communicating
and collaborating efficiently. Unfortunately, this definitely requires some
regularly scheduled meetings, as well as individuals being available for their
teammates to interrupt when they get stuck.

If you find that interruptions keep you from getting work done, don't
figuratively (or physically) shut the door on your team and start rejecting
any and all meeting invitations. Instead try intentionally tracking your
progress and mental context as you go. Over time, you'll find you are more
resilient to interruptions, can participate meaningfully in more discussions,
and enjoy a productive work day without having to set a timer to remind yourself
to get up every once in a while and go to the bathroom.
