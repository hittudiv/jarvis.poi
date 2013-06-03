#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# PyGtalkRobot: A simple jabber/xmpp bot framework using Regular Expression Pattern as command controller
# Copyright (c) 2008 Demiao Lin <ldmiao@gmail.com>
#
# RaspiBot: A simple software robot for Raspberry Pi based on PyGtalkRobot
# Copyright (c) 2013 Michael Mitchell <michael@mitchtech.net>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# PyGtalkRobot Homepage: http://code.google.com/p/pygtalkrobot/
# RaspiBot Homepage: http://code.google.com/p/pygtalkrobot/
#
import time
#import RPi.GPIO as GPIO
from PyGtalkRobot import GtalkRobot
from configs.config import configs
from configs.strings import strings



#GPIO.setmode(GPIO.BOARD) # or GPIO.setmode(GPIO.BCM)
############################################################################################################################


if __name__ == "__main__":
	bot = GtalkRobot(configs().settings['server'], configs().settings['port'], debug=configs().debug)
	bot.setState('available', strings().status)
	bot.start(configs().settings['BOT_GTALK_USER'], configs().settings['BOT_GTALK_PASS'])