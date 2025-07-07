# types on the basis of how model will be trained on production
# 1. Batch Training
#    - In batch training, the model is trained on the entire dataset at once.  
# Problem: 
#    - Retrain requires access to the entire dataset, which may not be feasible for large datasets.
#    - It can be time-consuming and resource-intensive, especially for large datasets.


# 2. Online Training
#    - In online training, the model is trained incrementally by processing one training example at a time. This allows the model to adapt to new data quickly.

# 3. Out-of-Core Training
#    - Out-of-core training is used when the dataset is too large to fit into memory. The model is trained on small batches of data that are loaded into memory one at a time.