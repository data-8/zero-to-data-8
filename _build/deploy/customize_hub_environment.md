---
redirect_from:
  - "deploy/customize-hub-environment"
title: 'Customize the JupyterHub environment for Data 8'
prev_page:
  url: /deploy/setup_jupyterhub
  title: 'Deploy your JupyterHub'
next_page:
  url: /deploy/connect_website_and_textbook
  title: 'Set up your course website and textbook'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Customizing the JupyterHub environment for Data 8

The Data 8 course uses a collection of Python modules and open-source
technology for course infrastructure as well as teaching. We've
provided all of these materials as a Docker image that you can connect
to your JupyterHub so that all users will have the environment needed
for the class. This page describes how to set up your JupyterHub
environment so that it serves the environment used in Data 8.

## Deploying a change to your JupyterHub configuration

First things first, to make changes to your JupyterHub configuration, you
need to know how to **deploy** those changes. This section covers how to deploy
a change to your configuration file ``config.yml`` in Kubernetes.

All modifications to the base JupyterHub deployment are made with
changes to your `config.yaml` file. When we first [created our JupyterHub](setup_jupyterhub.md),
we created this file with a single value inside that contained our secret token.

**Once you've made a change to `config.yaml`** you can deploy it with the following
steps:

1. **Double-check the syntax of your `config.yaml` file.** For example, you may have
   copy/pasted two code snippets that both had

   ```
   singleuser:
   ```

   as the top header, and should be merged under a single header.
   YAML is picky about how whitespaces/indentation are used,
   and can throw cryptic errors if you have small errors like type-os.

2. **Deploy your change to the JupyterHub.** Use the following command:

    ```
    helm upgrade << YOUR-HUB-NAMESPACE >> jupyterhub/jupyterhub --version=v0.6 -f config.yaml
    ```

    This runs a "Helm Upgrade", which tells Kubernetes to update its deployment to match
    the values that you've placed in `config.yaml`. The value in `<< YOUR-HUB-NAMESPACE >>` should
    be whatever you chose when [creating the JupyterHub](setup_jupyterhub.md).

    Most hardware modifications to your
    Kubernetes deployment will be done in this way.

### Common errors

**"time out waiting for the condition"**. It took too long to
pull the Docker image onto the JupyterHub. You can generally resolve this by including
a `--timeout=9999999` flag to your `helm upgrade` command. This will prevent Helm
from stopping too early.

## Customizing your Hub environment

The environment provided to your students is defined by a Docker image
that JupyterHub serves to new user sessions. Which image to use is configured
in your `config.yml` file.

### Using the Data 8 Docker image

First, we'll tell the JupyterHub to connect user sessions with the
Docker image used by Data 8. This is done by adding the following to your
`config.yaml` file:

```
singleuser:
  image:
    name: berkeleydsep/datahub-user
    tag: 21be6ff
```

To deploy the change, save the file, then run a helm upgrade:

```
helm upgrade data8 jupyterhub/jupyterhub --version=v0.6 -f config.yaml
```

Note that this will take a while if you're using the data8 image, perhaps
upwards of 10 minutes, as it pulls the image into your Kubernetes deployment.

### Extending each user's environment

If you need to extend the base Docker image, you can do so interactively from
a JupyterHub session. For example students can `pip` or `conda` install packages
into their own user directories, and these will persist over time.

## Modify the resources available to your users

In this section we'll define what kind of resources your students have. For example,
how much RAM / CPU / etc. See the [Data 8 user resource configuration](https://github.com/berkeley-dsep-infra/datahub/blob/staging/datahub/config.yaml#L140)
for example.

### Memory (RAM)
The following snippet will give each user 1 gig of ram,
which is the amount given to Data 8 students at Berkeley. Students will
always have at least the amount specified in `guarantee` and their Jupyter
server will restart if they use more than `limit`.

```
singleuser:
  memory:
    guarantee: 1G
    limit: 1G
```

### Disk Storage

The following snippet gives students 2 gigs of persistent storage:

```
singleuser:
  storage:
    capacity: 2Gi
```

## Authorization for your hub

Authorization allows you to control who has access to your JupyterHub, as well
as keep track of who is accessing the hub.

There are many options for
authorization with JupyterHub. The Data 8 deployment uses the Berkeley
CalNet authentication system, which is part of the Google "G Suite".
Your authentication approach depends on how your university authenticates.
You can also choose
authentication with popular services like GitHub.

See the [Zero to JupyterHub Authentication guide](https://zero-to-jupyterhub.readthedocs.io/en/latest/authentication.html) for information about various
authentication options and how to enable them.

For this guide, we'll show you how to authenticate using GitHub usernames,
as this is a free service that is more widely-accessible than the particular
authentication system that any one university uses.

### Authenticating with GitHub
To authenticate with GitHub, take the following the steps outlined
in the [Zero to JupyterHub Authentication Guide](https://zero-to-jupyterhub.readthedocs.io/en/latest/authentication.html#github).

Note: The DSEP authorization configuration [can be found here](https://github.com/berkeley-dsep-infra/datahub/blob/staging/datahub/config.yaml#L65).

### Adding admin users

JupyterHub has an **administrator** page that can be used to see all of the
active sessions currently on the hub, as well as perform some simple actions
to help debug and fix student problems. To add a list of admin usernames,
add the following to the `auth` section of your `config.yaml` file:

```
auth:
  admin:
    users:
      - <LIST>
      - <OF>
      - <ADMIN>
      - <USERNAMES>
```

## An example `config.yaml` file

If you've followed all of the instructions on this page
(including authenticating with GitHub), your `config.yaml` file should now
look something like this:

```
proxy:
  secretToken: "<< output of openssl rand -hex 32 >>"

singleuser:  # This defines the user environment
  image:
    name: berkeleydsep/datahub-user
    tag: da80cb1
  memory:
    guarantee: 2G
    limit: 2G
  storage:
    capacity: 2Gi

auth:
  type: github
  github:
    clientId: "<< YOUR-CLIENT-ID >>"
    clientSecret: "<< YOUR-CLIENT-SECRET >>"
    callbackUrl: "http://<< YOUR-HUB-IP-ADDRESS >>/hub/oauth_callback"
  admin:
    users:
        - <LIST>
        - <OF>
        - <ADMIN>
        - <USERNAMES>
```

## Confirm that your environment works

To confirm that you're running the correct environment needed for Data 8,
take the following steps:

1. Go to your JupyterHub's public IP address. You can find this address with:

   ```
   kubectl --namespace=data8 get svc proxy-public
   ```

2. Log in with your username/password (if you haven't logged in yet, use whatever
   username/password you'd like)
3. Click "Start My Server", then create a new Jupyter Notebook.
4. Run the following Python code

   ```python
   import datascience
   print(datascience.__version__)
   ```

You should see the version for the `datascience` package printed below the cell.
If this worked, then congratulations! Your JupyterHub is ready to go.

## Next: connect with course materials

Now that you've got your own working version of the textbook, it's time to
[connect your course with the homeworks, labs, and other course material in Data 8](connect_labs_and_homework.md).
