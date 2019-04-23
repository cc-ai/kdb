# Machine Learning 🤖

## Test different models

Having acquired the data (whether real or simulated), it is necessary to test different generative model approaches to establish which works best (e.g. [StarGAN](http://openaccess.thecvf.com/content_cvpr_2018/papers/Choi_StarGAN_Unified_Generative_CVPR_2018_paper.pdf), [vid2vid](https://arxiv.org/pdf/1903.04480.pdf), [cycleGAN with attention](https://arxiv.org/pdf/1806.02311.pdf), etc.).

## Modifying segmentation automatically

CycleGANs are good at changing texture but it is more difficult to make them change the image in more drastic ways. Controlling the changes at the level of textured segments might be easier. Recent results ([SPADE](https://nvlabs.github.io/SPADE/)) show that it is possible to transform a segmentation map into a realistic image quite convincingly. Since it is possible that a single end-to-end approach relying solely on images is not sufficient, we should also explore approaches that **use segmentation maps and images** in order to carry out more drastic changes to the input image (e.g. replace some ground segments by water segments). The pipeline would thus be: house image → segmentation map → modified (flooded) segmentation map → flooded house image. See 'Depth maps' below for a way to modify the segmentation map to paint water in it.

## Depth maps

Along with the street-level images that we query from the Google or Bing API, we can obtain **depth maps of the buildings in the image** that will allow us to calculate which pixels of the image to flood or not. A simple geometrical calculation (assuming a relative camera position, which StreetView can give us) allows to compute which pixels would be hidden by the water plane (given an 'altitude' where the flood reaches). This will probably be necessary to make the output images more realistic (but we would need to pair this with the image segmentation, for example). The corresponding pixels in the segmentation map would have their label changed to 'water'. This is important to make sure we paint only the right pixels as 'water'.

## Sim2Real

We can use Sim2Real techniques in order to transform the simulated images to be more realistic. This would be necessary if our GANs were trained mostly on simulated data.

## Neural Style Transfer

These are alternatives to CycleGAN types of models, where an optimization is performed at run-time in order to transform an image according to some style image. Does not need paired data. This might be used to paint water texture in the right places.

## Fine tuning DeepLab (or other segmentation models)

There are several segmentation models trained on the [Cityscapes dataset](https://www.cityscapes-dataset.com/), which includes many street-level scenes similar to the ones that we will use. We can therefore use these models out-of-the-box to segment our ‘before’ images. However, they are not robust enough to recognize flooded or damaged houses and streets, which means that some training or fine-tuning is needed to use an existing segmentation model on our ‘after’ images, in order to be able to pursue a segmentation-modification approach.
