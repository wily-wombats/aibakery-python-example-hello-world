import random

from aibakery.aibakery_service import AIBakeryService, ResultCapture
from pydantic import BaseModel

aibakery_service = AIBakeryService()


class RandomFeature(BaseModel):
    x1: int
    x2: int


@aibakery_service.prediction(model_loader=None,
                             feature_schema=RandomFeature)
def predict(model, feature: RandomFeature, results: ResultCapture):
    for i in range(2):
        results.add_result(
                key=f'some_random_num_{i}',
                value=random.randrange(feature.x1, feature.x2),
                meta={
                    'page': i,
                }
        )


if __name__ == '__main__':
    print(predict(
            feature={
                'x1': 0,
                'x2': 10
            }
    ))
