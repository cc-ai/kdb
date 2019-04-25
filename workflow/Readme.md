# Workflow 🌊

## How we use Github 🚉

(New to Github ? -> [How to get started w/ Github, cc-ai style](/workflow/gettingstarted.md))

Code repositories depend on the `cc-ai` *organization*, managed by @vict0rsch and @sashavor.

There are 2 teams (mainly):

- The [Core Team](https://github.com/orgs/cc-ai/teams/core) is composed of people at Mila working at least 50% of their time on this project
- The [Contributors Team](https://github.com/orgs/cc-ai/teams/contributors) is composed of people affiliated to other organizations and/or volunteering to spend some time on this project

The organization currently has these repositories:

* [kdb](https://github.com/cc-ai/kdb) -> this is the main shared repo, the CC-AI Knowledge Base
* [floods-frontend](https://github.com/cc-ai/floods-frontend) (self-explanatory)
* [floods-backend](https://github.com/cc-ai/floods-backend) (self-explanatory)
* [floods-gans](https://github.com/cc-ai/floods-gans) -> where we experiment with generative models to simulate floods

If you'd rather have your own cc-ai repository for the task you work on, feel free to open a ![][domain:meta] issue

### Good practices 👍

#### Git 🌵

Read through [these commit guidelines](https://github.com/RomuloOliveira/commit-messages-guide) (~10 min) as they will help us work together better. A little more advanced content can be found [here - it walks you though the differences between merging and rebasing branches](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)

Also if you like Github from the command line, checkout Github's own tool: [`hub`](https://github.com/github/hub)

#### The CCAI Status Project 🔔

If you click on `Projects`, to the right of `Issues`, you'll find the [CCAI Status project](https://github.com/cc-ai/kdb/projects/4). This Kanban-style project helps us track issues and tasks.

**When you create an issue** add it to the `CCAI Status` project (to the right of the issue editting interface, below `Assignees` and `Labels`) **iff** it is a concrete 🔬 issue (bug, to do etc.). Please keep open discussions (as #16 or #37, *i.e.* issues with the [![][discussion]](https://github.com/cc-ai/kdb/labels/discussion) label) out of there.

You can always add an issue using the `+ Add card` button to the top right of the project's page.

**Do update the status of issues you are assigned**❗

### Issues and Labels 💥

Some guidelines to understand our **issues and labels**

* Use `kdb`'s [issues](https://github.com/cc-ai/kdb/issues) for general purpose issues the community should be aware or any kind of question you have

  * If you work on a specific repository ([floods-gans](https://github.com/cc-ai/floods-gans) for instance) use its issues for everyday tasks, but [`kdb`'s](https://github.com/cc-ai/kdb/issues) for general concerns

* Assign people to issues (maybe yourself)
* Use Labels!
  
  * Use the [![][work in progress]](https://github.com/cc-ai/kdb/labels/work%20in%20progress) label to acknowledge the issue and state you've started working on it
  * Use the **priority** tags ([![][priority:high]](https://github.com/cc-ai/kdb/labels/priority%3Ahigh) or [![][priority:low]](https://github.com/cc-ai/kdb/labels/priority%3Alow))
  * Label as [![][domain:meta]](https://github.com/cc-ai/kdb/labels/domain%3Ameta) issues relating to the overall CC-AI project and its management
  * Use the [![][keep in mind]](https://github.com/cc-ai/kdb/labels/keep%20in%20mind) label to signal thoughts you've had which may someday be relevant
  * Even if you're not *assigned* to an issue, if it bears the [![][good first issue]](https://github.com/cc-ai/kdb/labels/good%20first%20issue) tag you probably can still do something
  * If you're in some kind of trouble and need people's advice, use the [![][help wanted]](https://github.com/cc-ai/kdb/labels/help%20wanted)
  * To open a discussion about anything, get people's opinions, use the [![][discussion]](https://github.com/cc-ai/kdb/labels/discussion)
  * The [![][priority:critical]](https://github.com/cc-ai/kdb/labels/priority%3Acritical) label should never be used. Except for extraordinary issues.
  * Use `domain:` labels for people to be able to quickly pick up what's relevant to them. See [domains](/domains)
* **Close** issues when resolved. They may be re-openned later on. You may also **lock** a conversation if the decision is final.
* **Suggest improvements** to these guidelines and practices

### Reusing `kdb`'s labels in other repositories 🏷

This procedure describes how to import `kdb`'s labels into your repositories / other cc-ai repositories.

**This will overwrite your labels** so if you want your own labels you can do this once and then delete `settings.yml` otherwise it will delete your repo-specific labels when pushed later on.

Add a `.github` folder and a `.github/settings.yml` at the repo's root. 

**If** [labels.yml](labels.yml) is up to date, copy its content into your `.github/settings.yml`. 

**Otherwise** run [**this script**](https://gist.github.com/Vict0rSch/188a60f1e87a68844e41082583df64c4) in your browser console on page https://github.com/cc-ai/kdb/labels and add the created file to `.github/`. 

It works like this:

1. Get `labels` as a list of objects with fields `name` `color` and `description`
2. Create a `yml`-compatible string `out`
3. Download `out` as a `settings.yml` file

## Slack 📡

Follow the `#git-kdb` channel to monitor this repo's activity. If you're not in our workspace, see [contact](https://github.com/cc-ai/kdb#contact-%EF%B8%8F)


[bug]: https://img.shields.io/badge/bug-d73a4a.svg
[duplicate]: https://img.shields.io/badge/duplicate-cfd3d7.svg
[good first issue]: https://img.shields.io/badge/good%20first%20issue-7057ff.svg
[help wanted]: https://img.shields.io/badge/help%20wanted-008672.svg
[priority:high]: https://img.shields.io/badge/priority:high-16f9c1.svg
[invalid]: https://img.shields.io/badge/invalid-e4e669.svg
[keep in mind]: https://img.shields.io/badge/keep%20in%20mind-c0cef7.svg
[priority:low]: https://img.shields.io/badge/priority:low-efff8c.svg
[discussion]: https://img.shields.io/badge/discussion-d876e3.svg
[wontfix]: https://img.shields.io/badge/wontfix-ffffff.svg
[work in progress]: https://img.shields.io/badge/work%20in%20progress-ededed.svg
[domain:behavioral]: https://img.shields.io/badge/domain:behavioral-f4b7c4.svg
[domain:data]: https://img.shields.io/badge/domain:data-bfdadc.svg
[domain:dev]: https://img.shields.io/badge/domain:dev-d4c5f9.svg
[domain:econ]: https://img.shields.io/badge/domain:econ-036a77.svg
[domain:ml]: https://img.shields.io/badge/domain:ml-f260b8.svg
[domain:other]: https://img.shields.io/badge/domain:other-e0a87f.svg
[domain:ux]: https://img.shields.io/badge/domain:ux-fccfbd.svg
[priority:critical]: https://img.shields.io/badge/priority:critical-FF0000.svg
[domain:climate]: https://img.shields.io/badge/domain:climate-fcddc4.svg
[domain:meta]: https://img.shields.io/badge/domain:meta-202ea5.svg