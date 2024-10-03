#!/bin/bash
#
# Install Arch Linux packages needed to run Odoo.

if [ "$1" = "-l" -o "$1" = "--list" ]; then
    cmd="echo"
else
    cmd="pacman -S --needed --noconfirm"
    if [ "$(id -u)" -ne "0" ]; then
        echo -e "\033[0;31mThis script must be run as root to install dependencies, starting a dry run.\033[0m" >&2
        cmd="$cmd --dry-run"
    else
        pacman -Sy
    fi
    if [ "$1" = "-q" -o "$1" = "--quiet" ]; then
        cmd="$cmd --quiet"
    fi
fi

# Define a list of common dependencies for Odoo
dependencies=(
    python
    python-pip
    python-virtualenv
    postgresql
    nodejs
    npm
    git
    libxml2
    libxslt
    libjpeg
    libpng
    freetype2
    zlib
    libyaml
    libsasl
    libldap
    libffi
    libzip
)

# Install dependencies
$cmd "${dependencies[@]}"

# Additional setup steps
if [ "$(id -u)" -eq "0" ] && [ "$1" != "-l" ] && [ "$1" != "--list" ]; then
    # Initialize PostgreSQL if not already done
    if [ ! -d "/var/lib/postgres/data" ]; then
        echo "Initializing PostgreSQL database..."
        sudo -u postgres initdb -D /var/lib/postgres/data
        systemctl enable postgresql
        systemctl start postgresql
    fi

    # Create PostgreSQL user for the current system user if it doesn't exist
    if ! sudo -u postgres psql -tAc "SELECT 1 FROM pg_roles WHERE rolname='$USER'" | grep -q 1; then
        echo "Creating PostgreSQL user for $USER..."
        sudo -u postgres createuser -s $USER
    fi

    echo "Installing less-plugin-clean-css..."
    npm install -g less less-plugin-clean-css
fi

echo "Odoo dependencies installation completed."