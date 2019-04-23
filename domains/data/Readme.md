# Data 

## Acquisition

In order to train the GANs we need to create a diverse dataset of places (houses, buildings, countryside and city etc.) which is also **open** (free of copyrights), showing places before and after an extreme climate event. 

Ideally we’d have paired images, the same location before and after the event, but recent advances in unpaired image to image translation (CycleGANs and variations for instance) give us hope that an unpaired dataset would suffice or that a large set of unpaired images could be successfully combined with a small set of paired ones.

As an **MVP** we have started with **floods**. We have gone through most major copyright-free images websites and gathered ~500 images of variable quality and relevance, of which we consider ~160 to be of good quality for the training of GANs ([link to data](https://github.com/cc-ai/floods/blob/master/data.md)).

Now we need to improve and augment this dataset. We need to either find new open data sources, or acquire (buy) images. Photographers/Media, Governments/Emergency Agencies and Insurance companies may be leveraged.

## Labeling/Segmentation

Recent advances (SPADE, Unsupervised Attention-guided Image-to-Image Translation etc. ) demonstrate how GANs can leverage segmentation information in order to generate locally-relevant features. In order to be able to explore such approaches, we need to segment (label pixel-wise) our images. 

This can be done either manually (if the guidelines are well defined) or automatically, using existing models (e.g. DeepLab).The issue with existing models is that they are not trained on damaged houses with flooded streets and floating cars, so some fine-tuning or even retraining is needed. This brings us back to manually labeling data.


## Simulation

As explained above, the image data that the project needs is scarce. On the other part, relaxing one of our constraints (images being real) could help us gather more data. Simulated data could help in a variety of approaches:

- Adding paired data to an unpaired dataset could “guide” the GAN into the right training region and allow it to become more robust
- Splitting the transformation process between a simulation-trained “flood-segmenter” and a SPADE-like “painter” could give us more freedom and modularity.
- Could be used not just to produce training data it could be used to generate videos of your flooded house

Needed:

- Appropriate software
- 3D or 2.5D models of a diversity of houses and neighborhood
- Computer graphics expertise

Notes:
 
 - Water is generally muddy in floods, probably easier to simulate ( no complicated reflections)
- Simulated images could be post-processed by GANs (see Sim2Real below)
