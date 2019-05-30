# CLAMS Apps

## Apps in action 

| App name | AnnotationType | Version | codebase | 
| ------------ | -------------- | ------- | -------- | 
| A text app | someTextAnnType | 0.0.1 | somewhere | 
| A video app | someVideoAnnType | 0.0.1 | elsewhere | 

## Repository naming convention

* Applications in the `clamsproject` organization should prefixed with `app-`. 
* An application that wraps an extant tool or application must be suffixed with `-wrapper`. 
* `LICENSE` file should always contains licensing information of the terminal tool. If the terminal tool is a wrapper, an additional file containing licensing information of the original tool must be placed next to the `LICENSE` file when the original license requires so. 

## Requirements for CLAMS applications

1. An app should implement [`ClamsApp`](https://github.com/clamsproject/clams-python-sdk/blob/master/clams/serve/__init__.py) in the python SDK
1. An app is recommended to be served as a REST-ful web service. See [`Resifier`](https://github.com/clamsproject/clams-python-sdk/blob/master/clams/restify/__init__.py) in the SDK. 
1. To be compatible with [the CLAMS galaxy appliance](https://github.com/clamsproject/appliance), an app repository should provide a `dockerfile` to make a single-purposed docker container for the app. 
