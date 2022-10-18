```commandline
% curl -X POST http://127.0.0.1:5000/predict -d '{"requested":20000,"annual_income":100000,"apr":2.5,"credit":"good"}' -H "Content-Type: application/json"
Must set application's model before attempting prediction
```
---
```commandline
% curl -X GET 127.0.0.1:5000/get_all_models                               
[{"created_at":"2022-10-18 18:56:11 UTC","description":"model #1","model_uuid":"3ecbec9b511940cc9c7a643cf559a0fb"},{"created_at":"2022-10-18 18:56:17 UTC","description":"model #2","model_uuid":"f3064871e1f4404cb204a210d49f2da8"}]
```
---
```commandline
% curl -X GET 127.0.0.1:5000/get_current_model 
{"model_uuid":null}
```
---
```commandline
% curl -X POST 127.0.0.1:5000/set_model -d '{"model_uuid":"3ecbec9b511940cc9c7a643cf559a0fb"}' -H "Content-Type: application/json"
{}
```
---
```commandline
curl -X GET 127.0.0.1:5000/get_current_model                                                                                    
{"model_uuid":"3ecbec9b511940cc9c7a643cf559a0fb"}
```
---
```commandline
% curl -X POST http://127.0.0.1:5000/predict -d '{"requested":20000,"annual_income":100000,"apr":2.5,"credit":"good"}' -H "Content-Type: application/json"
{"click_probability":0.026067497479385218}
```
---
```commandline
% curl -X POST 127.0.0.1:5000/set_model -d '{"model_uuid":"f3064871e1f4404cb204a210d49f2da8"}' -H "Content-Type: application/json"
{}
```
---
```commandline
% curl -X GET 127.0.0.1:5000/get_current_model 
{"model_uuid":"f3064871e1f4404cb204a210d49f2da8"}
```
---
```commandline
% curl -X POST http://127.0.0.1:5000/predict -d '{"requested":20000,"annual_income":100000,"apr":2.5,"credit":"good"}' -H "Content-Type: application/json"
{"click_probability":0.0009745599238229246}
```
