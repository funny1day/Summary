from ssd.data.datasets import VOCDataset
from .voc import voc_evaluation


class EvaluationMetrics:
    def __init__(self, dataset, evaluation_result):
        if isinstance(dataset, VOCDataset):
            self._parse_pascal_eval_metrics(evaluation_result)

    def _parse_pascal_eval_metrics(self, evaluation_result):
        self.info = {'metrics': evaluation_result['metrics']}

    def get_printable_metrics(self):
        return self.info


def evaluate(dataset, predictions, output_dir):
    """evaluate dataset using different methods based on dataset type.
    Args:
        dataset: Dataset object
        predictions(list[(boxes, labels, scores)]): Each item in the list represents the
            prediction results for one image. And the index should match the dataset index.
        output_dir: output folder, to save evaluation files or results.
    Returns:
        evaluation result
    """
    args = dict(
        dataset=dataset, predictions=predictions, output_dir=output_dir
    )
    if isinstance(dataset, VOCDataset):
        evaluation_result = voc_evaluation(**args)
    else:
        raise NotImplementedError

    return EvaluationMetrics(dataset, evaluation_result)
