class Project:
    def __init__(
        self, name, description, license, authors, dependencies, dev_dependencies
    ):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_contents(self, contents):
        if len(contents) > 0:
            return "\n".join([f"- {content}" for content in contents])
        return "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description}"
            f"\nLicense: {self.license}\n"
            f"\nAuthors:\n{self._stringify_contents(self.authors)}\n"
            f"\nDependencies:\n{self._stringify_contents(self.dependencies)}\n"
            f"\nDevelopment dependencies:\n{self._stringify_contents(self.dev_dependencies)}\n"
        )
