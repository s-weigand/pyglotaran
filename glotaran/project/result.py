from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Any
from typing import Literal

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

from glotaran.builtin.io.yml.utils import write_dict
from glotaran.io import save_dataset
from glotaran.io import save_parameters
from glotaran.model.errors import GlotaranUserError
from glotaran.model.experiment_model import ExperimentModel  # noqa: TCH001
from glotaran.optimization import OptimizationInfo  # noqa: TCH001
from glotaran.optimization.objective import OptimizationResult  # noqa: TCH001
from glotaran.parameter import Parameters  # noqa: TCH001

if TYPE_CHECKING:
    from pathlib import Path


class SavingOptions(BaseModel):
    """A collection of options for result saving."""

    data_filter: list[str] = Field(
        default_factory=list,
        description="List of per dataset optimization result attributes to exclude.",
    )
    data_format: Literal["nc"] = "nc"
    parameter_format: Literal["csv"] = "csv"


SAVING_OPTIONS_DEFAULT = SavingOptions()


class Result(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    datasets: dict[str, OptimizationResult]
    experiments: dict[str, ExperimentModel]
    optimization_info: OptimizationInfo
    initial_parameters: Parameters
    optimized_parameters: Parameters

    def save(
        self,
        path: Path,
        options: SavingOptions = SAVING_OPTIONS_DEFAULT,
        allow_overwrite: bool = False,
    ):
        if path.is_file():
            raise GlotaranUserError("Save path must be a folder.")
        if path.exists() and not allow_overwrite:
            raise GlotaranUserError(
                "Save path already exists. Use allow_overwrite=True to overwrite."
            )
        result_dict: dict[str, Any] = {
            "data": {},
            "experiments": {},
            "optimization_info": self.optimization_info.model_dump(
                exclude={
                    "parameter_history",
                    "optimization_history",
                    "covariance_matrix",
                    "jacobian",
                }
            ),
        }

        # TODO: Save scheme or experiments
        #  experiment_folder = path / "experiments"
        #  experiment_folder.mkdir()
        #  for label, experiment in self.experiments.items():
        #      experiment_path = experiment_folder / f"{label}.yml"
        #      result_dict["experiments"][label] = experiment_path
        #      write_dict(experiment.model_dump(), experiment_path)

        data_path = path / "datasets"
        for label, optimization_result in self.datasets.items():
            dataset_path = data_path / label
            data_path.mkdir(parents=True, exist_ok=True)
            result_dict["data"][label] = dataset_path.relative_to(path).as_posix()
            for top_level_dataset_attr in ["input_data", "residuals", "fitted_data"]:
                if top_level_dataset_attr not in options.data_filter:
                    value = getattr(optimization_result, top_level_dataset_attr)
                    if value is None:
                        continue
                    save_dataset(
                        value,
                        dataset_path / f"{top_level_dataset_attr}.{options.data_format}",
                        allow_overwrite=allow_overwrite,
                    )
            if "elements" not in options.data_filter:
                for element_label, element_result in optimization_result.elements.items():
                    save_dataset(
                        element_result,
                        dataset_path / "elements" / f"{element_label}.{options.data_format}",
                        allow_overwrite=allow_overwrite,
                    )
            if "activations" not in options.data_filter:
                for activation_label, activation_result in optimization_result.activations.items():
                    save_dataset(
                        activation_result,
                        dataset_path / "activations" / f"{activation_label}.{options.data_format}",
                        allow_overwrite=allow_overwrite,
                    )

        optimization_history_path = path / "optimization_history.csv"
        result_dict["optimization_history"] = optimization_history_path.relative_to(
            path
        ).as_posix()
        self.optimization_info.optimization_history.to_csv(optimization_history_path)

        initial_parameters_path = path / f"initial_parameters.{options.parameter_format}"
        result_dict["initial_parameters"] = initial_parameters_path.relative_to(path).as_posix()
        save_parameters(
            self.initial_parameters,
            initial_parameters_path,
            allow_overwrite=allow_overwrite,
        )

        parameters_optimized_path = path / f"parameters_optimized.{options.parameter_format}"
        result_dict["parameters_optimized"] = parameters_optimized_path.relative_to(
            path
        ).as_posix()
        save_parameters(
            self.optimized_parameters,
            parameters_optimized_path,
            allow_overwrite=allow_overwrite,
        )

        result_path = path / "glotaran_result.yml"
        write_dict(result_dict, result_path)
