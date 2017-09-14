# Genetic Edge Detector
The Genetic Edge Detector is an application which implements two genetic algorithms for the Edge Detection. These implementations 
have been created on the basis of the articles: 
  - *An edge detection technique using genetic algorithm-based optimization*, written by Suchendra M. Bhandarkar, Yiqing
  Zhang and Walter D. Potter (available at the [researchgate](https://www.researchgate.net/publication/222477449_An_edge_detection_technique_using_genetic_algorithm-based_optimization)
  portal);
  - *Optimal edge detection filter using genetic algorithm*, written by R. M. Naife and H. H. Abass (available on the 
  [Web](http://www.iasj.net/iasj?func=fulltext&aId=100469)).

## Requirements
You need to have a `python 3.4+` distribution installed (tested on the `3.5.2` version). If you want to install dependencies defined in the `requirements.txt` file, you also need to have a proper version of `pip` installed (tested on `8.1.2` and `9.0.1` versions for 
the `python 3.5`).

## Installation and Commissioning
Configuration files for both algorithms are included in the `resources/config` directory. First of all, please specify
required values (i.a. paths of input and output files and algorithms' parameters) in the appropriate configuration file.
Then, open the command prompt in the main directory of the application and type:
```
pip3 install -r requirements.txt
python3 run.py 
```
Please note that the algorithm to be used may be changed simply by editing the `run.py` script.

## Running the Canny edge detector
There is an implementation of the Canny edge detector provided by the [scikit-image](http://scikit-image.org/docs/dev/api/skimage.html)
library. The configuration file for the script performing Canny edge detection is placed in the `resources/config`
directory. In order to run the script, open the command prompt in the main directory of the application and type:
```
python3 canny/canny_detection.py
```
Note that it is necessary to have the dependencies installed already.

## Running the performance evaluators
This repository is equipped also with the scripts responsible for evaluation of the algorithms' performance (based both
on produced images and log files). The configuration file for evaluation scripts is included in the `resources/config`
directory. Firstly, please specify paths to input files which will be evaluated. Afterwards, open the command
prompt in the main directory of the application and type:
```
python3 evaluation/image_evaluation.py
```
to run the script evaluating output images, or:
```
python3 evaluation/logs_evaluation.py
```
to run the script evaluating log files produced by the algorithms. It is also necessary to install the dependencies
before.

