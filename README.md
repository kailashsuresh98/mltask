# Furniture Classifier API

Deep Learning Framework: Tensorflow2
Backend Framework: FastAPI

This is a project which has two parts:

- the Jupyter note book in side the directory "/model"
- the API which serves the model "/api"

## Model Creation

The model creation notebook uses transfer learning technique to create a multi class classifier. Once you executed the last cell. You will find the saved model as a folder "prediction_model" :
> Copy the folder "predicted_model" to the "/api/app"

## API setup in Local Environment:

> 1. Build the docker image
```sh
cd ./api
docker build -t <image_name> .
```
> 2. Run the image built
```sh
docker run -d --name <container_name> -p 80:80 <image_name>
```
> 3. Test the API
```sh
curl --location --request POST 'http://127.0.0.1:80/predict/image' \
--form 'file=@"path-to-image-file"'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
