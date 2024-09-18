# Define prompt for generating the dataset
sys_message = """
Generate a JSON dataset that contains details for two software packages: some legitimate and some simulated malicious. Each package should include the following fields:

- package_name: The name of the software package.
- version: The version number of the package.
- description: A brief description of the package.
- readme: A detailed explanation of what the package does.
- scripts: A list of script files contained in the package.
- distribution_tag: The tag associated with the distribution of the package.
- authors: An array of authors who contributed to the package.
- contributors: An array of contributors, with each contributor's name and email.
- maintainers: An array of maintainers, with each maintainer's name and email.
- publishers: The license or entity that publishes the package.
- dependencies: A list of dependencies that the package requires to run.
- development_dependencies: A list of development dependencies used during development.
- created_time: The time the package was originally created in ISO 8601 format.
- modified_time: The last time the package was modified in ISO 8601 format.
- published_time: The time the package was published in ISO 8601 format.
- NPM_link: A link to the NPM page for the package (for JavaScript/Node.js packages).
- homepage_link: A link to the homepage or repository of the package.
- GitHub_link: A link to the GitHub repository of the package (if available).
- bugs_link: A link to report bugs or issues for the package.
- issues_link: A link to the issue tracker for the package.
- keywords: An array of keywords relevant to the package.
- tags: An array of tags for the package.
- issues: The number of open issues for the package.
- fork_number: The number of forks of the package on GitHub.
- star: The number of stars the package has on GitHub.
- subscriber_count: The number of subscribers following the package.

Make sure that:
1. At least one package is legitimate with a clean description and common scripts.
2. The other packages may be malicious with hidden or harmful functionality, and the description should clearly reflect its malicious nature.

Ensure the JSON structure is correct and well-formed.

The output should start with :
```json
.......
```
"""


# Define prompt for generating the dataset
sys_message_2 = """
Generate a JSON dataset for two software packages: 60 percent legitimate and rest suspicious. Each package should include the following fields:

- package_name: The name of the software package.
- version_number: The version number of the package.
- package_size_kb: The size of the package in kilobytes.
- upload_time: The time when the package was uploaded.
- number_of_files: The total number of files in the package.
- file_types: The types of files contained in the package.
- developer_id: A unique identifier for the developer.
- known_developer: Whether the developer is known (true/false).
- signing_certificate: Whether the package has a valid signing certificate (true/false).
- previous_version_size_kb: The size of the previous version in kilobytes.
- size_change_percent: The percentage size change compared to the previous version.
- number_of_dependencies: Number of dependencies required by the package.
- number_of_downloads: The number of downloads for the package.
- update_frequency: The average time between updates in days.
- hash_of_contents: A hash value of the package content (e.g., SHA-256).
- has_known_vulnerabilities: Whether the package includes known vulnerabilities (true/false).
- presence_of_obfuscated_code: Whether the package contains obfuscated code (true/false).
- contains_network_related_keywords: Whether network-related keywords are present (true/false).
- new_external_dependencies: Whether the current package introduces new external dependencies (true/false).
- sensitive_keywords_detected: Whether sensitive keywords are detected (true/false).
- anomalous_behavior_score: A float score indicating how much the package deviates from previous versions.
- suspicious_file_extension: Whether the package contains files with suspicious extensions (true/false).
- is_suspicious: Whether the package is suspicious (true/false).

Make sure that:
1. At least one package is legitimate with a clean description and common scripts.
2. The other packages may be malicious with hidden or harmful functionality, and the description should clearly reflect its malicious nature.

Ensure the JSON structure is correct and well-formed.

The output should start with :
```json
.......
```
"""