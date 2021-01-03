from nyctaxi.settings import TAXI_MODEL_WORKDIR

import joblib

model_file = TAXI_MODEL_WORKDIR + '/Data/Modeling/taxi_model.jbl'

# Loading models at the service initialization
if 'globalTrainResults' not in dir():
    print('READING MODELS FROM ', model_file)
    globalTrainResults = joblib.load(model_file)
