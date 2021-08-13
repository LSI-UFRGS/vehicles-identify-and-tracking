open in Google colab notebook: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github.com/LSI-UFRGS/vehicles-identify-and-tracking/blob/main/ROI_selector/ROI.ipynb)
# ROI Selector and map of positions

This notebook implements a ROI selector, where we can define n rectangles over the scene. The main ideia is to select the regions where the vehicles enters and leaves the scene. Each point that enters in the ROI is saved as a new object that should leave the scenes. Lets take a look at the following flowchart:


![DataFlow](https://github.com/LSI-UFRGS/vehicles-identify-and-tracking/blob/main/ROI_selector/fluxo_trabalho.png)

First of all, the YOLO is trained to classify the vehicles with the specific Dataset (take a look on the YOLO training folder). Also, the Deep SORT needs to be trained in order to re-identify "objects" (vehicles in our case). Remember, the default DeepSORT is trained to identify people. 

After training the YOLO+DeepSORT is run with the target video, saving the csv file with track id, bounding boxes coordinates, class and frame time. This file is used to plot the map of point of the whole video with different collors identifying diferent objects. Also, the first image of the scene is saved with vectors indicating the tracking of each object (composed_image). This image is important because each lost tracking, during the presence of a occlusin for instance, will produce another vector (another ID). The ideal case is a single vector from one of the inputs to one of the outputs.

Finally, the user enters the ROIs by drawing rectangles, defining inputs and outputs or entries and exits of the vehicles in the scene. Thus, the code checks how many vehicles entered and leave the scene accountying by classes and also computying the tracking losses and so the errors in the accounting. 


