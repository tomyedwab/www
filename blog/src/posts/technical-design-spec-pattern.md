Title: How to keep your AI coding agent from going rogue
Subtitle: Written May 20, 2025
Description: Complete agentic LLM coding projects reliably with this proven workflow.
Modified: 2025-06-20

You fired up Windsurf, or Copilot, or Cursor. You got comfortable with tab
autocomplete, asking questions about your codebase, prompting AI to write a few
short functions for you. These tools are fun to use and are saving you a modest
amount of time, so when a colleague tells you they are getting projects done
twice, five times, even _ten times faster_ by using an AI agent, you don't
immediately dismiss it. You wanted to see it for yourself, so you found a small,
self-contained project and prompted the agent to complete it for you.

You immediately ran into problems:

- Your agent installed an older version of a package and immediately ran into compatibility issues.
- Your agent forgot an import and started to rewrite the entire file to try to clear the errors.
- Your agent broke or deleted perfectly working code that wasn't related to the task at hand.
- Your agent forgot where it wrote a file and re-created it elsewhere in your workspace.
- Your agent decided the easiest way to get a test to pass was to delete the test.
- Your agent entered a "death spiral" of ever larger and more broken changes to resolve a simple issue.

In the end a task that should have taken a few hours instead consumed a whole
day, leaving you frustrated and perplexed. How is anyone actually seeing
speed-ups here? Are they just pushing whatever broken code this idiotic model
emits into production?

What I'm going to describe in this post is a pattern that I've seen multiple
software developers use but haven't seen written about extensively. I have used
it myself to _reliably get good results_ using an agenting LLM coding assistant,
and to _quickly identify and recover from mistakes_ to minimize time spent in
death spirals; the net result of which is a significant speed-up over working
without an agent. I'm dubbing this the **"Technical Design Spec"** pattern, as
this term both conveys the lynchpin idea of the pattern, and also happens to
elicit the behavior I want from the LLMs I've tested.

Will this pattern be obviated by better models and smarter agents? We can hope!
But for now, it seems widely applicable across a variety of agentic tools and
foundational language models, so it's worth giving it a try if, like me, you've
struggled to get good results by directly asking the agent to implement a
feature.

The pattern is broken down into a set of independent ideas that work together to
keep the agent on track. Some of these ideas seem like a lot of extra work and
you might worry this will slow down development. If a human had to do all this
extra bookkeeping, this would be a real concern. But the AI agent is typically
so fast at doing and re-doing these steps that the added reliability and
predictability more than make up for the extra effort.

Anyway, without further ado:

## 💡 Idea #1: For any multi-step operation, prompt the agent to write a Technical Design Spec into a Markdown file in your workspace. This spec lives in source control for the duration of the project.

_Justification:_ Forcing the agent to commit plans to writing before starting implementation achieves several critical goals:

1. Allows you an opportunity to review and correct assumptions and technical decisions before committing to them,
2. Lays out a step-by-step implementation plan that can guide small, incremental changes (see Idea #3),
3. Provides a form of task memory for planning details and work in progress that can be checkpointed (see Ideas #4 and #5),
4. Summarizes implementation details that form the basis for technical documentation (see Idea #6).

Again, we're not writing a spec merely because it's a good practice to gather
requirements and break work down into discrete steps. We are exerting oversight
into what the agent has in its context window and minimizing the random behavior
that all LLMs exhibit by default.

What is and isn't included in a spec is fully up to you and your style of
coding. Usually my specs include project goals, a list of tasks, modules or
files to create or update, function definitions and APIs. Within an existing
codebase, the agent may have to do some research to complete the spec, but it
should not write any code at this stage.

For a larger project such as building a whole application from the ground up,
the individual steps might themselves involve multiple steps and therefore need
to be broken down in their own spec files before the agent can start
implementation. The parent spec should have only the details such as
API definitions that are needed to coordinate work across the different steps,
while further implementation details should be pushed down to the relevant child
spec.

_Note:_ For this task you will want to select a model with strong reasoning capabilities
and allow it as much time to think as possible: The more thinking that is done
ahead of time, the faster and smoother the implementation will go. (Honestly,
I've found this to be solid life advice as well.)

_Example:_ Here I am taking a high-level description of a feature and asking the
LLM agent to write a detailed technical spec. The model is
`gemini-2.5-pro-preview-05-06`.

> Write a comprehensive Technical Design Spec for a new backend feature in the
> users service allowing users to specify their favorite color. It should include
> a REST endpoint and a new database model. Use existing endpoints and models for
> reference. Break the work down into discrete tasks but do not include any code.
> Put the spec in specs/user-favorite-color.md.

The output spec is included verbatim in the appendix.

## 💡 Idea #2: Ensure that spec files include full file paths to any relevant files in your workspace.

_Justification:_ A specific failure case that happens in larger projects is the
agent losing track of which files it has created and creating duplicate
files in different paths. These incorrect paths seem to be exacerbated by
references in the spec to bare filenames like `main.go`, and it pays to be
vigilant against these and replace them with full paths such as
`server/cmd/main/main.go`. Including the path to each file in the spec
allows the agent to read and write directly without additional tool calls to
find the file's location.

## 💡 Idea #3: Implement against the spec by prompting for one step at a time, including the spec file in the context explicitly.

_Justification:_ Prompting the agent to implement only one step at a time
prevents it biting off more than it can chew, and gives you frequent checkpoints
to roll back to when &mdash; not if &mdash; something goes terribly wrong (see Idea #4).
This does require actively monitoring the agent, prompting it to move to the next
step and testing each change in isolation, so don't expect to submit your prompt
and come back the next morning to a finished project. That said, it's not
necessary to choose the next step or give context about the other steps since
that is all coming from the spec.

How much attention I pay to the output depends on whether the code will need to
be maintained for a long time, as opposed to short-lived code I can "vibe code"
quickly without any review. That said, the volume of changes for one step is
usually reasonable to at least skim through.

_Example:_ Since the spec contains all the steps, my prompt is very simple:

> Per @user-favorite-color.md, implement the first step.

_Note:_ Since the spec is fairly detailed, I don't need to waste a lot of thinking
tokens on this task. Therefore I can safely fall back to a simpler model like
`claude-3.5-sonnet` that is good at fast and accurate implementation.

## 💡 Idea #4: When the agent makes a mistake, roll back to a checkpoint and update the prompt before trying again.

_Justification:_ It's tempting to treat the agent like a coworker and correct it
when it makes a mistake. This works for very minor corrections, but if the agent
is really going down the wrong path, asking it to undo changes and take a
different approach leaves it with a large amount of its limited context window
consumed with invalid history that the model now has to actively ignore.
Performance on the second try invariably suffers.

Unlike your coworker, the agent will not feel offended if you revert all their
changes yourself and try again: you might clarify your prompt to avoid a
particular stumbling block, or you might make changes to ambiguous points in the
spec. If you are using rules files in your project, you might add new guidance
there as well. Sometimes due to the non-deterministic nature of the model,
simply retrying the same exact prompt will lead to a better result!

Some agenting coding tools have built-in support for rolling back to the last
prompt or rejecting all changes. If your tool does not have this feature, I
suggest committing to source control after each successful step so you have a
checkpoint to roll back to. You can always squash the commits later.

## 💡 Idea #5: At the end of every implementation step, let the agent update the spec and start a new chat session.

_Justification:_ Current-generation LLM performance degrades noticeably as the
context window gets full, increasing the rate of hallucinations and mistakes,
wasting more time and more tokens. Some agentic tools tell you when this is
happening, while others quietly drop parts of the conversation history. To get
the best and most predictable performance you want to keep the context window
focused on the task at hand, which means aggressively culling tasks from the
context window as soon as they are completed. This is achieved by simply
starting a new chat session at the end of each task.

Crucially, this requires that any information required by a subsequent task needs
to be retained in the spec file, which serves as "long term memory" and process
documentation for the duration of the project. Thus, at the end of each chat
session you should prompt the agent to update the spec if it hasn't already done
it (by instruction from rules files).

_Note:_ I haven't really tried this myself, but if the tasks are isolated
enough, you could run multiple agents concurrently in different work trees and
use the spec file to coordinate the work. Or multiple developers could share a
branch using their own agents on their assigned tasks. This is one potential
benefit of checking the spec file into a feature branch.

_Example:_ After completing each step, my final prompt is something like:

> Update the spec file with this progress and any technical details we will need
> for the rest of the project.

The most helpful details this step adds to the spec file are completed tasks (so
the next call to the agent doesn't try to implement steps that are already
complete) as well as absolute file paths and class names needed for subsequent
steps.

## 💡 Idea #6: Once a spec is complete, let the agent update the parent spec and relevant documentation.

_Justification:_ You could very reasonably just leave the spec files in the
repository long-term and use them as documentation. This is not my style; I find
I have very different needs of documentation for in-flight projects compared to
long-lived documentation such as API references, style guides, READMEs or
package/file-level docstrings. Therefore, I suggest one final best practice: at
the end of the project, prompt the agent to use the completed spec document to
create or update this long-lived documentation. Then delete the project spec
before merging to main, deploying, etc.

This applies whether the documentation lives in your repository or elsewhere;
you may have tooling to enable agents to easily read and update documentation in
a Wiki, for example. But the principle remains the same.

As well as updating documentation, if the completed spec has a parent spec, now
is a good time to update that spec with completion status and any relevant
decisions that were made during implementation.

## Summary

That's it! If you are struggling to make progress with an agent I highly
recommend trying this pattern in full, and then keeping the parts that work for
you. Or use this as inspiration to invent your own ways to manage the contents
of the context window, passing relevant context to the agent while removing
irrelevant details to keep it from being overwhelmed and allowing it to make
decisions while you stay in control.

Good luck!

----

## Appendix: Example Technical Design Spec

Below for reference is the verbatim output of the example prompt from Idea #1:

<pre>
# Technical Design Spec: User Favorite Color Feature

## 1. Overview

This document outlines the technical design for a new feature allowing users to specify and update their favorite color. This feature will integrate with the existing event-driven architecture of the users service. It involves creating a new database table to store favorite colors, defining a new event to signal color updates, implementing a state handler to process this event and manage the table, updating the event mapper, and exposing a new REST API endpoint for users to set their favorite color.

## 2. Database Model: `user_favorite_colors_v1`

A new SQL table will be created to store user favorite colors.

*   **Table Name**: `user_favorite_colors_v1`
*   **Purpose**: To store a single favorite color preference for each user.
*   **Schema Definition**:
    *   `user_id TEXT PRIMARY KEY`: The unique identifier for the user. This will be a foreign key referencing the primary ID of the main user table (e.g., `users_v1.id`).
    *   `color TEXT NOT NULL`: The user's chosen favorite color (e.g., "blue", "#00FF00").
    *   `updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP`: Timestamp of when the favorite color was last set or updated.
*   **Indexes**: A primary key index will automatically be created on `user_id`.
*   **Foreign Key Constraint**: `FOREIGN KEY(user_id) REFERENCES users_v1(id) ON DELETE CASCADE`. This ensures that if a user is deleted, their favorite color record is also removed.

## 3. Events

A new event type will be defined to represent the action of a user setting or updating their favorite color.

*   **Event Name**: `UserFavoriteColorUpdatedEvent`
*   **Base Event**: This event will embed `events.GenericEvent` to include common fields like `Id` and `Type`.
*   **Event Type String**: `"user:FAVORITE_COLOR_UPDATED"`
*   **Payload Fields**:
    *   `UserID string`: The ID of the user whose favorite color is being updated.
    *   `Color string`: The new favorite color.
*   **Conceptual Struct Definition**:
    ```go
    // type UserFavoriteColorUpdatedEvent struct {
    //     events.GenericEvent
    //     UserID string `json:"user_id"`
    //     Color  string `json:"color"`
    // }
    ```

## 4. State Handler: `UserFavoriteColorStateHandler`

A new state handler will be responsible for managing the `user_favorite_colors_v1` table.

*   **Handler Name**: `UserFavoriteColorStateHandler`
*   **Signature**: Conforming to `func(tx *sqlx.Tx, event events.Event) (bool, error)`.
*   **Responsibilities**:
    *   **Schema Initialization**: On receiving an `*events.DBInitEvent`, the handler will execute a `CREATE TABLE IF NOT EXISTS user_favorite_colors_v1 ...` DDL statement as defined in Section 2.
    *   **Event Processing**: On receiving a `*UserFavoriteColorUpdatedEvent`:
        *   It will perform an "upsert" operation (insert or update) into the `user_favorite_colors_v1` table.
        *   SQL (conceptual): `INSERT INTO user_favorite_colors_v1 (user_id, color, updated_at) VALUES ($1, $2, NOW()) ON CONFLICT (user_id) DO UPDATE SET color = EXCLUDED.color, updated_at = NOW();`
        *   It will return `true, nil` if the event is handled successfully.
    *   If the event is not `*events.DBInitEvent` or `*UserFavoriteColorUpdatedEvent`, it will return `false, nil`.

## 5. Event Mapper (e.g., `state.MapUserEventType`)

The existing event mapper function responsible for deserializing generic event messages into specific typed Go event structs will be updated.

*   **Modification**: Add a new `case` to the `switch generic.GetType()` statement.
*   **Logic for `"user:FAVORITE_COLOR_UPDATED"`**:
    *   Unmarshal the raw message (`*json.RawMessage`) into a `UserFavoriteColorUpdatedEvent` struct.
    *   Copy common fields from the input `generic` event to the specific event's embedded `GenericEvent`.
    *   Return the populated `*UserFavoriteColorUpdatedEvent` and `nil` error.

## 6. REST API Endpoint

A new REST API endpoint will be created to allow users (or authorized systems) to set/update a user's favorite color.

*   **Endpoint**: `PUT /api/users/{user_id}/favorite-color`
*   **HTTP Method**: `PUT` (chosen for its idempotency in setting/replacing the favorite color resource).
*   **Path Parameter**:
    *   `user_id (string)`: The unique identifier of the user.
*   **Request Body (JSON)**:
    ```json
    {
      "color": "sky blue"
    }
    ```
*   **Authentication**: Required. The caller must be authenticated.
*   **Authorization**:
    *   A user should typically only be allowed to update their own favorite color. The API handler will verify that the authenticated user's ID matches the `user_id` in the path.
    *   Administrative overrides might be considered for future iterations but are out of scope for the initial implementation.
*   **API Handler Logic**:
    1.  Authenticate the request.
    2.  Validate the `user_id` path parameter and the request body (e.g., `color` field is present and valid).
    3.  Authorize the request (e.g., check if authenticated user matches `user_id`).
    4.  If valid and authorized, create a `UserFavoriteColorUpdatedEvent` with the `user_id` and `color`.
    5.  Dispatch this event using the `database` core's event publishing mechanism.
    6.  Return an appropriate HTTP response.
*   **Success Response (200 OK)**:
    ```json
    {
      "user_id": "actual-user-id",
      "color": "sky blue",
      "updated_at": "iso8601-timestamp"
    }
    ```
*   **Error Responses**:
    *   `400 Bad Request`: Invalid request body (e.g., missing `color`, invalid color format).
    *   `401 Unauthorized`: Authentication failure.
    *   `403 Forbidden`: Authenticated user is not authorized to update the specified `user_id`'s favorite color.
    *   `404 Not Found`: The specified `user_id` does not exist.
    *   `500 Internal Server Error`: Unexpected server-side error during event processing.

## 7. Data Validation

*   **Color Field**: The `color` string in the request body should be non-empty. Further validation (e.g., specific formats like hex codes, or a list of allowed named colors) can be added. Initially, a non-empty string will suffice. Max length for the color string should also be considered (e.g., 50 characters).

## 8. Registration and Initialization (e.g., in `users/cmd/serve/main.go`)

The new components must be registered with the system:

*   **State Handler Map**: The `UserFavoriteColorStateHandler` will be added to the map of handlers passed to `database.Connect()`, associated with a key like `"user_favorite_colors_v1"`.
*   **Event Mapper**: Ensure the `database.InitHandlers()` (or equivalent) is called with the updated event mapper function that includes the new `UserFavoriteColorUpdatedEvent` mapping.
*   **API Endpoint**: The new `PUT /api/users/{user_id}/favorite-color` route and its handler function will be registered with the HTTP server.

## 9. Breakdown of Tasks

1.  **Define Event Struct**:
    *   Create the `UserFavoriteColorUpdatedEvent` struct (embedding `events.GenericEvent`) in the relevant events definition file (e.g., `users/state/events.go` or a new `users/state/db-user-favorite-colors-events.go`).
2.  **Implement State Handler**:
    *   Create the `UserFavoriteColorStateHandler` function (e.g., in a new file `users/state/db-user-favorite-colors.go`).
    *   Implement logic for `*events.DBInitEvent` to create the `user_favorite_colors_v1` table, including the foreign key constraint.
    *   Implement logic for `*UserFavoriteColorUpdatedEvent` to perform the upsert operation.
3.  **Update Event Mapper**:
    *   Modify the existing `MapUserEventType` (or equivalent function, likely in `users/state/mapper.go`) to include a case for `"user:FAVORITE_COLOR_UPDATED"`, deserializing it into `*UserFavoriteColorUpdatedEvent`.
4.  **Implement API Handler**:
    *   Create the HTTP handler function for the `PUT /api/users/{user_id}/favorite-color` endpoint.
    *   Include request validation (path params, body), authentication, and authorization logic.
    *   On success, construct and dispatch the `UserFavoriteColorUpdatedEvent`.
    *   Return appropriate HTTP success or error responses.
5.  **Register Components**:
    *   In `users/cmd/serve/main.go` (or the application's entry point):
        *   Add `UserFavoriteColorStateHandler` to the `handlers` map.
        *   Register the new API route and its handler.
6.  **Testing**:
    *   Write unit tests for:
        *   `UserFavoriteColorStateHandler` (DB initialization and event handling logic).
        *   The new case in the Event Mapper.
        *   The API endpoint handler (validation, auth, event dispatch, responses).
    *   Write integration tests to cover the end-to-end flow: API call -> event creation -> state handler processing -> database update.
7.  **Documentation**:
    *   Update any API documentation (e.g., Swagger/OpenAPI specifications) to include the new endpoint.
    *   Ensure internal documentation (like this spec) is accessible. 
</pre>