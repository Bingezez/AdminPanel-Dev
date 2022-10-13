import platform

from adminpanel.lib.utils import serialize


class Platform:
    def __init__(self) -> None:
        self.system = platform.system()
        self.platform = platform.platform()
        self.release = platform.release()
        self.version = platform.version()

    @property
    def json_platform(self):
        return serialize({
            "platform": self.platform,
            "system": self.system,
            "release": self.release,
            "version": self.version
        })


if __name__ == "__main__":
    pass
    