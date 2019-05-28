# test_repo

## To run tests: 
- From the base_tests folder, run - `py.test fixtures/` 
- For verbose output, run - `py.test -s -v fixtures/`

## To run tests for rest_api testing:
- From the base_tests folder, run - `py.test -s -v test_rest_api/test_api.py` with params `--all-services` or `--service` with service name                

## Parser for access.log
- To use the log parsing script `base_tests/opencart_testing/log_parser.py`, you need to specify the path to access.log or to the directory where to search for this log.
-  `log_parser.py ~/dir/access.log` the result will be saved to the `result.json` file in json format.