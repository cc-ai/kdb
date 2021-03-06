# VICC in practice

Visualizing the consequences of Climate Change is the primary goal of this project. Here's what we're working towards. For more details, read the [Executive Summary](https://github.com/cc-ai/kdb/blob/master/exective_summary.md).

## Website

Goal: query an address, get image of potential event

![landing](https://user-images.githubusercontent.com/9283470/57719414-b6074580-764d-11e9-9394-886efeecfd19.png)

---

Depending on whether or not there's a likelihood of increased flood risk, run a GAN model to illustrate how it would affect the place and nearby points of interest + user knobs to interact with the system and better understand 

* the different global warming scenario
* the impact of various actions (individual or organizational)

![query](https://user-images.githubusercontent.com/9283470/57719421-ba336300-764d-11e9-874e-944b4cb266f5.png)

---

Google Maps overlay inspiration ([Fathom](https://www.fathom.global/news/a-q-a-with-oliver-wing-fathoms-global-reach))

![fathom](https://uploads-ssl.webflow.com/5b1a5c7d151be0c8ce7048b5/5b1a5c7d151be038447049a6_Screen%20Shot%202017-12-04%20at%2008.33.21.png)

## Climate Backend

Frequency of occurence for different return periods under the +1.5 scenario. Color map illustrate the new return period for a given location (for instance from ~ every 20 years to ~ every 15 years for green areas in the second plot)

![Flooding frequency 1.5 degree scenario](https://i.postimg.cc/qRwrtb0V/flooding-1deg5-scenario.jpg)


## Visualizations

### Unsupervised image to image translation

![cyclegan horse zebra](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/blob/master/imgs/horse2zebra.gif?raw=true)

![cyclagan yosemite](https://i.postimg.cc/T1wtfLFr/Capture-d-e-cran-2019-09-16-a-09-24-53.png)

### Results

[Munit (Huang et. al)](https://github.com/NVlabs/MUNIT) for VICC

![munit ccai](https://i.postimg.cc/sDKWCfRJ/Capture-d-e-cran-2019-09-16-a-09-27-38.png)

<p float="left">
  <img src="https://mila.quebec/wp-content/uploads/2019/09/2-1.jpg" width="410" />
  <img src="https://mila.quebec/wp-content/uploads/2019/09/2_after-1.jpg" width="410" />
</p>


<p float="left">
  <img src="https://mila.quebec/wp-content/uploads/2019/09/1-1.jpg" width="410" />
  <img src="https://mila.quebec/wp-content/uploads/2019/09/1_after-1.jpg" width="410" />
</p>

## Going Further

### More data: using simulations

![sim data](https://i.postimg.cc/ZR3YbHvS/Capture-d-e-cran-2019-09-16-a-09-45-55.png)

* Augment the real dataset with paired images
* Pretrain the models ( + domain randomization)
* Enable totally different approach:
  * height estimation
  * ground-plane estimation


### Inpainting

<img src="https://user-images.githubusercontent.com/22609465/35317673-845730e4-009d-11e8-920e-62ea0a25f776.png" width=400 alt="inpainting illustration"/> <img src="https://user-images.githubusercontent.com/22609465/35317674-846418ea-009d-11e8-90c7-652e32cef798.png" width=400 alt="inpainting illustration"/>
