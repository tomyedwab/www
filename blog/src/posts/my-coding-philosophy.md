Title: TODO
Subtitle: Written December 22, 2025
Description: TODO
Modified: 2025-12-22

In college, I took a part time job working on the website for the Haas School of
Business at UC Berkeley. This mostly consisted of odd maintenance work, but one
regular task I was assigned was to take the weekly newsletter email and format
it into HTML for the website. The task took an hour or so each week, and was a
bit tedious so after a few weeks I spent a few hours of my own time to automate
it. Luckily, I didn't fall into this trap:

![A link to xkcd #1319: Automation](https://xkcd.com/1319){ .article-centered }

What I like about this particular xkcd comic is that it captures the lengths
some of us are willing to go to save a small amount of boring, repetitive work.
I am in this picture, and to be honest I do like it. In this instance I was able
to shave the time down to about 5 minutes of copy-pasting from the email into a
web form, and out popped the fully formatted HTML. This is not an impressive
technical feat, but I think it captures my personal philosphy pretty well and
explains why I got into programming computer software in the first place.

## My personal philosophy of coding

What is my goal in sharing this? I don't expect all readers to share my
background, and many of you will disagree for various reasons. What I hope is
that you better understand where I am starting from when I talk about
technology, professional software development, and building teams of developers.
Instead of simply disagreeing, perhaps we can talk to each other more clearly if
we understand each other's perspective.

So here goes: For me, *all code is fundamentally a form of automation*. You
start with a manual, human process and you automate it to reduce effort and
increase speed and reliability. I am undeniably lazy: I want to spend my time
doing things that matter to me, and tedious tasks sap my energy and
concentration. Automation increases quality of life in a highly leveraged way: I
build the automation once and then I can share it with others, like my roommate
who took over my job at the business school when I graduated.

I don't want to downplay how much laziness plays a role here: Many of my
projects get abandoned because they turned out to be too much work. This has
become such a pattern for me that I reflexively enter each project with the goal
of minimizing effort, which traditionally has meant trying to write as little
code as possible.

Judging by the proliferation of standard libraries and frameworks, I am in good
company here. As an example, in Ye Olde Days a typical first-round technical
interview question we used involved reversing a string efficiently. In C this is
a very straightforward for loop, however once the dominant languages became
Python and Javascript the only sensible solution was to use the standard
library, and the solution became a one-liner. We constantly build new
abstractions to reduce the code required to get from Idea to Implementation with
a minimum of bother.

So: minimizing the amount of code was always just a proxy for minimizing the
amount of _effort_, both in initial implementation and long-term maintenance. A
lot of what we are thinking about when we talk about "code quality" is also
about effort: The effort required to understand the code and the effort to
extend it. There are _heuristics_ like having a thundering herd of unit tests or
a straightjacket of linters, but frankly I don't love the presumption they add
more value than they consume in effort to write and maintain. Similarly,
heuristics like Don't Repeat Yourself (DRY) can be actively harmful when applied
with thoughtless zeal.

## What is important to me?

The quality of a software solution is rarely about its innate architectural or
stylistic qualities, and almost always to do with how well it solves a real,
human problem. Building the most efficient gigafactory to build Segways is still
a waste of time when you only end up selling a few thousand units. And if you
start with a bad manual process, automating it just leads to worse outcomes. If
time was an important asset when I started coding, it has become so much more
precious to the older, more responsible me, and I'm not going to spend it
perfecting code that already solves the problem at hand.

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

The hot new thing right now is undoubtedly LLM coding tools, but I don't think
that's the whole story of where we are headed. What I'm excited about in general
is *the automation of automation*: how can I skip the boring boilerplate such as
"set up a Typescript/Preact project with hotreload" to get to the interesting
part of solving my problem? One-size-fits-all npm scripts are simply not good
enough. LLMs can do a good job of this right now but are inefficient and
error-prone; regardless, just like reversing a string becaming a single line of
code, perhaps someday a full API or a database schema could also be generated in
a single line of code.

I know not everyone will be happy with this development. But for me, the act of
writing code is not meaningful or fun in and of itself; it's the understanding
and solving of real problems that after all these years still excites me and
motivates me. The scope and scale of problems we can solve today would have been
inconceivable a generation ago, and I don't see any reason why that progress
should end now.
