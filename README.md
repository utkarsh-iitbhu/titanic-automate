## Titanic automate

```
titanic/
├── __init__.py
├── components/
│   ├── __init__.py
│   ├── data_ingestion.py
│   ├── data_validation.py
│   ├── data_transformation.py
│   ├── model_trainer.py
│   ├── model_evaluation.py
│   └── model_pusher.py
├── configuration/
│   └── __init__.py
├── constants/
│   └── __init__.py
├── entity/
│   ├── __init__.py
│   ├── config_entity.py
│   └── artifact_entity.py
├── exception/
│   └── __init__.py
├── logger/
│   └── __init__.py
├── pipeline/
│   ├── __init__.py
│   ├── training_pipeline.py
│   └── prediction_pipeline.py
├── utils/
│   ├── __init__.py
│   └── main_utils.py
tests/
├── test_data_ingestion.py
├── test_data_validation.py
├── test_data_transformation.py
├── test_model_trainer.py
└── test_model_evaluation.py
app.py
requirements.txt
Dockerfile
.dockerignore
demo.py
setup.py
config/
├── model.yaml
└── schema.yaml
```

1. Updated template.py
2. Updates setup.py | add correct repo name 
3. Build the package pip install -e . | creates .egg-info 
4. Add .gitignore 

