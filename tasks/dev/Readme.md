# Front-end
The front-end will be critical. It needs to be flawless if we want things to get viral and emotionally compelling. Work with UX/UI is expected. We therefore need a front-end developer who will design a first version of the website, which will only show the images, and then integrate the behavioral knobs, links to actions, etc.

# Back-end

We need to design a back-end that will query the climate and GAN models and transmit the generated image to the front-end. This process needs to be seamless, which is relatively straightforward for the static MVP version of the tool, but will become more complex when we make the model interactive (by adding action knobs). If there are many knobs it becomes difficult to pre-compute climate trajectories for all of them (it would be too expensive), so some approximations are needed (e.g., merging all the configurations into a single dimension relating to the average amount of temperature forcing over the chosen period, or heavily discretizing the knob choices). In addition, will the on-the-fly generation of images be done on our servers or on the viewer’s computer? There are conceptual decisions that must be made up front so that we don’t end up reprogramming the backend later.

Francois, one of our team members, can do most of the work for the MVP during the summer. However he has no production experience and guidance in this matter would be helpful. We have started using Flask -> https://github.com/cc-ai/floods-backend
