#### High Level Steps
- Sign up and sign in to gitlab.com UI trial
- Create New project
- Create New file named .gitlab-ci.yml with desired content
- Commit changes
- Pipeline will start running automatically
- Click on it to see details
- For every change pipeline runs on its own
- We can see older pipelines in ci/cd --> pipelines
- We can see artifacts associated with each pipeline also
- We can cancel pipeline if not needed, in between
- We can retry jobs or pipelines also
- We can run pipelines again
- We can schedule pipeline runs from ci/cd -> schedules also
- We can set variables from settings --> ci/cd -> variables
- Pipeline has timeout defaulted to 1 hr.
- We can deploy projects to aws using banst/awscli image.
- Job can be skipped using .jobname.
---
- Merge Requests and branches are a way of keeping things separate from master temporarily.  
- We can create new branch from repository -> branches.
- We can create new merge request from merge requests tab.
- In settings --> ci/cd --> protected branches, we can change permissions for branches.
- In settings --> ci/cd --> merge requests, we can change merge checks.
- Pipeline runs whenever a branch is created or its contents are changed.

#### Architecture
- gitlab server
    - We can also host gitlab on our own server.
- database
- gitlab runner(s)
    - Uses default ruby docker image, clones our repo, starts execution, upload artifacts to gitlab server, stops task, destroys image.
    - We can add our own runner also, from settings --> ci/cd --> runners.

#### Pricing
- Paid

#### CI/CD
- Continuous Integration - of your code with other developers to make sure product still gets built and passes tests
- Continuous Delivery - to staging and eventually to production host

#### Docker
- Docker - It is a technology based on containers which allow virtualization.
- Image - file with set of instructions on how to package up code and utilities and all dependencies.
- Container - when docker executes image, it becomes container that is similar to VM.  
- It is used in CI to avoid conflict of different versions of dependency packages on CI server for diff tools.
