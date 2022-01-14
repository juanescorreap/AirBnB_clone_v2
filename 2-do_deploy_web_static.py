#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack."""
from fabric.api import *
from datetime import datetime
import os


def do_pack():
    """Fabric script that generates a .tgz archive from the contents of
    the web_static folder of your AirBnB Clone repo,
    using the function do_pack."""

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    tgz_file = "versions/web_static_{}.tgz".format(date)
    execute_tar = local("tar -cvzf {} web_static".format(tgz_file))

    if execute_tar.succeeded:
        return tgz_file
    else:
        return None


env.hosts = ['35.231.240.149', '54.167.32.11']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
        Distribute our file into servers
    """
    if os.path.exists(archive_path):
        storedfile = archive_path[9:]
        nv = "/data/web_static/releases/" + storedfile[:-4]
        storedfile = "/tmp/" + storedfile
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(nv))
        run("sudo tar -xzf {} -C {}/".format(storedfile,
                                             nv))
        run("sudo rm {}".format(storedfile))
        run("sudo mv {}/web_static/* {}".format(nv,
                                                nv))
        run("sudo rm -rf {}/web_static".format(nv))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(nv))

        return True

    return False
