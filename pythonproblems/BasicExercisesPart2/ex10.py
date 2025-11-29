import platform


def os_information_display() -> None:
    """
    This program displays some information about the OS where the script is running.
    Author: Gustavo Assi Alencar.
    Date:   26/11/2025.
    """

    # Step 1: List some atributes to retrieve from platform module.
    os_profile = [
        'architecture',
        'linux_distribution',
        'mac_ver',
        'machine',
        'node',
        'platform',
        'processor',
        'python_build',
        'python_compiler',
        'python_version',
        'release',
        'system',
        'uname',
        'version',
    ]

    for attribute in os_profile:
        if hasattr(platform, attribute):
            print(f"{attribute}: {str(getattr(platform, attribute)())}")


def main() -> None:
    os_information_display()


if __name__ == "__main__":
    main()
