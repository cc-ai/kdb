# Workflow

## Github

(New with Github ? -> [How to get started w/ Github, cc-ai style](/workflow/gettingstarted.md))

Code repositories depend on the `cc-ai` *organization*.

The [CCAI - Workflow](https://github.com/orgs/cc-ai/projects/1) *project* (**CWP** hereafter) tracks to-dos, issues suggestions and so on from these repositoires:

* [kdb](https://github.com/cc-ai/kdb) -> this is the main shared repo, the CC-AI Knowledge Base
* [floods-frontend](https://github.com/cc-ai/floods-frontend)
* [floods-backend](https://github.com/cc-ai/floods-backend)
* [floods](https://github.com/cc-ai/floods)

Use CWP as much as you can to better communicate and sync with the rest of the team.

For now it is a centralized project ; if one or more other repositories grows we'll simply create another one there. CWP is for the whole CC-AI team, not dealing with particular issues for a project. We'll learn as we go, if you want to modify this workflow, do open an issue in [kdb](https://github.com/cc-ai/kdb)

### Automation

#### Labels

This procedure describes how to import `kdb`'s labels into your repositories. 

**This will overwrite your labels** so if you want your own labels you can do this once and then delete `settings.yml` otherwise it will delete your repo-specific labels when pushed later on.

Add a `.github` folder and a `.github/settings.yml` at the repo's root. 

**If** [labels.yml](labels.yml) is up to date, copy its content into your `.github/settings.yml`. 

**Otherwise** run this script in your browser console on page https://github.com/cc-ai/kdb/labels and add the created file to `.github/`. 

```javascript
// 1
var labels = [];
[].slice.call(document.querySelectorAll(".label-link"))
.forEach(function(element) {
  labels.push({
    name: element.textContent.trim(),
    // using style.backgroundColor might returns "rgb(...)"
    color: element.getAttribute("style")
      .replace("background-color:", "")
      .replace(/color:.*/,"")
      .trim()
      // github wants hex code only without # or ;
      .replace(/^#/, "")
      .replace(/;$/, "")
      .trim(),
    description: element.parentElement.nextElementSibling.textContent.trim()
  })
})

// 2
let out = "labels:\n";
for (const l of labels){
    out += `  - name: ${l.name}\n    color: ${l.color}\n    description: ${l.description || '""'}\n`;
}

// 3
function saveYML(text, filename) {
  const blob = new Blob([text], { type: 'text/plain' });
  const e = document.createEvent('MouseEvents');
  const a = document.createElement('a');

  a.download = filename;
  a.href = window.URL.createObjectURL(blob);
  a.dataset.downloadurl = ['text/json', a.download, a.href].join(':');
  e.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
  a.dispatchEvent(e);
}
saveYML(out, "settings.yml")
```

It works like this:

1. Get `labels` as a list of objects with fields `name` `color` and `description`
2. Create a `yml`-compatible string `out`
3. Download `out` as a `settings.yml` file

## Slack

To Do