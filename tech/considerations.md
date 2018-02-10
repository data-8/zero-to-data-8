# Technical Considerations

Data 8 teaches a mixture of analytics and programming to nearly 1400 undergraduates, and makes no
strong assumptions about their background in either of these fields. Managing a class this size
doing non-trivial computational work is a big technical challenge. This page details many of
the guiding principles and priorities that the Data 8 team considered in solving these problems with
technology.

## Major hurdles
* **Standardizing environments is hard**. Anyone who has taught a bootcamp knows the pain involved in getting a room of 20 students with the same functioning environment. Data 8 has nearly two orders of magnitude more students. For an introduction class, requiring students to set up their own environment is a huge distraction and dis-equalizer.
* **Avoiding cloud lock-in**. There are many options for interacting with the cloud, but most are bespoke interfaces that pair with a *product* you eventually pay for (e.g. https://aws.amazon.com/education/). We didn't want Data 8 to depend on a specific provider.
* **Be platform-agnostic**. Most data analytics classes have similar problems (e.g., managing a kernel in the cloud) even if the tools they use are quite different (e.g., R vs. Python). Data 8 intentionally used tools that were platform-agnostic (e.g., tools in the Jupyter project) to make course infrastructure useful for many different topics.
* **Use open-source tools.** While there are many proprietary options for managing classrooms and technical resources, they are not as generalizable and serve as hurdles to wider adoption of material.
* **Development/Operations skills are not common**. Scaling class to large size requires technical + personnel that aren't always common in academia

## Priorities / Solutions

* **Use the cloud** - By utilizing cloud resources, the course material is available to all students regardless of the hardware available to them.
* **Be cloud agnostic** - We want to give students and instructors the ability to work on whatever platform they like. As such, we chose tools that were open-source and cloud-agnostic.
* **Shield students from complex APIs** - The world of data analytics has a diverse ecosystem of packages, each with their own API and quirks. We attempted to shield students from this diversity to focus on the fundamentals, and assume students will dig into specific APIs in subsequent courses.
* **Use diverse real-world / compelling data** -
* **Keep costs down** - Broader adoption of the course at Berkeley and beyond will only happen if costs are reasonably low. We shoot for a few dollars per student, per month.
* **Handle dynamic activity** - Students tend to operate in bursts of activity (e.g., during class or 30 minutes before the homework is due). We needed dynamic cloud infrastructure that could handle many patterns of activity.
* **Meet peak demand** - Moments of maximal cloud usage (e.g., during a test) are moments when the cloud *must be functional*.
* **Do all of the above with a small team** - The Data 8 model is not scalable if it requires a dedicated team of tech-savvy staff. While some technical skills are required, we wanted most course operations to be handled by a small team of undergraduates (usually Data 8 alumni).

## Desired Student Workflow

From a student's perspective, this is the workflow that we wanted them to have access to:

The instructor creates a piece of course material they want students to be able to use.
They push the latest version of this material to GitHub, then send students a link that
they can click in order to interact with the material.

The student clicks on the link, which triggers the following actions:

* The DataHub authenticates the user (either asking them to sign in, or discovering that their local computer already has credentials to proceed).
* The DataHub creates and starts a Jupyter instance for the user (or directs the user to a pre-existing environment from a previous session)
* The student's persistent storage volume is linked to their Jupyter instance
* The DataHub clones or pulls the content specified by the link into student’s instance
* The student is then directed to a live notebook instance in the browser. It contains the content specified in the link and can be immediately interacted with.
