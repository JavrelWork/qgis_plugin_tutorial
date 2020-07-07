FROM qgis/qgis:release-3_10_focal

ARG PLUGINS_PATH=/root/.local/share/QGIS/QGIS3/profiles/default/python/plugins

RUN mkdir -p $PLUGINS_PATH

# Add QuickMapServices to QGIS to save installing each time
RUN apt-get update && apt-get install -y \
    curl \
    unzip &&\
    curl -o /tmp/qms.zip https://plugins.qgis.org/plugins/quick_map_services/version/0.19.11.1/download/ && \
    unzip /tmp/qms.zip -d /tmp/ && \
    cp -r /tmp/quick_map_services $PLUGINS_PATH && \
    rm -rf /tmp/*

# Copy built plugin to plugins directory
COPY ./quick_api $PLUGINS_PATH/quick_api
COPY ./quick_api_interactive $PLUGINS_PATH/quick_api_interactive


