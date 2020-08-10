FROM centos:8

RUN dnf install -y rpmdevtools dnf-utils make

COPY * /

ENTRYPOINT ["/entrypoint.sh"] 
