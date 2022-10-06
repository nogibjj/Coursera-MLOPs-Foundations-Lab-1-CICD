[![CI](https://github.com/nogibjj/mlops-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/mlops-template/actions/workflows/cicd.yml)
[![Codespaces Prebuilds](https://github.com/nogibjj/mlops-template/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg)](https://github.com/nogibjj/mlops-template/actions/workflows/codespaces/create_codespaces_prebuilds)

## Lab 1-Introduction to Continuous Integration

### Tasks

1. Run the following steps of the `Makefile`:

`make lint`
`make format`
`make refactor`
`make test`

* Reflection Question:  Why does refactor combine `lint` and `format`?

2. Run the following command-line tool and then write a test for it using click test runner:

* Write a test for the `add_cli` functionality of the `main.py` function in the `test_main.py` test file.
* Use the test for for `./main.py --help` as a guide.  
* Reflection Question:  How could you use this style of testing to build MLOps tools quickly?


### References

* You can view this lab in [GitHub here https://github.com/nogibjj/Coursera-MLOPs-Foundations-Lab-1-CICD](https://github.com/nogibjj/Coursera-MLOPs-Foundations-Lab-1-CICD)