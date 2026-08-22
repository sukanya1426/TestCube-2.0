# coding=utf-8

import logging
import os
import time

from .adapter import Adapter

DROIDBOT_APP_PACKAGE = "io.github.ylimit.droidbotapp"
IME_SERVICE = DROIDBOT_APP_PACKAGE + "/.DroidBotIME"


class DroidBotImeException(Exception):
    """
    Exception in telnet connection
    """
    pass


def helper_apk_path():
    here = os.path.dirname(os.path.abspath(__file__))
    local = os.path.normpath(os.path.join(here, "..", "resources", "droidbotApp.apk"))
    if os.path.isfile(local):
        return local
    try:
        import pkg_resources
        path = pkg_resources.resource_filename("droidbot", "resources/droidbotApp.apk")
        if os.path.isfile(path):
            return path
    except Exception:
        pass
    return local


def install_droidbot_app(device, logger=None):
    log = logger or logging.getLogger("DroidBotIme")
    apk = helper_apk_path()
    if not os.path.isfile(apk):
        log.warning("DroidBot helper APK not found: %s" % apk)
        return False
    try:
        device.adb.run_cmd(["install", "-r", "-t", "-g", apk], check=False)
        log.debug("DroidBot app installed from %s" % apk)
        return True
    except Exception as exc:
        log.warning("Failed to install DroidBotApp: %s" % exc)
        return False


class DroidBotIme(Adapter):
    """
    a connection with droidbot ime app.
    """
    def __init__(self, device=None):
        """
        initiate a emulator console via telnet
        :param device: instance of Device
        :return:
        """
        self.logger = logging.getLogger(self.__class__.__name__)
        if device is None:
            from droidbot.device import Device
            device = Device()
        self.device = device
        self.connected = False

    def set_up(self):
        device = self.device
        try:
            installed = DROIDBOT_APP_PACKAGE in (device.adb.get_installed_apps() or [])
        except Exception:
            installed = False
        if installed:
            self.logger.debug("DroidBot app was already installed.")
            return
        install_droidbot_app(device, self.logger)

    def tear_down(self):
        try:
            self.device.uninstall_app(DROIDBOT_APP_PACKAGE)
        except Exception as exc:
            self.logger.warning("Could not uninstall DroidBot app: %s" % exc)

    def _ime_shell(self, *parts):
        return self.device.adb.shell(list(parts), check=False)

    def connect(self):
        """Enable DroidBotIME when the helper app is present. Never abort the run."""
        try:
            self.set_up()
            output = self._ime_shell("ime", "enable", IME_SERVICE)
            if "Unknown input method" in output or "cannot be enabled" in output:
                install_droidbot_app(self.device, self.logger)
                output = self._ime_shell("ime", "enable", IME_SERVICE)
            if "now enabled" in output or "already enabled" in output:
                r_set = self._ime_shell("ime", "set", IME_SERVICE)
                if IME_SERVICE in r_set or "selected" in r_set.lower():
                    self.connected = True
                    return
            self.logger.warning(
                "DroidBotIME is not available on this emulator (%s). "
                "Continuing with adb input text."
                % ((output or "").strip().splitlines()[-1] if output else "not installed")
            )
            self.connected = False
        except Exception as exc:
            self.logger.warning("DroidBotIME unavailable (%s); using adb input text." % exc)
            self.connected = False

    def check_connectivity(self):
        """
        check if droidbot app is connected
        :return: True for connected
        """
        return self.connected

    def disconnect(self):
        """
        disconnect telnet
        """
        self.connected = False
        try:
            r_disable = self._ime_shell("ime", "disable", IME_SERVICE)
            if "now disabled" in (r_disable or ""):
                print("[CONNECTION] %s is disconnected" % self.__class__.__name__)
                return
        except Exception as exc:
            self.logger.debug("ime disable: %s" % exc)
        print("[CONNECTION] %s is disconnected" % self.__class__.__name__)

    def input_text(self, text, mode=0):
        """
        Input text to target device
        :param text: text to input, can be unicode format
        :param mode: 0 - set text; 1 - append text.
        """
        text_nospace = text.replace(' ', '--')
        input_cmd = 'am broadcast -a DROIDBOT_INPUT_TEXT --es text %s --ei mode %d' % (text_nospace, mode)
        self.device.adb.shell(str(input_cmd), check=False)


if __name__ == "__main__":
    droidbot_ime_conn = DroidBotIme()
    droidbot_ime_conn.set_up()
    droidbot_ime_conn.connect()
    droidbot_ime_conn.input_text("hello world!", 0)
    droidbot_ime_conn.input_text("世界你好!", 1)
    time.sleep(2)
    droidbot_ime_conn.input_text("再见。Bye bye.", 0)
    droidbot_ime_conn.disconnect()
    droidbot_ime_conn.tear_down()
