from CNNClassifier import logger
from CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipelines


STAGE_NAME = "Data Ingestion Stage"
if __name__ == '__main__':
    try:
        logger.info(f'>>>>>> Stage {STAGE_NAME} Started <<<<<<')
        data_ingestion = DataIngestionTrainingPipelines()
        data_ingestion.main()
        logger.info(f'>>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nx==========x')
    except Exception as e:
        logger.exception(e)