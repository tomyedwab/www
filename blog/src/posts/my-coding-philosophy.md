Title: My coding philosophy
Subtitle: Written January 13, 2026
Description: Sharing my philosophy of software development and my hopes for the future of our craft.
Modified: 2026-01-13

In college, I held a part time job working on the website for the Haas School of
Business at UC Berkeley. This mostly consisted of odd maintenance work, but one
regular task I was assigned was to take the weekly newsletter email and reformat
it into HTML for publishing on the website. The task took an hour or so each
week and was a bit tedious, so naturally after a few weeks I spent a few hours
of my own time to automate it. Luckily, I didn't fall into this trap[^1]:

![xkcd #1319: Automation](https://imgs.xkcd.com/comics/automation.png){ .article-centered }

[^1]: [xkcd #1319: Automation](https://xkcd.com/1319)

What I like about this particular comic is that it captures the lengths some of
us are willing to go to save a small amount of boring, repetitive work. I am in
this picture, and to be honest I'm cool with it. With my script I was able to
shave the time down to about 5 minutes of copy-pasting from the email into a web
form, and out popped the fully formatted HTML. This is not an impressive
technical feat, but I think it captures my personal philosphy pretty well and
explains why I got into programming computer software in the first place.

## My personal philosophy of coding

What is my goal in sharing this? I don't expect all readers to share my
background, and many of you will disagree for various reasons. What I hope is
that you better understand where I am starting from when I talk about
technology, professional software development, and building teams of developers.
Instead of simply disagreeing, perhaps we can talk to each other more clearly if
we understand each other's perspective.

So here is my philosophy, boiled down to bare essentials:
* I enjoy making computers do new and interesting things.
* Computers doing something new is only interesting if it enables _humans_ to do something interesting and new.
* A computer and human working together will always outperform the average computer or human working alone.

A clear example of this is automation. I am undeniably lazy: I want to spend my
time doing things that matter to me, and tedious tasks sap my energy and
concentration. Automation increases quality of life in a highly leveraged way: I
build the automation once and then I can share it with others, like my roommate
who took over my job at the business school when I graduated.

Advancement in computer software comes primarily from automating our own
development processes and building ever-more-complex libraries and frameworks.
For example, in Ye Olde Days a typical first-round technical interview question
we used involved reversing a string efficiently. In C this can be done easily
with a for loop, but isn't entirely trivial. However once the dominant languages
became Python and Javascript the only sensible solution was to use the standard
library, and the "solution" became a one-liner and thus no longer a useful
interview question. We constantly build new abstractions to reduce the code
required to get from Idea to Implementation with a minimum of effort, and as a
result we can build software today at a scale that would have been inconceivable
thirty years ago.

Not all abstractions are good, however: _leaky_ abstractions promise to remove the
busywork of having to understand the implementation details of a framework only
to slow down and stymie development later on. We sometimes chase the heuristic
of writing less code to solve a given problem only to realize we don't fully
understand what that code is actually doing at the lower levels. Even compilers
sometimes do the wrong thing! In the end, being able to express what you want
tersely is good, but is not a substitute for as much understanding as humanly
possible of the abstraction stack upon which you are building.

## What is important to me?

For me, the quality of a software solution is rarely about its innate
architectural or stylistic qualities, and almost always to do with how well it
solves a real, human problem. Building the most efficient gigafactory to build
Segways is still a waste of time when you only end up selling a few thousand
units. And if you start with a bad human process, automating it just leads to
worse outcomes. If time was an important asset when I started coding, it has
become so much more precious to the older, more responsible me, and I'm not
going to spend it perfecting code that already solves the problem at hand, and
I am even less enthusiastic about perfecting code that solves no problem at all.

When faced with a new technology, new framework, new language, or new process, I
ask myself: Can this help me get from identifying an inefficiency to solving it
more quickly than my existing tools? How much time will be wasted on boilerplate
and trip hazards?

I have to be real with you: The last decade has felt like a regression on
basically all fronts.

1. Python. What used to be a simple scripting language in the Python 2 days now feels like a fragmented ecosystem in Python 3. Incompatibility between interpreter versions and libraries means everything needs to run in a venv, or uv, or poetry, or conda, or...
2. Javascript. What used to be a simple scripting language that ran anywhere you could run a browser now suddenly needs to be compiled from Typescript modules using webpack, or vite, or...
3. Mobile. What used to be simple native SDKs have been replaced with "simpler" cross-platform solutions like Flutter, or React Native, or...

The number of decisions I have to make every time I want to write a quick script
or app have exploded. I want to solve a problem, not spend an hour getting my
environment set up to print "Hello, World" to the console.

## The future I'm excited about

I see a lot of excitement around LLM coding tools, but frankly a lot of it is
misplaced: I don't think the future is about writing code faster. The rate that
every single software product I use on a day-to-day basis ships updates is
already too fast. We even have a word for this: enshittification. At many of
these tech companies, code is flying out the door based purely on the needs of
the business faster than any kind of feedback is coming in from users. Software
teams worry about code quality more than they do about product quality and
making sure the features they launch are actually improving the product in a
meaningful way for users. What I am excited about is the ability to try out
ideas more quickly, throw together prototypes, launch a bunch of experiments out
into the world to gather feedback and then make decisions based on actual
real-world usage and user sentiment. I'm not naive: I don't expect VC-backed,
growth-focused startups to change their culture, but it is possible a new breed
of customer-experience-focused startups could outcompete them.

I know not everyone who writes code for a living and is accustomed to the status
quo will be happy with this style of development. But for me, the act of writing
code is not meaningful or fun in and of itself; it's the understanding and
solving of real problems that after all these years still excites me and
motivates me. The scope and scale of problems we can solve today would have been
unimaginable a generation ago, and I don't see any reason why that progress
should end now.
