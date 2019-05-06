import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_kannel_service(host):
    kannel = host.service("kannel")

    assert kannel.is_running
    assert kannel.is_enabled


def test_packages(host):
    pkg = host.package("kannel")

    assert pkg.is_installed
