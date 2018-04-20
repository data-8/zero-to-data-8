# Customizing the JupyterHub environment for Data 8

The Data 8 course uses a collection of Python modules and open-source
technology for both course infrastructure as well as teaching. We've
provided all of these materials as a Docker image that you can connect
to your JupyterHub so that all users will have the environment needed
for the class. This page describes how to set up your JupyterHub
environment so that it serves the same environment that the Data 8
students have.

All modifications to the base JupyterHub deployment are made with
changes to your `config.yaml` file. While we created this file with
a single value for the secret token, we'll now extend it by adding
several components that customize the JupyterHub for Data 8.

## Using the Data 8 Docker image

First, we'll tell the JupyterHub to connect user sessions with the
Docker image used by Data 8. This is done by adding the following to your
`config.yaml` file:

```
singleuser:
  image:
    name: data8/jupyterhub-k8s-user
    tag: cd0fd4601757
```

To deploy the change, save the file, then run a helm upgrade:

```
helm upgrade data8 jupyterhub/jupyterhub --version=v0.6 -f config.yaml
```

Note that this will take a while if you're using the data8 image, perhaps
upwards of 10 minutes, as it pulls the image into your Kubernetes deployment.


## Define the resources available to your users

In this section we'll define what kind of resources your students have. For example,
how much RAM / CPU / etc. See the [Data 8 user resource configuration](https://github.com/berkeley-dsep-infra/datahub/blob/staging/datahub/config.yaml#L140)
for example.

### Memory (RAM)
The following snippet will give each user 1 gig of ram, and 2 gigs of storage,
which is the amount given to Data 8 students at Berkeley.

```
singleuser:
  memory:
    guarantee: 1G
    limit: 1G
  storage:
    capacity: 2Gi
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
authentication with popular services like GitHub. See the [Zero to JupyterHub Authentication guide](https://zero-to-jupyterhub.readthedocs.io/en/latest/authentication.html) for information about various
authentication options and how to enable them.

For this guide, we'll show you how to authenticate using GitHub usernames,
as this is a free service that is more widely-accessible than the particular
authentication system that Berkeley uses.

**To authenticate with GitHub**, we recommend following the steps outlined
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

## The final `config.yaml` file

If you've followed all of the instructions on this page
(including authenticating with GitHub), your `config.yaml` file should now
look something like this:

```
proxy:
  secretToken: "{{ output of openssl rand -hex 32 }}"

singleuser:  # This defines the user environment
  image:
    name: berkeleydsep/datahub-user
    tag: da80cb1
  memory:
    guarantee: 2G
    limit: 2G
  storage:
    capacity: 2Gi

prePuller:
   hook:
     enabled: false
    
auth:
  type: github
  github:
    clientId: "{{ YOUR-CLIENT-ID }}"
    clientSecret: "{{ YOUR-CLIENT-SECRET }}"
    callbackUrl: "http://{{ YOUR-HUB-IP-ADDRESS }}/hub/oauth_callback"
  admin:
    users:
        - <LIST>
        - <OF>
        - <ADMIN>
        - <USERNAMES>
```

Once you've configured `config.yaml` properly, you can upgrade your
JupyterHub with a Helm upgrade:

`helm upgrade data8 jupyterhub/jupyterhub --version=v0.6 -f config.yaml`