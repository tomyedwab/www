Title: Lay the cornerstone yourself
Subtitle: Written June 14, 2026
Description: As starting projects becomes easier than ever, it's never been more important to pay careful attention to the foundations and not let the AI make all the decisions for you.
Modified: 2026-06-14
Did: at://did:plc:k27kugtlg3jgnyqbrmr2wnbk/site.standard.document/3mobrymy2i52a

> A **cornerstone** (or **foundation stone** or **setting stone**) is the first stone set in the construction of a masonry foundation. All other stones will be set in reference to this stone, thus determining the position of the entire structure.[^1]

[^1]: [Cornerstone](https://en.wikipedia.org/wiki/Cornerstone) (Wikipedia)

Most software engineering projects, whether they are done professionally or as a
hobby, require compromises to get done in a reasonable time. There will always
be minor bugs to fix, user interfaces to polish, and small refactorings to clean
up nastier bits of the code that inevitably accumulate during development.
However, there is exactly one time in every project when you have the greatest
leverage over the long-term quality of the code, and that is right at the start.

That moment when you find yourself setting up a new environment, creating a new
service, or defining a new API is the best opportunity I have found to slow down
and consider every detail. Yes, even long "bike-shedding" conversations about
naming or documentation are worthwhile here. Why? Because no matter how
malleable we like to imagine software is, the path of least resistance for all
future work will be to replicate and extend the patterns already laid down. Like
a wheel in a rut, existing conventions define the default path, and any
deviation requires significant effort.

You might be skeptical about the link between the "path of least resistance"
patterns in the codebase on one hand and code quality on the other. One idea
that has stuck in my head for years is the concept of a "Pit of Success"[^2]:
a particular architectural solution that, if you can find it, makes it easier to
do the right thing by default and harder to do the wrong thing. The key insight
is that the naïve design is almost never a pit of success: it takes careful
thought and time to identify the failure modes and put the metaphorical bumpers
in place.

[^2]: As I heard about it from Jeff Atwood, ["Falling Into The Pit of Success"](https://blog.codinghorror.com/falling-into-the-pit-of-success/)

As an example, a few years ago at Khan Academy we rewrote our backend entirely
from Python to Go and from a single monolith to a small set of separately
deployed services. We spent the first few months of the project iterating on a
single trivial service, thinking through the specifics of deployment, routing,
caching, local development, linting, etc. Nailing everything down in detail
meant that when we were ready to start migrating code in massive quantities, the
codebases owned by different teams ended up looking very similar to each other
even though the work was happening in parallel. Compared to the decisions made
during those few months, any decision to change the patterns later on would
require gargantuan effort.

## Relevance for AI coding

So far I've only talked about engineering best practices, but as with all such
things this principle is even more critical now that AI has greased the wheels.
This is going to be a running theme on this blog: the benefits of many existing
best practices are amplified, not undermined, when onboarding AI coding agents
onto your team. The way it manifests here is that, while AI agents are
incredible at taking green-field projects from nothing to something, you should
_not_ rely on them to create good patterns for your project to follow.

While you can certainly prompt an agent to write a bunch of the initial
boilerplate for you, if you aren't careful it will tend to also make spot
decisions about:

* The stack the project will be built on
* Code organization, module boundaries, data models and abstractions
* Naming of core concepts and modules
* Approaches for error handling, parallism, security, observability
* What automated linters & tests should check and how stringent they should be
* Which parts of the domain deserve more attention than others

The common thread between these bullet points is that all these decisions will
set precedent in your codebase that will be replicated as more code gets
written, and the later you start to feel regret about a decision the larger an
effort will be required to change it.

The key piece of advice that has been working well for me on AI coding projects
is this: **Lay the cornerstone yourself.** For the first few commits to get your
project from zero to initial working implementation, do not just review the
code. Read through it line by line and imagine each pattern replicated ten or a
hundred times in your codebase. Are you happy with the function names? Is the
error handling clean and correct? Are the modules well organized and obviously
extensible? Do you feel _excited_ to be working in this codebase?

We may not yet know all the best ways to work with LLMs as coding agents, but we
do know that they will tend to follow existing patterns in the code. Even if
they miss something while reading the code it is much easier to point them to
positive examples than to try to explain the patterns in a prompt. Better still,
standards that can be enforced through static analysis (linters) give agents
immediate feedback that they can address without human intervention.

Beyond the technical aspects of putting your code on a solid footing from the
start, starting off with a solid _understanding_ of the foundational decisions
and organizational structure of the project is key to maintaining situational
awareness as the project evolves. This counteracts the phenomenon of "cognitive
debt"[^3], where your comprehension of the implementation degrades over time as
AI does more of the work. The clearer your initial understanding of the code,
the easier it will be to make sense of agent-authored changes, keeping you "in
the loop" in the decision-making beyond just rubber-stamping and enabling you to
sense when the changes feel strange or incorrect.

[^3]: [How Generative and Agentic AI Shift Concern from Technical Debt to Cognitive Debt](https://margaretstorey.com/blog/2026/02/09/cognitive-debt/), Margaret-Anne Storey

## Summary

Today in 2026 it's never been easier to get a project started from nothing: what
used to be an intimidating barrier to entry just to figure out what tooling to
use, setting up an environment, and getting something running on which to
iterate, is now a single prompt away. However, this is a compelling but vicious
trap if you want to keep developing beyond an initial proof-of-concept. While
you can still skip a lot of the drudgery and boilerplate, a smart strategy is to
get fully into the weeds of the initial decisions and patterns being implemented
to make sure you understand them and make improvements while the codebase is
small. You will almost certainly discover important questions you hadn't
considered, and possibly learn a great deal about how to architect projects.

**BUT WAIT!** Maybe you made it this far but you still want to give in to
temptation and just vibe code something quickly. There may be good reasons to do
this: maybe the idea isn't proven enough to dedicate significant time to a solid
implementation, or maybe you just need to see the tool working in a realistic
setting before you can answer some important design or technical questions. You
can still set yourself up for success if you commit ahead of time to **writing
it twice**. I'll cover this in a follow-up article.
