# TrAISformer

Pytorch implementation of TrAISformer---A generative transformer for AIS trajectory prediction (https://arxiv.org/abs/2109.03958).

The transformer part is adapted from: https://github.com/karpathy/minGPT

---
<p align="center">
  <img width="600" height="450" src="./results/ct_dma-pos-pos_vicinity-10-40-blur-True-False-2-1.0-data_size-250-270-30-72-embd_size-256-256-128-128-head-8-8-bs-32-lr-0.0006-seqlen-18-120//prediction_error.png">
</p>


#### Requirements: 
See requirements.yml

### Datasets:

The data used in this paper are provided by the [Danish Maritime Authority (DMA)](https://dma.dk/safety-at-sea/navigational-information/ais-data). 
Please refer to [the paper](https://arxiv.org/abs/2109.03958) for the details of the pre-processing step. The code is available here: https://github.com/CIA-Oceanix/GeoTrackNet/blob/master/data/csv2pkl.py

A processed dataset can be found in `./data/ct_dma/`
(the format is `[lat, log, sog, cog, unix_timestamp, mmsi]`).

### Run

Run `trAISformer.py` to train and evaluate the model.
(Please note that the values given by the code are in km, while the values presented in the paper were converted to nautical mile.)


### License

See `LICENSE`

### Contact
For any questions, please open an issue and assign it to @dnguyengithub.

# trAISformer
