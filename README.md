# algorithm-practise
# LeetCode Solutions

![GitHub last commit](https://img.shields.io/github/last-commit/longsizhuo123/algorithm-practise) [![GitHub issues](https://img.shields.io/github/issues-raw/<username>/<repo-name>)](https://github.com/<username>/<repo-name>/issues) [![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/<username>/<repo-name>)](https://github.com/<username>/<repo-name>/pulls) [![GitHub contributors](https://img.shields.io/github/contributors/<username>/<repo-name>)](https://github.com/<username>/<repo-name>/graphs/contributors)

A collection of LeetCode problems and solutions created by <username> and their friends. 

## Problems

| # | Title | Solution | Difficulty |
|---| ----- | -------- | ---------- |
{% for problem in problems %}
| {{problem.number}} | [{{problem.title}}]({{problem.link}}) | [{{problem.solution.language}}]({{problem.solution.link}}) | {{problem.difficulty}} |
{% endfor %}

## Contributing

We welcome contributions! If you want to add a solution:

1. Fork the repository.
2. Create a new branch for your solution.
3. Add your solution in the corresponding directory.
4. Commit your changes and push to your branch.
5. Create a pull request and we'll review your code.

## Contributors

Thank you to all the contributors who have helped create and maintain this repository!

{% for contributor in contributors %}
* [comeonboi](https://github.com/comeonboi)
* [longsizhuo123](https://github.com/longsizhuo123)
{% endfor %}

## License

This repository is licensed under the [MIT License](LICENSE).
