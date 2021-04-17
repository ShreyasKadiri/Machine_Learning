# Colab's file access feature
from google.colab import files

#retrieve uploaded file
uploaded = files.upload()

#print results
for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))
  
# Then move kaggle.json into the folder where the API expects to find it.
!mkdir -p ~/.kaggle/ && mv kaggle.json ~/.kaggle/ && chmod 600 ~/.kaggle/kaggle.json


!pip install --upgrade --force-reinstall --no-deps kaggle

#list competitions
!kaggle competitions list

#Getting the dataset
#!kaggle competitions download -c LANL-Earthquake-Prediction
!kaggle competitions download -c <Dataset_Name>

#unzip training data for usage, will take about 5 minutes (its big)
#!ls
#!unzip LANL-Earthquake-Prediction.zip
!unzip <Dataset_Name>.zip
#!ls
