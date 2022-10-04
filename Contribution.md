## 📝 Contribution Guidelines

- Fork this repo (button on top) _(Mandatory)_
- Clone this on your local machine _(Mandatory)_

```
git clone https://github.com/{username}/SmallWorkingProjects_Hacktoberfest22

```

- Navigate to project directory.

```
cd SmallWorkingProjects_Hacktoberfest22

```

- Create a new Branch

```
git checkout -b my-new-branch
```

- Add your contribution

```
git add .
```

- Commit your changes.

```markdown
git commit -m "Relevant message"
```

- Then push

```
git push origin my-new-branch
```

- Create a new pull request from your forked repository

<br>

## Avoid Conflicts {Syncing your fork}

An easy way to avoid conflicts is to add an 'upstream' for your git repo, as other PR's may be merged while you're working on your branch/fork.

```terminal
git remote add upstream https://github.com/{Username}/SmallWorkingProjects_Hacktoberfest22


```

You can verify that the new remote has been added by typing

```terminal
git remote -v
```

To pull any new changes from your parent repo simply run

```terminal
git merge upstream/master
```
