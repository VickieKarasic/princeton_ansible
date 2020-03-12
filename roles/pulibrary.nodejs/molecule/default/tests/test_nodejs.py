import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name", [
    "nodejs",
    "yarn",
    ])
def test_for_nodejs_install(host, name):
    pkg = host.package(name)

    assert pkg.is_installed
    if name == "nodejs":
        assert pkg.version.startswith("12.")
