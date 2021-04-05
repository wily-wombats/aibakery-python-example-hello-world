import random

from aibakery.aibakery_service import AIBakeryService, ResultCapture
from pydantic import BaseModel

aibakery_service = AIBakeryService()


class RandomFeature(BaseModel):
    x1: int
    x2: int


def load_model():
    return None


@aibakery_service.prediction(feature_schema=RandomFeature,
                             model_loader=load_model)
def predict(model, feature: RandomFeature, results: ResultCapture):
    for i in range(2):
        results.add_result(
                key=f'some_random_num_{i}',
                value=random.randrange(feature.x1, feature.x2),
                meta={
                    'page': i,
                }
        )
