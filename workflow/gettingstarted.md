# Github at `cc-ai` : getting started 🥋

Hello and welcome to the CCAI GitHub!

In this repository, we will of course share code, but also links, articles, websites, and ideas. We will also use it for defining who does what task (i.e. ticket) and follow the progress of tickets and tasks as they evolve.

Don't worry if you've never used GitHub before! You can actually use GitHub without knowing ANY code at all. It's really a straightforward tool, and this document will help you cover the basics.

<h3> Git 🌵</h3>

Git is a software to do version control, which means it will save any changes being done without overwriting any past work. This means that even if several people are working on the same file at the same time, each person can upload their changes to the page, and Git will save both copies. Later, they can be <b> merged </b> together without anyone losing their work. You can even go back to a previous version at any point, because Git will keep a history of every change ever made. Typically, git is used via a [terminal or command line](http://guides.beanstalkapp.com/version-control/common-git-commands.html) and stores the versions on your computer. But GitHub allows us to store the content and versions online ; plus, it adds a user interface on top of Git, which makes it possible to download and change files from your browser or your desktop, make comments, suggest fixes, etc.


<h3> Vocabulary 🙊</h3>

Some useful GitHub vocabulary (from [this guide](https://readwrite.com/2013/09/30/understanding-github-a-journey-for-beginners-part-1/))

<b> Repository or Repo </b>: A directory or storage space where your projects can live. It can be local to a folder on your computer, or it can be a storage space on GitHub or another online host. You can keep code files, text files, image files, you name it, inside a repository.

<b> Commit</b>: This is the command that gives Git its power. When you commit, you are taking a “snapshot” of your repository at that point in time, giving you a checkpoint to which you can reevaluate or restore your project to any previous state.

<b> Branch </b>: How do multiple people work on a project at the same time without Git getting them confused? Usually, they “branch off” of the main project with their own versions full of changes they themselves have made. After they’re done, it’s time to “merge” that branch back with the “master,” the main directory of the project.

<b> Issue </b>: Although the name may sound negative <i> ("Oh no, there's an issue with my project!") </i>, 'issue' is just the name used by GitHub for different tasks that contributors can assign to themselves. You can open an issue when you've defined it as something that needs to be worked on, tag it with labels depending on what it involves, and then assign it to yourself (or someone else!). A very important document that explains this workflow for the **cc-ai project** process can be found [**here**](https://github.com/cc-ai/kdb/tree/master/workflow).


<h3> What we will use GitHub for 🔦</h3>
<ul>
  <li> <b> Sharing code :</b> for the coders among us, GitHub will be a way to test out different parameters, make changes to the code, clone (a.k.a.) copy other repositories that we can test, share results, etc. This will be done via the various repositories in the project, which can be seen at https://github.com/cc-ai </li>

  <li> <b> Tracking progress:</b> Even if the task that you are working on doesn't involve coding (e.g. literature review, experimental testing, etc.), it's useful for the rest of the team to know that you are working on a certain task (or issue), and what the progress on it is: whether it is open, closed, in progress, pending, etc. We will do this via the Kanban: https://github.com/cc-ai/kdb/projects/4 </li>

 <li> <b> Sharing resources:</b> A section of the repository is dedicated specifically to sharing common resources : https://github.com/cc-ai/kdb/tree/master/resources. These can be research papres, code, news articles, tools, etc. If you encounter something useful in your literature review (or even during your spare time!), add it to the resource section! 
 
<ul>

<li>Let's see how you'd add a paper for instance:

<ol>
<li>From the home page (https://github.com/cc-ai/kdb) click on `resources` in the top folder structure, then on `papers` (or the link provided): you should be at https://github.com/cc-ai/kdb/tree/master/resources/papers</li>
<li>**By default, Github displays the file called `Readme.md`**</li>
<li>You can edit this file and add your preferred paper by clicking on the pencil icon to the top right of the displayed Readme</li>
<li>Add a line with your paper line this `* [paper title](https:// link to paper)`</li>

[![Gif illustration](https://media.giphy.com/media/co5O8kmFcr0kv6kj7M/giphy.gif)](https://media.giphy.com/media/co5O8kmFcr0kv6kj7M/giphy.gif)

</ol>

</li>

<li>Let's see how you'd add a paper for instance from a pdf

<ol>
<li>From the home page (https://github.com/cc-ai/kdb) click on `resources` in the top folder structure, then on `papers` (or the link provided): you should be at https://github.com/cc-ai/kdb/tree/master/resources/papers</li>
<li>**By default, Github displays the file called `Readme.md`**</li>
<li>You can edit this file and add your preferred paper by clicking on the pencil icon to the top right of the displayed Readme</li>
<li>Add a line with your paper line this `* [paper title](https:// link to paper)`</li>

[![Gif illustration](https://media.giphy.com/media/co5O8kmFcr0kv6kj7M/giphy.gif)](https://media.giphy.com/media/co5O8kmFcr0kv6kj7M/giphy.gif)

</ol>

</li>

<li>Opening an issue

<ol>
<li>From the home page (https://github.com/cc-ai/kdb) click on `resources` in the top folder structure, then on `papers` (or the link provided): you should be at https://github.com/cc-ai/kdb/tree/master/resources/papers</li>
<li>**By default, Github displays the file called `Readme.md`**</li>
<li>You can edit this file and add your preferred paper by clicking on the pencil icon to the top right of the displayed Readme</li>
<li>Add a line with your paper line this `* [paper title](https:// link to paper)`</li>

[![Gif illustration](https://media.giphy.com/media/co5O8kmFcr0kv6kj7M/giphy.gif)](https://media.giphy.com/media/co5O8kmFcr0kv6kj7M/giphy.gif)

</ol>

</li>



</ul>
 
 </li>

<li> <b> Sharing ideas:</b> If you see an open ticket that is labelled as "help wanted", or if you simply have an idea about a task that someone else is working on, don't hesitate to leave a comment on the issue: it can help open a discussion and generate new ideas! </li>

<li> <b> Collaborating with external contributors:</b> We are lucky enough to have a group of people interested in CCAI, who want to help us with different tasks depending on their domain of expertise: UI design, front-end development, economics.. the sky is the limit! To make this collaboration as smooth as possible, we want to give them specific tasks and ways to help us, check in with progress, ask questions, etc. GitHub is the place to do this!  </li>

<h3> Getting Started ⚡️</h3>

If you want to just dive in and get your hands dirty - go for it! Look at the tickets in the [Kanban](https://github.com/orgs/cc-ai/projects/2), choose the one that fits what you will start working on (check with Sasha or Karthik if you don't know what to pick), and get started!


If you want more information about GitHub (or Git), or to learn how to use it via command line, you can check out the resources below:

[GitHub for beginners Part 1](https://readwrite.com/2013/09/30/understanding-github-a-journey-for-beginners-part-1/) 

[GitHub for beginners Part 2](https://readwrite.com/2013/10/02/github-for-beginners-part-2/) 

[How to Use GitHub](https://www.edureka.co/blog/how-to-use-github/)

If you have any questions about GitHub, don't hesitate to reach out to Sasha Luccioni ([@sashavor](https://github.com/sashavor)) or Victor Schmidt ([@vict0rsch](https://github.com/vict0rsch)) or simply [open an issue](https://github.com/cc-ai/kdb/issues/new), we'll help you ! 👩‍✈️ 👨‍✈️
