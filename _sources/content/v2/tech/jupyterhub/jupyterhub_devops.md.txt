# The DataHub Deployment Process

This page details the practices used by the Data 8 tech team in order to maintain and upgrade their JupyterHub, called the DataHub. The DataHub is a JupyterHub deployment using Kubernetes that provides the environment in which all
Data 8 students work. 

## The DataHub deployment repository

The current deployment configuration for the DataHub is hosted as a
[GitHub repository](https://github.com/berkeley-dsep-infra/datahub). Any
changes made to this repository should immediately be reflected in the
live DataHub.

There are **two branches** for the DataHub repository - one for `staging`, and
another for `prod` (short for "production"). Each branch controls a
different JupyterHub deployment.

* `staging` lives at [staging.datahub.berkeley.edu](staging.datahub.berkeley.edu).
  It is used by the Data 8 development team to test modifications before they're
  deployed to the production environment. Students do not use this JupyterHub.
* `prod` lives at [datahub.berkeley.edu](datahub.berkeley.edu). It is the
  JupyterHub that students use, and as such has higher standards for stability.

The DataHub uses [Travis CI](https://travis-ci.org/) (short for
"continuous integration") to automatically run tests and code every
time a change is made to the DataHub master repository. This is
also used to automatically deploy these changes to the `staging`
and `prod` DataHub deployments when new changes are made.

## Modifying the DataHub 

The following steps are followed by the Data 8 tech team any time
a modification must be made to the DataHub.

1. Create a fork of the [DataHub repository](https://github.com/berkeley-dsep-infra/datahub) and work from this fork.
2. Pull the latest changes from the DataHub repository into your fork.
3. Create a new branch for your changes.
4. Make the modifications necessary to this branch (this is
  usually something like modifying the [DataHub helm chart](https://github.com/berkeley-dsep-infra/datahub/blob/staging/datahub/config.yaml) or editing the [DataHub Docker Image](https://hub.docker.com/u/berkeleydsep/)).
5. Commit your changes and create a pull request. The pull request
  should be against **`staging`**, not against `prod`.
6. The pull request will trigger a Travis CI process, and
  potentially a rebuild of docker images depending on what
  modifications have been proposed.
7. Once the CI process is complete and if there are no problems, the committer requests that someone review the PR before merging.
8. If all looks well, merge the PR into `staging`. This will trigger
  another Travis step which automatically upgrades the
  DataHub deployment at `staging.datahub.berkeley.edu`.
9. After this upgrade finishes (per the logs in Travis CI), the team
  tests the changes by performing actions on
  `staging.datahub.berkeley.edu` (e.g., trying to import
    a package that was added)
10. If `staging` tests fail, or if there are any problems during the
  live user testing, **never update `prod`**. Revert the change via
  the GitHub UI and debug before submitting another PR to `staging`.
11. If the change passes tests and looks successful on `staging`, create
  a **new PR** to merge `staging` into `prod`. This will trigger
  a similar Travis process to deploy to `prod` at
  [datahub.berkeley.edu](datahub.berkeley.edu).
  Test your change on production for good measure.
12. Celebrate!
