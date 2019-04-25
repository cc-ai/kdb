# Github at `cc-ai` : getting started 🥋

Hello and welcome to the CCAI GitHub!

In this repository, we will of course share code, but also links, articles, websites, and ideas. We will also use it for defining who does what task (i.e. ticket) and follow the progress of tickets and tasks as they evolve.

Don't worry if you've never used GitHub before! You can actually use GitHub without knowing ANY code at all. It's really a straightforward tool, and this document will help you cover the basics.

## Git 🌵 

Git is a software to do version control, which means it will save any changes being done without overwriting any past work. This means that even if several people are working on the same file at the same time, each person can upload their changes to the page, and Git will save both copies. Later, they can be <b> merged </b> together without anyone losing their work. You can even go back to a previous version at any point, because Git will keep a history of every change ever made. Typically, git is used via a [terminal or command line](http://guides.beanstalkapp.com/version-control/common-git-commands.html) and stores the versions on your computer. But GitHub allows us to store the content and versions online ; plus, it adds a user interface on top of Git, which makes it possible to download and change files from your browser or your desktop, make comments, suggest fixes, etc.


## Vocabulary 🙊 

Some useful GitHub vocabulary (from [this guide](https://readwrite.com/2013/09/30/understanding-github-a-journey-for-beginners-part-1/))

**Markdown**: A way to write text files so that they are rendered beautifully on Github without the hastle of using `html`. For instance, if you start a line with `# This is a title`, it will be rendered by Github as a Top-level title (as `# Github at cc-ai : getting started 🥋`). If you add a `#` it will be displayed as a secondary title (as `## Vocabulary 🙊 `) and so on until `###### minor title`. Including links is extremely easy too! `[website](https://website.com)` will be rendered like this: [website](https://website.com). These special text files have a `.md` extension. On GitHub if there is a `Readme.md` file in the current folder you're looking into, it will be automatically rendered. If you click on a specific `.md` file, it will also be rendered. To see the `raw` text, before rendering, you can just click on the `raw` button (no shit...). Remember: Markdown is easy, ask for help if you're stuck with something. In the mean time, [**checkout this cheatsheet to learn in 2 minutes how to use Markdown**](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

<p align="center"><img alt="editting a readme" src="https://media.giphy.com/media/TKifS1eBNfEud7jQuy/giphy.gif"/></p>

**Repository or Repo** : A directory or storage space where your projects can live. It can be local to a folder on your computer, or it can be a storage space on GitHub or another online host. You can keep code files, text files, image files, you name it, inside a repository.

**Commit**: This is the command that gives Git its power. When you commit, you are taking a “snapshot” of your repository at that point in time, giving you a checkpoint to which you can reevaluate or restore your project to any previous state.

**Branch**: How do multiple people work on a project at the same time without Git getting them confused? Usually, they “branch off” of the main project with their own versions full of changes they themselves have made. After they’re done, it’s time to “merge” that branch back with the “master,” the main directory of the project.

**Issue**: Although the name may sound negative <i> ("Oh no, there's an issue with my project!") </i>, 'issue' is just the name used by GitHub for different tasks that contributors can assign to themselves. You can open an issue when you've defined it as something that needs to be worked on, tag it with labels depending on what it involves, and then assign it to yourself (or someone else!). A very important document that explains this workflow for the **cc-ai project** process can be found [**here**](https://github.com/cc-ai/kdb/tree/master/workflow).



## What we will use GitHub for 🔦

- **Sharing code** : for the coders among us, GitHub will be a way to test out different parameters, make changes to the code, clone (a.k.a.) copy other repositories that we can test, share results, etc. This will be done via the various repositories in the project, which can be seen at https://github.com/cc-ai 

- **Tracking progress:** Even if the task that you are working on doesn't involve coding (e.g. literature review, experimental testing, etc.), it's useful for the rest of the team to know that you are working on a certain task (or issue), and what the progress on it is: whether it is open, closed, in progress, pending, etc. We will do this via the Kanban: https://github.com/cc-ai/kdb/projects/4 

- **Sharing resources:** A section of the repository is dedicated specifically to sharing common resources : https://github.com/cc-ai/kdb/tree/master/resources. These can be research papres, code, news articles, tools, etc. If you encounter something useful in your literature review (or even during your spare time!), add it to the resource section! 

- **Sharing ideas:**  If you see an open ticket that is labelled as "help wanted", or if you simply have an idea about a task that someone else is working on, don't hesitate to leave a comment on the issue: it can help open a discussion and generate new ideas! 

- **Collaborating with external contributors:** We are lucky enough to have a group of people interested in CCAI, who want to help us with different tasks depending on their domain of expertise: UI design, front-end development, economics.. the sky is the limit! To make this collaboration as smooth as possible, we want to give them specific tasks and ways to help us, check in with progress, ask questions, etc. GitHub is the place to do this!  

## Some Brief Tutorials
 
### Adding a paper from a link 

- From the home page (https://github.com/cc-ai/kdb) click on `resources` in the top folder structure, then on `papers` (or the link provided): you should be at https://github.com/cc-ai/kdb/tree/master/resources/papers
- Remember, **by default, Github displays the file called `Readme.md`**
- You can edit this file and add your preferred paper by clicking on the pencil icon to the top right of the displayed Readme
- Add a line with your paper line this `* [paper title](https:// link to paper)`

<p align="center"><img alt="adding a link" src="https://media.giphy.com/media/co5O8kmFcr0kv6kj7M/giphy.gif"/></p>


### Adding a paper from a pdf

If you can simply add a link to this pdf, it's better as it makes the hole repository heavier for others to sync with. But if you can't and want to share the file, here's how to:

- Host it elsewhere (Google Drive or something)
- Host it on the repository
  - From the home page (https://github.com/cc-ai/kdb) click on `resources` in the top folder structure, then on `papers` (or the link provided): you should be at https://github.com/cc-ai/kdb/tree/master/resources/papers
  - Click on `Upload files`
  - Drag and drop or `choose your files`
  - Commit (= save)
  - Copy link to file
- Add the hosted file link to the `Readme.md` as described previously

<p align="center"><img alt="adding a pdf" src="https://media.giphy.com/media/SwmmifQOkBjdrGGzcT/giphy.gif"/></p>

### Opening an issue

#### Why

Remember, issues are used to track problems, open discussions about a topic or simply create a task to be done. Basic use cases include:

- Getting people's opinion on a matter (like victo did for the who's who -> [see #39](https://github.com/cc-ai/kdb/issues/39))
- Signaling a bug in some code (unexpected behavior, error in execution, installation issues and so on)
- Reminding yourself (and possibly others) about something to be done (like the example issue below -> [see #43](https://github.com/cc-ai/kdb/issues/43) )

#### How

- From the home page (https://github.com/cc-ai/kdb) click on `issues` in the top folder structure: this should bring you to https://github.com/cc-ai/kdb/issues
- This will show you the list of currently open issues
- You can filter the issues by `Author`, `Labels`, `Assignee`, or sort by date
- To open a new issue, click on `New Issue`, in green at the top right of the list of open issues
- When opening an issue, you should add: a title and a brief (one or two sentence) summary 
- **Don't forget to label it with the corresponding label from the `Labels` dropdown list on the right** (for more information about labels, read this: https://github.com/cc-ai/kdb/tree/master/workflow) 
- If you already know who will be working on the issue, add an `Assignee` from the list on the right. If not, you can leave it blank.

<p align="center"><img alt="adding a pdf" src="https://media.giphy.com/media/IevI50cAejhnehJ7oH/giphy.gif"/></p>

#### Assigning an issue to yourself ###

- When you have found an issue that you want to tackle, possibly opened by someone else, click on its name
- To assign it to yourself, click `Assignees` on the right of the screen and select your GitHub handle from the list
- If you want to add details or comments, use the Write section at the bottom of the page

#### Closing an issue

- When the issue is solved, use the `close and comment` button
- You can always re-open an issue later if the fix is not complete or the same problem arises in a new context or whatever
- For instance, the example issue above, [#43](https://github.com/cc-ai/kdb/issues/43), is now closed because gifs have been added


**Bravo! You're all set!** 💪 Now checkout [the workflow's guide on using cc-ai's labels on issues](https://github.com/cc-ai/kdb/tree/master/workflow#issues-and-labels-)

## Getting Started ⚡️ 

If you want to just dive in and get your hands dirty - go for it! Look at the tickets in the [Kanban](https://github.com/orgs/cc-ai/projects/2), choose the one that fits what you will start working on (check with Sasha or Karthik if you don't know what to pick), and get started!

If you want more information about GitHub (or Git), or to learn how to use it via command line, you can check out the resources below:

[GitHub for beginners Part 1](https://readwrite.com/2013/09/30/understanding-github-a-journey-for-beginners-part-1/) 

[GitHub for beginners Part 2](https://readwrite.com/2013/10/02/github-for-beginners-part-2/) 

[How to Use GitHub](https://www.edureka.co/blog/how-to-use-github/)

If you have any questions about GitHub, don't hesitate to reach out to Sasha Luccioni ([@sashavor](https://github.com/sashavor)) or Victor Schmidt ([@vict0rsch](https://github.com/vict0rsch)) or simply [open an issue](https://github.com/cc-ai/kdb/issues/new), we'll help you ! 👩‍✈️ 👨‍✈️
