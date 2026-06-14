Title: Write It Twice
Subtitle: Written June 11, 2026
Description: <TODO>
Modified: 2026-06-11

<idea>The best time to throw away code is just before deployment.</idea>

Rewriting code from scratch is a controversial strategy. It is a natural
inclination for software engineers to want to rewrite code that is full of
technical debt rather than fix all the issues incrementally, especially if that
code is legacy and written by engineers who are no longer around to maintain it.
The code feels like more of a liability than an asset, and a strong temptation
can take hold to burn it all to the ground and start over.

There is sound advice against ever doing this[^1] and many potential pitfalls of
overconfidence that leave you worse off than you started[^2]. In particular, a
system that has been deployed in production and serving customer needs has proof
of its efficacy and months or years of accumulated edge-case logic and bug fixes
that are not easily distilled into a spec for a rewrite. The tl;dr of the
argument against rewrites is that they tend to take far longer than expected and
end up accumulating significant technical debt immediately as forgotten edge
cases resurface and brand new bugs are minted.

[^1] https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/
[^2] https://en.wikipedia.org/wiki/Second-system_effect

The same software engineer (me) itching to rewrite the legacy stack will also be
loathe to rewrite a system I just built. Logically, why would I redo work I
_just_ completed? Less logically, I find I am susceptible to sunk cost fallacy,
over-valuing the output (code) and under-value the knowledge and understanding I
gained in the process.

The realization I've come to is that the moment immediately _after_ getting a complex system working
and immediately _before_ deploying it to end users production is the perfect time
to rewrite it. Inevitable corner cases I encountered in development and
testing will have caused the implementation to diverge from the clean, beautiful
spec or plan I started with, and I've already started to accumulate technical
debt. On the other hand, since none of the code is being actively used, the cost of
refactoring is much lower than it will be after launch when changes must be
backward compatible and non-disruptive to users.

Moreover - and I am making some assumptions about team culture here - the period
immediately after a big feature has been delivered is often a difficult one in
which to argue for refactoring, as there are always more shiny new features on
the backlog.

So what does it look like to plan to write your next feature twice from the
outset, and what are the benefits?

First, if you know you'll be building your feature twice ahead of time, you'll
approach that first implementation differently. The coding standards can be as
low as you want, the UI can be as rough as necessary.

The goals of Implementation One are about much higher level concepts:
* Fleshing out and validating the system design and architecture
* Testing architectural decisions such as choice of libraries or frameworks
* Finding tricky corner cases and identifying error-prone logic that needs special attention

Importantly, Implementation One is **not** about:
* Clean code or elegant data models
* Commits that are easy to review
* Ticking all the boxes vis-a-vis compliance, security, cleanup of old data, etc.

I do want to draw a contrast between Implementation One and a "prototype"
implementation. Prototypes are generally not fully integrated with the codebase
and stick to the happy path to prove an idea works. This is more than a
prototype: you want to get this functionally complete and reasonably well
tested, to shake out the problem cases and inelegant solutions involved in fully
solving the problem. It is much easier to suggest throwing out a prototype and
starting from scratch, than throwing out a fully working implementation.

So far I haven't mentioned LLM coding at all, but if you look at this second
list, this is almost an exact list of things that LLMs are not naturally very
adept at! If you are moving quickly and letting your coding agent do most of the
work while skimming the output, I guarantee you are creating a lot of technical
debt in these areas. However, we can align the goals of the first implementation
with the strengths of these tools: fast integration and build-out of complex
systems to validate our ideas and identify areas that need more careful thought.

Getting through Implementation One as quickly as possible gives you insight into
where the "path of least resistance" turned out to be wrong, whether that is a
wrong UI flow, wrong library, or wrong data model. Your goal should be to
understand the decisions and tradeoffs that were made, evaluate the outcomes,
and then come up with a new, more detailed spec for the project incorporating
everything you've learned.

I will call out an opportunity here for an Implementation One Point Five: Once
you have everything working you may want to explore potential refactorings or
cleanup before moving on to the final implementation. This follows from the
principles of refactoring [^3] that prefer small incremental steps to trying to
improve the architecture while also attempting a rewrite. This still is
throw-away code, but it is a good opportunity to clean up interfaces and give
you a better sense for what the end state will look like.

[^3]: https://martinfowler.com/books/refactoring.html

Finally, you throw everything out and start again from scratch! You'll be amazed
at how quickly Implementation Two can happen once you have a draft
Implementation One, even without a Second Brain writing the code for you.
Frankly, I am not above copy-pasting code liberally and referring to the earlier
draft, bringing it up to coding standards and keeping code reviewers in mind at
each step. The resulting code will be much cleaner than your first attempt and
hopefully will last for longer before your successors start daydreaming about
tearing it out and replacing it.

To summarize: "Write it twice" is a technique I have practiced in the past when
I could and had a lot of success with, which _seemed_ in the moment to be
fantastically expensive but in hindsight only modestly increased the length of
projects. With LLM coding tools it becomes both much cheaper to do and much more
necessary: the first implementation can be incredibly fast but leave a tangled,
unreviewable mess. Taking the time to fully understand and rewrite it leads to
much higher quality code than I would have written in one pass while still
taking less time overall. I recommend trying this technique to see if you get
the same value out of it that I do.
