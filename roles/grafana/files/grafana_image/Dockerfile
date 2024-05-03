FROM debian:latest

ENV TZ=Europe/Prague

# Update packages and install necessary dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        vim \
        wget \
        curl \
        gnupg \
        python3 \
        python3-pip \
        daemontools \
    && rm -rf /var/lib/apt/lists/* \
    && python3 -m pip install requests --break-system-packages

# Download and install GPG key for Grafana repository
RUN wget -q -O - https://packages.grafana.com/gpg.key | apt-key add -

# Add Grafana repository to sources.list.d
RUN echo "deb https://packages.grafana.com/oss/deb stable main" > /etc/apt/sources.list.d/grafana.list

# Update packages and install Grafana
RUN apt-get update \
    && apt-get install -y grafana \
    && rm -rf /var/lib/apt/lists/*

# Expose the port Grafana will listen on
EXPOSE 3000

# Start Grafana as a daemon
CMD ["grafana-server", "--config=/etc/grafana/grafana.ini", "--homepath=/usr/share/grafana", "cfg:default.paths.logs=/var/log/grafana", "cfg:default.paths.data=/var/lib/grafana", "cfg:default.paths.plugins=/var/lib/grafana/plugins"]