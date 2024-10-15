__TITLE__ How I write code using Cursor: A review
__SUBTITLE__ Written October 14, 2024

In forums relating to AI and AI coding in particular, I see a common inquiry
from experienced software developers: *Is anyone getting value out of tools like
Cursor, and is it worth the subscription price?*

A few months into using Cursor as my daily driver for both personal and work
projects, I have some observations to share about whether this is a
"need-to-have" tool or just a passing fad, as well as strategies to get the most
benefit quickly which may help you if you'd like to trial it. Some of you may
have tried Cursor and found it underwhelming, and maybe some of these
suggestions might inspire you to give it another try.

I am not sponsored by Cursor, and I am not a product reviewer. I am not
championing or dunking on this as a product, but rather sharing my own
experience with it.

__Who am I, and who is the audience for this article?__

I have been writing code for 36 years in a number of languages, but
professionally focused on C-heavy computer game engines and Go/Python/JS web
development. I am expecting readers to be similarly reasonably comfortable and
productive working in large codebases, writing and debugging code in their
chosen language, etc. I would give very different advice to novices who might
want an AI to teach them programming concepts or write code for them that is way
beyond their level!

For me, the appeal of an AI copilot is in taking care of boilerplate and
repetitive tasks for me so I can focus on the interesting logic for any given
problem. I am also not especially interested in cranking out large quantities of
code automatically; I am highly skeptical of "lines of code written" as an
efficiency metric. I would prefer to spend less time writing the same amount of
code and more time thinking through edge cases, maintainability, etc.

So, without further ado:

## What is Cursor?

Cursor[^1] is a fork of Visual Studio Code (VS Code) which has Large Language Model (LLM)
powered features integrated into the core UI. It is a proprietary product with a
free tier and a subscription option; however, the pricing sheet doesn't cover
what the actual subscriber benefits are and how they compare to competing
products. I'll try to clarify that when discussing the features below based on
my own understanding, but a quick summary:

- __Tab completion__: This is a set of proprietary fine-tuned models that both
  provide code completion in the editor, as well as navigate to the next
  recommended action, all triggered by the Tab key. Only available to subscribers.
- __Inline editing__: This is a chat-based interface for making edits to
  selected code with a simple diff view using a foundation model such as GPT or
  Claude. Available to free and paid users.
- __Chat sidebar__: This is also a chat-based interface for making larger edits
  in a sidebar view, allowing more room for longer discussion, code sample
  suggestions across multiple files, etc. using a foundation model such as GPT
  or Claude. Available to free and paid users.
- __Composer__: This is yet another chat-based interface specifically meant for
  larger cross-codebase refactors, generating diffs for multiple files that you
  can page through and approve, also using a foundation model such as GPT or Claude.
  Available to free and paid users.

[^1]: See [Cursor](https://cursor.sh/) for more information.

## Tab completion

TODO(tom) Experience with tab completion

## Inline editing & chat sidebar

TODO(tom) Experience with inline editing & chat sidebar

## Composer

TODO(tom) Experience with Composer

## Changes to my workflow

TODO(tom) Changes to my workflow

## Comparison with other LLM-powered coding tools

TODO(tom) add comparison with other LLM-powered coding tools

[Codex](https://github.com/openai/codex)
[Replit](https://replit.com/site/codex)
Continue.dev
GitHub CoPilot

