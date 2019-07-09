# Data 💾

## Mila Cluster

Data is located in `/network/tmp1/ccai`

* `data/` folder contains the raw datasets
* `preprocessed/` contains data prepared/preprocessed for inference (format, crops, etc.)
* `results/` contains the results of training procedures: intermediate/final inferences, checkpoints etc.


### Datasets

|Folder name|description|
|:---------:|:----------|
|27.02.FloodingData|First version of the dataset with open-access images of houses and flooded areas. Includes images of Venice and some donated by a photographer|
|280_flooded_houses| 280 images of flooded houses segmented by the ccai team with LabelBox. Masks are binary|
|deeplab_segmented_houses|Images of houses from the 1k dataset segmented by deeplab: ground labels are merged together to create a binary mask. Labels merged as ground: Road, sidewalk, terrain. More info in [floods-gans/ground_segmentation](https://github.com/cc-ai/floods-gans/tree/master/ground_segmentation)|
|mapillary|dataset w/ labels, instances and panoptic segmentation https://research.mapillary.com/|
|SimFlood 50-50f-50p-50m|50 Synthetic images of flooded/non-flooded pairs + pink images (where the water is) + masks (where the pink was -> see pink_to_mask.py in various scripts)|
|val_set|CCAI's validation set: Currently, the validation set consists of 50 streetview images (random selection of coordinates) but it's made sure that images are from urban/suburban areas and contain atleast one house/building (mostly from urban)|
|video_water_database|Images with masks from Water Detection through Spatio-Temporal Invariant Descriptors, http://isis-data.science.uva.nl/mettes/VideoWaterDatabase.tar.gz|
