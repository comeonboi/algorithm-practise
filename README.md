# LeetCode Solutions

![GitHub last commit](https://img.shields.io/github/last-commit/comeonboi/leetcode-solutions) [![GitHub issues](https://img.shields.io/github/issues-raw/comeonboi/leetcode-solutions)](https://github.com/comeonboi/leetcode-solutions/issues) [![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/comeonboi/leetcode-solutions)](https://github.com/comeonboi/leetcode-solutions/pulls) [![GitHub contributors](https://img.shields.io/github/contributors/comeonboi/leetcode-solutions)](https://github.com/comeonboi/leetcode-solutions/graphs/contributors)

A collection of LeetCode problems and solutions created by HeyHey大魔王 and 龙龙.

## Problems

| # | Title | Solution | Difficulty |
|---| ----- | -------- | ---------- |
{% for issue in site.issues %}
| {{ issue.number }} | [{{ issue.title }}]({{ issue.html_url }}) | [Python]({{ site.baseurl }}/python/{{ issue.number }}_{{ issue.title | replace: ' ', '_' | replace: '.', '_' | downcase }}.py) | {{ issue.labels[0].name }} |
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

* [HeyHey大魔王](https://github.com/comeonboi)
* [龙龙](https://github.com/longsizhuo123)

## License

This repository is licensed under the [MIT License](LICENSE).
