
## Create requirements file
### Need to export out locale settings
export LC_ALL=en_US.utf-8
export LANG=en_US.utf-8

### Export Requirements file
pip-compile

### Install from requirements file
pip-sync


# Install locally AFTER pip-sync or else pip-sync will uninstall your local library
## Install Pkg Locally

pip install . --upgrade --no-cache-dir
