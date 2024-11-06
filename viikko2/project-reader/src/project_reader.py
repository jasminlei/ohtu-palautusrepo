from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        data = toml.loads(content)
        name = data["tool"]["poetry"].get("name", "-")
        description = data["tool"]["poetry"].get("description", "-")
        license = data["tool"]["poetry"].get("license", "-")
        authors = data["tool"]["poetry"].get("authors", [])
        dependencies = list(data["tool"]["poetry"].get("dependencies", {}).keys())
        dev_dependencies = list(
            data["tool"]["poetry"]
            .get("group", {})
            .get("dev", {})
            .get("dependencies", {})
            .keys()
        )

        return Project(
            name, description, license, authors, dependencies, dev_dependencies
        )
