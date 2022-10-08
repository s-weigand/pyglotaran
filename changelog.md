# Changelog

(changes-0_7_0)=

## 🚀 0.7.0 (Unreleased)

### 💥 BREAKING CHANGE

- 💥🚧 Dropped support for Python 3.8 and 3.9 and only support 3.10 (#1135)

### ✨ Features

- ✨ Add optimization history to result and iteration column to parameter history (#1134)

### 👌 Minor Improvements:

- 👌🎨 Wrap model section in result markdown in details tag for notebooks (#1098)

### 🩹 Bug fixes

### 📚 Documentation

### 🗑️ Deprecations (due in 0.9.0)

### 🗑️❌ Deprecated functionality removed in this release

### 🚧 Maintenance

- 🚇🩹 Fix wrong comparison in pr_benchmark workflow (#1097)
- 🔧 Set sourcery-ai target python version to 3.8 (#1095)
- 🚇🩹🔧 Fix manifest check (#1099)
- ♻️ Refactor: optimization (#1060)

(changes-0_6_0)=

## 🚀 0.6.0 (2022-06-06)

### ✨ Features

- ✨ Python 3.10 support (#977)
- ✨ Add simple decay megacomplexes (#860)
- ✨ Feature: Generators (#866)
- ✨ Project Class (#869)
- ✨ Add clp guidance megacomplex (#1029)

### 👌 Minor Improvements:

- 👌🎨 Add proper repr for DatasetMapping (#957)
- 👌 Add SavingOptions to save_result API (#966)
- ✨ Add parameter IO support for more formats supported by pandas (#896)
- 👌 Apply IRF shift in coherent artifact megacomplex (#992)
- 👌 Added IRF shift to result dataset (#994)
- 👌 Improve Result, Parameter and ParameterGroup markdown (#1012)
- 👌🧹 Add suffix to rate and lifetime and guard for missing datasets (#1022)
- ♻️ Move simulation to own module (#1041)
- ♻️ Move optimization to new module glotaran.optimization (#1047)
- 🩹 Fix missing installation of clp-guide megacomplex as plugin (#1066)
- 🚧🔧 Add 'extras' and 'full' extras_require installation options (#1089)

### 🩹 Bug fixes

- 🩹 Fix Crash in optimization_group_calculator_linked when using guidance spectra (#950)
- 🩹 ParameterGroup.get degrades full_label of nested Parameters with nesting over 2 (#1043)
- 🩹 Show validation problem if parameters are missing values (default: NaN) (#1076)

### 📚 Documentation

- 🎨 Add new logo (#1083, #1087)

### 🗑️ Deprecations (due in 0.8.0)

- `glotaran.io.save_result(result, result_path, format_name='legacy')` -> `glotaran.io.save_result(result, Path(result_path) / 'result.yml')`
- `glotaran.analysis.simulation` -> `glotaran.simulation.simulation`
- `glotaran.analysis.optimize` -> `glotaran.optimization.optimize`

### 🗑️❌ Deprecated functionality removed in this release

- `glotaran.ParameterGroup` -> `glotaran.parameter.ParameterGroup`
- `glotaran.read_model_from_yaml` -> `glotaran.io.load_model(..., format_name="yaml_str")`
- `glotaran.read_model_from_yaml_file` -> `glotaran.io.load_model(..., format_name="yaml")`
- `glotaran.read_parameters_from_csv_file` -> `glotaran.io.load_parameters(..., format_name="csv")`
- `glotaran.read_parameters_from_yaml` -> `glotaran.io.load_parameters(..., format_name="yaml_str")`
- `glotaran.read_parameters_from_yaml_file` -> `glotaran.io.load_parameters(..., format_name="yaml")`
- `glotaran.io.read_data_file` -> `glotaran.io.load_dataset`
- `result.get_dataset("<dataset_name>")` -> `result.data["<dataset_name>"]`
- `glotaran.analysis.result` -> `glotaran.project.result`
- `glotaran.analysis.scheme` -> `glotaran.project.scheme`

### 🚧 Maintenance

- 🔧 Improve packaging tooling (#923)
- 🔧🚇 Exclude test files from duplication checks on sonarcloud (#959)
- 🔧🚇 Only run check-manifest on the CI (#967)
- 🚇👌 Exclude dependabot push CI runs (#978)
- 🚇👌 Exclude sourcery AI push CI runs (#1014)
- 👌📚🚇 Auto remove notebook written data when building docs (#1019)
- 👌🚇 Change integration tests to use self managed examples action (#1034)
- 🚇🧹 Exclude pre-commit bot branch from CI runs on push (#1085)

(changes-0_5_1)=

## 🚀 0.5.1 (2021-12-31)

### 🩹 Bug fixes

- 🩹 Bugfix Use normalized initial_concentrations in result creation for decay megacomplex (#927)
- 🩹 Fix save_result crashes on Windows if input data are on a different drive than result (#931)

### 🚧 Maintenance

- 🚧 Forward port Improve result comparison workflow and v0.4 changelog (#938)
- 🚧 Forward port of #936 test_result_consistency

(changes-0_5_0)=

## 🚀 0.5.0 (2021-12-01)

### ✨ Features

- ✨ Feature: Megacomplex Models (#736)
- ✨ Feature: Full Models (#747)
- ✨ Damped Oscillation Megacomplex (a.k.a. DOAS) (#764)
- ✨ Add Dataset Groups (#851)
- ✨ Performance improvements (in some cases up to 5x) (#740)

### 👌 Minor Improvements:

- 👌 Add dimensions to megacomplex and dataset_descriptor (#702)
- 👌 Improve ordering in k_matrix involved_compartments function (#788)
- 👌 Improvements to application of clp_penalties (equal area) (#801)
- ♻️ Refactor model.from_dict to parse megacomplex_type from dict and add simple_generator for testing (#807)
- ♻️ Refactor model spec (#836)
- ♻️ Refactor Result Saving (#841)
- ✨ Use ruaml.yaml parser for roundtrip support (#893)
- ♻️ Refactor Result and Scheme loading/initializing from files (#903)
- ♻️ Several refactoring in `glotaran.Parameter` (#910)
- 👌 Improved Reporting of Parameters (#910, #914, #918)
- 👌 Scheme now excepts paths to model, parameter and data file without initializing them first (#912)

### 🩹 Bug fixes

- 🩹 Fix/cli0.5 (#765)
- 🩹 Fix compartment ordering randomization due to use of set (#799)
- 🩹 Fix check_deprecations not showing deprecation warnings (#775)
- 🩹 Fix and re-enable IRF Dispersion Test (#786)
- 🩹 Fix coherent artifact crash for index dependent models #808
- 🩹 False positive model validation fail when combining multiple default megacomplexes (#797)
- 🩹 Fix ParameterGroup repr when created with 'from_list' (#827)
- 🩹 Fix for DOAS with reversed oscillations (negative rates) (#839)
- 🩹 Fix parameter expression parsing (#843)
- 🩹 Use a context manager when opening a nc dataset (#848)
- 🚧 Disallow xarray versions breaking plotting in integration tests (#900)
- 🩹 Fix 'dataset_groups' not shown in model markdown (#906)

### 📚 Documentation

- 📚 Moved API documentation from User to Developer Docs (#776)
- 📚 Add docs for the CLI (#784)
- 📚 Fix deprecation in model used in quickstart notebook (#834)

### 🗑️ Deprecations (due in 0.7.0)

- `glotaran.model.Model.model_dimension` -> `glotaran.project.Scheme.model_dimension`
- `glotaran.model.Model.global_dimension` -> `glotaran.project.Scheme.global_dimension`
- `<model_file>.type.kinetic-spectrum` -> `<model_file>.default_megacomplex.decay`
- `<model_file>.type.spectral-model` -> `<model_file>.default_megacomplex.spectral`
- `<model_file>.spectral_relations` -> `<model_file>.clp_relations`
- `<model_file>.spectral_relations.compartment` -> `<model_file>.clp_relations.source`
- `<model_file>.spectral_constraints` -> `<model_file>.clp_constraints`
- `<model_file>.spectral_constraints.compartment` -> `<model_file>.clp_constraints.target`
- `<model_file>.equal_area_penalties` -> `<model_file>.clp_area_penalties`
- `<model_file>.irf.center_dispersion` -> `<model_file>.irf.center_dispersion_coefficients`
- `<model_file>.irf.width_dispersion` -> `<model_file>.irf.width_dispersion_coefficients`
- `glotaran.project.Scheme(..., non_negative_least_squares=...)` -> `<model_file>dataset_groups.default.residual_function`
- `glotaran.project.Scheme(..., group=...)` -> `<model_file>dataset_groups.default.link_clp`
- `glotaran.project.Scheme(..., group_tolerance=...)` -> `glotaran.project.Scheme(..., clp_link_tolerance=...)`
- `<scheme_file>.maximum-number-function-evaluations` -> `<scheme_file>.maximum_number_function_evaluations`
- `<model_file>.non-negative-least-squares: true` -> `<model_file>dataset_groups.default.residual_function: non_negative_least_squares`
- `<model_file>.non-negative-least-squares: false` -> `<model_file>dataset_groups.default.residual_function: variable_projection`
- `glotaran.parameter.ParameterGroup.to_csv(file_name=parameters.csv)` -> `glotaran.io.save_parameters(parameters, file_name=parameters.csv)`

### 🚧 Maintenance

- 🩹 Fix Performance Regressions (between version) (#740)
- 🧪🚇 Add integration test result validation (#754)
- 🔧 Add more QA tools for parts of glotaran (#739)
- 🔧 Fix interrogate usage (#781)
- 🚇 Speedup PR benchmark (#785)
- 🚇🩹 Use pinned versions of dependencies to run integration CI tests (#892)
- 🧹 Move megacomplex integration tests from root level to megacomplexes (#894)
- 🩹 Fix artifact download in pr_benchmark_reaction workflow (#907)

(changes-0_4_2)=

## 🚀 0.4.2 (2021-12-31)

### 🩹 Bug fixes

- 🩹🚧 Backport of bugfix #927 discovered in PR #860 related to initial_concentration normalization when saving results (#935).

### 🚧 Maintenance

- 🚇🚧 Updated 'gold standard' result comparison reference ([old](https://github.com/glotaran/pyglotaran-examples/commit/9b8591c668ad7383a908b853339966d5a5f7fe43) -> [new](https://github.com/glotaran/pyglotaran-examples/commit/fc5a5ca0c7fd8b224c85027b510a15717c696c7b))
- 🚇 Refine test_result_consistency (#936).

(changes-0_4_1)=

## 🚀 0.4.1 (2021-09-07)

### ✨ Features

- Integration test result validation (#760)

### 🩹 Bug fixes

- Fix unintended saving of sub-optimal parameters (0ece818, backport from #747)
- Improve ordering in k_matrix involved_compartments function (#791)

(changes-0_4_0)=

## 🚀 0.4.0 (2021-06-25)

### ✨ Features

- Add basic spectral model (#672)
- Add Channel/Wavelength dependent shift parameter to irf. (#673)
- Refactored Problem class into GroupedProblem and UngroupedProblem (#681)
- Plugin system was rewritten (#600, #665)
- Deprecation framework (#631)
- Better notebook integration (#689)

### 🩹 Bug fixes

- Fix excessive memory usage in `_create_svd` (#576)
- Fix several issues with KineticImage model (#612)
- Fix exception in sdt reader index calculation (#647)
- Avoid crash in result markdown printing when optimization fails (#630)
- ParameterNotFoundException doesn't prepend '.' if path is empty (#688)
- Ensure Parameter.label is str or None (#678)
- Properly scale StdError of estimated parameters with RMSE (#704)
- More robust covariance_matrix calculation (#706)
- `ParameterGroup.markdown()` independent parametergroups of order (#592)

### 🔌 Plugins

- `ProjectIo` 'folder'/'legacy' plugin to save results (#620)
- `Model` 'spectral-model' (#672)

### 📚 Documentation

- User documentation is written in notebooks (#568)
- Documentation on how to write a `DataIo` plugin (#600)

### 🗑️ Deprecations (due in 0.6.0)

- `glotaran.ParameterGroup` -> `glotaran.parameterParameterGroup`
- `glotaran.read_model_from_yaml` -> `glotaran.io.load_model(..., format_name="yaml_str")`
- `glotaran.read_model_from_yaml_file` -> `glotaran.io.load_model(..., format_name="yaml")`
- `glotaran.read_parameters_from_csv_file` -> `glotaran.io.load_parameters(..., format_name="csv")`
- `glotaran.read_parameters_from_yaml` -> `glotaran.io.load_parameters(..., format_name="yaml_str")`
- `glotaran.read_parameters_from_yaml_file` -> `glotaran.io.load_parameters(..., format_name="yaml")`
- `glotaran.io.read_data_file` -> `glotaran.io.load_dataset`
- `result.save` -> `glotaran.io.save_result(result, ..., format_name="legacy")`
- `result.get_dataset("<dataset_name>")` -> `result.data["<dataset_name>"]`
- `glotaran.analysis.result` -> `glotaran.project.result`
- `glotaran.analysis.scheme` -> `glotaran.project.scheme`
- `model.simulate` -> `glotaran.analysis.simulation.simulate(model, ...)`

(changes-0_3_3)=

## 🚀 0.3.3 (2021-03-18)

- Force recalculation of SVD attributes in `scheme._prepare_data` (#597)
- Remove unneeded check in `spectral_penalties._get_area` Fixes (#598)
- Added python 3.9 support (#450)

(changes-0_3_2)=

## 🚀 0.3.2 (2021-02-28)

- Re-release of version 0.3.1 due to packaging issue

(changes-0_3_1)=

## 🚀 0.3.1 (2021-02-28)

- Added compatibility for numpy 1.20 and raised minimum required numpy version to 1.20 (#555)
- Fixed excessive memory consumption in result creation due to full SVD computation (#574)
- Added feature parameter history (#557)
- Moved setup logic to `setup.cfg` (#560)

(changes-0_3_0)=

## 🚀 0.3.0 (2021-02-11)

- Significant code refactor with small API changes to parameter relation specification (see docs)
- Replaced lmfit with scipy.optimize

(changes-0_2_0)=

## 🚀 0.2.0 (2020-12-02)

- Large refactor with significant improvements but also small API changes (see docs)
- Removed doas plugin

(changes-0_1_0)=

## 🚀 0.1.0 (2020-07-14)

- Package was renamed to `pyglotaran` on PyPi

(changes-0_0_8)=

## 🚀 0.0.8 (2018-08-07)

- Changed `nan_policiy` to `omit`

(changes-0_0_7)=

## 🚀 0.0.7 (2018-08-07)

- Added support for multiple shapes per compartment.

(changes-0_0_6)=

## 🚀 0.0.6 (2018-08-07)

- First release on PyPI, support for Windows installs added.
- Pre-Alpha Development
