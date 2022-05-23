# MLFLOW-LASSO and RIDGE regression  experiments tracking:

* In this project you will understand how we can use MLFLOW and log various metrics.

* We will conduct the data analysis and draw various infrenses that are needed. 

* We will compare the performance of the model using MLFLOW  comparsion GUI.

* This experimrnt is going to be a more advanced than the simple demo we saw earlier(AIOPS-MLFLOW)
*
* This experimrnt will also show us a way how to serve a model using MLFLOW capabilities.
* 


## commands used -

### for getting user interface

```bash
mlflow ui
```

### This code can be easily run from anywhere with simple command as below 
* The advantage is that you dont need to download the code into local machine or no need to change any code snippets.
* Experiments can be run easily without any need.

```bash
 mlflow run https://github.com/premchand228/MLFLOW-LASSO-experiment-tracking.git
```

### for running an MLproject

#### To run a MLproject inside a current working directory 
```bash
mlflow run . 
```
#### To run a MLproject inside a current working directory with existing conda env
```bash
mlflow run . --no-conda
```

#### To run a MLproject inside a current working directory with parameters specified in MLproject
```bash
mlflow run . -P param1=0.2 
```
#### To run a MLproject inside from a github repository 
```bash
mlflow run https://github.com/<USERNAME>/<REPO_NAME.git -P param=5.0
```
#### To export conda environment to a file 
```bash
conda env export > conda.yaml
```
### To serve a model we need to run following command which will act as API.
```bash 
mlflow models serve -m /home/premchand228/Datascience/mlflow/MLFLOW-Lasso_exp/MLFLOW-LASSO-experiment-tracking/mlruns/0/00271c67ea9c4dfdb5fec5bcc98f1930/artifacts/model -p 1234
```

### command for prediction on serving model 
#### for windows -
```bash
curl -X POST -H "Content-Type:application/json; format=pandas-split" --data "{\"columns\":[\"alcohol\", \"chlorides\", \"citric acid\", \"density\", \"fixed acidity\", \"free sulfur dioxide\", \"pH\", \"residual sugar\", \"sulphates\", \"total sulfur dioxide\", \"volatile acidity\"],\"data\":[[12.8, 0.029, 0.48, 0.98, 6.2, 29, 3.33, 1.2, 0.39, 75, 0.66]]}" http://127.0.0.1:1234/invocations
```
#### On Linux and macOS
```bash
curl -X POST -H "Content-Type:application/json; format=pandas-split" --data '{"columns":["alcohol", "chlorides", "citric acid", "density", "fixed acidity", "free sulfur dioxide", "pH", "residual sugar", "sulphates", "total sulfur dioxide", "volatile acidity"],"data":[[12.8, 0.029, 0.48, 0.98, 6.2, 29, 3.33, 1.2, 0.39, 75, 0.66]]}' http://127.0.0.1:1234/invocations
```
#### Or use `Thunder client` extension on VSCode or use PostMan


### Comparing diffrent experiments and identifying the accurate parameters and metrics.

![alt text](https://github.com/premchand228/MLFLOW-LASSO-experiment-tracking/blob/master/canvas.png)
