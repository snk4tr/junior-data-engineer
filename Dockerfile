FROM ufoym/deepo:pytorch

LABEL maintainer="sergey.kastryulin@philips.com"

# ===========================================================
# Copy configuration file and set env variables for Flask
# -----------------------------------------------------------

COPY requirements.txt /tmp/
ENV FLASK_APP=junior_data_engineer
ENV FLASK_ENV=development

# ===========================================================
# Allows to use package managers behind company's firewall
# Only required for running from inside Philips intranet
# -----------------------------------------------------------

ENV http_proxy=http://proxy.pfh.research.philips.com:8080/
ENV https_proxy=https://proxy.pfh.research.philips.com:8080/

RUN echo "Acquire::http::Proxy \"http://proxy.pfh.research.philips.com:8080/\";" \
        >> /etc/apt/apt.conf.d/10proxy && \
    echo "Acquire::https::Proxy \"https://proxy.pfh.research.philips.com:8080/\";" \
        >> /etc/apt/apt.conf.d/10proxy && \

    # ===========================================================
    # Python packages
    # -----------------------------------------------------------

    pip install --upgrade pip && \
    pip install --no-cache-dir --requirement /tmp/requirements.txt

# ===========================================================
# Create a new user
# -----------------------------------------------------------

ARG UID=1000
ARG GID=1000
RUN groupadd -g $GID user && \
    useradd -m -s /bin/bash -u $UID -g user -G root user && \
    usermod -aG sudo user && \
    echo "user:user" | chpasswd

WORKDIR /home/sergey/dev/junior_data_engineer