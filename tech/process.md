# The DataHub Deployment Process

The DataHub is a JupyterHub that provides the environment in which all
Data 8 students will work. JupyterHub has made great improvements to
scalability and reliability in recent years, and has adopted modern-day
cloud deployment technology such as Kubernetes.

This page details the process that the Data 8 tech team uses in order to
maintain and upgrade the DataHub.

## The DataHub deployment repository

The current deployment configuration for the DataHub is hosted as a
[GitHub repository](https://github.com/berkeley-dsep-infra/datahub). Any
changes made to this repository should immediately be reflected in the
live DataHub.

There are **two branches** for the DataHub repository - one for `staging`, and
another for `prod` (short for "production"). Each branch controls a
different JupyterHub deployment.

* `staging` lives at [staging.datahub.berkeley.edu](staging.datahub.berkeley.edu).
  It has less resources than `prod`, and is used to test new modifications
  before they're deployed to the live student environment. Students
  do not use this JupyterHub, only the Data 8 development team.
* `prod` lives at [datahub.berkeley.edu](datahub.berkeley.edu). It is
  the JupyterHub that students use, and as such has more resources as
  well as higher standards for stability.

The DataHub uses [Travis CI](https://travis-ci.org/) (short for
"continuous integration") to automatically run tests and code every
time a change is made to the DataHub master repository. This is
also used to automatically deploy these changes to the `staging`
and `prod` DataHub deployments when new changes are made.

## Modifying the DataHub deployment

The following steps are followed by the Data 8 tech team any time
a modification must be made to the DataHub.

* Create a fork of the [DataHub repository](https://github.com/berkeley-dsep-infra/datahub), always work from this fork.
* Pull the latest changes from the DataHub repository into your fork.
* Create a new branch for your changes.
* Make the modifications necessary to this branch (this is
  usually something like modifying the [DataHub helm chart](https://github.com/berkeley-dsep-infra/datahub/blob/staging/datahub/config.yaml) or editing the [DataHub Docker Image](https://hub.docker.com/u/berkeleydsep/)).
* Commit your changes and create a pull request. The pull request
  should be against **`staging`**, not against `prod`.
* The pull request will trigger a Travis CI process, and
  potentially a rebuild of docker images depending on what
  modifications have been proposed.
* Once the CI process is complete and if there are no problems, the committer requests that someone review the PR before merging.
* If all looks well, merge the PR into `staging`. This will trigger
  another Travis step which automatically upgrades the
  DataHub deployment at `staging.datahub.berkeley.edu`.
* After this upgrade finishes (per the logs in Travis CI), the team
  tests the changes by performing actions on
  `staging.datahub.berkeley.edu` (e.g., trying to import
    a package that was added)
* If `staging` tests fail, or if there are any problems during the
  live user testing, **never update `prod`**. Revert the change via
  the GitHub UI and debug before submitting another PR to `staging`.
* If the change passes tests and looks successful on `staging`, create
  a **new PR** to merge `staging` into `prod`. This will trigger
  a similar Travis process to deploy to `prod` at
  [datahub.berkeley.edu](datahub.berkeley.edu).
  Test your change on production for good measure.
* Celebrate!
