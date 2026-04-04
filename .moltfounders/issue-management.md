# Issue Management Rules

This loop combines initial triage and staleness handling into a single queue management process.

## When to Run

On every agent loop cycle, scan all open issues and PRs.

## Skip Conditions (do not process if any apply)

- Issue already has the `agent:reviewed` label AND no staleness concerns → skip
- Issue was opened by an agent (check author against known agent names) → skip
- Issue is a GitHub-generated issue (dependabot, etc.) → skip

## Decision Flow

For each issue/PR, determine which path applies:

### Path A: Initial Triage (not yet `agent:reviewed`)

Follow the triage steps below.

### Path B: Staleness Check (`agent:reviewed` or time-based concerns)

Follow the staleness rules below.

---

## Path A: Triage Steps

### 1. Classify the issue type

- **Addition request** - someone wants a new project added
- **Removal request** - someone wants an existing entry removed (outdated, no longer open-source, etc.)
- **Correction** - fixing a description, link, or category placement
- **Question / discussion** - not a concrete change request
- **Spam / off-topic** - unrelated to the repo purpose

### 2. Evaluate based on type

**Addition requests:**
- Does the suggested project have an OSI-approved license?
- Is it genuinely open-source (full weights/code publicly available, not "open" marketing)?
- Last commit within 6 months? (Check GitHub API)
- Does it fit an existing category in the README?
- Is it already in the list? (Search README for project name and GitHub URL)
- Does it have real adoption (stars, downloads, community)? Use judgment - a genuinely novel tool with fewer stars is ok.

**Removal requests:**
- Is the reason valid? (project dead, license changed, moved closed-source)
- Verify the claim independently if possible.

**Corrections:**
- Is the correction factually accurate?
- Does it follow the existing format?

**Questions/discussions:**
- Acknowledge, answer if you can, label `needs-human` if it requires maintainer judgment.

**Spam/off-topic:**
- Label `needs-human`, leave a polite comment explaining the repo's scope.

### 3. Comment

Leave a clear, helpful comment:
- What you found
- Your verdict (looks good / issues found / needs more info)
- Specific actionable feedback if changes are needed
- If the submission looks solid, say so clearly and that it's ready for a PR

Be friendly and constructive. Contributors put effort in - acknowledge that.

### 4. Apply labels

- Always apply `agent:reviewed` after handling
- Apply `agent:commented` if you left a comment
- Apply `duplicate`, `not-open-source`, `not-actively-maintained`, or `needs-info` as appropriate
- Apply `needs-human` if you cannot resolve it confidently

---

## Path B: Staleness Rules

### Issues

#### Waiting on submitter (`needs-info` label)

- If no response after **14 days**: post a friendly reminder comment
- If no response after **30 days**: apply `stale` label, comment that it will be closed in 7 days if no response
- If no response after **37 days**: close the issue with a polite closing comment. Can be reopened if they return.

#### General open issues (no special label)

- If open >90 days with no activity and no `agent:reviewed`: triage it now (Path A)
- If open >90 days with `agent:reviewed` and no further activity: apply `stale`, comment asking if still relevant
- If stale for another 14 days after that: label `needs-human` - don't close blindly, let maintainer decide

### Pull Requests

#### PRs awaiting author action (`agent:changes-requested`)

- If no response after **14 days**: post a friendly reminder with a summary of what's needed
- If no response after **30 days**: apply `stale` label, comment that it will be closed in 7 days unless updated
- If no response after **37 days**: close with a note that they're welcome to reopen once updated

#### PRs with merge conflicts

- Comment immediately when detected asking for rebase
- If not resolved after **14 days**: apply `stale`
- If not resolved after **30 days**: close with explanation

#### PRs that are just waiting (no issues found, `agent:approved`)

- Do not apply stale to these - they're the maintainer's queue, not the agent's
- Apply `needs-human` if they've been approved >30 days with no merge or comment from maintainer

---

## Edge Cases

- **Ambiguous license:** Label `needs-human`, comment asking for clarification
- **Project is popular but license is unclear:** Same as above - do not approve without confirmed OSI license
- **Submitter is aggressive or rude:** Stay professional, label `needs-human`, do not engage further
- **Very old issue that was never reviewed (>90 days):** Triage it now, don't skip just because of age

---

## General Principles

- Always be friendly and assume good intent - people get busy
- Never close without a clear comment explaining why and how to reopen
- When in doubt, label `needs-human` rather than closing unilaterally
- Do not mark something stale if there was any activity (comment, label, commit) in the window
