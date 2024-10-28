Title: Coding for review
Subtitle: Written March 14, 2013
Description: Learning to appreciate the benefits of code reviews.
Modified: 2024-10-27

## Ship, ship, ship!

This past Friday, I shipped about a month's worth of extensive refactoring to
the content editing infrastructure of the site. As with many refactoring
projects, the best possible outcome would have been that no one would notice I'd
done anything. The worst would have been visible breakage of the site for
content authors or users. That launch was a success (whew!), and although it
took a lot of effort and planning on my part to make that happen, I want to
credit two powerful methodologies that ensured I wasn't working alone: unit
tests and peer code reviews. I want to focus on code reviews here, because while
the benefits of unit tests (especially in refactoring projects) are
well-documented, I've found that subjecting code to peer review has subtly and
unexpectedly changed the way I actually write my code.

![Three amazing engineers mugging for the camera](../images/13-03-14/having-fun.jpg){ .article-width }
The exercises team might be having a little *too* much fun on this code review.
{ .image-caption }

## Come all ye reviewers

About a year ago, Khan Academy instituted a policy to peer review all non-trivial code commits. For coders who don't follow this regime, there are several benefits we were looking for:

* Fewer bugs. Bugs won't reach production if they are caught in a review first.
* Improved code quality. A strong check on coders' tendencies to take shortcuts,
  sacrifice code readability or understandability, or put in temporary
  half-measures that don't solve the underlying problem. In many cases criticism
  in a review caused me to rethink a problem and come up with a more elegant
  solution.
* On-boarding of new developers. Getting your head around a new codebase can be
  challenging. By reviewing new devs' commits we catch redundancy, unwanted side
  effects, and potential conflicts, as well as enforcing our style guide and
  setting a standard for high quality code from the very beginning.
* Diffusion of knowledge. Anything that facilitates communication between
  members of the team pays dividends over the long run. If nothing else, there
  will be a day when a critical developer will be on vacation/trapped in an
  elevator/at home with the swine flu and a reviewer will come to the rescue.

It's worth acknowledging the obvious cost to reviewing every commit: time. Time
that used to be spent writing, testing and committing new code is now taken up
with conversation and iteration on already-written code. So is the net result a
drop in productivity for the entire development team? Not necessarily. Let's
look at the list above again:

* Fewer bugs. A bug not caught during review will still have to be found and
  fixed later on. Tracking down a bug in production takes significantly more
  time, and fixing it is more difficult.
* Improved code quality. Quality code is easier to read, easier to implement new
  features on top of, and incurs less technical debt (TODO-laden code that will
  have to be revisited in the future). Of course, code reviews don't force this,
  they enforce whatever the team decides. If the team needs something done
  yesterday, then by all means do the quick thing and come back and fix it
  later.
* On-boarding of new developers. Efficient mentoring of new developers bends the
  productivity curve in a positive way. Even experienced devs are less
  productive while they are learning a new codebase.
* Diffusion of knowledge. Good documentation won't replace having multiple devs
  who understand any piece of code. Projects won't stall because the one
  developer who knows a system is busy doing something else and the code isn't
  clear. Our mantra is "anybody can fix anything", and it's critical that anyone
  be able to jump into any piece of code and understand it.

I won't go much further with this argument; in my mind it's a settled matter
that compulsory code reviews are a Good Thing and they have helped us in many
ways as an organization. What I hope to share here is a surprising and totally
non-obvious fact: code reviews have changed the way I design and write code for
the better.

![More ridiculously talented product developers being awesome](../images/13-03-14/nighttime.jpg){ .article-width }
It's actually night-time in this photo. Such is the awesome power of teamwork at Khan Academy!
{ .image-caption }

## Evolution of a code monkey

All the lessons I've drawn from this ongoing experiment have taken some time to
understand and internalize. When we first instituted mandatory code reviews, I
didn't notice any immediate changes. For trivial bug fixes, reviews are
transparent: I make the fix, commit to stable, and send off the review after the
fact. The fix might ship before the review is done, but bug fixes are high
priority and that's OK.

Similarly for minor features: I make the change in a private branch, test and
document, then send a review. Then there is a period of answering reviewer
questions and iteration. In the meantime I might move on to other work, and when
the review is accepted I merge to stable and deploy.

With larger projects and changesets, I began to notice breakdowns happening when
I got to the review stage. Reviews were too large for reviewers to comprehend,
or too convoluted to follow. By the time a reviewer responded to a review, I
would have several more reviews open for subsequent commits, and it wasn't clear
which review fixes should be assigned to. Reviewers were reviewing
already-replaced or rewritten code. It became a real mess.

While it was clear what the problem was - too many and too large reviews - the
solution wasn't obvious. I could cut the size of the commits, and stop to wait
for reviewers before proceeding, but that would mean dramatically slowing my
progress - a busy reviewer can take hours or days to thoroughly read an
important review. Instead, I adopted (with lots of guidance from coworkers Ben
Komalo, Craig Silverstein, and Ben Kamens[^1]) some habits that enable me to get
useful feedback on code reviews and use that feedback effectively. Here is what
I learned:

[^1]: <sup>1</sup> See [Ben Kamens](https://bjk5.com) blog.

* Make one conceptual change per commit. (As opposed to one functional change
  per commit.) When I started working on a change, I would often be thinking
  about a requirement: "The user can set a bookmark." I would add a UserBookmark
  object, write the get/set API calls, and some UI. Later I would come back and
  write some unit tests. This is all one functional change, but many conceptual
  changes, and they deserve their own commits: A new UserBookmark object, with
  full documentation and unit tests. Then the API calls, with their own
  documentation and unit tests. Each change is much easier to understand, can be
  critiqued on its own merits, and will tend to be confined to a particular part
  of the code.
* Cut the thread. Many times, especially while refactoring, a change will have
  cascading effects: While testing I find multiple side effects from my change,
  fix them, and then those fixes cause more side effects, and so on. Sometimes
  fixing a side effect triggers another refactor, or fixing a totally unrelated
  bug, and when the code finally gets committed it is both unreasonably large
  and completely unfathomable. Even I can't remember exactly what prompted a
  particular change in a day-long marathon of bugfixing. I could try to split
  the fixes among several commits after the fact, but that's error-prone and
  difficult. A better solution is to "cut the thread" at some reasonable point,
  and start sprinkling TODO's liberally where fixes need to be made. It's clear
  to the reviewer that this code is not yet functional and just what the side
  effects of the change are without actually fixing those side effects in that
  commit. Best of all, it's clear from looking at the commit history what
  motivated each fix.
* Write throw-away experimental code. When starting a project, I find it helpful
  to quickly iterate on a prototype implementation for a thorny code problem
  before settling on a final solution. These sketches are not useful to have
  reviewed; rather it is better to write up the proposed solution in a Google
  Doc or email and iterate on that with reviewers before sitting down to
  implement it for real. The second implementation takes into account reviewer
  feedback and is written more carefully, with documentation and unit tests that
  would be a waste of time during a prototyping phase. The prototype is
  eventually thrown away and doesn't become part of the commit history.
* Work on multiple tasks in parallel. There is some inevitable downtime while
  waiting for reviewers to look at newly submitted code. Having a list of bugs
  or small tasks unrelated to my main project gives me something productive to
  do in that downtime. It's a great way to make sure that small, lower-priority
  tasks don't get crowded out by larger projects. I can assign the reviews for
  these smaller tasks to different reviewers, balancing the review load among
  the team.
* Don't get too far ahead of the reviewer. I do my best never to push changes
  that build on unreviewed changes. When I can't switch to a different task, I
  keep new changes local and don't push them until they previous reviews are
  done. That way I can implement changes from reviews cleanly on top of the
  pushed commits and rebase my local changes on top. (I use Mercurial bookmarks
  or Git branches for this.) Sometimes after discussion with the reviewer
  changes will be made that force the later work to be rewritten, and that is
  fine. It's better than having to roll back later commits to fix something from
  a review!
* Document everything, even if it's in progress. If I'm going to have to explain
  some complex bit of logic or a long list of method arguments to a reviewer, I
  may as well just do it in the code itself. Even if the code has `## TEMPORARY
  ##` or `// TODO(HACK) UGLY HACK` all over it, it still gets documented. It never
  ceases to surprise me how long those things live in the codebase, and the
  short-term solutions are the ones that need the most explanation: Why do we
  need this? What should replace this? When can it safely be replaced?

I firmly believe that all of these techniques make my commit history easier for
me and others to understand and make me more efficient as a programmer, and I
probably wouldn't have adopted them if not for the practice of peer code
reviews. I have also learned a lot about Python/JS/IE/life from my peers and
maybe taught someone something they didn't know.

Even if you work alone or don't do code reviews in your team, perhaps you may
benefit from these tips in your own work. If you do participate in code reviews,
do you organize or think about your code differently to take full advantage of
the review process? I'd love to hear from you.

*Photo credits: Jason Rosoff, embedded Khan Academy documentarist and lead designer.*