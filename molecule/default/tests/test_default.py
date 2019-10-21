import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_hosts_file(host):
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"


def test_snort_dir(host):
    f = host.file("/etc/snort")
    assert f.is_directory


def test_snort_rules_white_list(host):
    f = host.file("/etc/snort/rules/white_list.rules")
    assert f.exists


def test_snort_rules_black_list(host):
    f = host.file("/etc/snort/rules/black_list.rules")
    assert f.exists


def test_sid_msg_map_conf(host):
    f = host.file("/etc/snort/sid-msg.map")
    assert f.exists


def test_gen_map_map_conf(host):
    f = host.file("/etc/snort/gen-msg.map")
    assert f.exists


def test_systemd_unit(host):
    f = host.file("/etc/systemd/system/snort.service")
    assert f.exists
