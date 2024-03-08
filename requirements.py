import subprocess

def install_package(package):
    try:
        subprocess.check_call(['pip', 'install', package])
        print(f"Successfully installed {package}")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}")

def main():
    # List of packages to install
    packages = ['ipinfo', 'python-whois', 'python-nmap']

    # Install each package
    for package in packages:
        install_package(package)

if __name__ == "__main__":
    main()
