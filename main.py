from CNNClassifier import logger
from CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipelines
from CNNClassifier.pipeline.stage_02_prepare_basemodel import PrepareBaseModelTrainingPipeline
from CNNClassifier.pipeline.stage_03_training import ModelTrainingPipeline
STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f'>>>>>> Stage {STAGE_NAME} Started <<<<<<')
    data_ingestion = DataIngestionTrainingPipelines()
    data_ingestion.main()
    logger.info(
        f'>>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nx==========x')
except Exception as e:
    logger.exception(e)


STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f'>>>>>> Stage {STAGE_NAME} Started <<<<<<')
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nx==========x')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
