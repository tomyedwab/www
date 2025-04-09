Title: Overcoming the legacy roadblock
Subtitle: Written April 8, 2025
Description: Legacy codebases are the bane of AI tools. How can we overcome this?
Modified: 2025-04-08

> Staff Software Engineer, noun: An IT professional who over a long career has developed strong opinions about legacy codebases.

It is now 2025, and there has never been a better time to be sitting down at a
computer to write a first iteration of a product. The last time I was this
productive working by myself on something new, I was writing chat client apps in
Java (J2SE 1.4!) in between summer classes in college. LLM-powered AI coding
tools are making it possible for me to get an idea from conception to deployment
in a fraction of the time it would have otherwise taken. Given this stunning
personal sea change, it would be natural to expect the output of teams of 50-100
software developers (such as my team at work) to also suddenly increase by a
significant margin, but evidence of this across the industry is scant. Why might
that be?

An easy potential scapegoat here is adoption: Perhaps we are too busy or
skeptical to train up on new tools? Is the ship just too large to steer in a new
direction? I don't buy this argument: I see my own colleagues routinely adopt
new web frameworks, databases, and CI tools that show clear advantages.

Another common theory is that while AI agents do a fantastic job at green-field
or prototyping work, once the codebase no longer fits into the context window
they start to fail miserably. These agents do seem to struggle more with
locating relevant code, making changes that conform to documented or
undocumented standards, avoiding hallucination, preserving existing
functionality, avoiding code duplication, and passing complex tests or lint
rules.

This argument is very plausible: even seasoned developers can struggle to
understand and be productive in a legacy codebase. However, as most professional
builders of software are working with existing code of some kind, it's worth
probing deeper to ask if this is a problem we can overcome without appealing to
dramatic improvements in the foundational models themselves.

## Defining the term "legacy codebase"

Perhaps you have a definite idea of what this term means, or maybe you just know
it when you see it. There are many ways one might identify a legacy codebase:

1. __Age.__ The same thing being built today would look completely different.[^1]
2. __Size.__ Sprawling, convoluted codebases are difficult to reason about.
3. __Limited documention/tests.__ The code's purpose and intended functionality is obscured.
4. __Maintainer churn.__ Code is unowned or institutional knowledge has been lost.
5. __Obsolete stack.__ Old frameworks, unsupported platforms, abandoned architectural patterns.
6. __Brittle logic.__ Developers afraid to touch anything for fear of unexpected breakages.
7. __Deprioritized or inactive.__ Demand has diminished or the product is no longer a business priority.

[^1]: <sup>1</sup> One variation on this holds that "all code is legacy as soon as it is written", but that is too extreme for my taste.

These are all signs that a codebase could be annoying to work in. However, it's
not a physical law that code becomes less maintainable over time, or that having
tests necessarily makes code more maintainable. What _does_ tend to increase is
the amount of domain and historical context necessary to understand what the
code does.

So here I would like to define a spectrum from true legacy to non-legacy code:

* _"Legacy code"_ represents a previously solved problem that is poorly
  communicated, no longer understood or has become obsolete.
* _"Non-legacy code"_ effectively communicates a complete understanding of the
  problems it is solving, and those problems are still relevant to the business.

To reiterate: Code does not become "legacy" just by being old. I have code that
I wrote many years ago that still works fine and still gets updated from time to
time: The problem it is solving hasn't changed, the code communicates the
problem well, and there is little to be gained by rewriting it. How legacy a
system is depends on how much our understanding has shifted across a handoff to
a new developer, deprecation of a technology, or addition of features that clash
with the system's original purpose.

## Implications for modern development

If we want to benefit as much as possible from new technologies such as AI
agents, we have to make the job easier for them. Thus it is imperative that our
code be easy to discover, easy to understand without reference to external or
incomplete documentation, and easy to change without breaking hidden
dependencies across the codebase.

All of these attributes are easier to attain when the code accurately reflects a
deep understanding of the business domain. For example, suppose I am a new
employee and want to make a change to a user flow in the application. The
codebase can help or hinder this task:

* I should be able to find a module clearly corresponding to the relevant
  process in the codebase, not pieces of discrete functionality accrued over
  years and repurposed for this process.
* I should be able to understand the module and how it relates to the relevant
  user flow jusy by reading it, without wading through half-implemented
  workarounds, abandoned experiments, or tacked-on special cases papering over
  an inconsistent design that has evolved over time.
* I should be able to make simple changes simply, without triggering a cascade
  of test failures or invalidating undocumented assumptions made by other
  modules in the code and unknowingly causing an incident in production.

You might well ask, if these attributes of the codebase make it easier for
software developers to be productive in a codebase faster, why bring it up in
the context of AI? A few years ago, if a dev team was able to bring new hires up
to speed twice as fast, that would have constituted a moderate competitive
advantage. Today, I would bet that being able to onboard an AI agent _for each
member of your dev team_ will be an _enormous_ competitive advantage, and possibly
an existential risk for teams who are stuck with a legacy codebase.

## So what can we do?

There will doubtless be techniques developed over the next few years to improve
the ability of AI agents to work in legacy codebases. My bet is that better
documentation, especially inline documentation that lives alongside the code the
LLM is already reading, is the first step. Better tests could also help by
catching flights of fancy early and avoiding wasted time and tokens. This is
low-hanging fruit partly because LLMs are amazing at writing both of these. But
at some point you'll want to consider reorganizing, refactoring or simply
rewriting your code.

I want to be clear: Being disgruntled with your legacy tech stack is normal, and
if you are creative you can _always_ find incremental improvements to
intersperse with other technical debt and new features. However, a codebase that
has diverged from the original problem it was solving creates immense drag and
it can be hard to incrementally change fundamental assumptions in the code, such
as:

* Who is the customer or user?
* What is the relationship of the user to the application?
* What is the operating environment of the application?
* What are the expected performance or reliability characteristics of the application?

As an example, if your initially user-centric application underwent a hasty pivot
to a B2B model and your codebase is littered with special cases for tying users
to organizations, you may benefit a huge amount from rewriting significant, core
pieces of your code (such as database models) to reflect that new reality.

Rather than a line that should never be crossed[^2], the question of whether
to do a big rewrite has actually always been a cost/benefit analysis. But the
good news is that AI can bend the cost side of the analysis downward because
writing new code when you have a clear specification is now significantly
cheaper.

[^2]: <sup>2</sup> This article was hugely influential on me when I was a junior developer:
[Things You Should Never Do, Part I, by Joel Spolsky](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/).
There are lots of takes on Joel's advice around, and I attribute a big part of my
maturity as a software engineering leader to learning to discriminate between a
desire to modernize code for its own sake, and a real liability introduced by a
shifting understanding of the business domain. 

To sum up: If a large software development team is slow to deliver features,
adding an AI coding tool to the mix is unlikely to magically accelerate
everything. However, if small teams are organized around some aspect of the
business domain and are allowed to rewrite their code as needed to clearly
reflect their understanding, those teams will be able to move astonishingly
quickly with or without AI tools.  The tools do however make it easier to bring
that code into alignment with the domain, and once unblocked these teams will
begin to see the same exhilerating speedup that I'm seeing working on my
personal projects.
