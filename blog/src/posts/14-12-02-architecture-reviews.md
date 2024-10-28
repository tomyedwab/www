Title: Architecture vs. Implementation Reviews
Subtitle: Written December 2, 2014
Description: Differentiating between two different flavors of code reviews.
Modified: 2024-10-27

In a [previous post](./13-03-14-code-reviews.html), I opined on the virtues of
having every code change be reviewed before it gets deployed to production. That
was almost two years ago! Our development team at Khan Academy has grown a lot
since then, and I believe even more strongly now that mandatory code reviews are
an indispensable tool for creating and maintaining quality code. Code reviews
are awesome! I'm not the only one[^1] who thinks so[^2]. And for more "best
practices" advice, this article[^3] is spot-on and definitely worth a read.
However, there's a nuance to code reviews that I haven't seen much discussion
of.

[^1]: <sup>1</sup> [Code Reviews: Just Do It](https://blog.codinghorror.com/code-reviews-just-do-it/), Coding Horror.
[^2]: <sup>2</sup> [Every team needs kick-ass code
reviews](https://www.atlassian.com/blog/archives/every-team-needs-kick-ass-code-reviews),
Atlassian Blog.
[^3]: <sup>3</sup> [Practical Lessons in Peer Code
Review](https://blog.salsita.ai/practical-lessons-in-peer-code-review/), Salsita
Blog.

![Cat writing code on a MacBook](../images/14-12-02/cat_review.jpg){ .article-width }
My trick? Naming variables `laser_pointer` and `ball_of_yarn` to hold the
reviewer's attention.
{ .image-caption }


To provide some context for what follows, here is my process when writing code.
I may spend a while at the outset *thinking about how I want to solve a
particular problem*, or researching the problem and possible solutions. Then I
*write some code* - it may be a new API call, or some UI changes, or a background
task. I spend no more than a day coding before *sending a review*. I can send the
review to anyone on the team, but I prefer those who know most about the area of
the code I'm working in. In the commit message I *explain what motivates the
change*, any important information that isn't already in the comments, and what
work remains (if any) before shipping the change. If the change is not yet
shippable then there will be TODO comments in the code *highlighting what still
needs to be done*. Since reviewers have other tasks, I don't expect to get the
review back for a day or two, during which time I do more thinking/research or
switch to another task. I respond to each and every comment (even if I choose
not to change any code) and when everything is addressed I *push my local branch
and close the review*.

In my original post I did mention some challenges when reviewing large new
systems or gargantuan refactor projects. The reason these are difficult is that
for many programmers the instinct is to want to see something in a working state
as soon as possible, which means writing lots of code quickly across the entire
codebase (database, API calls, frontend infrastructure, UI) and then fleshing it
out with additional logic, documentation and tests later. This is fine for
prototypes, but for code that's meant to be shipped it's really
counterproductive.

With more and more complex systems, it becomes critically important to involve
reviewers in the process as early as possible. Here is an example of all the
steps you might take on the path toward completing a new feature in a web
application:

* Architecture design
    * Sketch out a design of how the UI should look or behave.
    * Define a view hierarchy, class hierarchy or database models with pseudocode or UML diagrams
    * Define API method signatures with parameter and return value definitions
    * Decide how corner cases will be dealt with, and what the performance implications of the design might be

* Architecture scaffolding
    * Implement the full API with dummy placeholder functions
    * Implement all the required datastore models
    * Wire up the API calls to read from/write to the datastore models
    * Write unit tests for the API calls
    * Implement all the required client-side models
    * Implement GET/POST calls to populate and save the client-side models
    * Write client-side model tests

* Final implementation
    * Implement remaining server-side logic (asynchronous jobs, monitoring, etc.)
    * Create a set of UI components to display model data
    * Hook up events and update client data
    * Write client-side UI or end-to-end tests
    * Finalize the style or layout of the UI components according to the design

Not everyone codes this way, but the advantage this has is that *each step builds
on the previous step*. The reason is that the way you structure your datastore
models or the way you design your API has huge implications for the rest of the
code - how many AJAX calls the client needs to send, for instance, or how things
can be cached. In contrast, the CSS styles you use in your UI have basically no
effects on anything else, which means if you make a mistake at this point it is
much easier to fix. Getting the architecture right is by far the most important
part of the project and should rightfully take the bulk of the time.

There are two direct consequences of this phenomenon: It matters a lot who
reviews architectural changes, and "architectural" code reviews proceed very
differently from "implementation" code reviews. Both reviewer and reviewee
should be on the same page as to what kind of review is being done.

Let's look at two superficially similar real-world code changes and the kinds of
comments a reviewer might submit for each one:

![A code review with high-level comments about code structure and
intent.](../images/14-12-02/review-1.png){ .article-width }
Review 1
{ .image-caption }

![A code review with granular feedback about typos, style issues and
bugs.](../images/14-12-02/review-2.png){ .article-width }
Review 2
{ .image-caption }

In both cases something new is being added - in the first case a database model
for an Error in an error monitor, and in the second a new React UI component.
This may be a bit of a contrived example, but it conveys the difference in the
*tone* and *content* of the comments.

In the *architecture review* (the first case), new infrastructure is being put in
that will have implications for performance and affect all the other code that
will be written on top of it. Furthermore, it's early on in the project so
changes will be much harder to make later in the process. So naturally you see
conversation about what solution is best. There is a lot of emphasis on
documentation and code cleanliness so that readers who want to build on this can
easily understand how it works. And related to that, it's crucial to establish
conceptual clarity about what is being built. Bugs will get called out too (this
code is expected to ship after all) but since most of the business logic hasn't
yet been introduced, the emphasis is really on the overall architecture.

Note the difference between an *architecture* review and a review of the
*design* of the architecture. It is well worth involving reviewers in your
thinking when you sketch out these ideas, but this is the first actual,
shippable code that conveys the final architecture and the concreteness *always*
make new problems suddenly apparent! Don't assume that because your reviewer
approved a written design doc, they won't have a lot of feedback or get inspired
by new ideas when looking at the actual code.

In the *implementation* review (the second case) the functionality required is
very clear. In this case the markup already existed in another template and was
refactored into a new component. Not only that, but we already have many
existing components similar to this one (the first few of which were hashed out
in great detail in what were essentially architecture reviews) so I'm not
expecting any comments on the structure of the new code. This is closer to how
most programmers conceive of a code review, which is meant to catch bugs,
suggest algorithmic improvements, and enforce style conventions. It's less of a
conversation and more of a checklist.

Another key difference: if a reviewer makes a suggestion on an implementation
review, I may decide to ignore it if I disagree - as professionals we may offer
suggestions but (style violations aside) we respect that at the end of the day
the author is the one responsible for the code. In an architecture review, I
have to take suggestions seriously because more often than not other developers
will at some point have to work on or extend my code. If I disagree, it's my
responsibility to bring the reviewer around to my point of view, and then
document that reasoning process so that future developers understand why it was
done this way.

![Architecture review represented by a edifice of ionic columns. Implementation
review represented by gargoyles on a rooftop.](../images/14-12-02/gargoyle.jpg){ .article-centered }

This is why it feels so disappointing to submit a review expecting feedback on
the architectural changes and instead get feedback only on your typos. The best
way to avoid that is to pass along not just the code to be reviewed but a
description of what you the author expect from the review.

In an architecture review:

> This is my first pass at the database models for the new error monitor. The
> use cases are described in the comments. I wasn't quite sure how to divide up
> the files - what do you think? Does this look like it will be performant and
> maintainable in the long term? 

In an implementation review:

> This is the completed error monitor UI. I've addressed all the TODO's and
> tested thoroughly. Attached are a few screenshots. I'd like to ship this on
> Monday to the dev team.

I hope that understanding the difference between these two types of reviews -
*architecture* and *implementation* - helps you communicate better with your
teammates when reviewing code or having your code reviewed.