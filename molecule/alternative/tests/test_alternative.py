import pytest
import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_directories(host):
    dirs = [
        "/opt/another-venv"
    ]
    for dir in dirs:
        d = host.file(dir)
        assert d.is_directory
        assert d.exists


def test_files(host):
    files = [
        "/etc/systemd/system/sockpuppet.service",
        "/opt/venv-sockpuppet/bin/sockpuppet"
    ]
    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file


def test_service(host):
    s = host.service("sockpuppet")
    assert s.is_running


def test_socket(host):
    sockets = [
        "tcp://127.0.0.1:30001"
    ]
    for socket in sockets:
        s = host.socket(socket)
        assert s.is_listening


def test_socket_negative(host):
    sockets = [
        "tcp://127.0.0.1:30000"
    ]
    for socket in sockets:
        s = host.socket(socket)
        assert not s.is_listening
