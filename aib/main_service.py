import random

from aibakery import logger
from aibakery.aibakery_service import AIBakeryService, ResultCapture
from pydantic import BaseModel

aibakery_service = AIBakeryService()


class RandomFeature(BaseModel):
    x1: int
    x2: int


@aibakery_service.prediction(model_loader=None,
                             feature_schema=RandomFeature)
def predict(model, feature: RandomFeature, results: ResultCapture):
    logger.info('Starting model prediction')
    for i in range(2):
        logger.info(f'Prediction {i+1} running')

        results.add_result(
                key=f'some_random_num_{i}',
                value=random.randrange(feature.x1, feature.x2),
                meta={
                    'page': i,
                }
        )

        logger.info(f'Prediction {i+1} complete')


if __name__ == '__main__':
    print(predict(
            feature={
                'x1': 0,
                'x2': 10
            }
    ))
